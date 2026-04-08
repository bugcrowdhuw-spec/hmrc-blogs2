from typing import Dict, List, Optional
from datetime import datetime


class TaxCalculator:
    """UK Property Tax Calculator"""
    
    BASIC_RATE = 0.20
    HIGHER_RATE = 0.40
    ADDITIONAL_RATE = 0.45
    
    HIGHER_THRESHOLD = 50270
    ADDITIONAL_THRESHOLD = 125140
    
    NIC_RATE = 0.09
    NIC_THRESHOLD = 12570
    
    def __init__(self, data_store):
        self.data_store = data_store
    
    def calculate_tax_liability(self, user_id: str, tax_year: str = "2025-26") -> Dict:
        """Calculate estimated tax liability for a tax year"""
        income = self.data_store.get_income(user_id, tax_year=tax_year)
        expenses = self.data_store.get_expenses(user_id, tax_year=tax_year)
        
        total_income = sum(i['amount'] for i in income)
        total_expenses = sum(e['amount'] for e in expenses)
        net_profit = total_income - total_expenses
        
        income_tax = self._calculate_income_tax(net_profit)
        national_insurance = self._calculate_national_insurance(net_profit)
        
        return {
            "tax_year": tax_year,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_profit": net_profit,
            "income_tax": income_tax,
            "national_insurance": national_insurance,
            "total_tax": income_tax + national_insurance,
            "effective_rate": (income_tax + national_insurance) / net_profit if net_profit > 0 else 0
        }
    
    def _calculate_income_tax(self, net_profit: float) -> float:
        """Calculate income tax on rental profit"""
        if net_profit <= 0:
            return 0
        
        tax = 0
        remaining = net_profit
        
        if remaining > 0:
            personal_allowance = 12570
            taxable = max(0, remaining - personal_allowance)
            tax += taxable * self.BASIC_RATE
            remaining -= personal_allowance
        
        if remaining > 0:
            higher_band = max(0, min(remaining, self.HIGHER_THRESHOLD - 37700))
            tax += higher_band * (self.HIGHER_RATE - self.BASIC_RATE)
            remaining -= higher_band
        
        if remaining > 0:
            tax += remaining * (self.ADDITIONAL_RATE - self.HIGHER_RATE)
        
        return max(0, tax)
    
    def _calculate_national_insurance(self, net_profit: float) -> float:
        """Calculate Class 4 National Insurance"""
        if net_profit <= self.NIC_THRESHOLD:
            return 0
        
        profit_above_threshold = net_profit - self.NIC_THRESHOLD
        return profit_above_threshold * self.NIC_RATE
    
    def check_mtd_compliance(self, user_id: str) -> Dict:
        """Check MTD compliance status"""
        income = self.data_store.get_income(user_id)
        total_income = sum(i['amount'] for i in income)
        
        if total_income >= 50000:
            status = "Mandatory"
            requirement = "You must register for MTD and use compatible software"
            action_required = [
                "Sign up for MTD for Income Tax",
                "Choose MTD-compatible software",
                "Start keeping digital records"
            ]
        elif total_income >= 10000:
            status = "Voluntary"
            requirement = "You can choose to join MTD voluntarily"
            action_required = [
                "Consider joining MTD for better record keeping",
                "Choose MTD-compatible software if interested"
            ]
        else:
            status = "Exempt"
            requirement = "MTD not required (income under £10,000)"
            action_required = []
        
        return {
            "annual_income": total_income,
            "mtds_status": status,
            "requirement": requirement,
            "action_required": action_required
        }
    
    def calculate_expense_deductions(self, user_id: str, tax_year: str = "2025-26") -> Dict:
        """Calculate allowable expense deductions"""
        expenses = self.data_store.get_expenses(user_id, tax_year=tax_year)
        
        categories = {}
        for exp in expenses:
            cat = exp.get('category', 'other')
            if cat not in categories:
                categories[cat] = {'total': 0, 'items': []}
            categories[cat]['total'] += exp['amount']
            categories[cat]['items'].append(exp)
        
        allowable = 0
        disallowed = 0
        
        for cat, data in categories.items():
            if cat in ['repairs', 'insurance', 'legal_fees', 'accounting', 
                       'agent_fees', 'cleaning', 'utilities', 'travel', 'office']:
                allowable += data['total']
            else:
                disallowed += data['total']
        
        return {
            "total_expenses": sum(e['amount'] for e in expenses),
            "allowable": allowable,
            "disallowed": disallowed,
            "by_category": categories
        }
    
    def get_tax_summary(self, user_id: str, tax_year: str = "2025-26") -> Dict:
        """Get comprehensive tax summary"""
        properties = self.data_store.get_properties(user_id)
        
        summary = {
            "tax_year": tax_year,
            "properties": len(properties),
            "calculation": self.calculate_tax_liability(user_id, tax_year),
            "expenses": self.calculate_expense_deductions(user_id, tax_year),
            "mtd": self.check_mtd_compliance(user_id)
        }
        
        return summary