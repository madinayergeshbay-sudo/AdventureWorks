# 🚴 AdventureWorks 

## AI 기반 CRM Business Intelligence & Sales Prediction System

이 프로젝트는 교수님 과제 조건에 맞추어 **AdventureWorks Sales.xlsx** 데이터를 기반으로 만든 AI 분석 프로젝트입니다.

---

## ✅ 교수님 요구사항 충족 여부

| 요구사항 | 수행 여부 | 설명 |
|---|---:|---|
| Excel 데이터 사용 | ✅ | AdventureWorks Sales.xlsx의 7개 시트 사용 |
| Data Preprocessing | ✅ | 결측치, 중복값, 이상치 처리 |
| Missing Data 처리 | ✅ | 총 36,257개 결측 셀 처리 |
| Duplicate 제거 | ✅ | 중복 행 0개 확인 및 제거 |
| Outlier 제거 | ✅ | IQR 방식으로 10,735개 이상치 제거 |
| EDA | ✅ | 국가, 카테고리, 시간, 고객, 상품 분석 |
| Classification | ✅ | RandomForestClassifier 적용 |
| Regression | ✅ | RandomForestRegressor 적용 |
| CRM 관점 분석 | ✅ | RFM, CLV, 고객 세분화, Churn Risk |
| 발표용 자료 | ✅ | reports 폴더에 발표 대본 포함 |

---

## 📊 데이터 처리 결과

- 원본 데이터 행 수: **121,253**
- 최종 정제 데이터 행 수: **110,518**
- 결측 셀 수: **36,257**
- IQR 이상치 제거 수: **10,735**
- RFM 분석 고객 수: **18,148**

---

## 🤖 모델 성능

| 모델 | 목적 | 성능 |
|---|---|---:|
| RandomForestClassifier | Buy / Not Buy 예측 | Accuracy 0.9998 |
| RandomForestRegressor | Sales Amount 예측 | R² 0.9999 |
| RandomForestRegressor | Sales Amount 예측 | MAE 0.3334 |

---

## 📁 프로젝트 구조

```text
AdventureWorks_REAL_100_Project/
│
├── app/
│   ├── main.py
│   └── pages/
│       ├── 01_Executive_Dashboard.py
│       ├── 02_EDA_Analytics.py
│       ├── 03_AI_Prediction.py
│       ├── 04_Customer_CRM.py
│       └── 05_Strategy_Simulator.py
│
├── src/
│   ├── data_preprocessing.py
│   ├── eda_analysis.py
│   ├── model_training.py
│   ├── rfm_clv_churn.py
│   └── recommendation_engine.py
│
├── data/
│   ├── processed/
│   │   ├── adventureworks_clean.csv
│   │   └── rfm_segments.csv
│   └── reports/
│       └── preprocessing_model_summary.csv
│
├── notebooks/
│   ├── 01_Data_Preprocessing.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Classification.ipynb
│   ├── 04_Regression.ipynb
│   └── 05_RFM_CRM.ipynb
│
├── reports/
│   └── presentation/
│       ├── 발표대본_5분.md
│       └── PPT_슬라이드_내용.md
│
├── README.md
└── requirements.txt
```

---

## 🚀 실행 방법

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

---

## 🎯 프로젝트 목표

이 프로젝트의 목표는 단순한 판매 데이터 분석이 아니라, CRM 관점에서 고객 행동을 분석하고 머신러닝으로 구매 여부와 미래 매출을 예측하는 것입니다.

주요 기능은 다음과 같습니다.

1. 7개 시트 병합 및 전처리  
2. 결측치, 중복값, 이상치 처리  
3. 국가·상품·시간·고객별 EDA  
4. RandomForestClassifier를 이용한 Buy / Not Buy 예측  
5. RandomForestRegressor를 이용한 Sales Amount 예측  
6. RFM 기반 고객 세분화  
7. CLV 기반 고객 가치 평가  
8. Churn Risk 기반 이탈 위험 분석  
9. CRM 전략 추천  
10. Streamlit 기반 발표용 Dashboard  

---

## 🏆 차별점

일반적인 프로젝트는 EDA와 단일 모델에서 끝나지만, 본 프로젝트는 **CRM + 머신러닝 + 고객 세분화 + 비즈니스 전략**을 하나의 시스템으로 연결했습니다.

특히 RFM, CLV, Churn Risk를 추가하여 실제 기업의 마케팅 의사결정에 활용 가능한 구조로 설계했습니다.
