import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("vi.csv")

# Colors for each subplot
colors = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728"   # Red
]

# Create figure
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(
    "Comparison of Modern AI Heterogeneous Computing Platforms",
    fontsize=18,
    fontweight='bold'
)

# -------------------------------------------------
# (a) Memory Capacity
# -------------------------------------------------

bars = axs[0,0].bar(
    df["Platform"],
    df["Memory_GB"],
    color=colors[0],
    edgecolor="black"
)

axs[0,0].set_title("(a) Memory Capacity")
axs[0,0].set_ylabel("Memory (GB)")

for bar in bars:
    axs[0,0].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+5,
        f"{bar.get_height():.0f}",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# -------------------------------------------------
# (b) Memory Bandwidth
# -------------------------------------------------

bars = axs[0,1].bar(
    df["Platform"],
    df["Bandwidth_TBps"],
    color=colors[1],
    edgecolor="black"
)

axs[0,1].set_title("(b) Memory Bandwidth")
axs[0,1].set_ylabel("Bandwidth (TB/s)")

for bar in bars:
    axs[0,1].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.1,
        f"{bar.get_height():.1f}",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# -------------------------------------------------
# (c) AI Compute
# -------------------------------------------------

bars = axs[1,0].bar(
    df["Platform"],
    df["AI_TFLOPS"],
    color=colors[2],
    edgecolor="black"
)

axs[1,0].set_title("(c) AI Compute Performance")
axs[1,0].set_ylabel("Dense FP16/BF16 TFLOPS")

for bar in bars:
    axs[1,0].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+50,
        f"{bar.get_height():,.0f}",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# -------------------------------------------------
# (d) Thermal Design Power
# -------------------------------------------------

bars = axs[1,1].bar(
    df["Platform"],
    df["TDP"],
    color=colors[3],
    edgecolor="black"
)

axs[1,1].set_title("(d) Thermal Design Power")
axs[1,1].set_ylabel("Power (Watts)")

for bar in bars:
    axs[1,1].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+20,
        f"{bar.get_height():.0f}",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# -------------------------------------------------
# Common Formatting
# -------------------------------------------------

for ax in axs.flat:
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.tick_params(axis="x", rotation=20)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig(
    "modern_ai_platforms.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()