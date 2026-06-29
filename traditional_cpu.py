import numpy as np
import matplotlib.pyplot as plt

# 1. Read the data using NumPy
data = np.genfromtxt('traditional_cpu.csv', delimiter=',', dtype=str, skip_header=1)

# Extract the Processor names (Col 0), Release Years (Col 1), and Core Counts (Col 2)
processors = data[:, 0]
years = data[:, 1]
core_counts = data[:, 2].astype(int)

# 2. Combine Processor Name and Year for the x-axis labels
combined_labels = [f"{p} ({y})" for p, y in zip(processors, years)]

# 3. Set up the figure dimensions
plt.figure(figsize=(12, 7))

# Create the formal 'cividis' color palette
colors = plt.cm.cividis(np.linspace(0.15, 0.9, len(combined_labels)))

# 4. Create the bar graph using the new combined labels
bars = plt.bar(combined_labels, core_counts, color=colors, edgecolor='black', linewidth=1)

# 5. Format the graph
plt.title('Evolution of Processor Core Counts by Year', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Processor Model (Release Year)', fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel('Core Count', fontsize=12, fontweight='bold', labelpad=10)

# Rotate labels by 45 degrees so they don't overlap
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(fontsize=11)

# Add horizontal gridlines
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Increase y-axis limit slightly for top labels
plt.ylim(0, max(core_counts) * 1.1)

# Add exact numerical values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 2,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()

# 6. Save the image as a new PNG
plt.savefig('processor_core_counts_with_year.png', dpi=300, bbox_inches='tight')

print("Image successfully saved as 'processor_core_counts_with_year.png'")