import shap
import pandas as pd

def get_sku_shap_explanation(model, feature_matrix, sku_id):
    """
    Generates feature impact explanations for a specific SKU using SHAP.
    """
    # Initialize the explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(feature_matrix)
    
    # Find the specific SKU in our data
    sku_idx = feature_matrix[feature_matrix['sku_id'] == sku_id].index[0]
    
    # Map the SHAP values to their corresponding feature names
    impacts = dict(zip(feature_matrix.columns, shap_values.values[sku_idx]))
    
    # Sort the impacts from most important to least important
    sorted_impacts = sorted(impacts.items(), key=lambda x: abs(x[1]), reverse=True)
    
    return sorted_impacts