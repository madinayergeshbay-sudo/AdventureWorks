import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="AdventureWorks REAL 100 Project", page_icon="🚴", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#f8f5ff,#eef8ff);}
.hero {padding:30px;border-radius:24px;background:linear-gradient(135deg,#21164a,#6a55e6);color:white;margin-bottom:20px;}
.card {background:white;padding:20px;border-radius:18px;box-shadow:0 8px 25px rgba(0,0,0,.08);}
.kpi {font-size:30px;font-weight:900;color:#5d46d6;}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='hero'><h1>AdventureWorks AI Business Intelligence Platform</h1><p>CRM 기반 고객 분석 · Buy/Not Buy 예측 · 매출 예측 · RFM · CLV · Churn Risk</p></div>", unsafe_allow_html=True)

df = pd.read_csv("data/processed/adventureworks_clean.csv")
rfm = pd.read_csv("data/processed/rfm_segments.csv")
summary = pd.read_csv("data/reports/preprocessing_model_summary.csv").iloc[0]

c1,c2,c3,c4 = st.columns(4)
c1.metric("Final Clean Rows", f"{int(summary['final_clean_rows']):,}")
c2.metric("Missing Cells Treated", f"{int(summary['raw_missing_cells']):,}")
c3.metric("IQR Outliers Removed", f"{int(summary['outliers_removed_by_iqr']):,}")
c4.metric("Regression R²", f"{summary['regression_r2']:.4f}")

tab1, tab2, tab3, tab4 = st.tabs(["EDA", "Model Performance", "CRM Analysis", "Presentation Summary"])

with tab1:
    a,b = st.columns(2)
    with a:
        st.plotly_chart(px.bar(df.groupby("Country", as_index=False)["Sales Amount"].sum().sort_values("Sales Amount", ascending=False), x="Country", y="Sales Amount", title="국가별 매출"), use_container_width=True)
    with b:
        st.plotly_chart(px.pie(df.groupby("Category", as_index=False)["Sales Amount"].sum(), names="Category", values="Sales Amount", title="카테고리별 매출 비중"), use_container_width=True)
    monthly = df.groupby(["Year","Month_num"], as_index=False)["Sales Amount"].sum()
    monthly["YM"] = monthly["Year"].astype(str) + "-" + monthly["Month_num"].astype(str).str.zfill(2)
    st.plotly_chart(px.line(monthly, x="YM", y="Sales Amount", title="월별 매출 추세", markers=True), use_container_width=True)

with tab2:
    st.write("RandomForestClassifier Accuracy:", summary["classification_accuracy"])
    st.write("RandomForestRegressor R²:", summary["regression_r2"])
    st.write("RandomForestRegressor MAE:", summary["regression_mae"])

with tab3:
    st.plotly_chart(px.bar(rfm["Segment"].value_counts().reset_index(), x="Segment", y="count", title="RFM 고객 세그먼트"), use_container_width=True)
    st.dataframe(rfm.sort_values("CLV", ascending=False).head(30), use_container_width=True)

with tab4:
    st.markdown("""
    ### 발표 핵심
    - 7개 Excel 시트를 통합했습니다.
    - 결측치, 중복값, 이상치를 처리했습니다.
    - EDA로 국가/상품/시간/고객 패턴을 분석했습니다.
    - RandomForestClassifier로 Buy/Not Buy를 예측했습니다.
    - RandomForestRegressor로 매출을 예측했습니다.
    - RFM, CLV, Churn Risk로 CRM 전략을 제안했습니다.
    """)
