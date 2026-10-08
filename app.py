import streamlit as st
import pandas as pd
import joblib


# =========================================================
# 1. LOAD MODEL, PREPROCESSOR AND THRESHOLD
# =========================================================

model = joblib.load("xgboost_churn_model.pkl")
preprocessor = joblib.load("churn_preprocessor.pkl")
threshold = joblib.load("churn_threshold.pkl")


# =========================================================
# 2. STREAMLIT PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction & Retention System")
st.write(
    "Predict customer churn probability and receive personalized "
    "retention recommendations."
)


# =========================================================
# 3. CUSTOMER INPUT
# =========================================================

st.header("👤 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )


with col2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


with col3:

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

    cltv = st.number_input(
        "CLTV",
        min_value=0.0,
        value=5000.0
    )


# =========================================================
# 4. CREATE INPUT DATAFRAME
# =========================================================

input_data = pd.DataFrame({
    "Gender": [gender],
    "Senior Citizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "Tenure Months": [tenure],
    "Phone Service": [phone_service],
    "Multiple Lines": [multiple_lines],
    "Internet Service": [internet_service],
    "Online Security": [online_security],
    "Online Backup": [online_backup],
    "Device Protection": [device_protection],
    "Tech Support": [tech_support],
    "Streaming TV": [streaming_tv],
    "Streaming Movies": [streaming_movies],
    "Contract": [contract],
    "Paperless Billing": [paperless_billing],
    "Payment Method": [payment_method],
    "Monthly Charges": [monthly_charges],
    "Total Charges": [total_charges],
    "CLTV": [cltv]
})


# =========================================================
# 5. PREDICT CHURN
# =========================================================

if st.button("🔮 Predict Churn", use_container_width=True):

    # Preprocess
    processed_data = preprocessor.transform(input_data)

    # Probability
    probability = model.predict_proba(processed_data)[0][1]

    # Prediction using our selected threshold
    churn_prediction = int(probability >= threshold)


    # =====================================================
    # 6. RISK LEVEL
    # =====================================================

    if probability < 0.30:
        risk = "Low"

    elif probability < 0.60:
        risk = "Medium"

    elif probability < 0.80:
        risk = "High"

    else:
        risk = "Very High"


    # =====================================================
    # 7. DISPLAY PREDICTION
    # =====================================================

    st.divider()

    st.header("📈 Prediction Result")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:

        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )

    with result_col2:

        st.metric(
            "Risk Level",
            risk
        )

    with result_col3:

        if churn_prediction == 1:
            st.error("⚠️ Customer likely to churn")
        else:
            st.success("✅ Customer likely to stay")


    # =====================================================
    # 8. RETENTION RECOMMENDATION
    # =====================================================

    st.header("💡 Retention Recommendations")


    recommendations = []


    # Risk-based recommendation

    if risk == "Very High":

        recommendations.append(
            "🚨 Immediate retention call"
        )

    elif risk == "High":

        recommendations.append(
            "🎯 Targeted retention offer"
        )

    elif risk == "Medium":

        recommendations.append(
            "📢 Engagement campaign"
        )

    else:

        recommendations.append(
            "✅ No immediate action required"
        )


    # Tenure

    if tenure <= 6:

        recommendations.append(
            "🆕 Provide new-customer onboarding support"
        )


    # Monthly charges

    if monthly_charges >= 70:

        recommendations.append(
            "💰 Review pricing and offer a suitable plan"
        )


    # Payment method

    if payment_method == "Electronic check":

        recommendations.append(
            "💳 Encourage automatic payment"
        )


    # Technical support

    if tech_support == "No":

        recommendations.append(
            "🛠️ Offer technical support"
        )


    # Online security

    if online_security == "No":

        recommendations.append(
            "🔐 Offer online security service"
        )


    # Contract

    if contract == "Month-to-month":

        recommendations.append(
            "📄 Offer a longer-term contract"
        )


    # Display recommendations

    for recommendation in recommendations:

        st.info(recommendation)


    # =====================================================
    # 9. CUSTOMER SUMMARY
    # =====================================================

    st.header("👤 Customer Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Tenure",
            "Contract",
            "Internet Service",
            "Monthly Charges",
            "Payment Method",
            "Online Security",
            "Tech Support",
            "Dependents"
        ],

        "Value": [
            f"{tenure} months",
            contract,
            internet_service,
            f"₹{monthly_charges:.2f}",
            payment_method,
            online_security,
            tech_support,
            dependents
        ]
    })

    st.table(summary)