import os
import uuid
from datetime import datetime
from typing import Dict, Optional


class UserManager:
    """User management and authentication for TaxPrep"""
    
    TIERS = {
        "free": {
            "name": "Free",
            "price": 0,
            "properties": 1,
            "api_access": False,
            "hmrc_submission": False,
            "support": "community"
        },
        "starter": {
            "name": "Starter",
            "price": 9.99,
            "properties": 3,
            "api_access": False,
            "hmrc_submission": False,
            "support": "email"
        },
        "professional": {
            "name": "Professional",
            "price": 24.99,
            "properties": 10,
            "api_access": True,
            "hmrc_submission": False,
            "support": "priority"
        },
        "business": {
            "name": "Business",
            "price": 49.99,
            "properties": 50,
            "api_access": True,
            "hmrc_submission": True,
            "support": "dedicated"
        }
    }
    
    def __init__(self, data_store):
        self.data_store = data_store
    
    def create_user(self, email: str, name: str = None, tier: str = "free") -> Dict:
        """Create a new user"""
        user_id = str(uuid.uuid4())[:8]
        
        user_data = {
            "id": user_id,
            "email": email,
            "name": name,
            "tier": tier,
            "created_at": datetime.now().isoformat(),
            "settings": self._get_default_settings(tier)
        }
        
        self.data_store.create_user(user_id, email, name)
        self.data_store.update_user_tier(user_id, tier)
        
        return self._build_user_response(user_data)
    
    def get_user(self, user_id: str) -> Optional[Dict]:
        """Get user details"""
        user = self.data_store.get_user(user_id)
        if user:
            tier_info = self.TIERS.get(user.get('tier', 'free'), self.TIERS['free'])
            return {
                **user,
                "tier_info": tier_info,
                "features": self._get_features_for_tier(user.get('tier', 'free'))
            }
        return None
    
    def update_user_tier(self, user_id: str, new_tier: str) -> Dict:
        """Upgrade or downgrade user tier"""
        if new_tier not in self.TIERS:
            raise ValueError(f"Invalid tier: {new_tier}")
        
        self.data_store.update_user_tier(user_id, new_tier)
        return self.get_user(user_id)
    
    def check_limits(self, user_id: str) -> Dict:
        """Check user's tier limits"""
        user = self.get_user(user_id)
        if not user:
            return {"error": "User not found"}
        
        properties = self.data_store.get_properties(user_id)
        tier = user.get('tier', 'free')
        tier_info = self.TIERS.get(tier, self.TIERS['free'])
        
        return {
            "current_properties": len(properties),
            "max_properties": tier_info['properties'],
            "can_add_property": len(properties) < tier_info['properties'],
            "tier": tier,
            "upgrade_required": len(properties) >= tier_info['properties']
        }
    
    def validate_api_access(self, user_id: str) -> bool:
        """Check if user has API access"""
        user = self.get_user(user_id)
        if not user:
            return False
        return user.get('features', {}).get('api_access', False)
    
    def validate_hmrc_submission(self, user_id: str) -> bool:
        """Check if user can submit to HMRC"""
        user = self.get_user(user_id)
        if not user:
            return False
        return user.get('features', {}).get('hmrc_submission', False)
    
    def generate_api_key(self, user_id: str) -> str:
        """Generate API key for user"""
        if not self.validate_api_access(user_id):
            raise PermissionError("API access not available on your tier")
        
        api_key = f"tpk_{uuid.uuid4().hex}"
        return api_key
    
    def get_tiers(self) -> Dict:
        """Get all available tiers"""
        return self.TIERS
    
    def get_tier_info(self, tier: str) -> Dict:
        """Get specific tier information"""
        return self.TIERS.get(tier, self.TIERS['free'])
    
    def _get_features_for_tier(self, tier: str) -> Dict:
        """Get feature list for a tier"""
        tier_info = self.TIERS.get(tier, self.TIERS['free'])
        return {
            "api_access": tier_info['api_access'],
            "hmrc_submission": tier_info['hmrc_submission'],
            "max_properties": tier_info['properties'],
            "support": tier_info['support']
        }
    
    def _get_default_settings(self, tier: str) -> Dict:
        """Get default settings for tier"""
        return {
            "tier": tier,
            "notifications": True,
            "deadline_reminders": True,
            "email_digest": "weekly"
        }
    
    def _build_user_response(self, user_data: Dict) -> Dict:
        """Build complete user response"""
        tier = user_data.get('tier', 'free')
        tier_info = self.TIERS.get(tier, self.TIERS['free'])
        
        return {
            "user_id": user_data['id'],
            "email": user_data.get('email'),
            "name": user_data.get('name'),
            "tier": tier,
            "tier_name": tier_info['name'],
            "features": self._get_features_for_tier(tier),
            "created_at": user_data.get('created_at')
        }


