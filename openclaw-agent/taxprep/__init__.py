#!/usr/bin/env python3
"""
TaxPrep CLI - Command-line interface for TaxPrep agent functionality
Provides commands for tax calculations, data import, report generation, and more.
"""

import argparse
import json
import sys
import os
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from taxprep.data_store import TaxPrepDataStore
from taxprep.tax_calculator import TaxCalculator
from taxprep.report_generator import ReportGenerator
from taxprep.hmrc_client import HMRCClient
from taxprep.platform_clients import AirbnbClient, BookingClient

DATA_DIR = Path(__file__).parent.parent / "data"


def cmd_init(args):
    """Initialize TaxPrep data storage"""
    store = TaxPrepDataStore(DATA_DIR)
    store.initialize()
    print(f"TaxPrep initialized at {DATA_DIR}")
    print("Run 'taxprep --help' for available commands")


def cmd_add_property(args):
    """Add a new property to track"""
    store = TaxPrepDataStore(DATA_DIR)
    property_data = {
        "name": args.name,
        "address": args.address,
        "property_type": args.type,
        "platforms": args.platforms.split(",") if args.platforms else [],
        "notes": args.notes or ""
    }
    property_id = store.add_property(property_data, args.user_id)
    print(f"Property added with ID: {property_id}")


def cmd_list_properties(args):
    """List all properties for a user"""
    store = TaxPrepDataStore(DATA_DIR)
    properties = store.get_properties(args.user_id)
    if not properties:
        print("No properties found")
        return
    for p in properties:
        print(f"  {p['id']}: {p['name']} ({p['property_type']})")
        if p.get('address'):
            print(f"      Address: {p['address']}")


def cmd_add_income(args):
    """Add rental income for a property"""
    store = TaxPrepDataStore(DATA_DIR)
    income_data = {
        "property_id": args.property_id,
        "amount": float(args.amount),
        "date": args.date,
        "source": args.source,
        "platform": args.platform,
        "reference": args.reference or ""
    }
    income_id = store.add_income(income_data, args.user_id)
    print(f"Income record added with ID: {income_id}")


def cmd_add_expense(args):
    """Add an expense for a property"""
    store = TaxPrepDataStore(DATA_DIR)
    expense_data = {
        "property_id": args.property_id,
        "description": args.description,
        "amount": float(args.amount),
        "date": args.date,
        "category": args.category,
        "vat": float(args.vat) if args.vat else 0.0,
        "notes": args.notes or ""
    }
    expense_id = store.add_expense(expense_data, args.user_id)
    print(f"Expense record added with ID: {expense_id}")


def cmd_calculate_tax(args):
    """Calculate estimated tax liability"""
    store = TaxPrepDataStore(DATA_DIR)
    calc = TaxCalculator(store)
    
    result = calc.calculate_tax_liability(
        user_id=args.user_id,
        tax_year=args.tax_year
    )
    
    print(f"\n=== Tax Calculation {args.tax_year} ===")
    print(f"Total Income: £{result['total_income']:,.2f}")
    print(f"Total Expenses: £{result['total_expenses']:,.2f}")
    print(f"Net Profit: £{result['net_profit']:,.2f}")
    print(f"\nEstimated Tax:")
    print(f"  Income Tax: £{result['income_tax']:,.2f}")
    print(f"  National Insurance: £{result['national_insurance']:,.2f}")
    print(f"  Total: £{result['total_tax']:,.2f}")
    print(f"\nNote: These figures are estimates only. Verify with an accountant.")


def cmd_generate_report(args):
    """Generate a tax report"""
    store = TaxPrepDataStore(DATA_DIR)
    generator = ReportGenerator(store)
    
    report = generator.generate_report(
        user_id=args.user_id,
        tax_year=args.tax_year,
        format=args.format
    )
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)


