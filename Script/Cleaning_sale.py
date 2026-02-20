import pandas as pd
df=pd.read_csv("sales_data.csv",encoding="latin-1")
# Misses checkimg ::
#print(df.isnull().sum())
# duplicates checking ::
print(df.duplicated().sum())
# remove duplicate values ::
df.drop_duplicates()
# drop ADDRESSLINE2 because it having too much missing values ::
df.drop(columns=["ADDRESSLINE2"],inplace=True)
# STATE COLUMN FILLING ::
df["STATE"]=df["STATE"].fillna("Unknown")
# POSTALCODE FILLING ::
df["POSTALCODE"]=df["POSTALCODE"].fillna("Not Available")
# TERRITORY FILLING ::
df["TERRITORY"]=df["TERRITORY"].fillna("Unknown")
# Orderdate dtype checking ::
#print(df["ORDERDATE"].dtype)
# setting data  d type ::
df["ORDERDATE"]=pd.to_datetime(df["ORDERDATE"],errors="coerce")

# standarization of columns ::

# List of text/categorical columns
text_columns = [
    "STATUS", "PRODUCTLINE", "PRODUCTCODE", "CUSTOMERNAME", "PHONE",
    "ADDRESSLINE1", "CITY", "STATE", "POSTALCODE",
    "COUNTRY", "TERRITORY", "CONTACTLASTNAME", "CONTACTFIRSTNAME", "DEALSIZE"
]

# Standardize each column
for col in text_columns:
    # Convert to string (safe if some cells are numeric)
    df[col] = df[col].astype(str)
    
    # Strip leading/trailing spaces
    df[col] = df[col].str.strip()
# Specific transformations
# 1) Names, cities, states, territory, deal size → Title case
title_case_cols = ["CUSTOMERNAME", "CITY", "STATE", "TERRITORY", 
                   "CONTACTLASTNAME", "CONTACTFIRSTNAME", "DEALSIZE","STATUS","PRODUCTLINE"]
for col in title_case_cols:
    df[col] = df[col].str.title()

# 2) Codes, postal codes → Upper case
upper_case_cols = ["PRODUCTCODE", "POSTALCODE", "COUNTRY",]
for col in upper_case_cols:
    df[col] = df[col].str.upper()
 # MAPPING STATE ::
# Mapping of common state abbriviations
state_mapping = {
    "NY": "New York",
    "CA": "California",
    "TX": "Texas",
    "FL": "Florida",
    "IL": "Illinois",
    "PA": "Pennsylvania",
    "OH": "Ohio",
    "MI": "Michigan",
    "GA": "Georgia",
    # Add more as needed for your dataset
}

# Standardize STATE column
df["STATE"] = df["STATE"].str.upper().str.strip()   # make uppercase first for mapping
df["STATE"] = df["STATE"].replace(state_mapping)   # replace abbreviations with full name
df["STATE"] = df["STATE"].str.title()              # convert to title case for uniformity

# Mapping of abbreviations to full state names
state_mapping_2 = {
    "MA": "Massachusetts",
    "NSW": "New South Wales",  # if this is international dataset
    "CT": "Connecticut",
    "BC": "British Columbia",  # adjust if needed
    "NH": "New Hampshire",
    "NV": "Nevada",
    "NJ": "New Jersey"
}

# Apply mapping to STATE column
df["STATE"] = df["STATE"].str.upper().str.strip()  # ensure consistency
df["STATE"] = df["STATE"].replace(state_mapping_2)
df["STATE"] = df["STATE"].str.title()  # proper case


# setting phone column ::
# Keep only digits
df["PHONE"] = df["PHONE"].astype(str).str.replace(r'\D', '', regex=True)

# Keep only last 10 digits
df["PHONE"] = df["PHONE"].str[-10:]

# Identify invalid / short numbers
invalid_phones = df[df["PHONE"].str.len() != 10]

# Replace invalid/short numbers with "Unknown"
df.loc[df["PHONE"].str.len() != 10, "PHONE"] = "Unknown"

# Format valid numbers
df["PHONE"] = df["PHONE"].apply(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}" if x != "Unknown" else x)
# checking missing values now ::
print(df.isnull().sum().sum())
# export file as excel ::
df.to_excel("Cleaned_sale.xlsx",index=False)