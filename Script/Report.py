import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Cleaned_sale.xlsx")

# Total Sales per Product Line (Bar Chart)
sales_by_product = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_sales_productline.png", dpi=300)
plt.close()

# Deal Size Distribution (Pie Chart)
deal_counts = df['DEALSIZE'].value_counts()
plt.figure(figsize=(6,6))
deal_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'gold', 'salmon'])
plt.title('Deal Size Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig("deals_distribution.png", dpi=300)
plt.close()

# Quantity Ordered Distribution (Histogram)
plt.figure(figsize=(8,5))
df['QUANTITYORDERED'].plot(kind='hist', bins=20, color='orange')
plt.title('Distribution of Order Quantities')
plt.xlabel('Quantity Ordered')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("quantity_distribution.png", dpi=300)
plt.close()

# Orders per State (Bar Chart)
orders_by_state = df[df['STATE'] != "Unknown"]['STATE'].value_counts().sort_values(ascending=False)
orders_by_state = df['STATE'].value_counts().sort_values(ascending=False)
plt.figure(figsize=(10,5))
orders_by_state.plot(kind='bar', color='purple')
plt.title('Number of Orders per State')
plt.xlabel('State')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("orders_by_state.png", dpi=300)
plt.close()

# Create Excel writer using context manager
report_file = "reporting_and_summary.xlsx"

with pd.ExcelWriter(report_file) as writer:
    # --- 1. Overview ---
    overview = pd.DataFrame({
        "Column": df.columns,
        "DataType": df.dtypes,
        "MissingValues": df.isna().sum(),
        "UniqueValues": df.nunique()
    })
    overview.to_excel(writer, sheet_name="Overview", index=False)

    # --- 2. Numeric Summary ---
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    numeric_summary = df[numeric_cols].agg(['count','mean','median','min','max'])
    numeric_summary.to_excel(writer, sheet_name="Numeric Summary")

    # --- 3. Categorical Summary ---
    categorical_cols = df.select_dtypes(include=['object']).columns
    cat_summary_list = []

    for col in categorical_cols:
        top_value = df[col].mode()[0] if not df[col].mode().empty else "None"
        top_freq = df[col].value_counts().iloc[0] if not df[col].value_counts().empty else 0
        cat_summary_list.append({
            "Column": col,
            "UniqueValues": df[col].nunique(),
            "TopValue": top_value,
            "TopFrequency": top_freq
        })

    categorical_summary = pd.DataFrame(cat_summary_list)
    categorical_summary.to_excel(writer, sheet_name="Categorical Summary", index=False)

# No need to call save() — file is saved automatically
print(f"Simple reporting and summary Excel file created: {report_file}")

