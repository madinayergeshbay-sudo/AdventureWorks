import pandas as pd
import numpy as np

def load_and_preprocess(excel_path):
    sheets = pd.read_excel(excel_path, sheet_name=None)

    sales = sheets["Sales_data"].copy()
    order = sheets["Sales Order_data"].copy()
    territory = sheets["Sales Territory_data"].copy()
    product = sheets["Product_data"].copy()
    customer = sheets["Customer_data"].copy()
    date = sheets["Date_data"].copy()
    reseller = sheets["Reseller_data"].copy()

    df = sales.merge(order, on="SalesOrderLineKey", how="left")
    df = df.merge(territory, on="SalesTerritoryKey", how="left")
    df = df.merge(product, on="ProductKey", how="left")
    df = df.merge(date[["DateKey","Date","Fiscal Year","Fiscal Quarter","Month","MonthKey"]], left_on="OrderDateKey", right_on="DateKey", how="left")
    df = df.merge(customer[["CustomerKey","Customer","City","State-Province","Country-Region"]], on="CustomerKey", how="left")
    df = df.merge(reseller[["ResellerKey","Business Type","Reseller"]], on="ResellerKey", how="left")

    report = {}
    report["raw_rows"] = len(df)
    report["missing_cells"] = int(df.isna().sum().sum())
    report["duplicates"] = int(df.duplicated().sum())

    df = df.replace("[Not Applicable]", np.nan)
    df = df.drop_duplicates()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Missing")
        else:
            df[col] = df[col].fillna(df[col].median())

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Year"] = df["Date"].dt.year.fillna(2019).astype(int)
    df["Month_num"] = df["Date"].dt.month.fillna(1).astype(int)

    season_map = {12:"Winter",1:"Winter",2:"Winter",3:"Spring",4:"Spring",5:"Spring",6:"Summer",7:"Summer",8:"Summer",9:"Fall",10:"Fall",11:"Fall"}
    df["Season"] = df["Month_num"].map(season_map)
    df["Profit"] = df["Sales Amount"] - df["Total Product Cost"]
    df["Margin_Rate"] = np.where(df["Sales Amount"] > 0, df["Profit"] / df["Sales Amount"], 0)
    df["High_Value_Buy"] = (df["Sales Amount"] > df["Sales Amount"].median()).astype(int)

    q1 = df["Sales Amount"].quantile(0.25)
    q3 = df["Sales Amount"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    df["Sales_Outlier"] = ((df["Sales Amount"] < lower) | (df["Sales Amount"] > upper)).astype(int)
    report["outliers_removed"] = int(df["Sales_Outlier"].sum())

    df_clean = df[df["Sales_Outlier"] == 0].copy()
    report["final_rows"] = len(df_clean)

    return df_clean, report
