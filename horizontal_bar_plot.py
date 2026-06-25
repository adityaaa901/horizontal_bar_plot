import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [25, 35, 20, 40, 30]
}

df = pd.DataFrame(data)

# Create horizontal bar plot
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'purple']
bars = ax.barh(df['Category'], df['Values'], color=colors, edgecolor='black', linewidth=1.5)

# Customize plot
ax.set_xlabel('Values', fontweight='bold', fontsize=12)
ax.set_ylabel('Category', fontweight='bold', fontsize=12)
ax.set_title('Horizontal Bar Graph', fontweight='bold', fontsize=14)
ax.grid(axis='x', alpha=0.3)

# Add value labels at the end of bars
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f'{int(width)}',
            ha='left', va='center', fontweight='bold', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

plt.tight_layout()
plt.show()