def cmd_import_csv(args):
    """Import data from CSV file"""
    store = TaxPrepDataStore(DATA_DIR)
    
    import csv
    with open(args.file, 'r') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            if args.data_type == 'income':
                store.add_income({
                    "property_id": row.get('property_id', ''),
                    "amount": float(row.get('amount', 0)),
                    "date": row.get('date', datetime.now().strftime('%Y-%m-%d')),
                    "source": row.get('source', 'csv_import'),
                    "platform": row.get('platform', ''),
                    "reference": row.get('reference', '')
                }, args.user_id)
            elif args.data_type == 'expense':
                store.add_expense({
                    "property_id": row.get('property_id', ''),
                    "description": row.get('description', ''),
                    "amount": float(row.get('amount', 0)),
                    "date": row.get('date', datetime.now().strftime('%Y-%m-%d')),
                    "category": row.get('category', 'other'),
                    "vat": float(row.get('vat', 0)),
                    "notes": row.get('notes', '')
                }, args.user_id)
            count += 1
    
    print(f"Imported {count} {args.data_type} records")


def cmd_deadlines(args):
    """Show upcoming tax deadlines"""
    from taxprep.deadline_tracker import DeadlineTracker
    tracker = DeadlineTracker()
    
    deadlines = tracker.get_upcoming_deadlines(
        user_id=args.user_id,
        days=args.days
    )
    
    if not deadlines:
        print("No upcoming deadlines")
        return
    
    print("=== Upcoming Tax Deadlines ===")
    for d in deadlines:
        print(f"  {d['date']}: {d['title']}")
        print(f"       {d['description']}")


def cmd_invoice(args):
    """Generate an invoice"""
    from taxprep.invoice_generator import InvoiceGenerator
    generator = InvoiceGenerator(TaxPrepDataStore(DATA_DIR))
    
    invoice = generator.generate(
        user_id=args.user_id,
        property_id=args.property_id,
        invoice_type=args.type,
        date=args.date
    )
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(invoice)
        print(f"Invoice saved to {args.output}")
    else:
        print(invoice)


def cmd_mtd_status(args):
    """Check MTD compliance status"""
    store = TaxPrepDataStore(DATA_DIR)
    calc = TaxCalculator(store)
    
    status = calc.check_mtd_compliance(
        user_id=args.user_id
    )
    
    print(f"\n=== MTD Compliance Status ===")
    print(f"Annual Rental Income: £{status['annual_income']:,.2f}")
    print(f"MTD Status: {status['mtds_status']}")
    print(f"Requirement: {status['requirement']}")
    
    if status.get('action_required'):
        print("\nAction Required:")
        for action in status['action_required']:
            print(f"  - {action}")


def cmd_hmrc_submit(args):
    """Submit data to HMRC (simulation)"""
    client = HMRCClient()
    print("Connecting to HMRC API...")
    print("Note: This is a simulation. Configure API credentials for real submission.")
    print(f"Would submit: {args.data_type} for tax year {args.tax_year}")


def cmd_sync_platform(args):
    """Sync data from rental platform"""
    if args.platform == 'airbnb':
        client = AirbnbClient()
        print("Syncing Airbnb data...")
    elif args.platform == 'booking':
        client = BookingClient()
        print("Syncing Booking.com data...")
    else:
        print(f"Unknown platform: {args.platform}")
        return
    
    print("Note: Configure API credentials for real sync.")


