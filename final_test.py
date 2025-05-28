import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal, rankdata, chi2

df = pd.read_csv('orders_with_department.csv')
df['order_hour_of_day'] = pd.to_numeric(df['order_hour_of_day'], errors='coerce')
df = df.dropna(subset=['department', 'order_hour_of_day'])
df = df[~df['department'].isin(['missing', 'other'])]

overall_mean = df['order_hour_of_day'].mean()
print(f"\nGlobal mean order hour across all departments: {overall_mean:.2f}\n")

group_stats = (
    df.groupby('department')['order_hour_of_day']
    .agg(['mean', 'count'])
    .rename(columns={'mean': 'group_mean', 'count': 'n'})
)

print("Number of orders per department:")
print(group_stats[['n']].sort_values('n', ascending=False))

grouped = df.groupby('department')['order_hour_of_day'].apply(list)
valid_groups = {dept: vals for dept, vals in grouped.items() if len(vals) >= 3}

# Run Kruskal-Wallis test
stat, p_value = kruskal(*valid_groups.values())

formatted_p_value = format(p_value, ".2e")

print("\nKruskal–Wallis H-statistic:", stat)
print("Kruskal–Wallis p-value:", formatted_p_value)
# Decision to reject or fail to reject the null
if p_value < 0.05:
    print("Reject H₀: At least one department has a different distribution of order times.")
else:
    print("Fail to reject H₀: No significant difference between departments.")

all_values = []
group_labels = []
for dept, values in valid_groups.items():
    all_values.extend(values)
    group_labels.extend([dept] * len(values))

ranks = rankdata(all_values)
rank_df = pd.DataFrame({'department': group_labels, 'rank': ranks})

n_total = len(ranks)
grand_mean_rank = (n_total + 1) / 2
rank_variance = (n_total**2 - 1) / 12
adjustment_factor = (n_total - 1) / n_total

normalized_contribs = []

for dept, group in rank_df.groupby('department'):
    n_i = len(group)
    mean_rank = group['rank'].mean()
    raw = n_i * (mean_rank - grand_mean_rank) ** 2
    normalized = (raw / rank_variance) * adjustment_factor
    normalized_contribs.append((dept, normalized))

normalized_contribs.sort(key=lambda x: x[1], reverse=True)

fig, ax = plt.subplots(figsize=(10, len(normalized_contribs) * 0.4))
ax.axis('tight')
ax.axis('off')

table_data = [[dept, f"{contrib:.2f}"] for dept, contrib in normalized_contribs]
table = ax.table(cellText=table_data,
                 colLabels=["Department", "Contribution to H"],
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Normalized Department Contributions to Kruskal–Wallis H-statistic", pad=20, fontsize=14)
plt.tight_layout()
plt.show()