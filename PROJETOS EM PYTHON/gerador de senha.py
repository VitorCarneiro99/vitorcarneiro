import random
import string

def generate_password(length, num_letters, num_uppercase, num_digits, num_special_chars):
    """Gera uma senha aleatória de tamanho `length` com `num_letters`
    letras minúsculas, `num_uppercase` letras maiúsculas, `num_digits`
    números e `num_special_chars` caracteres especiais."""
    
    # Cria uma lista com os caracteres possíveis
    letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters

    # Adicionar as letras minúsculas
    for i in range(num_letters):
        all_chars += letters

    # Adicionar as letras maiúsculas
    for i in range(num_uppercase):
        all_chars += uppercase_letters

    # Adicionar os números
    for i in range(num_digits):
        all_chars += digits

    # Adicionar os caracteres especiais
    for i in range(num_special_chars):
        all_chars += special_chars

    # Gerar a senha aleatória
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

# Ler as opções do usuário
length = int(input("Quantos caracteres deve ter a senha? "))
num_letters = int(input("Quantas letras minúsculas devem ter na senha? "))
num_uppercase = int(input("Quantas letras maiúsculas devem ter na senha? "))
num_digits = int(input("Quantos números devem ter na senha? "))
num_special_chars = int(input("Quantos caracteres especiais devem ter na senha? "))

# Gerar a senha aleatória
password = generate_password(length, num_letters, num_uppercase, num_digits, num_special_chars)

# Exibir a senha gerada
print("Senha gerada:", password)