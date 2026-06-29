import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("hsa.csv")

# Colors
colors = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728"   # Red
]

# Figure
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(
    "Evolution of GPU Architecture Characteristics",
    fontsize=18,
    fontweight='bold'
)

# -----------------------------
# (a) Compute Performance
# -----------------------------
bars = axs[0,0].bar(
    df["Platform"],
    df["TFLOPS"],
    color=colors[0],
    edgecolor='black'
)

axs[0,0].set_title("(a) Compute Performance")
axs[0,0].set_ylabel("TFLOPS")

for bar in bars:
    axs[0,0].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():,.0f}',
        ha='center',
        va='bottom',
        fontsize=8
    )

# -----------------------------
# (b) Memory Bandwidth
# -----------------------------
bars = axs[0,1].bar(
    df["Platform"],
    df["Bandwidth_TBps"],
    color=colors[1],
    edgecolor='black'
)

axs[0,1].set_title("(b) Memory Bandwidth")
axs[0,1].set_ylabel("TB/s")

for bar in bars:
    axs[0,1].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():.2f}',
        ha='center',
        va='bottom',
        fontsize=8
    )

# -----------------------------
# (c) Memory Capacity
# -----------------------------
bars = axs[1,0].bar(
    df["Platform"],
    df["Memory_GB"],
    color=colors[2],
    edgecolor='black'
)

axs[1,0].set_title("(c) Memory Capacity")
axs[1,0].set_ylabel("GB")

for bar in bars:
    axs[1,0].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():.0f}',
        ha='center',
        va='bottom',
        fontsize=8
    )

# -----------------------------
# (d) Thermal Design Power
# -----------------------------
bars = axs[1,1].bar(
    df["Platform"],
    df["TDP_Watts"],
    color=colors[3],
    edgecolor='black'
)

axs[1,1].set_title("(d) Thermal Design Power")
axs[1,1].set_ylabel("Watts")

for bar in bars:
    axs[1,1].text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():.0f}',
        ha='center',
        va='bottom',
        fontsize=8
    )

# Common Formatting
for ax in axs.flat:
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.tick_params(axis='x', rotation=30)

plt.tight_layout(rect=[0,0,1,0.96])

plt.savefig(
    "gpu_architecture_characteristics.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()