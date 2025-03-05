import numpy as np
import pandas as pd

# Lê o dataset
df = pd.read_csv("Netflix Engagement Dataset.csv")

def tabela_distributiva(coluna): 
    if df[coluna].dtype == 'object':      # Variáveis em String
        freq = df[coluna].value_counts()  # Contagem dos valores
        Fi = np.cumsum(freq)  # Frequência acumulada
        porcentagem = df[coluna].value_counts(normalize=True) * 100  # (contagem ÷ total) × 100
        tabela = pd.DataFrame({
            'Frequência': freq, 
            'Percentual (%)': porcentagem,
            "Frequência Acumulada": Fi
            })
    
    else:
        n = len(df[coluna])
        A = round(max(df[coluna]) - min(df[coluna]))  # Amplitude = maior - menor
        i = round(1 + 3.3 * np.log10(n))  # Quantidade de classes
        h = max(1, round(A / i))  # Amplitude da classe

        menor = min(df[coluna])
        intervalos = []
        fi = []
        xi = []

        while menor <= max(df[coluna]):
            maior = menor + h
            intervalo = f"{menor:.2f} - {maior:.2f}"
            intervalos.append(intervalo)
            freq = len(df[(df[coluna] >= menor) & (df[coluna] < maior)])
            fi.append(freq)  # Frequência
            xi.append((menor + maior) / 2)  # Ponto médio
            menor = maior

        Fi = np.cumsum(fi)  # Frequência acumulada

        tabela = pd.DataFrame({
            "Intervalo": intervalos,
            "Frequência": fi,
            "Ponto Médio": xi,
            "Frequência Acumulada": Fi
        })

    print("\n" + "=" * 50)
    print(f"Tabela de Distribuição: {coluna}")
    print("=" * 50)
    print(tabela) 


# Exibe as colunas disponíveis por números
print("\nColunas:")
colunas = list(df.columns)
for i, nome in enumerate(colunas):
    print(f"{i+1}. {nome}")
print(f"{len(colunas) + 1}. Sair")

# Solicita a escolha da coluna pelo número
while True:
    try:
        escolha = int(input("\nDigite o número da coluna desejada: ")) - 1
        if 0 <= escolha < len(colunas):
            tabela_distributiva(colunas[escolha])
        elif escolha == len(colunas):
            print("Saindo...")
            break
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número correspondente a uma coluna.") # Caso entrada não seja um número, o código não da erro
