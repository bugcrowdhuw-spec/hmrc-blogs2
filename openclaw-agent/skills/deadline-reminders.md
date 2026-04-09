# Skill: Deadline Reminders

_Capability to track and remind about important UK tax deadlines and compliance dates._

## Triggers

- "deadlines", "upcoming dates", "tax calendar"
- "reminders", "due dates", "what do I need to do"
- "self assessment deadline", "mtd deadline", "vat deadline"

## Key UK Tax Deadlines

### Self Assessment
| Deadline | Date | Description |
|----------|------|-------------|
| SA Return | 31 Jan | File tax return for previous tax year |
| SA Payment | 31 Jan | Pay any tax owed for previous year |
| SA Extension | 31 Jul | If paying through PAYE code |

### Making Tax Digital (MTD)
| Quarter | Period | Deadline |
|---------|--------|----------|
| Q1 | Apr-Jun | 5 Aug |
| Q2 | Jul-Sep | 5 Nov |
| Q3 | Oct-Dec | 5 Feb |
| Q4 | Jan-Mar | 5 May |

### Other Deadlines
- **P11D** - 6 July (employee benefits)
- **Corporation Tax** - 9 months + 1 day after year end
- **VAT** - Various (monthly/quarterly)
- **CGT** - 31 Dec (report property sales)

## Actions

1. **Deadline Monitoring**
   - Track upcoming deadlines based on user profile
   - Calculate days remaining
   - Prioritize by urgency

2. **Reminder Generation**
   - Generate friendly reminders for upcoming dates
   - Include preparation steps
   - Suggest actions to take

3. **Calendar Integration**
   - Export to iCal format
   - Support Google Calendar sync
   - Email reminders (if configured)

## Output Format

```
## Upcoming Tax Deadlines

### Critical (within 7 days)
- **Self Assessment Return** - 31 Jan 2026 (5 days)
  Action: Complete and submit your SA100 return

### High Priority (7-30 days)
- **MTD Q2 Submission** - 5 Nov 2025 (45 days)
  Action: Prepare quarterly figures

### Upcoming (30-90 days)
- **MTD Q3 Submission** - 5 Feb 2026 (90 days)
```

## CLI Commands

```bash
# Check deadlines
taxprep deadlines --days 90

# Get specific deadline info
taxprep deadlines --type self_assessment

# Export to calendar
taxprep deadlines --export ical
```

## Urgency Levels

| Level | Days Until | Color |
|-------|------------|-------|
| Critical | ≤7 days | Red |
| High | 8-30 days | Amber |
| Medium | 31-60 days | Yellow |
| Low | 61-90 days | Green |

## Tax Year Reference

Current Tax Year: 2025-26 (6 April 2025 - 5 April 2026)

---

_Reference: HMRC Deadlines Guide, Tax Calendar_