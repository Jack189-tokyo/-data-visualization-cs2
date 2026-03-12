import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Try to import adjustText for optimal text placement (pip install adjustText)
try:
    from adjustText import adjust_text
except ImportError:
    adjust_text = None
    print("Warning: 'adjustText' library not found. Labels may overlap. Please run: pip install adjustText")

def main():
    # File path
    file_path = r'd:\code\数据可视化CS2\hot-dog-contest-winners.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load data
    df = pd.read_csv(file_path)

    # Initialize the plot
    plt.figure(figsize=(14, 9))
    ax = plt.gca()

    # 1. Get record data and sort it chronologically for the new layout
    records = df[df['New record'] == 1].sort_values('Year').reset_index()

    # 2. Plot the base bar chart
    bar_width = 0.6
    plt.bar(df['Year'], df['Dogs eaten'], color='#4CAF50', width=bar_width, label='Winning Performance', alpha=0.8)

    # 3. Plot Single Big Star on top (Only for Records)
    plt.scatter(records['Year'], records['Dogs eaten'], 
                color='#A78BFA', marker='*', s=350, label='New Record', 
                edgecolors='white', linewidth=1.0, zorder=5)

    # 4. Annotate Record Winners
    texts = []
    for _, row in records.iterrows():
        year = row['Year']
        dogs_eaten = row['Dogs eaten']
        label_text = f"{row['Winner'].strip()}\n({dogs_eaten})"
        texts.append(plt.text(year, dogs_eaten, label_text, fontsize=9, fontweight='bold', ha='right', va='bottom'))

    # 5. Prevent Annotation Overlap
    if adjust_text:
        # Use more aggressive parameters to ensure labels do not overlap,
        # especially for closely clustered data points like in 2001/2002 or 2004/2006.
        adjust_text(
            texts,
            force_text=(2.0, 1.5), expand_points=(3.5, 3.5), force_points=(0.5, 0.5), # Prefer left placement
            arrowprops=dict(arrowstyle='->', color='#E2011C', lw=0.7, shrinkA=10, shrinkB=10))

    # 6. Signature in Top-Left
    plt.text(0.02, 0.98, 'Signature: Gemini Code Assist', transform=ax.transAxes,
             fontsize=12, verticalalignment='top', style='italic',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.5'))

    # Titles and Labels
    plt.title('Hot Dog Eating Contest: Winners & New Records', fontsize=18, pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Dogs Eaten', fontsize=12)
    plt.legend(loc='lower right')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()