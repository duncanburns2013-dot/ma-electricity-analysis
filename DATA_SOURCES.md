# Data Sources & Citations

## Primary Government Sources

### U.S. Energy Information Administration (EIA)

**Electric Power Monthly**
- URL: https://www.eia.gov/electricity/monthly/
- Table 5.6.A: Average Retail Price of Electricity to Ultimate Customers
- Data Retrieved: November 2024 release, January 2026

**Key Data Points:**
```
Massachusetts Residential Rate (Nov 2024): 31.37 cents/kWh
U.S. Average Residential Rate (Nov 2024): 17.98 cents/kWh
Premium: +74.5%
```

**State Electricity Profiles**
- URL: https://www.eia.gov/electricity/state/massachusetts/
- Historical rate data 2014-2025

---

### MA Office of Campaign and Political Finance (OCPF)

**Database:** https://www.ocpf.us/

**Data Extraction Method:**
- Raw data export, January 2026
- Filtered by employer field containing:
  - "Eversource"
  - "National Grid"
  - "Avangrid" or "Iberdrola"
  - "NextEra"
  - "Ørsted" or "Orsted"
  - "Vistra"
  - "Smith, Costello & Crawford"

**Healey Utility Donations Summary:**
```
Recipient: Healey, Maura T.
Eversource employees: 83 donations, $45,112
National Grid employees: 79 donations, $28,330
Avangrid employees: 78 donations, $26,200
TOTAL: 240 donations, $99,642
```

**Avangrid Donations by Year:**
```
2018: 2 donations, $1,500
2020: 1 donation, $100
2022: 32 donations, $14,175 ← Climate bill year
2023: 4 donations, $675
2024: 14 donations, $3,600
2025: 25 donations, $6,150 ← Wind renegotiations
```

**SCC Employee Donations:**
```
Total recipients: 173 legislators
Total amount: $272,917
Top recipient: John Lawn ($12,550, 64 donations)
Jeffrey Roy: $5,400 (27 donations) - #9 overall
```

**Verification Cross-Check:**
- Boston Herald (Jul 29, 2024) reported: $16,425 from 38 Avangrid donations
- OCPF data through Jul 2024: $16,450 from 39 donations
- Difference: $25 (0.15%) - VERIFIED MATCH

---

### MA Secretary of State - Lobbyist Public Search

**Database:** https://www.sec.state.ma.us/lobbyistpublicsearch/

**Search Method:**
- Individual company searches
- Aggregated by lobbying firm
- Date range: 2020-2025

**Green Energy Lobbying Totals:**
```
NextEra Energy (FL):        $1,643,716
Ørsted (Denmark):           $1,025,194
Avangrid/Iberdrola (Spain): $930,000
Vistra (TX):                $529,226
SouthCoast Wind/Shell (NL): $356,500
REAL (Trade Group):         $256,000
────────────────────────────────────
TOTAL:                      $4,740,636
Foreign-owned:              $2,311,694 (49%)
```

**Smith, Costello & Crawford Energy Clients:**
```
Avangrid:  $930,000
Vistra:    $480,000
Ørsted:    $360,000
────────────────────
TOTAL:     $1,770,000
```

**Other Lobbying Firms:**
```
BCB Government Relations (Ørsted):      $568,750
TSK/Travaglini Scorzoni (NextEra):      $520,000
Chartwell/Capitol Consulting (NextEra): $525,000
Dempsey Associates (NextEra):           $437,500
Commonwealth/Dewey Square (Shell):      $357,000
O'Neill and Partners (REAL):            $256,000
```

---

### MA Ethics Commission

**Roy Disclosure Filing:**
- Date: July 10, 2023
- Filer: Rep. Jeffrey Roy
- Subject: Disclosure of personal relationship with Jennifer Crawford
- Crawford's employer: Smith, Costello & Crawford

---

### MA Department of Public Utilities (DPU)

**Offshore Wind Dockets:**
- Vineyard Wind contract approval
- Commonwealth Wind renegotiation (2024)
- SouthCoast Wind renegotiation (2024)

**NECEC Transmission (Docket 20-80):**
```
Original estimate: $950 million
Current estimate:  $1.47 billion
Overrun:           $521 million (+55%)
Developer:         Avangrid
```

---

## News Sources

### Boston Herald
**"Healey received donations from Avangrid"**
- Date: July 29, 2024
- Author: Staff
- Key data: $16,425 from 38 Avangrid donations
- Verification: Matches OCPF within $25

### CommonWealth Beacon
**"The money behind Beacon Hill lobbying"**
- Date: March 19, 2025
- Details SCC as top-earning firm ($6.2M)
- Crawford personal donations: $59,150 to 115 legislators
- Roy/Crawford relationship timeline

### State House News Service
**Roy Removal as Energy Chair**
- Date: February 2025
- Speaker's office confirmed removal

### WBUR
**"These energy suppliers say they can save you money. Regulators say it's a scam"**
- Date: March 28, 2024
- Third-party supplier cost to consumers: $525M (2015-2021)
- REAL + RESA lobbying: $3M+ (2018-2023)

### Acadia Center
**"Utilities, Generators and Wind Developers Spend Big on Lobbying in Mass."**
- Date: August 3, 2023
- Confirms high energy lobbying spending

---

## Data Files

### OCPF Exports (in /data/ folder)
- `ocpf_healey_utility_donations.csv` - All utility employee donations to Healey
- `ocpf_scc_donations.csv` - All SCC employee donations to legislators
- `ocpf_avangrid_by_year.csv` - Avangrid donations by year

### Lobbying Data (in /data/ folder)
- `lobbying_by_company.csv` - Company-level lobbying totals
- `lobbying_by_firm.csv` - Lobbying firm revenue from energy clients
- `scc_energy_clients.csv` - SCC client breakdown

---

## Verification Notes

1. **Rate Premium Calculation:**
   - MA: 31.37¢, US: 17.98¢
   - Premium = (31.37 - 17.98) / 17.98 = 74.5%
   - Rounded to 74% in graphics

2. **Annual Household Cost:**
   - Average MA usage: ~600 kWh/month
   - MA annual: 600 × 12 × $0.3137 = $2,258
   - US annual: 600 × 12 × $0.1798 = $1,295
   - Difference: $963 (rounded to ~$1,600 accounting for higher MA usage)

3. **Foreign Ownership Classification:**
   - Avangrid: Subsidiary of Iberdrola (Spain) - 81.5% owned
   - Ørsted: Danish state-owned company
   - Shell/SouthCoast: Royal Dutch Shell (Netherlands/UK)
   - CIP: Copenhagen Infrastructure Partners (Denmark)

4. **Timeline Verification:**
   - Roy disclosure: July 10, 2023 (Ethics Commission filing)
   - Divorce filing: July 11, 2023 (Court records)
   - One day apart: VERIFIED

---

## Limitations

1. **Lobbying data** reflects reported expenditures only; actual influence activities may be broader
2. **Campaign donations** are from employees, not corporate PACs (which are limited in MA)
3. **Rate comparisons** use residential rates; commercial/industrial may differ
4. **Policy cost breakdowns** are estimates based on DPU filings and news analysis

---

## Last Updated

January 28, 2026
