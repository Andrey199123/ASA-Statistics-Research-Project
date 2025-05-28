import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('orders_with_department.csv')
df['order_hour_of_day'] = pd.to_numeric(df['order_hour_of_day'], errors='coerce')
df = df.dropna(subset=['department', 'order_hour_of_day'])
df = df[~df['department'].isin(['missing', 'other'])]

overall_mean = df['order_hour_of_day'].mean()

dept_means = (
    df.groupby('department')['order_hour_of_day']
    .mean()
    .reset_index()
    .rename(columns={'order_hour_of_day': 'Department Mean Hour'})
)

dept_means = dept_means.sort_values('Department Mean Hour')
overall_row = pd.DataFrame([{'department': 'Overall', 'Department Mean Hour': overall_mean}])
combined = pd.concat([overall_row, dept_means], ignore_index=True)

table_data = [[row['department'], f"{row['Department Mean Hour']:.2f}"] for _, row in combined.iterrows()]

fig, ax = plt.subplots(figsize=(10, len(combined) * 0.4))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=table_data,
                 colLabels=["Department", "Mean Order Hour"],
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title("Mean Hour of Day Orders Are Placed (Overall and by Department)", pad=20, fontsize=14)
plt.tight_layout()
plt.show()