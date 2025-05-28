import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders_with_department.csv')

df['order_hour_of_day'] = pd.to_numeric(df['order_hour_of_day'], errors='coerce')

hourly_counts = (
    df
    .groupby('order_hour_of_day')
    .size()
    .reset_index(name='count')
)


plt.figure(figsize=(10, 6))
plt.bar(hourly_counts['order_hour_of_day'], hourly_counts['count'], color='skyblue')
plt.title('Total Order Counts by Hour (All Departments Combined)')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()