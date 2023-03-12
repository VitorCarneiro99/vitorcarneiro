def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def verifica_fibonacci(num):
    fib = fibonacci(num)
    if num in fib:
        print(f"{num} pertence à sequência de Fibonacci!")
        print(f"Os próximos 10 números da sequência a partir de {num} são: {fibonacci(num+11)[-10:]}")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

# loop principal
while True:
    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci e mostrar os próximos 10 números da sequência a partir deste número: "))
    verifica_fibonacci(num)
    
    # perguntar se o usuário quer fazer novamente ou sair
    resposta = input("Deseja fazer novamente? (s/n)").lower()
    if resposta == "n":
        break