import pandas as pd
import os
import sys
import pandas as pd
import ast
import numpy as np
import re
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
import datetime as dt


def concat_csv():
    '''
    Uso de la librería "os" para la carga de todas las provincias que las tenemos almacenadas en una ruta especifica.
    
        Returns:
               dataframe concatenado con la totalidad de registros extraídos.
    '''

    path = "/mnt/c/Users/chris/Ironhack/projects/Real_Estate_Market_Analysis/Data/csv_provinces"
    filesname = os.listdir(path)
    all_df =[]

    for file in filesname:
        csv_prov = os.path.join(path, file)
        df_prov = pd.read_csv(f"{csv_prov}")
        all_df.append(df_prov)
    all_dataset = pd.concat(all_df, axis=0, ignore_index=True)
    all_dataset.to_csv("../Data/merged_dataset.csv", index=False)
    return all_dataset


def cleaning_data(df):
    '''
    Función que limpia los datos de un dataset.
    Return:
        dataset limpio.
    '''
    
    # drop column
    df.drop('typeId', axis=1, inplace=True)
    
    #  ------------cleaning columns------------
    
    #column subtypeId
    df['subtypeId'].replace({55: 5, 52: 5, 0: 9, 54: 8}, inplace= True)
    subtype_name = {1: "Piso", 3: "Chalet", 5: "Casa adosada", 2: "Apartamento", 7: "Duplex", 6 : "Atico", 9 : "Finca", 8 : "Estudio o loft"}
    df['subtypeId'] = df['subtypeId'].map(subtype_name)
    # column descriptions
    df['descriptions'] = df['descriptions'].apply(lambda dict: ast.literal_eval(dict))
    df['descriptions'] = df['descriptions'].apply(lambda x: x.setdefault('es-ES', np.nan))
    # column zipcode
    df['zipcode'] = df['zipcode'].apply(extract_cp)
    df['zipcode'] = df.groupby(['city'])['zipcode'].apply(lambda x: x.fillna(x.mode()[0]) if x.mode().empty == False else x.fillna(np.nan))
    df = df.dropna(subset=["zipcode"])
    df['zipcode'] = df['zipcode'].astype('category')
    #column date
    df['date'] = pd.to_datetime(df['date']).dt.date.astype("datetime64")
    df = df[df['date'] > '2021']
    # column price
    df = df.dropna(subset=["price"])
    df['price'] = df['price'].astype('int64')
    # column city
    df['city'] = df['city'].apply(lambda x: x.strip().replace("'"," "))
    
    #  ------------cleaning Outliers------------
    
    df = df[(df['rooms'] > 0) & (df['rooms'] < 8)]
    df = df[(df['bathrooms'] > 0) & (df['bathrooms'] < 5)]
    df = df[(df['surface'] > 30) & (df['surface'] < 600)]
    df = df[df['floor'] < 12]
    df = df[df['surfaceland'] < 2500]
    df = df[(df['price'] > 20000) & (df['price'] < 900000)]
    
    #  ------------new column------------
    
    df['€/m2'] = df['price'] / (df['surface'] + df['surfaceland'])

    print("La limpieza del dataset ha sido completada")
    print(f"El dataset tiene {df.shape[0]} registros y {df.shape[1]} columnas")
    return df


def extract_cp(i):
    '''
    Función que extrae el código postal de una ciudad.
    Return:
        código postal de la ciudad.
    '''
    try:
        i = str(i)
        if type(i) == str:
            i = re.findall(r'^\d*', i)[0].lstrip("0")
            if len(i) > 3:
                return i
            else:
                return np.nan
    except:
        return np.nan


