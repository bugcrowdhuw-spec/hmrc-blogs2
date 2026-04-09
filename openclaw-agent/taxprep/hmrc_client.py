import os
import json
from typing import Dict, Optional


class HMRCClient:
    """HMRC MTD API Client - Simulation"""
    
    BASE_URL = "https://api.hmrc.gov.uk"
    
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.client_id = client_id or os.getenv("HMRC_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("HMRC_CLIENT_SECRET")
        self.bearer_token = None
    
    def authenticate(self) -> bool:
        """Authenticate with HMRC API"""
        if not self.client_id or not self.client_secret:
            print("HMRC API credentials not configured")
            print("Set HMRC_CLIENT_ID and HMRC_CLIENT_SECRET environment variables")
            return False
        
        print(f"Authenticating with HMRC MTD API...")
        print(f"Client ID: {self.client_id[:8]}...")
        return True
    
    def submit_income(self, user_id: str, tax_year: str, income_data: Dict) -> Dict:
        """Submit income to HMRC"""
        print(f"Submitting income for {tax_year}...")
        print(f"Income: £{income_data.get('total_income', 0):,.2f}")
        
        return {
            "status": "simulated",
            "submission_id": f"SIM-{tax_year}-{user_id}",
            "timestamp": "2026-04-08T12:00:00Z",
            "message": "This is a simulation. Configure real API credentials for actual submission."
        }
    
    def submit_report(self, user_id: str, tax_year: str, report_data: Dict) -> Dict:
        """Submit final report to HMRC"""
        print(f"Submitting tax report for {tax_year}...")
        
        return {
            "status": "simulated",
            "submission_id": f"RPT-{tax_year}-{user_id}",
            "timestamp": "2026-04-08T12:00:00Z",
            "message": "This is a simulation. Configure real API credentials for actual submission."
        }
    
    def get_obligations(self, user_id: str, tax_year: str) -> Dict:
        """Get MTD obligations"""
        return {
            "status": "simulated",
            "obligations": [
                {
                    "period": "2025-26",
                    "due_dates": [
                        {"quarter": "Q1", "start": "2025-04-06", "end": "2025-07-05", "due": "2025-08-05"},
                        {"quarter": "Q2", "start": "2025-07-06", "end": "2025-10-05", "due": "2025-11-05"},
                        {"quarter": "Q3", "start": "2025-10-06", "end": "2026-01-05", "due": "2026-02-05"},
                        {"quarter": "Q4", "start": "2026-01-06", "end": "2026-04-05", "due": "2026-05-05"}
                    ]
                }
            ]
        }
    
    def check_compliance(self, user_id: str) -> Dict:
        """Check MTD compliance status"""
        return {
            "compliant": True,
            "last_submission": "2026-01-31",
            "next_due": "2026-08-05"
        }
    
    def create_vat_return(self, vat_number: str, period: str, vat_data: Dict) -> Dict:
        """Submit VAT return (if applicable)"""
        return {
            "status": "simulated",
            "vat_number": vat_number,
            "period": period
        }
    
    def get_business_details(self, user_id: str) -> Dict:
        """Get business details from HMRC"""
        return {
            "business_name": "Property Landlord",
            "accounting_type": "cash",
            "vat_registered": False,
            "mtd_enrolled": True
        }
    
    def list_properties(self, user_id: str) -> Dict:
        """List properties registered with HMRC"""
        return {
            "properties": [],
            "message": "Configure real API for property data"
        }
    
    def update_property(self, user_id: str, property_id: str, property_data: Dict) -> Dict:
        """Update property details with HMRC"""
        return {
            "status": "simulated",
            "property_id": property_id
        }
    
    def simulate_full_submission(self, user_id: str, tax_year: str, income: list, expenses: list) -> Dict:
        """Simulate a full tax submission"""
        total_income = sum(i.get('amount', 0) for i in income)
        total_expenses = sum(e.get('amount', 0) for e in expenses)
        net_profit = total_income - total_expenses
        
        estimated_tax = net_profit * 0.20
        
        return {
            "submission_type": "self_assessment",
            "tax_year": tax_year,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_profit": net_profit,
            "estimated_tax": estimated_tax,
            "status": "ready_for_submission",
            "note": "Configure HMRC API credentials for actual submission"
        }