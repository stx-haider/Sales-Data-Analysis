📊 Sales Data Cleaning, Reporting & Visualization Project
📌 Project Overview
This project demonstrates a complete data analysis workflow using Python.
The objective was to clean and standardize a raw sales dataset, perform exploratory analysis, generate automated reporting in Excel, and create professional visualizations.
The project simulates a real-world business scenario where raw transactional data must be transformed into meaningful insights.

🧹 Data Cleaning & Preprocessing

The following steps were performed to ensure data quality:
Removed duplicate records
Handled missing values (e.g., filled missing STATE values with "Unknown")
Converted numeric columns:
SALES
QUANTITYORDERED
PRICEEACH
MSRP
Converted ORDERDATE to proper datetime format
Standardized categorical columns:
STATUS
PRODUCTLINE
Converted state abbreviations to full state names
Cleaned and formatted PHONE numbers
Trimmed whitespace and standardized text formatting
After cleaning, the dataset became fully structured and analysis-ready.

📊 Reporting & Summary (Excel Automation)

An automated Excel report was generated containing:
Dataset overview
Summary statistics for numeric columns
Categorical column summaries
Business-relevant aggregated metrics
Embedded charts
Generated file:

reports/reporting_and_summary_with_charts.xlsx
📈 Visualizations

Using Matplotlib, the following charts were created:
Total Sales by Product Line (Bar Chart)
Deal Size Distribution (Pie Chart)
Quantity Ordered Distribution (Histogram)
Orders per State (Bar Chart)
All visualization images are stored in the visuals/ folder.
🛠 Tools & Technologies
Python
Pandas
Matplotlib
XlsxWriter
VS Code
Git & GitHub

        PROJECT STRUCTURE :
Sales-Data-Cleaning-Project/
│
├── data/
│   └── cleaned_sale.xlsx
│
├── script/
│   ├── cleaning_sale.py
│   ├── reporting_summary.py
│   └── visualization.py
│
├── report/
│   └── reporting_and_summary_with_charts.xlsx
│
├── visuals/
│   ├── total_sales_productline.png
│   ├── deals_distribution.png
│   ├── quantity_distribution.png
│   └── orders_by_state.png
│
└── README.md

🎯 Key Skills Demonstrated

Data Cleaning & Preprocessing
Data Transformation
Exploratory Data Analysis (EDA)
Data Visualization
Excel Report Automation
Project Structuring & Documentation

🚀 Project Workflow

Raw Dataset
→ Data Cleaning
→ Standardization
→ Analysis
→ Reporting
→ Visualization

📌 Conclusion
This project showcases the complete data analytics pipeline from raw data to business-ready insights.
It demonstrates practical skills required for entry-level Data Analyst and Business Analyst roles.