# TaxPrep OpenCLAW Agent

**Version:** 2.0.0  
**License:** Commercial - All Rights Reserved  
**Author:** TaxPrep

## Product Overview

TaxPrep is an autonomous AI agent built on the OpenCLAW framework, specializing in UK HMRC property tax reporting. It helps property landlords manage their tax compliance obligations, generate compliant reports, and stay on top of Making Tax Digital requirements.

### Key Features

- **Autonomous Operation** - Persistent AI agent with memory and identity
- **HMRC Compliance** - Generates MTD-compliant reports
- **Multi-Channel** - Works via chat, email digest, and scheduled heartbeats
- **Tax Deadline Monitoring** - Proactive reminders for Self Assessment and quarterly submissions
- **Python CLI** - Full command-line interface for data processing
- **Platform Integration** - Sync from Airbnb, Booking.com, Vrbo
- **Invoice Generation** - Create professional rental invoices
- **Commercial Ready** - Multi-tier pricing with user management

---

## Architecture

```
TaxPrep Agent
├── SOUL.md                   # Agent personality & behaviour
├── IDENTITY.md               # Who the agent is
├── USER.md                   # Customer data template
├── AGENTS.md                 # System documentation
├── config/
│   └── agent.yaml            # Runtime configuration
├── skills/
│   ├── tax-reporting.md
│   ├── mtd-compliance.md
│   ├── expense-categorization.md
│   ├── property-portfolio.md
│   ├── deadline-reminders.md
│   ├── invoice-generation.md
│   └── platform-integration.md
├── taxprep/                  # Python modules
│   ├── cli.py                # Command-line interface
│   ├── data_store.py         # SQLite storage
│   ├── tax_calculator.py     # Tax calculations
│   ├── report_generator.py   # Report generation
│   ├── hmrc_client.py        # HMRC API client
│   ├── platform_clients.py   # Platform APIs
│   ├── deadline_tracker.py  # Deadline tracking
│   ├── invoice_generator.py # Invoice generation
│   └── user_manager.py       # User management
├── data/                     # Data storage (runtime)
├── memory/                   # Session logs (runtime)
├── Dockerfile                # Docker support
├── docker-compose.yml        # Docker Compose
└── requirements.txt          # Python dependencies
```

## Python CLI

Install dependencies and use the CLI:

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python -m taxprep.cli init

# Add a property
python -m taxprep.cli property add --name "London Flat" --address "123 High St" --type fhl

# Add income
python -m taxprep.cli income --property-id <ID> --amount 1200 --source rental --platform airbnb

# Add expense
python -m taxprep.cli expense --property-id <ID> --description "Repairs" --amount 150 --category repairs

# Calculate tax
python -m taxprep.cli tax --user-id default --tax-year 2025-26

# Generate report
python -m taxprep.cli report --user-id default --tax-year 2025-26 --output report.md

# Check deadlines
python -m taxprep.cli deadlines --days 90

# Check MTD compliance
python -m taxprep.cli mtd --user-id default
```

---

## Prerequisites

- OpenCLAW framework (latest) - https://docs.openclaw.ai
- Claude API access (Anthropic)
- UK tax year knowledge base
- Linux/macOS deployment environment

### Environment Variables

```bash
# Required
export CLAUDE_API_KEY="sk-ant-..."
export OPENCLAW_API_KEY="your_openclaw_key"

# Optional
export AGENT_NAME=TaxPrep
export USER_DATA_PATH=./data/users
export LOG_LEVEL=info
```

---

## Installation

### Quick Start

```bash
# 1. Clone or extract agent to your OpenCLAW agents directory
cp -r taxprep-assistant /path/to/openclaw/agents/

# 2. Set environment variables
export CLAUDE_API_KEY="your_key"
export OPENCLAW_API_KEY="your_key"

# 3. Run deployment script
cd taxprep-assistant
chmod +x deploy.sh
./deploy.sh
```

### Manual Installation

```bash
# Set environment variables
export CLAUDE_API_KEY="your_key"
export OPENCLAW_API_KEY="your_key"

# Start the agent
openclaw run taxprep-assistant

# Interact via chat
openclaw chat taxprep-assistant
```

---

## Configuration

### Agent Settings (config/agent.yaml)

Key configuration options:

| Setting | Description | Default |
|---------|-------------|---------|
| `model` | AI model to use | claude-sonnet-4-20250514 |
| `max_tokens` | Response length | 4000 |
| `temperature` | Creativity level | 0.7 |
| `heartbeat.interval_minutes` | Heartbeat frequency | 60 |

### Skills Configuration

The agent includes 3 core skills that can be triggered by specific keywords:

1. **Tax Reporting** - "generate report", "hmrc report", "sa100", "sa105"
2. **MTD Compliance** - "mtd compliance", "making tax digital"
3. **Expense Categorization** - "expenses", "deductions", "allowable costs"

---

## Commercial Deployment

### For Service Providers

If you're integrating TaxPrep into a service offering:

1. Review the LICENSE terms
2. Configure the agent with your API keys
3. Set up user data storage (`data/users/`)
4. Customize USER.md template for your customers
5. Deploy on your infrastructure

### Docker Deployment

```dockerfile
FROM node:20-slim

WORKDIR /app

# Install OpenCLAW
RUN npm install -g openclaw

# Copy agent files
COPY . /app/taxprep-assistant/

WORKDIR /app/taxprep-assistant

# Set environment
ENV CLAUDE_API_KEY=${CLAUDE_API_KEY}
ENV OPENCLAW_API_KEY=${OPENCLAW_API_KEY}

CMD ["./deploy.sh"]
```

### Production Considerations

- **Security**: Store API keys in secure vault (AWS Secrets, HashiCorp Vault)
- **Monitoring**: Set up log aggregation for agent interactions
- **Backups**: Regularly backup memory and user data directories
- **Updates**: Subscribe to OpenCLAW releases for framework updates

---

## Usage Examples

### Generate Tax Report

```
User: Generate my tax report for 2024/25

Agent: I'll help you prepare your property tax report. Please provide:
- Total rental income for the year
- Property type (FHL or standard)
- List of expenses incurred
```

### Check MTD Compliance

```
User: Am I MTD compliant?

Agent: Let me check your MTD status. Please share:
- Your annual rental income
- Whether you're currently enrolled for MTD
- Your current accounting software
```

### Categorize Expenses

```
User: What expenses can I deduct?

Agent: Based on UK HMRC rules, here are the main categories...
```

---

## Support

- **Documentation**: https://docs.openclaw.ai
- **Community**: https://discord.com/invite/clawd
- **Issues**: Contact Licensor for commercial support

### Disclaimer

This agent is designed to assist with UK property tax compliance. It provides guidance and generates reports based on HMRC rules, but figures should be verified with a qualified accountant before final submission to HMRC.

---

## What's Included

| Component | Description |
|-----------|-------------|
| SOUL.md | Agent personality and behaviour definition |
| IDENTITY.md | Agent identity and role |
| USER.md | Customer data capture template |
| AGENTS.md | System documentation |
| config/agent.yaml | Runtime configuration |
| skills/ | 3 core tax skills |
| deploy.sh | Automated deployment script |
| LICENSE | Commercial license agreement |

---

**Commercial Product - Not for redistribution without written permission.**

&copy; 2026 HMRC Reporter. All rights reserved.