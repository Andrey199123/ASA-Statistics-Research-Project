import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_csv('products.csv')
order_products_prior = pd.read_csv('order_products__prior.csv')
aisles = pd.read_csv('aisles.csv')
orders = pd.read_csv('orders.csv')


orders['order_hour_of_day'] = pd.to_numeric(orders['order_hour_of_day'], errors='coerce')

merged = (
    order_products_prior
    .merge(products, on='product_id')
    .merge(aisles, on='aisle_id')
    .merge(orders[['order_id', 'order_hour_of_day']], on='order_id')
)

aisle_hour_counts = (
    merged.groupby(['aisle', 'order_hour_of_day'])
    .size()
    .reset_index(name='count')
)

aisles_list = aisle_hour_counts['aisle'].unique()

for aisle_name in sorted(aisles_list):
    subset = aisle_hour_counts[aisle_hour_counts['aisle'] == aisle_name]
    plt.figure(figsize=(8, 4))
    plt.plot(subset['order_hour_of_day'], subset['count'], marker='o')
    plt.title(f'Orders by Hour for Aisle: {aisle_name}')
    plt.xlabel('Hour of Day')
    plt.ylabel('Order Count')
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()