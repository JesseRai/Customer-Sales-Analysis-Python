import matplotlib.pyplot as plt
import pandas
import seaborn as sns

# Set themes with Seaborn
sns.set_theme(style='darkgrid')

# load the dataset
df = pandas.read_csv('/Users/jesserai/Downloads/Sample - Superstore 2.csv', encoding='latin1')

# Convert order date to datetime
df['Order Date'] = pandas.to_datetime(df['Order Date'])

# Add a month column for the grouping
df['Month'] = df['Order Date'].dt.to_period('M')

# Monthly sales trend
plt.figure(figsize=(10,6))
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend (2014-2017)', fontsize=14)
plt.ylabel('Total Sales ($)')
plt.xlabel('Order Month')
plt.show()

# Revenue by customer
plt.figure(figsize=(10,6))
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind='barh', title='Top 10 Customers by Revenue')
plt.xlabel('Total Sales ($)')
plt.show()

# Sales by category
plt.figure(figsize=(10,6))
category_sales = df.groupby('Category')['Sales'].sum()
sns.barplot(x=category_sales.index, y=category_sales.values, palette='viridis')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
total_sales = category_sales.sum()
for i, v in enumerate(category_sales.values):
    percent = (v / total_sales) * 100
    label = f"${v:,.0f}\n({percent:.1f}%)"
    plt.text(i, v + 10000, label, ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# Create pivot table: Region (rows) x Category (columns)
pivot = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')

# Plot heatmap
plt.figure(figsize=(10,6))
sns.heatmap(pivot,annot=True, fmt='.0f', cmap='YlGnBu')
plt.title('Sales by Region and Category')
plt.xlabel('Category')
plt.ylabel('Region')
plt.tight_layout()
plt.show()
