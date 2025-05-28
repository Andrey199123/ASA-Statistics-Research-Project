import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders_with_department.csv')


df['order_hour_of_day'] = pd.to_numeric(df['order_hour_of_day'], errors='coerce')

grouped = (
    df
    .groupby(['department', 'order_hour_of_day'])
    .size()
    .reset_index(name='count')
)

for dept in grouped['department'].unique():
    dept_data = grouped[grouped['department'] == dept]
    plt.figure(figsize=(8, 4))
    plt.bar(dept_data['order_hour_of_day'], dept_data['count'])
    plt.title(f'Order Counts by Hour — {dept}')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Orders')
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.show()