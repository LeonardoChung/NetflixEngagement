import pandas as pd

df = pd.read_csv("Netflix Engagement Dataset.csv")

estatisticas = {}

# valor da média, mediana, moda, variância, desvio padrão e desvio absoluto média (DAM)
# quando algum não puder ser calculado indicando o porquê
for coluna in df.columns:
    if df[coluna].dtype in ['int64', 'float64']: # variáveis numéricas
        media = df[coluna].mean()
        mediana = df[coluna].median()
        moda = df[coluna].mode()
        variancia = df[coluna].var()
        desvio_padrao = df[coluna].std()
        desvio_absoluto_media = (df[coluna] - media).abs().mean()

        if not moda.empty:  
            moda = moda.tolist() 
        else:  
            moda = "Não há moda"
    
    elif df[coluna].dtype == 'object': # variáveis categóricas
        media = "Não é possível calcular em variáveis categóricas"
        mediana = "Não é possível calcular em variáveis categóricas"
        variancia = "Não é possível calcular em variáveis categóricas"
        desvio_padrao = "Não é possível calcular em variáveis categóricas"
        desvio_absoluto_media = "Não é possível calcular em variáveis categóricas"

        moda = df[coluna].mode()
        if not moda.empty:  
            moda = moda.tolist()
        else:  
            moda = "Não há moda"

    else: # exceção
        media = "Tipo de dado não suportado"
        mediana = "Tipo de dado não suportado"
        moda = "Tipo de dado não suportado"
        variancia = "Tipo de dado não suportado"
        desvio_padrao = "Tipo de dado não suportado"
        desvio_absoluto_media = "Tipo de dado não suportado"
    
    estatisticas[coluna] = {"Média": media, "Mediana": mediana, "Moda": moda, "Variância": variancia, "Desvio Padrão": desvio_padrao, "Desvio Absoluto Média (DAM)": desvio_absoluto_media}


# distribuição simétrica, para direita ou esquerda
for variavel in estatisticas:
    media = estatisticas[variavel]["Média"]
    mediana = estatisticas[variavel]["Mediana"]
    moda = estatisticas[variavel]["Moda"]

    # media e mediana como variáveis categóricas
    if not isinstance(media, (int, float)) or not isinstance(mediana, (int, float)):
        estatisticas[variavel]["Distribuição"] = "Indefinida -> variável categórica sem média ou mediana numérica"

    # casos de não existir moda
    elif moda == "Não há moda":
        if media == mediana:
            estatisticas[variavel]["Distribuição"] = "Simétrica -> média = mediana"
        elif media > mediana:
            estatisticas[variavel]["Distribuição"] = "Assimetria para direita / positiva -> média > mediana"
        else:
            estatisticas[variavel]["Distribuição"] = "Assimetria para esquerda / negativa -> média < mediana"

    else:
        # pode ter mais de uma moda
        if isinstance(moda, list):
            if media == mediana and any(media == x for x in moda):
                estatisticas[variavel]["Distribuição"] = "Simétrica -> média = mediana = moda"
            elif media >= mediana and any(mediana >= x for x in moda):
                estatisticas[variavel]["Distribuição"] = "Assimetria para direita / positiva -> média > mediana > moda"
            elif media <= mediana and any(mediana <= x for x in moda):
                estatisticas[variavel]["Distribuição"] = "Assimetria para esquerda / negativa -> média < mediana < moda"
            else:
                estatisticas[variavel]["Distribuição"] = "Indefinida -> média, mediana e moda não seguem padrões (???)"
        else:
            estatisticas[variavel]["Distribuição"] = "Indefinida"

# inverte linha e coluna para melhor visualização
estatisticas_df = pd.DataFrame(estatisticas).T

print(estatisticas_df)
