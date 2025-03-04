import numpy as np
import pandas as pd

# Lê o dataset
df = pd.read_csv("Netflix Engagement Dataset.csv")

def tabela_distributiva(coluna):
    """Gera uma tabela de distribuição de frequência para uma variável categórica ou numérica."""
    
    if df[coluna].dtype == 'object':  # Variável categórica
        freq = df[coluna].value_counts()  # Contagem dos valores
        porcentagem = df[coluna].value_counts(normalize=True) * 100  # (contagem ÷ total) × 100
        tabela = pd.DataFrame({'Frequência': freq, 'Percentual (%)': porcentagem})
    
    else:  # Variável numérica
        n = len(df[coluna])
        A = round(max(df[coluna]) - min(df[coluna]))  # Amplitude total
        i = round(1 + 3.3 * np.log10(n))  # Quantidade de classes
        h = max(1, round(A / i))  # Amplitude da classe (mínimo 1 para evitar divisão por zero)

        menor = min(df[coluna])
        intervalos, fi, xi = [], [], []

        while menor <= max(df[coluna]):
            maior = menor + h
            intervalo = f"{menor:.2f} - {maior:.2f}"  # Intervalos com 2 casas decimais
            intervalos.append(intervalo)
            freq = len(df[(df[coluna] >= menor) & (df[coluna] < maior)])
            fi.append(freq)  # Frequência
            xi.append((menor + maior) / 2)  # Ponto médio
            menor = maior

        Fi = np.cumsum(fi)  # Frequência acumulada

        # Cria a tabela com formatação
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

# Solicita a escolha da coluna pelo número
while True:
    try:
        escolha = int(input("\nDigite o número da coluna desejada: ")) - 1
        if 0 <= escolha < len(colunas):
            tabela_distributiva(colunas[escolha])
            break
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número correspondente a uma coluna.") #caso o usuario digita algo que não seja o número, o código não da erro
