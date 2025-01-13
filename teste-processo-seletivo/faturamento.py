import json

def calcular_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    faturamento = dados['faturamento']

    # Filtrando os valores de faturamento
    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    if not valores:
        print("Não há dias com faturamento.")
        return

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_faturamento = sum(valores) / len(valores)

    # Contando os dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in valores if valor > media_faturamento)

    print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
    print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Chamada da função com o arquivo JSON
calcular_faturamento('faturamento.json')