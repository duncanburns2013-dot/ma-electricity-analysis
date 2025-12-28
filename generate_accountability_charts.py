#!/usr/bin/env python3
"""
Massachusetts Electricity Cost Analysis - Accountability Charts
Generate visualizations showing legislative mandates vs. utility costs

This script creates charts to counter the narrative that utilities are responsible
for high electricity costs, when the data shows legislative mandates are the
primary driver.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Color scheme
COLORS = {
    'policy': '#e53935',      # Red - Policy mandates
    'utility': '#1976d2',     # Blue - Utility costs
    'healey': '#c62828',      # Dark red - What Healey blames
    'truth': '#2e7d32',       # Green - The truth
    'warning': '#ff6f00',     # Orange - Warnings
    'info': '#fff59d',        # Yellow - Information boxes
}

def create_who_is_responsible_chart(output_path='who_is_responsible.png'):
    """
    Create side-by-side comparison showing what Governor Healey blames
    vs. what the data actually shows
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'WHO\'S REALLY RESPONSIBLE?', 
            ha='center', fontsize=22, fontweight='bold', color=COLORS['healey'])
    ax.text(5, 9.0, 'Breaking Down the Bill Increase: 2014-2025', 
            ha='center', fontsize=14, color='#333')

    # Left box - What Healey blames
    left_box = mpatches.FancyBboxPatch((0.5, 5.5), 4, 2.8,
                                       boxstyle="round,pad=0.03",
                                       facecolor='#ffebee', 
                                       edgecolor=COLORS['healey'], linewidth=3)
    ax.add_patch(left_box)

    ax.text(2.5, 8.0, 'WHAT HEALEY BLAMES:', 
            ha='center', fontsize=13, fontweight='bold', color=COLORS['healey'])
    ax.text(2.5, 7.5, 'Utility Companies', 
            ha='center', fontsize=16, fontweight='bold', color='#333')

    # Breakdown of what Healey blames
    breakdown_left = [
        ('Distribution', '+25/mo', '27%'),
        ('Transmission', '+14/mo', '15%'),
        ('Supply', '+8/mo', '9%'),
    ]

    y = 6.8
    for item, cost, pct in breakdown_left:
        ax.text(0.9, y, f'{item}:', fontsize=11, color='#666')
        ax.text(4.0, y, f'{cost} ({pct})', fontsize=11, 
                fontweight='bold', ha='right', color='#333')
        y -= 0.4

    ax.text(2.5, 5.7, 'Subtotal: +47/month', ha='center', fontsize=12, 
            fontweight='bold', color=COLORS['healey'],
            bbox=dict(boxstyle='round', facecolor='white', 
                     edgecolor=COLORS['healey'], linewidth=2))

    # Right box - THE REAL CAUSE
    right_box = mpatches.FancyBboxPatch((5.5, 5.5), 4, 2.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#e8f5e9', 
                                        edgecolor=COLORS['truth'], linewidth=3)
    ax.add_patch(right_box)

    ax.text(7.5, 8.0, 'THE REAL DRIVER:', 
            ha='center', fontsize=13, fontweight='bold', color=COLORS['truth'])
    ax.text(7.5, 7.5, 'LEGISLATIVE MANDATES', 
            ha='center', fontsize=16, fontweight='bold', color='#333')

    # Breakdown of real causes
    breakdown_right = [
        ('Mass Save', '+21/mo', '23%'),
        ('RPS/RGGI', '+14/mo', '15%'),
        ('Solar programs', '+9/mo', '10%'),
    ]

    y = 6.8
    for item, cost, pct in breakdown_right:
        ax.text(6.0, y, f'{item}:', fontsize=11, color='#666')
        ax.text(9.0, y, f'{cost} ({pct})', fontsize=11, 
                fontweight='bold', ha='right', color='#333')
        y -= 0.4

    ax.text(7.5, 5.7, 'Subtotal: +44/month', ha='center', fontsize=12, 
            fontweight='bold', color=COLORS['truth'],
            bbox=dict(boxstyle='round', facecolor='white', 
                     edgecolor=COLORS['truth'], linewidth=2))

    # VS in middle
    ax.text(5, 4.7, 'vs', ha='center', fontsize=24, 
            fontweight='bold', style='italic', color='#666')

    # Truth box
    truth_box = mpatches.FancyBboxPatch((1.0, 2.5), 8, 1.8,
                                        boxstyle="round,pad=0.03",
                                        facecolor=COLORS['info'], 
                                        edgecolor='black', linewidth=3)
    ax.add_patch(truth_box)

    ax.text(5, 4.0, 'THE TRUTH', ha='center', fontsize=15, 
            fontweight='bold', color=COLORS['healey'])

    truth_text = """Utilities CANNOT change policy mandates - they only implement what Legislature requires
48% of bill increase comes from LEGISLATIVE MANDATES (not utility decisions)
Distribution/transmission increases fund mandated grid upgrades for renewables"""

    ax.text(5, 3.35, truth_text, ha='center', fontsize=10, 
            color='#333', multialignment='center')

    # Who can fix this
    stats_box = mpatches.FancyBboxPatch((1.0, 0.8), 8, 1.3,
                                        boxstyle="round,pad=0.03",
                                        facecolor='#e3f2fd', 
                                        edgecolor=COLORS['utility'], linewidth=2)
    ax.add_patch(stats_box)

    ax.text(5, 1.85, 'WHO CAN FIX THIS?', ha='center', fontsize=13, 
            fontweight='bold', color=COLORS['utility'])

    fix_text = """CANNOT: Utilities (they only implement legislative mandates)
CAN: Legislature (cap Mass Save, reform RPS, consolidate programs)  
CAN: Governor (propose reform legislation instead of blaming utilities)"""

    ax.text(5, 1.30, fix_text, ha='center', fontsize=10.5, 
            color='#333', multialignment='left', family='monospace')

    # Footer
    ax.text(5, 0.3, 'Source: Eversource rate filings 2014-2025', 
            ha='center', fontsize=9, style='italic', color='#666')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✓ Created {output_path}")
    plt.close()


