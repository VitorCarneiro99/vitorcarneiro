
import requests

# Insira sua chave de API aqui
API_KEY = "OYA0yuafJNXyH1aJZ9knz6EZqIrlmPER"

# Obtenha as taxas de câmbio atuais
def get_exchange_rates(base_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&access_key={API_KEY}"
    response = requests.get(url)
    exchange_rates = response.json()["rates"]
    exchange_rates[base_currency] = 1.0  # Adicione a taxa base
    return exchange_rates

# Defina as taxas de câmbio atuais
base_currency = "USD"
exchange_rates = get_exchange_rates(base_currency)

# Solicite a entrada do usuário para a moeda base e a moeda de destino
print("Conversor de moedas")
print("Moedas suportadas: USD, EUR, GBP, BRL")
base_currency = input("Digite a moeda base (ex: USD): ")
target_currency = input("Digite a moeda de destino (ex: EUR): ")

# Verifique se as moedas de entrada são suportadas
if base_currency not in exchange_rates.keys() or target_currency not in exchange_rates.keys():
    print("Erro: moeda não suportada")
    exit()

# Solicite a entrada do usuário para o valor a ser convertido
amount = float(input(f"Digite o valor em {base_currency}: "))

# Converta o valor para a moeda de destino
target_amount = amount * exchange_rates[target_currency]

# Imprima o resultado
print(f"{amount:.2f} {base_currency} = {target_amount:.2f} {target_currency}")