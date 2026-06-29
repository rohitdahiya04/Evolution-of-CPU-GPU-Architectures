import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("hsa_1.csv")

fig, ax = plt.subplots(figsize=(15, 4))

# Draw horizontal timeline
ax.hlines(1, df["Year"].min(), df["Year"].max(),
          color='black', linewidth=2)

# Plot milestones
ax.scatter(
    df["Year"],
    [1]*len(df),
    s=180,
    color='royalblue',
    edgecolors='black',
    zorder=3
)

# Add year below
for i, row in df.iterrows():
    ax.text(
        row["Year"],
        0.87,
        str(row["Year"]),
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

# Add architecture above
for i, row in df.iterrows():
    ax.text(
        row["Year"],
        1.13,
        row["Architecture"],
        ha='center',
        rotation=35,
        fontsize=9
    )

# Clean up axes
ax.set_ylim(0.6, 1.35)
ax.set_xlim(1998, 2026)

ax.set_yticks([])
ax.set_xticks([])

ax.set_title(
    "Evolution of Heterogeneous Computing Architectures",
    fontsize=16,
    fontweight='bold'
)

# Remove borders
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()

plt.savefig(
    "heterogeneous_evolution_timeline.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()