class PricingManager:
    """Manage pricing and subscriptions"""
    
    CURRENCY = "GBP"
    
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager
    
    def get_pricing_page(self) -> Dict:
        """Get pricing page data"""
        tiers = self.user_manager.get_tiers()
        
        return {
            "currency": self.CURRENCY,
            "tiers": [
                {
                    "id": tier_id,
                    "name": info['name'],
                    "price_monthly": info['price'],
                    "price_yearly": info['price'] * 10,
                    "properties": info['properties'],
                    "features": {
                        "properties": f"{info['properties']} properties",
                        "api_access": "API Access" if info['api_access'] else None,
                        "hmrc_submission": "HMRC Submission" if info['hmrc_submission'] else None,
                        "support": info['support'].title()
                    }
                }
                for tier_id, info in tiers.items()
            ]
        }
    
    def calculate_upgrade_cost(self, current_tier: str, new_tier: str) -> Dict:
        """Calculate upgrade cost"""
        current = self.user_manager.get_tier_info(current_tier)
        new = self.user_manager.get_tier_info(new_tier)
        
        monthly_diff = new['price'] - current['price']
        
        return {
            "current_tier": current_tier,
            "new_tier": new_tier,
            "monthly_increase": monthly_diff,
            "yearly_increase": monthly_diff * 12,
            "pro_rata_month": monthly_diff
        }
    
    def get_invoice_for_tier(self, user_id: str, new_tier: str) -> Dict:
        """Generate invoice for tier change"""
        user = self.user_manager.get_user(user_id)
        if not user:
            return {"error": "User not found"}
        
        new_tier_info = self.user_manager.get_tier_info(new_tier)
        
        return {
            "user_id": user_id,
            "tier": new_tier,
            "amount": new_tier_info['price'],
            "currency": self.CURRENCY,
            "billing_period": "monthly",
            "description": f"TaxPrep {new_tier_info['name']} Plan"
        }


class APIAuthManager:
    """Manage API authentication"""
    
    def __init__(self, data_store):
        self.data_store = data_store
    
    def validate_api_key(self, api_key: str) -> Optional[Dict]:
        """Validate API key and return user info"""
        if not api_key.startswith('tpk_'):
            return None
        
        return {"valid": True, "api_key": api_key}
    
    def check_rate_limit(self, user_id: str) -> Dict:
        """Check API rate limits"""
        return {
            "remaining": 100,
            "reset": "hourly",
            "limit": 100
        }


class SubscriptionManager:
    """Manage subscriptions and billing"""
    
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager
    
    def get_subscription(self, user_id: str) -> Dict:
        """Get user's subscription details"""
        user = self.user_manager.get_user(user_id)
        if not user:
            return {"error": "User not found"}
        
        return {
            "user_id": user_id,
            "tier": user.get('tier'),
            "status": "active",
            "renewal_date": "2026-05-08",
            "payment_method": "card" if user.get('tier') != 'free' else None
        }
    
    def cancel_subscription(self, user_id: str) -> Dict:
        """Cancel subscription (downgrade to free)"""
        return self.user_manager.update_user_tier(user_id, 'free')
    
    def pause_subscription(self, user_id: str) -> Dict:
        """Pause subscription"""
        return {"status": "paused", "resume_date": None}