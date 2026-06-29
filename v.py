import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("v.csv")

# Create figure
plt.figure(figsize=(11,6))

# Plot line
plt.plot(
    df["Model"],
    df["Parameters_Billion"],
    marker='o',
    linewidth=2.5,
    markersize=8,
    color='royalblue'
)

# Logarithmic Y-axis
plt.yscale('log')

# Add value labels
for i, row in df.iterrows():
    plt.text(
        i,
        row["Parameters_Billion"] * 1.15,
        f'{row["Parameters_Billion"]}',
        ha='center',
        fontsize=9,
        fontweight='bold'
    )

# Formatting
plt.title(
    "Growth of AI Model Parameters (2012–2024)",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("AI Models", fontsize=12)
plt.ylabel("Parameters (Billions, Log Scale)", fontsize=12)

plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.xticks(rotation=30)

plt.tight_layout()

# Save high-quality image
plt.savefig(
    "ai_model_parameters_log.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()