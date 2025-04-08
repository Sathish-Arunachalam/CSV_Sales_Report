
import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("client_sales_data.csv")

df['sale_date'] = pd.to_datetime(df['sale_date'], format="%d-%m-%Y").dt.date

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",        # or use "127.0.0.1"
    user="root",
    password="Hsisath@1",
    database="p2_sales_db"
)
cursor = conn.cursor()

# Insert Data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO P2_sales_data (product, region, sales_rep, quantity, price, sale_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

# Load Data from SQL
query = "SELECT * FROM P2_sales_data"
df = pd.read_sql(query, conn)

# Show Top 5 Rows
print("Sample Data:\n", df.head())

# Total Sales Amount
df['total'] = df['quantity'] * df['price']
total_sales = df['total'].sum()
print("\nTotal Sales: ₹", round(total_sales, 2))

# Sales by Region
region_sales = df.groupby('region')['total'].sum().reset_index()
print("\nSales by Region:\n", region_sales)

# Top 3 Sales Reps
top_sales_reps = df.groupby('sales_rep')['total'].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Sales Reps:\n", top_sales_reps)

# Add total sales summary
summary_df = pd.DataFrame({'Metric': ['Total Sales'], 'Value': [total_sales]})
summary_df.to_csv("output_total_sales.csv", index=False)

# Save region-wise sales to CSV
region_sales.to_csv("output_sales_by_region.csv", index=False)

# Save top 3 sales reps to CSV
top_sales_reps_df = top_sales_reps.reset_index()
top_sales_reps_df.columns = ['sales_rep', 'total_sales']
top_sales_reps_df.to_csv("output_top_sales_reps.csv", index=False)


cursor.close()
conn.close()
