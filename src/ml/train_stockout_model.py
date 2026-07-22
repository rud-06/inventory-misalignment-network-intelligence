import xgboost as xgb
from sklearn.model_selection import train_test_split
import os

def train_and_save_model(X, y, model_path='models/xgboost_stockout.json'):
    """
    Trains an XGBoost classifier for inventory misalignment risk.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.05,
        eval_metric='logloss'
    )
    
    model.fit(X_train, y_train)
    model.save_model(model_path)
    print(f"Model saved successfully to {model_path}")
    return model