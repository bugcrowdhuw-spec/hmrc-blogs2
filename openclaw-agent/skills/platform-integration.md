# Skill: Platform API Integration

_Capability to connect with and import data from major holiday rental platforms (Airbnb, Booking.com, Vrbo)._

## Triggers

- "sync airbnb", "import booking", "connect platform"
- "sync data", "import transactions", "get platform data"
- "airbnb income", "booking earnings", "vrbo revenue"

## Supported Platforms

### Airbnb
- **API:** Airbnb Host API
- **Data:** Reservations, Payouts, Calendar, Reviews
- **Auth:** OAuth 2.0 with host credentials

### Booking.com
- **API:** Booking.com Connectivity API
- **Data:** Bookings, Revenue, Availability, Reviews
- **Auth:** API key with partner ID

### Vrbo
- **API:** Vrbo API
- **Data:** Reservations, Property details
- **Auth:** API key with owner ID

## Data Synchronization

### Full Sync
Complete data pull for a date range:
- All properties
- All reservations
- All revenue/payouts
- Calendar updates

### Incremental Sync
Changes since last sync:
- New reservations
- Updated bookings
- Recent reviews

## Output Format

```
## Platform Sync Results

### Airbnb
- Properties synced: 2
- Reservations imported: 15
- Income imported: £4,250.00

### Booking.com
- Properties synced: 1
- Bookings imported: 8
- Revenue imported: £2,100.00

### Summary
- Total transactions: 23
- Total income: £6,350.00
```

## CLI Commands

```bash
# Sync Airbnb data
taxprep sync --platform airbnb --host-id HOST123

# Sync Booking.com data
taxprep sync --platform booking --partner-id PARTNER456

# Sync all platforms
taxprep sync --platform all --start-date 2025-04-06 --end-date 2026-04-05
```

## API Configuration

Set environment variables for each platform:

```bash
# Airbnb
export AIRBNB_API_TOKEN="your_token"

# Booking.com
export BOOKING_API_KEY="your_key"

# Vrbo
export VRBO_API_KEY="your_key"
```

## Data Mapping

Platform data is mapped to TaxPrep records:

| Platform Field | TaxPrep Field |
|----------------|---------------|
| listing_id | property_id |
| reservation_id | reference |
| payout_amount | amount |
| check_in | date |
| guest_name | notes |

## Constraints

- Rate limits apply per platform
- Some data may require manual verification
- Platform API credentials required

---

_Reference: Airbnb API Docs, Booking.com Partner API, Vrbo Developer_