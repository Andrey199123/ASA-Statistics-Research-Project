import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('orders_with_department.csv')

department_counts = df['department'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
department_counts.plot(kind='bar')
plt.title('Frequency of Each Department in Orders')
plt.xlabel('Department')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()