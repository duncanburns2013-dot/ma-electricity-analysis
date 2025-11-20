# Quick Start Guide

## Getting Started in 5 Minutes

### 1. Clone or Download

```bash
# If you have the tar.gz file:
tar -xzf ma-electricity-analysis.tar.gz
cd ma-electricity-analysis

# Or if cloning from GitHub:
git clone https://github.com/[your-username]/ma-electricity-analysis.git
cd ma-electricity-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Test the Data

```bash
cd scripts
python test_data.py
```

You should see:
```
✓ ALL TESTS PASSED!
```

### 4. Generate Visualizations

```bash
python generate_visualizations.py
```

This creates 4 PNG files in the `outputs/` directory:
- `comprehensive_dashboard.png` - Main overview
- `ma_vs_national_rates.png` - Rate trends
- `state_ranking.png` - State comparison
- `how_bad_is_it_infographic.png` - Summary infographic

### 5. Explore the Data

```python
import pandas as pd

# Load the data
rates = pd.read_csv('../data/electricity_rates.csv')

# Quick analysis
print(f"MA 2025 rate: {rates.iloc[-1]['ma_rate_cents_per_kwh']}¢/kWh")
print(f"US 2025 rate: {rates.iloc[-1]['us_rate_cents_per_kwh']}¢/kWh")
print(f"Premium: {((rates.iloc[-1]['ma_rate_cents_per_kwh'] / rates.iloc[-1]['us_rate_cents_per_kwh']) - 1) * 100:.1f}%")
```

## File Structure

```
ma-electricity-analysis/
├── README.md              ← Start here
├── requirements.txt       ← Python dependencies
├── data/                  ← CSV data files
│   ├── electricity_rates.csv
│   ├── state_rankings_2025.csv
│   └── bill_breakdown.csv
├── scripts/               ← Python scripts
│   ├── generate_visualizations.py  ← Main script
│   └── test_data.py                ← Data verification
├── outputs/               ← Generated charts (PNG)
└── docs/                  ← Documentation
    ├── MA_Electricity_Cost_Analysis.md
    └── METHODOLOGY.md
```

## Common Tasks

### Modify the Data

Edit the CSV files in `data/`:
```bash
nano data/electricity_rates.csv
```

Then regenerate visualizations:
```bash
cd scripts
python generate_visualizations.py
```

### Add New Visualizations

Edit `scripts/generate_visualizations.py` and add new functions following the existing patterns.

### Verify Data Changes

After modifying data:
```bash
cd scripts
python test_data.py
```

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'pandas'`
**Solution**: Install dependencies: `pip install -r requirements.txt`

**Issue**: `FileNotFoundError: ../data/electricity_rates.csv`
**Solution**: Make sure you're running scripts from the `scripts/` directory

**Issue**: Charts look wrong after data changes
**Solution**: Delete old charts first: `rm -f ../outputs/*.png` then regenerate

## Next Steps

1. Read the full analysis: `docs/MA_Electricity_Cost_Analysis.md`
2. Understand the methodology: `docs/METHODOLOGY.md`
3. Explore the data files in `data/`
4. Customize visualizations in `scripts/generate_visualizations.py`

## Questions?

- Check `README.md` for detailed documentation
- Review `METHODOLOGY.md` for data sources and calculations
- Open an issue on GitHub for bugs or questions
