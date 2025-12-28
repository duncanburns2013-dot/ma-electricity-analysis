# Massachusetts Electricity Accountability Charts

Python script to generate charts showing that **legislative mandates**, not utility companies, are driving Massachusetts electricity cost increases.

## Purpose

These charts counter Governor Healey's narrative that utilities are to blame for high electricity costs. The data shows that legislative mandates (Mass Save, RPS, RGGI, solar programs) have grown 6x faster than utility operational costs.

## Charts Generated

### 1. Who's Really Responsible?
Side-by-side comparison showing:
- **What Governor Healey Blames:** Utility companies (+$47/month)
- **The Real Driver:** Legislative mandates (+$44/month)
- **The Truth:** Utilities cannot change mandates set by Legislature

### 2. Policy vs. Utility Growth
Bar chart showing growth from 2014-2025:
- **Policy Mandates:** +293% growth
- **Utility Costs:** +48% growth
- **Conclusion:** Policy grew 6x faster

## Requirements

```bash
pip install matplotlib numpy
```

## Usage

```bash
python generate_accountability_charts.py
```

This will generate:
- `who_is_responsible.png`
- `policy_vs_utility_growth.png`

## Key Findings

| Component | 2014 | 2025 | Growth | Annual Rate |
|-----------|------|------|--------|-------------|
| **Policy Mandates** | $15/mo | $59/mo | **+293%** | **13.1%/year** |
| Utility Operations | $98/mo | $145/mo | +48% | 3.6%/year |

**Finding:** 48% of the total bill increase comes from legislative mandates that utilities are required by law to implement.

## The Problem with Healey's Narrative

Governor Healey has called for:
> "Rigorously scrutinize utility investments"
> "Hold companies accountable for controlling spending"

**Why this misses the point:**
- Utilities don't set Mass Save budgets ($1.5B/year) - Legislature does
- Utilities can't refuse RPS compliance - it's mandated by statute
- Utilities can't opt out of RGGI - it's required by law
- DPU cannot override legislative mandates

## Who Can Actually Fix This?

❌ **CANNOT Fix:**
- Utilities (only implement mandates)
- DPU (cannot override statutes)

✅ **CAN Fix:**
- **Legislature** - Cap Mass Save, reform RPS, consolidate programs
- **Governor** - Propose reform legislation (instead of blaming utilities)

## Data Sources

- Eversource rate filings (2014-2025)
- Massachusetts DPU rate cases
- Fiscal Alliance Foundation White Paper (November 2025)

## Use Cases

**For Advocacy:**
- Share on social media to counter utility-blaming narrative
- Use in presentations to legislators
- Include in testimony at DPU hearings

**For Media:**
- Illustrate the real source of cost increases
- Provide data-driven counterpoint to political rhetoric

**For Research:**
- Document the impact of legislative mandates
- Compare policy vs. operational cost growth

## Customization

Edit the script to:
- Change colors (see `COLORS` dictionary)
- Adjust chart dimensions
- Modify output file names
- Add additional data points

## License

Data compiled from public sources. Visualizations provided for educational and advocacy purposes.

## Citation

If using these charts, please cite:
> "Massachusetts Electricity Costs: The Real Source of the Problem"  
> Fiscal Alliance Foundation White Paper, November 2025  
> Cross-referenced with Eversource rate filings 2014-2025

## Contact

For questions about the underlying data or methodology, see the full analysis documentation.

---

**Bottom Line:** Governor Healey is blaming utilities for implementing the very mandates her administration supports. The data is clear: legislative policy, not utility management, is driving costs.
