# Skill: Property Portfolio Tracking

_Capability to manage and track property portfolios, including multi-property analysis and performance metrics._

## Triggers

- "add property", "new property", "property portfolio"
- "track properties", "property performance", "portfolio summary"
- "property details", "property info", "update property"

## Actions

1. **Property Management**
   - Add new properties with details (address, type, platforms)
   - Update existing property information
   - Track property status (active, inactive, sold)
   - Store property documents and references

2. **Portfolio Analysis**
   - Calculate total portfolio value/income
   - Generate property-by-property breakdown
   - Identify underperforming properties
   - Track platform distribution (Airbnb, Booking, etc.)

3. **Performance Metrics**
   - Occupancy rates (per property, portfolio average)
   - Revenue trends (monthly, quarterly, yearly)
   - Expense ratios per property
   - Net profit margins

## Property Types

- **Furnished Holiday Let (FHL)** - Short-term holiday rentals
- **Standard Residential** - Long-term lets
- **HMO** - Houses in Multiple Occupation
- **Commercial** - Commercial property rentals

## Property Data Fields

| Field | Description | Required |
|-------|-------------|----------|
| name | Property name/identifier | Yes |
| address | Full property address | Yes |
| property_type | Type of property | Yes |
| platforms | List of booking platforms | No |
| purchase_price | Original purchase price | No |
| purchase_date | Date acquired | No |
| notes | Additional notes | No |

## Portfolio Metrics

```
## Portfolio Summary

### Holdings
- Total Properties: X
- Active: X | Inactive: X

### Income (YTD)
- Total: £X
- Average per property: £X

### Expenses (YTD)
- Total: £X
- Average per property: £X

### Net Performance
- Portfolio profit: £X
- Average ROI: X%
```

## CLI Commands

```bash
# Add property
taxprep property add --name "London Flat" --address "123 High St" --type fhl --platforms airbnb,booking

# List properties
taxprep property list

# View portfolio
taxprep report --format markdown
```

## Constraints

- Require property address for UK tax purposes
- Track which platforms each property is listed on
- Flag properties approaching thresholds (MTD, VAT)

---

_Reference: HMRC Property Income Manual, Landlord Guide_