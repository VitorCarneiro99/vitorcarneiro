dados = [
    {"dia": 1, "valor": 31490.7866},
    {"dia": 2, "valor": 37277.94},
    {"dia": 3, "valor": 37708.4303},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 17934.2269},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 6965.1262},
    {"dia": 9, "valor": 24390.9374},
    {"dia": 10, "valor": 14279.6481},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 39807.6622},
    {"dia": 14, "valor": 27261.6304},
    {"dia": 15, "valor": 39775.6434},
    {"dia": 16, "valor": 29797.6232},
    {"dia": 17, "valor": 17216.5017},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 12974.2},
    {"dia": 21, "valor": 28490.9861},
    {"dia": 22, "valor": 8748.0937},
    {"dia": 23, "valor": 8889.0023},
    {"dia": 24, "valor": 17767.5583},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 3071.3283},
    {"dia": 28, "valor": 48275.2994},
    {"dia": 29, "valor": 10299.6761},
    {"dia": 30, "valor": 39874.1073},
]

# Calcula menor e maior valor de faturamento
valores = [d["valor"] for d in dados]
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula média mensal de faturamento
soma = sum(valores)
media = soma / len(dados)

# Calcula número de dias com faturamento superior à média
dias_acima_da_media = sum(1 for d in dados if d["valor"] > media)

# Imprime resultados
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)