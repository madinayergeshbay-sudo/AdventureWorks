import pandas as pd
import numpy as np

def build_rfm(df):
    base = df[df["Customer"].astype(str) != "Missing"].copy()
    snapshot = base["Date"].max() + pd.Timedelta(days=1)

    rfm = base.groupby("Customer").agg(
        Recency=("Date", lambda x: (snapshot - x.max()).days),
        Frequency=("Sales Order", "nunique"),
        Monetary=("Sales Amount", "sum")
    ).reset_index()

    rfm["R_Score"] = pd.qcut(rfm["Recency"].rank(method="first"), 5, labels=[5,4,3,2,1]).astype(int)
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5]).astype(int)
    rfm["M_Score"] = pd.qcut(rfm["Monetary"].rank(method="first"), 5, labels=[1,2,3,4,5]).astype(int)

    def segment(x):
        if x.R_Score >= 4 and x.F_Score >= 4 and x.M_Score >= 4:
            return "Champions"
        if x.R_Score >= 4 and x.F_Score >= 3:
            return "Loyal Customers"
        if x.R_Score >= 4 and x.F_Score <= 2:
            return "New Customers"
        if x.R_Score <= 2 and x.F_Score >= 3:
            return "At Risk"
        if x.R_Score <= 2 and x.F_Score <= 2:
            return "Lost Customers"
        return "Need Attention"

    rfm["Segment"] = rfm.apply(segment, axis=1)
    rfm["CLV"] = rfm["Monetary"] * (1 + rfm["Frequency"] / rfm["Frequency"].max())
    rfm["Churn_Risk"] = np.where(
        (rfm["Recency"] > rfm["Recency"].median()) & (rfm["Frequency"] <= rfm["Frequency"].median()),
        "High", "Low"
    )
    return rfm
