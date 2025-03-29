import pandas as pd

df = pd.read_csv("Netflix Engagement Dataset.csv")

estatisticas = {}

for coluna in df.columns:
    if df[coluna].dtype in ['int64', 'float64']: # numericas
        media = df[coluna].mean()
        mediana = df[coluna].median()
        moda = df[coluna].mode()
        if not moda.empty:  
            moda = moda.tolist() 
        else:  
            moda = "Não há moda"
    
    elif df[coluna].dtype == 'object': # categoricas
        media = "Não é possível calcular em variáveis categóricas"
        mediana = "Não é possível calcular em variáveis categóricas"
        moda = df[coluna].mode()
        if not moda.empty:  
            moda = moda.tolist()
        else:  
            moda = "Não há moda"
    
    else:
        media = "Tipo de dado não suportado"
        mediana = "Tipo de dado não suportado"
        moda = "Tipo de dado não suportado"
    
    estatisticas[coluna] = {"Média": media, "Mediana": mediana, "Moda": moda}

# inverte linha e coluna para melhor visualzacaoe
estatisticas_df = pd.DataFrame(estatisticas).T

print(estatisticas_df)
