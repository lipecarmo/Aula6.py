#  Crie um programa que converta metros para centímetros.
# Peça ao usuário para digitar um valor em metros, armazene
# em uma variável e converta para centímetros.

# while True:
#     try:
#       metros = float(input('Digite um valor em metros:').replace(',','.'))
#     except:
#         print('Apenas números são aceitos')
#     else:
#         centimetros = metros * 100
#         break
    
    

# print(f'O valor convertido para centímetros é igual a:{centimetros:.2f}')0



# Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.

# Passo 1: Solicitar a idade do usuário
# idade = int(input("Digite a sua idade: "))

# # Passo 2: Classificar a idade
# if idade < 12:
#     categoria = "criança"
# elif 12 <= idade < 18:
#     categoria = "adolescente"
# elif 18 <= idade < 60:
#     categoria = "adulto"
# else:
#     categoria = "idoso"

# # Passo 3: Exibir a categoria
# print(f"Você é {categoria}.")


# Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100
# e informe o conceito (A, B, C, D, F) com base na nota.

# # Passo 1: Solicitar a nota do usuário
# nota = float(input("Digite uma nota de 0 a 100: "))

# # Passo 2: Verificar se a nota está dentro do intervalo válido
# if 0 <= nota <= 100:
#     # Passo 3: Determinar o conceito com base na nota
#     if nota >= 90:
#         conceito = "A"
#     elif nota >= 80:
#         conceito = "B"
#     elif nota >= 70:
#         conceito = "C"
#     elif nota >= 60:
#         conceito = "D"
#     else:
#         conceito = "F"
    
#     # Passo 4: Exibir o conceito
#     print(f"O conceito para a nota {nota} é: {conceito}.")
# else:
#     # Passo 5: Informar que a nota é inválida
#     print("Nota inválida. Por favor, digite uma nota entre 0 e 100.")



# Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.


# # Passo 1: Solicitar o dia e o mês de nascimento
# dia = int(input("Digite o dia do seu nascimento (1-31): "))
# mes = int(input("Digite o mês do seu nascimento (1-12): "))

# # Passo 2: Determinar o signo com base no dia e mês
# if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
#     signo = "Aquário"
# elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
#     signo = "Peixes"
# elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
#     signo = "Áries"
# elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
#     signo = "Touro"
# elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
#     signo = "Gêmeos"
# elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
#     signo = "Câncer"
# elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
#     signo = "Leão"
# elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
#     signo = "Virgem"
# elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
#     signo = "Libra"
# elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
#     signo = "Escorpião"
# elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
#     signo = "Sagitário"
# else:
#     signo = "Capricórnio"

# # Passo 3: Exibir o signo
# print(f"Seu signo é: {signo}.")

# Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

# # Passo 1: Inicializar variáveis
soma = 0  # Variável para armazenar a soma dos números pares
numero = 1  # Começar a contagem a partir de 1

# # Passo 2: Usar um laço while para iterar de 1 a 100
while numero <= 100:
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero  # Adiciona o número par à soma
    numero += 1  # Incrementa o número

# # Passo 3: Exibir o resultado
print(f"A soma dos números pares de 1 a 100 é: {soma}.")


# Verificação de Palíndromo:
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo
# (lê-se da mesma forma de trás para frente).

# Passo 1: Solicitar uma palavra ao usuário
palavra = input("Digite uma palavra: ").strip()

# # Passo 2: Inicializar variáveis
inicio = 0  # Índice do início da palavra
fim = len(palavra) - 1  # Índice do final da palavra

# # Passo 3: Usar um laço while para verificar se a palavra é um palíndromo
eh_palindromo = True  # Assume que a palavra é um palíndromo

# while inicio < fim:
    if palavra[inicio].lower() != palavra[fim].lower():  # Verifica os caracteres
        eh_palindromo = False  # Se não forem iguais, não é palíndromo
        break  # Sai do laço se não for palíndromo
    inicio += 1  # Move o índice do início para a direita
    fim -= 1  # Move o índice do fim para a esquerda

# # Passo 4: Exibir o resultado
if eh_palindromo:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

