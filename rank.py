import pandas as pd
from scipy.stats import rankdata
import matplotlib.pyplot as plt

df = pd.read_csv('orders_with_department.csv')
df['order_hour_of_day'] = pd.to_numeric(df['order_hour_of_day'], errors='coerce')
df = df.dropna(subset=['department', 'order_hour_of_day'])
df = df[~df['department'].isin(['missing', 'other'])]

grouped = df.groupby('department')['order_hour_of_day'].apply(list)
valid_groups = {dept: vals for dept, vals in grouped.items() if len(vals) >= 3}

all_values = []
group_labels = []
for dept, values in valid_groups.items():
    all_values.extend(values)
    group_labels.extend([dept] * len(values))

ranks = rankdata(all_values)
rank_df = pd.DataFrame({'department': group_labels, 'rank': ranks})

mean_ranks = (
    rank_df.groupby('department')['rank']
    .mean()
    .reset_index()
    .rename(columns={'rank': 'Average Rank'})
    .sort_values(by='Average Rank')
)

fig, ax = plt.subplots(figsize=(10, len(mean_ranks) * 0.4))
ax.axis('tight')
ax.axis('off')
table_data = [[dept, f"{avg_rank:.1f}"] for dept, avg_rank in zip(mean_ranks['department'], mean_ranks['Average Rank'])]
table = ax.table(cellText=table_data,
                 colLabels=["Department", "Average Rank"],
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Average Rank of Order Hour by Department", pad=20, fontsize=14)
plt.tight_layout()
plt.show()