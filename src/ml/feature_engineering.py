import pandas as pd

def extract_inventory_features(inventory_df, sales_df, procurement_df):
    """
    Transforms Canonical Data Model tables into an ML feature matrix.
    """
    # 1. Calculate 30-day sales velocity per SKU & store/node
    sales_30d = sales_df.groupby(['sku_id', 'node_id'])['quantity'].sum().reset_index()
    sales_30d.rename(columns={'quantity': 'sales_velocity_30d'}, inplace=True)
    
    # 2. Merge velocity with current inventory levels
    features = pd.merge(inventory_df, sales_30d, on=['sku_id', 'node_id'], how='left').fillna(0)
    
    # 3. Calculate Days of Supply (Current Stock / Daily Sales Rate)
    features['days_of_supply'] = features['current_stock'] / (features['sales_velocity_30d'] / 30 + 1e-5)
    
    # 4. Aggregate Lead Time metrics from procurement
    lead_times = procurement_df.groupby('sku_id')['supplier_lead_time_days'].agg(['mean', 'std']).reset_index()
    features = pd.merge(features, lead_times, on='sku_id', how='left').fillna(0)
    
    return features