# AGENTS.md - TaxPrep Agent System

This file defines the agent system for the TaxPrep OpenCLAW agent.

## Agent Configuration

```
Agent Name: TaxPrep Assistant
Type: Property Tax Specialist
Framework: OpenCLAW
Version: 2.0.0
```

## Capabilities

| Skill | Description | Status |
|-------|-------------|--------|
| Tax Reporting | Generate HMRC-compliant property income reports | ✅ Active |
| MTD Compliance | Check Making Tax Digital requirements | ✅ Active |
| Expense Categorization | Analyze and classify deductible expenses | ✅ Active |
| Property Portfolio | Track and manage property portfolios | ✅ Active |
| Deadline Reminders | Track tax year key dates | ✅ Active |
| Invoice Generation | Create professional rental invoices | ✅ Active |
| Platform Integration | Sync data from Airbnb, Booking.com | ✅ Active |
| HMRC API | MTD submission capability | ✅ Active |

## Python CLI Commands

```bash
# Initialize
taxprep init

# Add property
taxprep property add --name "London Flat" --address "123 High St" --type fhl --platforms airbnb,booking

# Add income
taxprep income --property-id <ID> --amount 1200 --source rental --platform airbnb

# Add expense
taxprep expense --property-id <ID> --description "Repairs" --amount 150 --category repairs

# Calculate tax
taxprep tax --user-id <user> --tax-year 2025-26

# Generate report
taxprep report --user-id <user> --tax-year 2025-26 --format markdown --output report.md

# Check deadlines
taxprep deadlines --days 90

# Generate invoice
taxprep invoice --property-id <ID> --type rental --output invoice.md

# Check MTD compliance
taxprep mtd --user-id <user>
```

## Commercial Tiers

| Tier | Price | Properties | Features |
|------|-------|------------|----------|
| Free | £0 | 1 | Basic tracking |
| Starter | £9.99/mo | 3 | Email support |
| Professional | £24.99/mo | 10 | API access |
| Business | £49.99/mo | 50 | HMRC submission |

## Data Storage

- **Database:** SQLite (`data/taxprep.db`)
- **User Profiles:** Stored per customer
- **Reports:** History maintained in database
- **Invoices:** Auto-generated and stored

## Docker Deployment

```bash
# Build
docker build -t taxprep:latest .

# Run
docker-compose up -d

# Environment variables
AIRBNB_API_TOKEN=<token>
BOOKING_API_KEY=<key>
HMRC_CLIENT_ID=<id>
HMRC_CLIENT_SECRET=<secret>
```

## Memory Management

- **Daily Notes:** `memory/YYYY-MM-DD.md` - Session logs and interactions
- **User Profiles:** Stored in database per customer
- **Long-term:** `MEMORY.md` - Important client context

## Communication

- **Primary:** Text-based (chat interface)
- **Reports:** Markdown-formatted with HMRC references
- **Urgency:** Flag key deadlines and compliance requirements

## Heartbeat Configuration

Check for:
- Upcoming tax deadlines (Self Assessment: 31 Jan)
- MTD quarterly submission windows
- Any unresolved compliance questions

## Safety

- No automatic submission to HMRC - always require user confirmation
- Include disclaimers on all calculated figures
- Recommend professional accountancy for final submissions

---

_This agent is designed to assist with UK property tax compliance. Not a substitute for qualified professional advice._