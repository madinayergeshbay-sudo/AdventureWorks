from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error
import pandas as pd

def train_models(df):
    work = df.copy()
    cat_cols = ["Category", "Subcategory", "Country", "Region", "Group", "Channel", "Season"]
    encoders = {}

    for col in cat_cols:
        le = LabelEncoder()
        work[col] = work[col].astype(str)
        work[col + "_enc"] = le.fit_transform(work[col])
        encoders[col] = le

    features = [
        "Order Quantity", "Unit Price", "Product Standard Cost", "Month_num",
        "Category_enc", "Subcategory_enc", "Country_enc", "Region_enc",
        "Group_enc", "Channel_enc", "Season_enc"
    ]

    X = work[features].fillna(0)

    y_cls = work["High_Value_Buy"]
    X_train, X_test, y_train, y_test = train_test_split(X, y_cls, test_size=0.2, random_state=42, stratify=y_cls)

    classifier = RandomForestClassifier(
        n_estimators=250,
        max_depth=14,
        min_samples_leaf=2,
        random_state=42,
        class_weight="balanced"
    )
    classifier.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, classifier.predict(X_test))

    y_reg = work["Sales Amount"]
    X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

    regressor = RandomForestRegressor(
        n_estimators=300,
        max_depth=16,
        min_samples_leaf=2,
        random_state=42
    )
    regressor.fit(X_train, y_train)

    pred = regressor.predict(X_test)
    r2 = r2_score(y_test, pred)
    mae = mean_absolute_error(y_test, pred)

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": regressor.feature_importances_
    }).sort_values("Importance", ascending=False)

    return classifier, regressor, encoders, features, accuracy, r2, mae, importance
