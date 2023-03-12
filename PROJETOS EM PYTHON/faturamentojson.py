import json

with open('dados.json') as arquivo:
    dados_json = json.load(arquivo)

menor_valor = float('inf')
dia_menor_valor = 0
maior_valor = float('-inf')
dia_maior_valor = 0
total_faturamento = 0
dias_acima_media = 0

for dado in dados_json:
    dia = dado['dia']
    valor = float(dado['valor'])
    total_faturamento += valor
    
    if valor < menor_valor:
        menor_valor = valor
        dia_menor_valor = dia
        
    if valor > maior_valor:
        maior_valor = valor
        dia_maior_valor = dia

media_faturamento = total_faturamento / len(dados_json)

for dado in dados_json:
    if float(dado['valor']) > media_faturamento:
        dias_acima_media += 1

print("Menor valor de faturamento:", menor_valor, "no dia", dia_menor_valor)
print("Maior valor de faturamento:", maior_valor, "no dia", dia_maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_media)
print("Faturamento total do mês:", total_faturamento)