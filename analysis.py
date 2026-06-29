import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_accelerators.csv")
plt.figure(figsize=(10,6))
plt.bar(df["Accelerator"], df["Memory_GB"])
plt.title("Memory Capacity of AI Accelerators")
plt.xlabel("Accelerator")
plt.ylabel("Memory (GB)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/memory.png")
plt.show()