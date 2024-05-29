# train.py

import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.feature_selection import SelectFromModel
import warnings
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')

def load_data(filepath):
    data = pd.read_excel(filepath)
    return data

def preprocess_data(data):
    # Eliminar filas con valores faltantes
    data.dropna(inplace=True)
    
    def change_into_datetime(col):
         data[col]=pd.to_datetime(data[col])
    
    for i in ['Date_of_Journey','Dep_Time', 'Arrival_Time']:
        change_into_datetime(i)
    
    data['Journey_day']=data['Date_of_Journey'].dt.day
    data['Journey_month']=data['Date_of_Journey'].dt.month    
    data.drop('Date_of_Journey', axis=1, inplace=True)
    
    
    def extract_hour(data,col):
        data[col+"_hour"]=data[col].dt.hour

    def extract_min(data,col):
        data[col+"_minute"]=data[col].dt.minute

    def drop_column(data,col):
        data.drop(col,axis=1,inplace=True)
    
    extract_hour(data,'Dep_Time')
    extract_min(data,'Dep_Time')
    drop_column(data,'Dep_Time')
    extract_hour(data,'Arrival_Time')
    extract_min(data,'Arrival_Time')
    drop_column(data,'Arrival_Time') 
    
    
    
    # Funcion para dar formato a la columna
    duration=list(data['Duration']) # Crea un lista

    for i in range(len(duration)): # Itera sobre todos los índices de la lista
            if len(duration[i].split(' '))==2:
                pass
            else:
                if 'h' in duration[i]:
                    duration[i]=duration[i] + ' 0m'
                else:
                    duration[i]='0h '+ duration[i]   
    
    # Replazamos la culumna con la que tiene el formato
    data['Duration']=duration
    # Funcion para extraer la hora
    def hour(x):
        return x.split(' ')[0][0:-1]
    #Funcion para extraer los minutos
    def min(x):
        return x.split(' ')[1][0:-1]
    # Agregamos las columnas nuevas al Dataframe
    data['Duration_hours']=data['Duration'].apply(hour)
    data['Duration_mins']=data['Duration'].apply(min)
    
    # eliminamos la columna Duration
    data.drop('Duration',axis=1,inplace=True)
    
    data['Duration_hours']=data['Duration_hours'].astype(int)
    data['Duration_mins']=data['Duration_mins'].astype(int)
    num_features=[col for col in data.columns if data[col].dtype!='O']
    cat_features=[col for col in data.columns if data[col].dtype=='O']
    
    
    categorical=data[cat_features]
    # Convirtiendo la columna 'Source' en variables dummy
    Source=pd.get_dummies(categorical['Source'], drop_first=True)
    
    # Convirtiendo la columna 'Airline' en variables dummy
    Airline=pd.get_dummies(categorical['Airline'], drop_first=True) 
    
    # Convirtiendo la columna 'Source' en variables dummy
    Source=pd.get_dummies(categorical['Source'], drop_first=True)
    
    # Convirtiendo la columna 'Destination' en variables dummy
    Destination=pd.get_dummies(categorical['Destination'], drop_first=True)
    
    # Se se crea y se divide en 5 columnas para su tratamiento
    categorical['Route_1']=categorical['Route'].str.split('→').str[0]
    categorical['Route_2']=categorical['Route'].str.split('→').str[1]
    categorical['Route_3']=categorical['Route'].str.split('→').str[2]
    categorical['Route_4']=categorical['Route'].str.split('→').str[3]
    categorical['Route_5']=categorical['Route'].str.split('→').str[4]
    
    # Remplaza los valos NaN por None en los datos faltantes de las nuevas columnas
    categorical['Route_1'].fillna('None',inplace=True)
    categorical['Route_2'].fillna('None',inplace=True)
    categorical['Route_3'].fillna('None',inplace=True)
    categorical['Route_4'].fillna('None',inplace=True)
    categorical['Route_5'].fillna('None',inplace=True)
    
    # creamos una instancia
    encoder=LabelEncoder()
    
    # Se cambian los valores de los Routes por valores numericos
    for i in ['Route_1', 'Route_2', 'Route_3', 'Route_4','Route_5']:
        categorical[i]=encoder.fit_transform(categorical[i])
        
    drop_column(categorical,'Route')
    drop_column(categorical,'Additional_Info')
    
    # Se crea un diccionario mapeado con los valores de Total_Stops
    dict={'non-stop':0, '2 stops':2, '1 stop':1, '3 stops':3, '4 stops':4}
    
    # Aplicamos el mapeo a la columna Total_Stops
    categorical['Total_Stops']=categorical['Total_Stops'].map(dict) 
    
    
    data[num_features]
    data = pd.concat([categorical,Airline,Source,Destination,data[num_features]],axis=1)
    
    drop_column(data,'Airline')
    drop_column(data,'Source')
    drop_column(data,'Destination')
    
    # Se analiza y se establece cambiar cada precio mayor que 30000 por la media de la columna Price
    data['Price']=np.where(data['Price']>=30000,data['Price'].median(),data['Price'])
    
    # Se crea un Dataframe sin la columna Price y una variable con la columna Price
    X=data.drop('Price',axis=1)
    y=data['Price']
    X.head()
    
    # Aplicamos el modelo Lasso para buscar la caracteristica
    feature_sel_model = SelectFromModel(Lasso(alpha=0.2, random_state=0)) # se establece el estado aleatorio(semilla)
    feature_sel_model.fit(X,y)
    
    # establece que caracteristicas son importantes
    feature_sel_model.get_support()
    
    # Se guardan los nopmbres de las columnas del Dataframe X
    cols=X.columns
    
    # Creamos una lista con las características seleccionadas
    selected_feat = cols[(feature_sel_model.get_support())]
    
    # Creamos un Dataframe con las caracteristicas seleccionadas
    x=X[selected_feat]
    
    
    
    return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ################################################################
    
    # Codificación de etiquetas para variables categóricas
    


def train_model(X, y):
    model = GradientBoostingRegressor(alpha=.3 , n_estimators=320,learning_rate=0.9, max_depth=30)
    model.fit(X, y)
    return model


def save_model(model, filename):
    joblib.dump(model, filename)

# Main execution
if __name__ == "__main__":
    data = load_data('Data_Train.xlsx')
    
    data = preprocess_data(data)
    
    
    # Se crea un Dataframe sin la columna Price y una variable con la columna Price
    X=data.drop('Price',axis=1)
    y=data['Price']
   
    
    # Aplicamos el modelo Lasso para buscar la caracteristica
    feature_sel_model = SelectFromModel(Lasso(alpha=0.2, random_state=0)) # se establece el estado aleatorio(semilla)
    feature_sel_model.fit(X,y)
    
    # establece que caracteristicas son importantes
    feature_sel_model.get_support()
    
    # Se guardan los nopmbres de las columnas del Dataframe X
    cols=X.columns
    
    # Creamos una lista con las características seleccionadas
    selected_feat = cols[(feature_sel_model.get_support())]
    
    # Creamos un Dataframe con las caracteristicas seleccionadas
    x=X[selected_feat]
   
    # Eliminar la primera columna 'Kolkata' encontrada.
    x = x.loc[:,~x.columns.duplicated()]
 
   
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=44, shuffle =True)
    
    
    model = train_model(X_train, y_train)
    save_model(model, 'flight_price_model.pkl')