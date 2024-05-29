# predict.py

import pandas as pd
import joblib

def load_model(filepath):
    return joblib.load(filepath)

def make_prediction(model, input_df):
    prediction = model.predict(input_df)
    return prediction

# Main execution
if __name__ == "__main__":
    model = load_model('flight_price_model.pkl')
    # Ejemplo de datos de entrada
    input_df = pd.read_csv('30_predict.csv')
    
    prediction = make_prediction(model, input_df)
    print("Predicted Flight Price:", prediction)


