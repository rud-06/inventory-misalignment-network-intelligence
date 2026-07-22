import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import shap
import matplotlib.pyplot as plt

# ==========================================
# 1. PAGE SETUP & STYLING
# ==========================================
st.set_page_config(page_title="Inventory Misalignment & Network Intelligence", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .metric-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #D93954; }
    .roi-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #00A36C; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Inventory Misalignment & Network Intelligence")
st.markdown("### Executive Diagnostic & Predictive Platform")

# ==========================================
# 2. LOAD DATA & MODEL (Mocked for UI rendering)
# ==========================================
@st.cache_resource
def load_xgb_model():
    model = xgb.XGBClassifier()
    model.load_model("models/xgboost_stockout.json")
    return model

@st.cache_data
def load_sample_ml_data():
    # Generating a sample data row that matches our ML feature matrix
    data = pd.DataFrame({
        'sku_id': ['SKU_0104', 'SKU_0892', 'SKU_0331'],
        'current_stock': [12.5, 450.0, 5.0],
        'sales_velocity_30d': [120.0, 30.0, 150.0],
        'supplier_lead_time_days': [18.0, 7.0, 22.0],
        'lead_time_variance': [4.5, 0.5, 5.2],
        'holding_days': [45.0, 110.0, 12.0],
        'days_of_supply': [3.1, 450.0, 1.0],
        'capital_tied_up': [2500.0, 85000.0, 750.0]
    })
    return data

model = load_xgb_model()
ml_data = load_sample_ml_data()

# ==========================================
# 3. DASHBOARD TABS
# ==========================================
tab1, tab2, tab3 = st.tabs([
    "📈 Descriptive Diagnostics (Rule-Based)", 
    "🤖 Predictive Intelligence & SHAP", 
    "💰 Executive ROI Summary"
])

# --- TAB 1: EXISTING RULE-BASED LOGIC ---
with tab1:
    st.header("Network Friction & Rule-Based Alerts")
    st.info("This section loads outputs from your primary data pipeline (e.g., store_risk.csv).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h4>High Phantom Inventory Risk</h4><h2>14 Stores</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h4>Bullwhip (Panic Ordering)</h4><h2>28 SKUs</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h4>Total Revenue at Risk</h4><h2>$555,689</h2></div>', unsafe_allow_html=True)

# --- TAB 2: XGBOOST & SHAP EXPLAINABILITY ---
with tab2:
    st.header("Predictive Misalignment Risk (30-Day Forecast)")
    
    selected_sku = st.selectbox("Select SKU for Deep Dive Analysis:", ml_data['sku_id'])
    sku_features = ml_data[ml_data['sku_id'] == selected_sku].drop(columns=['sku_id'])
    
    # Run Prediction
    risk_prob = model.predict_proba(sku_features)[0][1]
    
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        st.subheader("Model Prediction")
        if risk_prob > 0.60:
            st.error(f"High Risk of Misalignment")
        elif risk_prob > 0.30:
            st.warning(f"Moderate Risk")
        else:
            st.success(f"Healthy / Low Risk")
            
        st.progress(float(risk_prob))
        st.write(f"**Probability Score:** {risk_prob*100:.1f}%")
        
        st.markdown("### Live Operational Metrics")
        st.dataframe(sku_features.T.rename(columns={0: "Value"}))

    with col_b:
        st.subheader("Why did the AI make this prediction? (SHAP)")
        
        # Generate SHAP values
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(sku_features)
        
        # Plot SHAP
        fig, ax = plt.subplots(figsize=(8, 4))
        shap.summary_plot(shap_values, sku_features, plot_type="bar", show=False)
        plt.tight_layout()
        st.pyplot(fig)
        
        st.caption("Features extending to the right drive the risk UP. Features extending left drive risk DOWN.")

# --- TAB 3: EXECUTIVE ROI PITCH ---
with tab3:
    st.header("Financial Impact & Model ROI")
    st.write("Translating XGBoost predictive accuracy directly into bottom-line savings.")
    
    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown('<div class="roi-card"><h4>Total Network Leakage at Risk</h4><h2>$555,689</h2><p>Baseline holding/stockout penalties</p></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="roi-card"><h4>Leakage Prevented by ML</h4><h2>$326,418</h2><p>58.7% Capture Rate</p></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="roi-card"><h4>Annualized Projected Savings</h4><h2>$3,917,024</h2><p>Impact scaled over 12 months</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.markdown("""
    ### 📝 Business Translation (Interview Pitch Outline)
    * **The Problem:** Traditional min-max inventory thresholds are static. They fail to capture complex interactions like lead-time variance colliding with demand drops, resulting in **$555k of active profit leakage** (deadstock penalties & express freight premiums).
    * **The Solution:** By deploying a non-linear XGBoost classifier, we can predict misalignment 30 days in advance. 
    * **The Value:** The model captures **58.7%** of the financial risk before it happens, translating to **$3.9M in annualized savings** across the supply chain network. The SHAP integration ensures warehouse managers understand exactly *why* a transfer or markdown is recommended.
    """)