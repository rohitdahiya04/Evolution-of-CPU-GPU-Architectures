import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("vii.csv")

fig, ax = plt.subplots(figsize=(15,5))

# Draw timeline
ax.hlines(
    y=0,
    xmin=df["Year"].min(),
    xmax=df["Year"].max(),
    color="black",
    linewidth=2
)

# Plot milestones
ax.scatter(
    df["Year"],
    [0]*len(df),
    s=220,
    color="royalblue",
    edgecolor="black",
    linewidth=1.5,
    zorder=3
)

# Alternate labels above and below
for i, row in df.iterrows():

    if i % 2 == 0:
        # Technology above
        ax.vlines(row["Year"], 0, 0.35,
                  linestyle="--",
                  color="gray")

        ax.text(
            row["Year"],
            0.42,
            row["Technology"],
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

        ax.text(
            row["Year"],
            -0.25,
            row["Focus"],
            ha="center",
            fontsize=9,
            color="dimgray"
        )

    else:
        # Technology below
        ax.vlines(row["Year"], -0.35, 0,
                  linestyle="--",
                  color="gray")

        ax.text(
            row["Year"],
            -0.47,
            row["Technology"],
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

        ax.text(
            row["Year"],
            0.22,
            row["Focus"],
            ha="center",
            fontsize=9,
            color="dimgray"
        )

    # Year labels
    ax.text(
        row["Year"],
        -0.08,
        str(row["Year"]),
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# Formatting
ax.set_xlim(2024.5,2035.5)
ax.set_ylim(-0.7,0.7)

ax.set_xticks([])
ax.set_yticks([])

ax.set_title(
    "Projected Evolution of AI-Driven Heterogeneous Computing Architectures",
    fontsize=18,
    fontweight="bold",
    pad=20
)

# Remove borders
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()

plt.savefig(
    "future_roadmap.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()