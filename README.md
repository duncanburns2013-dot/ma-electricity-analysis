# Massachusetts Electricity Cost Analysis

A data-driven analysis of Massachusetts electricity costs compared to national averages, based on the Fiscal Alliance Foundation White Paper by Lisa Linowes (November 2025) and cross-referenced with U.S. Energy Information Administration (EIA) official data.

## Key Findings

- **57% higher rates** than the U.S. average (27.40¢/kWh vs 17.47¢/kWh)
- **#3 most expensive state** in the nation (behind only Connecticut and Hawaii)
- **81% rate increase** since 2014, growing 2.5x faster than both inflation and the national average
- **Policy charges quadrupled** from $15/month to $59/month (2014-2025)
- **$4.4 billion annual burden** on ratepayers statewide
- **+$1,188/year extra cost** per household compared to national average

## Repository Structure

```
ma-electricity-analysis/
├── data/                           # Source data files (CSV)
│   ├── electricity_rates.csv      # Historical rate and bill data
│   ├── state_rankings_2025.csv    # State-by-state comparison
│   └── bill_breakdown.csv         # Bill component breakdown
├── scripts/                        # Python scripts
│   └── generate_visualizations.py # Main script to generate all charts
├── outputs/                        # Generated visualizations (PNG)
├── docs/                          # Documentation
└── README.md                      # This file
```

## Data Sources

All data in this repository is derived from:

1. **Fiscal Alliance Foundation White Paper**: "Massachusetts Electricity Costs: The Real Source of the Problem" by Lisa Linowes (November 2025)
2. **U.S. Energy Information Administration (EIA)**: 
   - Electric Power Monthly
   - State Electricity Profiles
   - Form EIA-861 (Annual Electric Power Industry Report)
3. **Bureau of Labor Statistics**: Consumer Price Index (CPI-U)
4. **Massachusetts Department of Public Utilities**: Eversource and National Grid rate filings

## Usage

### Requirements

```bash
pip install pandas matplotlib numpy
```

### Generate All Visualizations

```bash
cd scripts
python generate_visualizations.py
```

This will generate:
- `comprehensive_dashboard.png` - Main 4-panel overview
- `ma_vs_national_rates.png` - Rate trends over time
- `state_ranking.png` - State-by-state comparison
- `how_bad_is_it_infographic.png` - Summary infographic

### Use the Data

Load the CSV files directly:

```python
import pandas as pd

# Load historical rates
rates = pd.read_csv('data/electricity_rates.csv')

# Load state rankings
states = pd.read_csv('data/state_rankings_2025.csv')

# Load bill breakdown
breakdown = pd.read_csv('data/bill_breakdown.csv')
```

## Data Dictionary

### electricity_rates.csv

| Column | Description | Unit |
|--------|-------------|------|
| year | Calendar year | - |
| ma_rate_cents_per_kwh | Massachusetts average residential rate | ¢/kWh |
| us_rate_cents_per_kwh | U.S. national average residential rate | ¢/kWh |
| ma_monthly_bill_600kwh | MA monthly bill for 600 kWh usage | $ |
| us_monthly_bill_600kwh | US monthly bill for 600 kWh usage | $ |
| policy_charges_cents_per_kwh | MA policy charge component | ¢/kWh |
| policy_charges_monthly_600kwh | MA policy charges for 600 kWh | $ |

### state_rankings_2025.csv

| Column | Description | Unit |
|--------|-------------|------|
| state | State name | - |
| rate_cents_per_kwh | Average residential rate (Nov 2025) | ¢/kWh |
| rank | National ranking (1=highest) | - |

### bill_breakdown.csv

| Column | Description | Unit |
|--------|-------------|------|
| component | Bill component name | - |
| amount_2014 | Amount in 2014 for 600 kWh | $ |
| amount_2025 | Amount in 2025 for 600 kWh | $ |

## Key Metrics

### Rate Growth (2014-2025)
- Massachusetts: **+81%** (18.8¢ → 34.0¢)
- U.S. Average: **+40%** (12.5¢ → 17.5¢)
- Inflation (CPI): **+32%**

### Policy Charges Growth (2014-2025)
- From **2.5¢/kWh** to **9.8¢/kWh** (+293%)
- From **$15/month** to **$59/month** for typical household
- Now represents **29% of total bill** (up from 13%)

### Annual Cost Impact
- Extra cost per household: **+$1,188/year** vs. national average
- Statewide burden: **$4.4 billion/year**
- Cumulative extra cost per household (2014-2025): **>$10,000**

## Policy Programs Driving Costs

The primary cost drivers are state-mandated climate and energy programs:

1. **Renewable Portfolio Standard (RPS)** - Mandated renewable energy credits
2. **Regional Greenhouse Gas Initiative (RGGI)** - Carbon allowance purchases
3. **SMART Solar Program** - Solar incentive payments
4. **Net Metering** - Above-market compensation for solar
5. **Mass Save** - Energy efficiency programs ($1.5 billion annually)

## Analysis Notes

- All rates are for **residential customers**
- Monthly bill calculations assume **600 kWh usage** (typical MA household)
- Policy charges include RPS, RGGI, solar programs, and energy efficiency surcharges
- Growth rates are compounded annual growth rates (CAGR)
- Inflation measured using BLS CPI-U (1982-84=100)

## License

Data is compiled from public sources. Visualizations and code are provided for educational and research purposes.

## Citation

If using this data or analysis, please cite:

> Linowes, Lisa. "Massachusetts Electricity Costs: The Real Source of the Problem." 
> Fiscal Alliance Foundation White Paper, November 2025.
> Cross-referenced with U.S. Energy Information Administration data.

## Contact

For questions about the underlying white paper, contact:
- Fiscal Alliance Foundation: www.fiscalalliancefoundation.org

For questions about this repository:
- Open an issue on GitHub

## Updates

- **2025-11-19**: Initial release with data through February 2025
