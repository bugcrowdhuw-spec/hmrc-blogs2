from datetime import datetime, timedelta
from typing import List, Dict
from dateutil import parser as date_parser


class DeadlineTracker:
    """Track UK tax deadlines"""
    
    DEADLINES = [
        {
            "type": "self_assessment",
            "title": "Self Assessment Return",
            "description": "File your SA100 tax return for previous tax year",
            "month": 1,
            "day": 31,
            "recurring": True
        },
        {
            "type": "self_assessment_payment",
            "title": "Self Assessment Payment",
            "description": "Pay any outstanding tax for previous tax year",
            "month": 1,
            "day": 31,
            "recurring": True
        },
        {
            "type": "mtd_q1",
            "title": "MTD Q1 Submission",
            "description": "Quarter 1 VAT/MTD submission (Jul-Sep)",
            "month": 8,
            "day": 5,
            "recurring": True
        },
        {
            "type": "mtd_q2",
            "title": "MTD Q2 Submission",
            "description": "Quarter 2 VAT/MTD submission (Oct-Dec)",
            "month": 11,
            "day": 5,
            "recurring": True
        },
        {
            "type": "mtd_q3",
            "title": "MTD Q3 Submission",
            "description": "Quarter 3 VAT/MTD submission (Jan-Mar)",
            "month": 2,
            "day": 5,
            "recurring": True
        },
        {
            "type": "mtd_q4",
            "title": "MTD Q4 Submission",
            "description": "Quarter 4 VAT/MTD submission (Apr-Jun)",
            "month": 5,
            "day": 5,
            "recurring": True
        },
        {
            "type": "paye_annual",
            "title": "Paye Annual Return",
            "description": "Submit P11D for employees (if applicable)",
            "month": 7,
            "day": 6,
            "recurring": True
        },
        {
            "type": "capital_gains",
            "title": "Capital Gains Tax",
            "description": "Report property sales for CGT",
            "month": 12,
            "day": 31,
            "recurring": True
        }
    ]
    
    def __init__(self):
        pass
    
    def get_upcoming_deadlines(self, user_id: str = None, days: int = 90) -> List[Dict]:
        """Get deadlines within the next N days"""
        today = datetime.now()
        end_date = today + timedelta(days=days)
        
        deadlines = []
        
        for deadline in self.DEADLINES:
            for year in [today.year, today.year + 1]:
                deadline_date = datetime(
                    year,
                    deadline["month"],
                    deadline["day"]
                )
                
                if today <= deadline_date <= end_date:
                    days_until = (deadline_date - today).days
                    deadlines.append({
                        "id": f"{deadline['type']}-{year}",
                        "type": deadline["type"],
                        "title": deadline["title"],
                        "description": deadline["description"],
                        "date": deadline_date.strftime("%Y-%m-%d"),
                        "days_until": days_until,
                        "urgency": self._get_urgency(days_until)
                    })
        
        return sorted(deadlines, key=lambda x: x["days_until"])
    
    def _get_urgency(self, days_until: int) -> str:
        """Determine urgency level"""
        if days_until <= 7:
            return "critical"
        elif days_until <= 30:
            return "high"
        elif days_until <= 60:
            return "medium"
        else:
            return "low"
    
    def get_deadline_by_type(self, deadline_type: str) -> Dict:
        """Get specific deadline details"""
        for d in self.DEADLINES:
            if d["type"] == deadline_type:
                return d
        return None
    
    def get_mtd_deadlines(self) -> List[Dict]:
        """Get MTD-specific deadlines for current year"""
        today = datetime.now()
        year = today.year
        
        return [
            {
                "type": "mtd_q1",
                "title": "Q1 MTD Submission",
                "period": "April - June",
                "due": datetime(year, 8, 5).strftime("%Y-%m-%d")
            },
            {
                "type": "mtd_q2",
                "title": "Q2 MTD Submission",
                "period": "July - September",
                "due": datetime(year, 11, 5).strftime("%Y-%m-%d")
            },
            {
                "type": "mtd_q3",
                "title": "Q3 MTD Submission",
                "period": "October - December",
                "due": datetime(year + 1, 2, 5).strftime("%Y-%m-%d")
            },
            {
                "type": "mtd_q4",
                "title": "Q4 MTD Submission",
                "period": "January - March",
                "due": datetime(year + 1, 5, 5).strftime("%Y-%m-%d")
            }
        ]
    
    def get_self_assessment_deadline(self) -> Dict:
        """Get current Self Assessment deadline"""
        today = datetime.now()
        
        if today.month <= 1:
            year = today.year
        else:
            year = today.year + 1
        
        return {
            "type": "self_assessment",
            "title": "Self Assessment Return",
            "description": "File your SA100 tax return",
            "date": datetime(year, 1, 31).strftime("%Y-%m-%d"),
            "days_until": max(0, (datetime(year, 1, 31) - today).days)
        }
    
    def is_deadline_approaching(self, deadline_type: str, days_threshold: int = 14) -> bool:
        """Check if a specific deadline is approaching"""
        upcoming = self.get_upcoming_deadlines(days=days_threshold)
        return any(d["type"] == deadline_type for d in upcoming)
    
    def generate_reminder_text(self, deadlines: List[Dict]) -> str:
        """Generate reminder text for deadlines"""
        if not deadlines:
            return "No upcoming tax deadlines."
        
        text = "## Tax Deadline Reminders\n\n"
        
        critical = [d for d in deadlines if d["urgency"] == "critical"]
        high = [d for d in deadlines if d["urgency"] == "high"]
        other = [d for d in deadlines if d["urgency"] not in ["critical", "high"]]
        
        if critical:
            text += "### Urgent\n"
            for d in critical:
                text += f"- **{d['title']}** - {d['date']} ({d['days_until']} days)\n"
            text += "\n"
        
        if high:
            text += "### Coming Up\n"
            for d in high:
                text += f"- {d['title']} - {d['date']} ({d['days_until']} days)\n"
            text += "\n"
        
        if other:
            text += "### Later\n"
            for d in other:
                text += f"- {d['title']} - {d['date']}\n"
        
        return text


try:
    from dateutil import parser as date_parser
except ImportError:
    date_parser = None