def main():
    parser = argparse.ArgumentParser(
        description='TaxPrep - UK Property Tax Assistant',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Init
    subparsers.add_parser('init', help='Initialize TaxPrep data storage')
    
    # Property commands
    prop_parser = subparsers.add_parser('property', help='Property management')
    prop_sub = prop_parser.add_subparsers(dest='subcommand')
    
    add_prop = prop_sub.add_parser('add', help='Add a property')
    add_prop.add_argument('--name', required=True, help='Property name')
    add_prop.add_argument('--address', required=True, help='Property address')
    add_prop.add_argument('--type', default='residential', help='Property type')
    add_prop.add_argument('--platforms', help='Comma-separated platforms')
    add_prop.add_argument('--notes', help='Additional notes')
    add_prop.add_argument('--user-id', default='default', help='User ID')
    
    list_prop = prop_sub.add_parser('list', help='List properties')
    list_prop.add_argument('--user-id', default='default', help='User ID')
    
    # Income commands
    inc_parser = subparsers.add_parser('income', help='Income management')
    inc_parser.add_argument('--property-id', required=True, help='Property ID')
    inc_parser.add_argument('--amount', required=True, help='Amount')
    inc_parser.add_argument('--date', default='today', help='Date (YYYY-MM-DD)')
    inc_parser.add_argument('--source', default='manual', help='Income source')
    inc_parser.add_argument('--platform', help='Platform')
    inc_parser.add_argument('--reference', help='Reference number')
    inc_parser.add_argument('--user-id', default='default', help='User ID')
    
    # Expense commands
    exp_parser = subparsers.add_parser('expense', help='Expense management')
    exp_parser.add_argument('--property-id', required=True, help='Property ID')
    exp_parser.add_argument('--description', required=True, help='Description')
    exp_parser.add_argument('--amount', required=True, help='Amount')
    exp_parser.add_argument('--date', default='today', help='Date (YYYY-MM-DD)')
    exp_parser.add_argument('--category', default='other', help='Category')
    exp_parser.add_argument('--vat', help='VAT amount')
    exp_parser.add_argument('--notes', help='Additional notes')
    exp_parser.add_argument('--user-id', default='default', help='User ID')
    
    # Tax calculation
    tax_parser = subparsers.add_parser('tax', help='Tax calculations')
    tax_parser.add_argument('--user-id', default='default', help='User ID')
    tax_parser.add_argument('--tax-year', default='2025-26', help='Tax year')
    
    # Report generation
    report_parser = subparsers.add_parser('report', help='Generate tax report')
    report_parser.add_argument('--user-id', default='default', help='User ID')
    report_parser.add_argument('--tax-year', default='2025-26', help='Tax year')
    report_parser.add_argument('--format', default='markdown', choices=['markdown', 'pdf', 'html'])
    report_parser.add_argument('--output', help='Output file')
    
    # Import
    imp_parser = subparsers.add_parser('import', help='Import from CSV')
    imp_parser.add_argument('--file', required=True, help='CSV file path')
    imp_parser.add_argument('--data-type', required=True, choices=['income', 'expense'])
    imp_parser.add_argument('--user-id', default='default', help='User ID')
    
    # Deadlines
    dl_parser = subparsers.add_parser('deadlines', help='Show tax deadlines')
    dl_parser.add_argument('--user-id', default='default', help='User ID')
    dl_parser.add_argument('--days', type=int, default=90, help='Days ahead to check')
    
    # Invoice
    inv_parser = subparsers.add_parser('invoice', help='Generate invoice')
    inv_parser.add_argument('--property-id', required=True, help='Property ID')
    inv_parser.add_argument('--type', default='rental', help='Invoice type')
    inv_parser.add_argument('--date', default='today', help='Date')
    inv_parser.add_argument('--user-id', default='default', help='User ID')
    inv_parser.add_argument('--output', help='Output file')
    
    # MTD status
    mtd_parser = subparsers.add_parser('mtd', help='Check MTD compliance')
    mtd_parser.add_argument('--user-id', default='default', help='User ID')
    
    # HMRC submit
    hmrc_parser = subparsers.add_parser('hmrc', help='Submit to HMRC')
    hmrc_parser.add_argument('--data-type', required=True, choices=['income', 'report'])
    hmrc_parser.add_argument('--tax-year', default='2025-26', help='Tax year')
    
    # Platform sync
    sync_parser = subparsers.add_parser('sync', help='Sync from platform')
    sync_parser.add_argument('--platform', required=True, choices=['airbnb', 'booking'])
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Handle date defaults
    if hasattr(args, 'date') and args.date == 'today':
        args.date = datetime.now().strftime('%Y-%m-%d')
    
    # Dispatch commands
    if args.command == 'init':
        cmd_init(args)
    elif args.command == 'property':
        if args.subcommand == 'add':
            cmd_add_property(args)
        elif args.subcommand == 'list':
            cmd_list_properties(args)
        else:
            prop_parser.print_help()
    elif args.command == 'income':
        cmd_add_income(args)
    elif args.command == 'expense':
        cmd_add_expense(args)
    elif args.command == 'tax':
        cmd_calculate_tax(args)
    elif args.command == 'report':
        cmd_generate_report(args)
    elif args.command == 'import':
        cmd_import_csv(args)
    elif args.command == 'deadlines':
        cmd_deadlines(args)
    elif args.command == 'invoice':
        cmd_invoice(args)
    elif args.command == 'mtd':
        cmd_mtd_status(args)
    elif args.command == 'hmrc':
        cmd_hmrc_submit(args)
    elif args.command == 'sync':
        cmd_sync_platform(args)


if __name__ == '__main__':
    main()