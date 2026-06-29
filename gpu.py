import numpy as np
import matplotlib.pyplot as plt

# 1. Read the data from gpu.csv using NumPy
# We skip the header row and load everything as strings first
data = np.genfromtxt('gpu.csv', delimiter=',', dtype=str, skip_header=1)

# Extract the columns and convert numerical columns to floats
years = data[:, 0]
gpus = data[:, 1]
tflops = data[:, 2].astype(float)
bandwidth = data[:, 3].astype(float)

# Combine GPU and Year for x-axis labels
labels = [f"{g} ({y})" for g, y in zip(gpus, years)]

x = np.arange(len(labels))
width = 0.35  # Set the width of the bars

# 2. Create figure and primary axes
fig, ax1 = plt.subplots(figsize=(12, 7))

# 3. Plotting TFLOPS on the primary (left) y-axis
color1 = '#1f77b4'  # Formal Blue
ax1.set_xlabel('GPU Model (Year)', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_ylabel('Dense TFLOPS (FP16)', color=color1, fontsize=12, fontweight='bold', labelpad=10)

# Shift the blue bars slightly to the left
bars1 = ax1.bar(x - width/2, tflops, width, label='Dense TFLOPS', color=color1, edgecolor='black', linewidth=1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, max(tflops) * 1.15)  # Leave 15% padding at the top for labels

# 4. Create a secondary (right) y-axis for Bandwidth
ax2 = ax1.twinx()
color2 = '#ff7f0e'  # Formal Orange
ax2.set_ylabel('Bandwidth (TB/s)', color=color2, fontsize=12, fontweight='bold', labelpad=10)

# Shift the orange bars slightly to the right
bars2 = ax2.bar(x + width/2, bandwidth, width, label='Bandwidth', color=color2, edgecolor='black', linewidth=1)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(0, max(bandwidth) * 1.15)  # Leave 15% padding at the top for labels

# 5. Set X-axis ticks and rotate labels
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right', fontsize=11)

# 6. Add exact numerical value labels on top of the bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + (max(tflops)*0.02), 
             f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color=color1)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + (max(bandwidth)*0.02), 
             f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color=color2)

# 7. Add Title and Legends
plt.title('GPU Evolution: Compute (TFLOPS) vs. Memory Bandwidth', fontsize=16, fontweight='bold', pad=15)

# Combine legends from both axes into one box in the upper left
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=11, framealpha=0.9)

# Adjust layout so nothing is cut off
fig.tight_layout()

# 8. Save the high-resolution image
plt.savefig('gpu_performance_evolution.png', dpi=300, bbox_inches='tight')
print("Image successfully saved as 'gpu_performance_evolution.png'")