def create_policy_vs_utility_growth_chart(output_path='policy_vs_utility_growth.png'):
    """
    Create comparison chart showing policy mandates grew 6x faster than utility costs
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    # Data
    years = ['2014', '2016', '2018', '2020', '2022', '2024', '2025']
    policy = [15, 19, 26, 32, 42, 57, 59]
    utility = [98, 110, 122, 115, 142, 155, 145]

    x = np.arange(len(years))
    width = 0.35

    # Side-by-side bars
    bars1 = ax.bar(x - width/2, policy, width, label='Policy Mandates', 
                   color=COLORS['policy'], edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, utility, width, label='Utility Costs', 
                   color=COLORS['utility'], edgecolor='black', linewidth=1.5)

    ax.set_ylabel('Monthly Cost ($)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_title('Policy Mandates vs. Utility Costs', 
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, 180)

    # Summary at bottom
    summary = 'Policy Mandates: +293% (2014-2025)  |  Utility Costs: +48%  |  Policy grew 6x faster'
    ax.text(0.5, -0.15, summary, 
            transform=ax.transAxes, ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=COLORS['info'], 
                     edgecolor='black', linewidth=2))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✓ Created {output_path}")
    plt.close()


def main():
    """
    Generate all accountability charts
    """
    print("Generating accountability charts...")
    print("These charts show that legislative mandates, not utility companies,")
    print("are driving Massachusetts electricity cost increases.\n")
    
    # Create charts
    create_who_is_responsible_chart('who_is_responsible.png')
    create_policy_vs_utility_growth_chart('policy_vs_utility_growth.png')
    
    print("\n✅ All charts created successfully!")
    print("\nThese charts counter Governor Healey's narrative by showing:")
    print("• 48% of bill increases come from legislative mandates")
    print("• Policy costs grew 293% vs. utility costs +48%")
    print("• Utilities cannot change policy mandates set by Legislature")
    print("• Only Legislature can provide meaningful relief")


if __name__ == "__main__":
    main()
