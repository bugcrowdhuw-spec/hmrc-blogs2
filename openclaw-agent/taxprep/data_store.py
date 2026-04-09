import sqlite3
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict


class TaxPrepDataStore:
    """SQLite-based data storage for TaxPrep"""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.db_path = data_dir / "taxprep.db"
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def initialize(self):
        """Create database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT,
                name TEXT,
                tier TEXT DEFAULT 'free',
                created_at TEXT,
                settings TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                name TEXT,
                address TEXT,
                property_type TEXT,
                platforms TEXT,
                notes TEXT,
                created_at TEXT,
                updated_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS income (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                property_id TEXT,
                amount REAL,
                date TEXT,
                source TEXT,
                platform TEXT,
                reference TEXT,
                created_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (property_id) REFERENCES properties(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                property_id TEXT,
                description TEXT,
                amount REAL,
                date TEXT,
                category TEXT,
                vat REAL,
                notes TEXT,
                created_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (property_id) REFERENCES properties(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                tax_year TEXT,
                format TEXT,
                content TEXT,
                created_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS invoices (
                id TEXT PRIMARY KEY,
                user_id TEXT,
                property_id TEXT,
                invoice_type TEXT,
                date TEXT,
                amount REAL,
                content TEXT,
                created_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (property_id) REFERENCES properties(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    # User methods
    def create_user(self, user_id: str, email: str = None, name: str = None) -> str:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO users (id, email, name, created_at) VALUES (?, ?, ?, ?)",
            (user_id, email, name, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return user_id
    
    def get_user(self, user_id: str) -> Optional[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "email": row[1], "name": row[2], "tier": row[3], "created_at": row[4], "settings": json.loads(row[5] or '{}')}
        return None
    
    def update_user_tier(self, user_id: str, tier: str):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET tier = ? WHERE id = ?", (tier, user_id))
        conn.commit()
        conn.close()
    
    # Property methods
    def add_property(self, property_data: Dict, user_id: str = "default") -> str:
        property_id = str(uuid.uuid4())[:8]
        conn = self._get_connection()
        cursor = conn.cursor()
        now = datetime.now().isoformat()
        cursor.execute(
            """INSERT INTO properties 
               (id, user_id, name, address, property_type, platforms, notes, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (property_id, user_id, property_data.get('name'), property_data.get('address'),
             property_data.get('property_type'), json.dumps(property_data.get('platforms', [])),
             property_data.get('notes', ''), now, now)
        )
        conn.commit()
        conn.close()
        return property_id
    
    def get_properties(self, user_id: str = "default") -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM properties WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row, ['id', 'user_id', 'name', 'address', 'property_type', 'platforms', 'notes', 'created_at', 'updated_at']) for row in rows]
    
    def get_property(self, property_id: str) -> Optional[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM properties WHERE id = ?", (property_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return self._row_to_dict(row, ['id', 'user_id', 'name', 'address', 'property_type', 'platforms', 'notes', 'created_at', 'updated_at'])
        return None
    
    # Income methods
    def add_income(self, income_data: Dict, user_id: str = "default") -> str:
        income_id = str(uuid.uuid4())[:8]
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO income 
               (id, user_id, property_id, amount, date, source, platform, reference, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (income_id, user_id, income_data.get('property_id'), income_data.get('amount'),
             income_data.get('date'), income_data.get('source'), income_data.get('platform'),
             income_data.get('reference', ''), datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return income_id
    
    def get_income(self, user_id: str = "default", property_id: str = None, tax_year: str = None) -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM income WHERE user_id = ?"
        params = [user_id]
        if property_id:
            query += " AND property_id = ?"
            params.append(property_id)
        if tax_year:
            year_start = f"20{tax_year.split('-')[0]}-04-06"
            year_end = f"20{tax_year.split('-')[1]}-04-05"
            query += " AND date >= ? AND date <= ?"
            params.extend([year_start, year_end])
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row, ['id', 'user_id', 'property_id', 'amount', 'date', 'source', 'platform', 'reference', 'created_at']) for row in rows]
    
    # Expense methods
    def add_expense(self, expense_data: Dict, user_id: str = "default") -> str:
        expense_id = str(uuid.uuid4())[:8]
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO expenses 
               (id, user_id, property_id, description, amount, date, category, vat, notes, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (expense_id, user_id, expense_data.get('property_id'), expense_data.get('description'),
             expense_data.get('amount'), expense_data.get('date'), expense_data.get('category'),
             expense_data.get('vat', 0), expense_data.get('notes', ''), datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return expense_id
    
    def get_expenses(self, user_id: str = "default", property_id: str = None, tax_year: str = None) -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM expenses WHERE user_id = ?"
        params = [user_id]
        if property_id:
            query += " AND property_id = ?"
            params.append(property_id)
        if tax_year:
            year_start = f"20{tax_year.split('-')[0]}-04-06"
            year_end = f"20{tax_year.split('-')[1]}-04-05"
            query += " AND date >= ? AND date <= ?"
            params.extend([year_start, year_end])
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row, ['id', 'user_id', 'property_id', 'description', 'amount', 'date', 'category', 'vat', 'notes', 'created_at']) for row in rows]
    
    # Report methods
    def save_report(self, user_id: str, tax_year: str, format: str, content: str) -> str:
        report_id = str(uuid.uuid4())[:8]
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reports (id, user_id, tax_year, format, content, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (report_id, user_id, tax_year, format, content, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return report_id
    
    def get_reports(self, user_id: str = "default") -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reports WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row, ['id', 'user_id', 'tax_year', 'format', 'content', 'created_at']) for row in rows]
    
    # Invoice methods
    def save_invoice(self, user_id: str, property_id: str, invoice_type: str, date: str, amount: float, content: str) -> str:
        invoice_id = str(uuid.uuid4())[:8]
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO invoices (id, user_id, property_id, invoice_type, date, amount, content, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (invoice_id, user_id, property_id, invoice_type, date, amount, content, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return invoice_id
    
    def get_invoices(self, user_id: str = "default", property_id: str = None) -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM invoices WHERE user_id = ?"
        params = [user_id]
        if property_id:
            query += " AND property_id = ?"
            params.append(property_id)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row, ['id', 'user_id', 'property_id', 'invoice_type', 'date', 'amount', 'content', 'created_at']) for row in rows]
    
    def _row_to_dict(self, row, columns):
        result = {}
        for i, col in enumerate(columns):
            value = row[i]
            if col == 'platforms' and value:
                try:
                    value = json.loads(value)
                except:
                    value = []
            result[col] = value
        return result