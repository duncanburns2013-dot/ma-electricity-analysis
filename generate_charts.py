import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0d0d0d')
ax.set_facecolor('#0d0d0d')

# Data - EIA verified
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
ma_rates = [18.8, 19.8, 21.5, 21.8, 24.7, 25.5, 24.5, 24.5, 30.7, 29.2, 35.3, 31.4]
us_rates = [12.5, 12.7, 12.6, 12.9, 13.0, 13.0, 13.2, 13.7, 15.1, 16.2, 16.8, 18.0]

# Plot lines
ax.plot(years, ma_rates, color='#ef4444', linewidth=4, marker='o', markersize=10, label='Massachusetts', zorder=5)
ax.plot(years, us_rates, color='#22c55e', linewidth=4, marker='s', markersize=10, label='U.S. Average', zorder=5)

# Fill between to show the gap
ax.fill_between(years, us_rates, ma_rates, alpha=0.2, color='#ef4444')

# Annotations
ax.annotate('Gap: 6.3¢', xy=(2014, 15.5), fontsize=11, color='#fbbf24', fontweight='bold', ha='center')
ax.annotate('Gap: 13.4¢', xy=(2025, 24.5), fontsize=11, color='#fbbf24', fontweight='bold', ha='center')
ax.annotate('GAP\nDOUBLED', xy=(2019.5, 19), fontsize=14, color='#fbbf24', fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1f1f1f', edgecolor='#fbbf24', linewidth=2))

# Styling
ax.set_xlim(2013.5, 2025.5)
ax.set_ylim(10, 40)
ax.set_xlabel('Year', fontsize=14, color='white', fontweight='bold')
ax.set_ylabel('Residential Rate (¢/kWh)', fontsize=14, color='white', fontweight='bold')
ax.tick_params(colors='white', labelsize=12)
ax.grid(True, alpha=0.2, color='white')

# Spines
for spine in ax.spines.values():
    spine.set_color('#404040')

# Legend
legend = ax.legend(loc='upper left', fontsize=12, facecolor='#1f1f1f', edgecolor='#404040', labelcolor='white')

# Title
fig.suptitle('MA vs. U.S. Electricity Rates (2014-2025)', fontsize=22, fontweight='bold', color='white', y=0.96)
ax.set_title('Source: U.S. Energy Information Administration | MA rates grew 67% vs 44% nationally', 
             fontsize=11, color='#a0a0a0', pad=10)

# Stats boxes at bottom
stats_y = 0.02
fig.text(0.2, stats_y, '+67%\nMA Growth', ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#dc2626', edgecolor='none'))
fig.text(0.4, stats_y, '+44%\nUS Growth', ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#16a34a', edgecolor='none'))
fig.text(0.6, stats_y, '+74%\nMA Premium', ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#7c3aed', edgecolor='none'))
fig.text(0.8, stats_y, '$963/yr\nExtra Cost', ha='center', fontsize=14, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#d97706', edgecolor='none'))

plt.tight_layout(rect=[0, 0.08, 1, 0.94])
plt.savefig('/mnt/user-data/outputs/chart1_rates_over_time.png', dpi=150, facecolor='#0d0d0d', edgecolor='none', bbox_inches='tight')
plt.close()
print("Chart 1 saved!")
-e 

# ========== CHART 2 ==========

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0d0d0d')
ax.set_facecolor('#0d0d0d')

# Data
categories = ['Policy Mandates\n(Mass Save, RPS, RGGI, Solar)', 'Utility Costs', 'Inflation']
growth = [293, 48, 32]
colors = ['#ef4444', '#3b82f6', '#6b7280']

# Horizontal bar chart
bars = ax.barh(categories, growth, color=colors, height=0.6, edgecolor='white', linewidth=1)

# Add value labels
for bar, val in zip(bars, growth):
    ax.text(val + 8, bar.get_y() + bar.get_height()/2, f'+{val}%', 
            va='center', ha='left', fontsize=18, fontweight='bold', color='white')

# Styling
ax.set_xlim(0, 350)
ax.set_xlabel('Growth Since 2014 (%)', fontsize=14, color='white', fontweight='bold')
ax.tick_params(colors='white', labelsize=13)
ax.invert_yaxis()

for spine in ax.spines.values():
    spine.set_color('#404040')

ax.axvline(x=32, color='#fbbf24', linestyle='--', linewidth=2, alpha=0.7, label='Inflation baseline')

# Title
fig.suptitle('THE GASLIGHTING: What They Say vs Reality', fontsize=22, fontweight='bold', color='white', y=0.96)
ax.set_title('Policy grew 9x FASTER than inflation — but they blame utilities!', 
             fontsize=13, color='#fbbf24', pad=15, fontweight='bold')

# Quote box
quote_text = '"Mass Save is a much smaller percentage of the bill\ncompared to what is being driven by Eversource and National Grid"'
fig.text(0.5, 0.02, quote_text, ha='center', fontsize=11, color='#fbbf24', style='italic',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#1f1f1f', edgecolor='#fbbf24', linewidth=2))
fig.text(0.5, -0.04, '— Rep. Erika Uyterhoeven (D-Somerville)', ha='center', fontsize=10, color='#a0a0a0')

# Reality boxes
fig.text(0.18, 0.18, 'UTILITY PROFIT\n~10% of bill\n(Regulated margin)', ha='center', fontsize=11, color='white',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#1e40af', edgecolor='#3b82f6', linewidth=2))
fig.text(0.82, 0.18, 'POLICY MANDATES\n17% of bill\n("Public Benefits")', ha='center', fontsize=11, color='white',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#991b1b', edgecolor='#ef4444', linewidth=2))

plt.tight_layout(rect=[0, 0.12, 1, 0.92])
plt.savefig('/mnt/user-data/outputs/chart2_gaslighting_growth.png', dpi=150, facecolor='#0d0d0d', edgecolor='none', bbox_inches='tight')
plt.close()
print("Chart 2 saved!")
-e 

# ========== CHART 3 ==========

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure with two subplots
fig = plt.figure(figsize=(14, 8), facecolor='#0d0d0d')

# Left side - Pie chart
ax1 = fig.add_axes([0.05, 0.15, 0.45, 0.65])

# VERIFIED Eversource breakdown (Dec 2025)
labels = ['Supply\n40%', 'Distribution\n30%', 'Public Benefits\n17%', 'Transmission\n13%']
sizes = [40, 30, 17, 13]
colors = ['#3b82f6', '#22c55e', '#ef4444', '#8b5cf6']
explode = (0, 0, 0.08, 0)  # Explode the Public Benefits slice

wedges, texts = ax1.pie(sizes, explode=explode, colors=colors, startangle=90,
                         wedgeprops=dict(width=0.6, edgecolor='white', linewidth=2))

# Add percentage labels manually for better control
for i, (wedge, label, size) in enumerate(zip(wedges, labels, sizes)):
    ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    x = np.cos(np.deg2rad(ang))
    y = np.sin(np.deg2rad(ang))
    
    # Position for label
    label_x = 0.7 * x
    label_y = 0.7 * y
    
    ax1.annotate(label, xy=(label_x, label_y), ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

ax1.set_title('Official Eversource\nBill Breakdown', fontsize=16, fontweight='bold', color='white', pad=10)

# Right side - Real bills bar chart
ax2 = fig.add_axes([0.55, 0.15, 0.4, 0.65])
ax2.set_facecolor('#0d0d0d')

# Real bill data with 17% policy charges
bills = ['$427 Bill\n(Easthampton 2BR)', '$709 Bill\n(Billerica home)', '$853 Bill\n(Stoughton w/ solar!)']
policy_charges = [73, 121, 145]
total_bills = [427, 709, 853]

y_pos = np.arange(len(bills))

# Stacked bars - policy vs rest
rest = [t - p for t, p in zip(total_bills, policy_charges)]
bars1 = ax2.barh(y_pos, rest, color='#404040', height=0.5, label='Other charges')
bars2 = ax2.barh(y_pos, policy_charges, left=rest, color='#ef4444', height=0.5, label='Policy (17%)')

# Add labels
for i, (r, p, t) in enumerate(zip(rest, policy_charges, total_bills)):
    ax2.text(t + 20, i, f'${p}/mo\nto policy!', va='center', ha='left', 
             fontsize=12, fontweight='bold', color='#ef4444')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(bills, fontsize=11, color='white')
ax2.set_xlabel('Monthly Bill ($)', fontsize=12, color='white', fontweight='bold')
ax2.set_xlim(0, 1000)
ax2.tick_params(colors='white', labelsize=10)
ax2.invert_yaxis()

for spine in ax2.spines.values():
    spine.set_color('#404040')

ax2.legend(loc='lower right', fontsize=10, facecolor='#1f1f1f', edgecolor='#404040', labelcolor='white')
ax2.set_title('Real MA Bills → Policy Charges', fontsize=16, fontweight='bold', color='white', pad=10)

# Main title
fig.suptitle('Where Your Electric Bill ACTUALLY Goes', fontsize=24, fontweight='bold', color='white', y=0.97)

# Subtitle
fig.text(0.5, 0.91, '17% labeled "Public Benefits" = Policy Mandates you pay every month', 
         ha='center', fontsize=13, color='#fbbf24', fontweight='bold')

# Source
fig.text(0.5, 0.03, 'Source: Eversource Official Breakdown (Dec 2025, Western Mass News) • Real bills from WCVB, WBUR, Boston Globe',
         ha='center', fontsize=10, color='#808080')

# Bottom callout
fig.text(0.5, 0.08, 'They call it "Public Benefits" — but you didn\'t vote for $145/month in policy charges!',
         ha='center', fontsize=13, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#991b1b', edgecolor='#ef4444', linewidth=2))

plt.savefig('/mnt/user-data/outputs/chart3_bill_breakdown.png', dpi=150, facecolor='#0d0d0d', edgecolor='none', bbox_inches='tight')
plt.close()
print("Chart 3 saved!")
-e 

# ========== CHART 4 ==========

import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 9), facecolor='#0d0d0d')
ax.set_facecolor('#0d0d0d')

# Data - EIA October 2025 - Focus on expensive states and US avg
states = ['Hawaii', 'California', 'MASSACHUSETTS', 'Rhode Island', 'Maine', 'Connecticut', 'New Hampshire', 'New York', 'Vermont', 'U.S. AVERAGE']
rates = [39.74, 33.60, 31.37, 31.16, 29.42, 27.72, 27.27, 26.95, 24.78, 17.98]

# Colors - MA red, US green, New England orange, others gray
colors = []
for state in states:
    if state == 'MASSACHUSETTS':
        colors.append('#ef4444')
    elif state == 'U.S. AVERAGE':
        colors.append('#22c55e')
    elif state in ['Rhode Island', 'Maine', 'Connecticut', 'New Hampshire', 'Vermont']:
        colors.append('#f97316')  # Orange for other New England
    else:
        colors.append('#6b7280')

y_pos = np.arange(len(states))

# Horizontal bars
bars = ax.barh(y_pos, rates, color=colors, height=0.7, edgecolor='white', linewidth=0.5)

# Add value labels - positioned to avoid overlap
for i, (bar, val, state) in enumerate(zip(bars, rates, states)):
    fontweight = 'bold' if state in ['MASSACHUSETTS', 'U.S. AVERAGE'] else 'normal'
    ax.text(val + 0.8, bar.get_y() + bar.get_height()/2, f'{val}¢', 
            va='center', ha='left', fontsize=12, fontweight=fontweight, color='white')

# Reference line for US average
ax.axvline(x=17.98, color='#22c55e', linestyle='--', linewidth=2, alpha=0.8)

# Styling
ax.set_xlim(0, 50)
ax.set_xlabel('Residential Electricity Rate (¢/kWh)', fontsize=14, color='white', fontweight='bold')
ax.set_yticks(y_pos)
ax.set_yticklabels(states, fontsize=13, color='white')
ax.tick_params(colors='white', labelsize=12)
ax.invert_yaxis()

for spine in ax.spines.values():
    spine.set_color('#404040')

# Highlight MA row
ax.axhspan(1.5, 2.5, alpha=0.15, color='#ef4444')

# Title
fig.suptitle('Massachusetts: 3rd Most Expensive Electricity in America', fontsize=22, fontweight='bold', color='white', y=0.96)
ax.set_title('Source: U.S. Energy Information Administration (October 2025)', 
             fontsize=11, color='#a0a0a0', pad=15)

# Single callout box - MA premium
fig.text(0.85, 0.55, 'MA pays\n+74%\nabove\nUS avg', ha='center', fontsize=16, color='white', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.6', facecolor='#dc2626', edgecolor='white', linewidth=2))

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#ef4444', edgecolor='white', label='Massachusetts'),
    Patch(facecolor='#f97316', edgecolor='white', label='Other New England'),
    Patch(facecolor='#22c55e', edgecolor='white', label='U.S. Average'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=11, 
          facecolor='#1f1f1f', edgecolor='#404040', labelcolor='white')

# Bottom note
fig.text(0.5, 0.03, '6 of the 10 most expensive states are in New England — all with similar "green" policies',
         ha='center', fontsize=13, color='#fbbf24', fontweight='bold')

plt.tight_layout(rect=[0, 0.07, 0.92, 0.94])
plt.savefig('/mnt/user-data/outputs/chart4_state_comparison.png', dpi=150, facecolor='#0d0d0d', edgecolor='none', bbox_inches='tight')
plt.close()
print("Chart 4 saved!")
