# # Função para calcular a média e situação do aluno
# def sistema_notas():
#     # Solicita o nome do aluno
#     nome = input("Digite o nome do aluno: ")

#     # Solicita as três notas
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))
#     nota3 = float(input("Digite a terceira nota: "))

#     # Calcula a média
#     media = (nota1 + nota2 + nota3) / 3

#     # Verifica a situação do aluno
#     if media >= 7:
#         situacao = "Aprovado"
#     elif media >= 5:
#         situacao = "Recuperação"
#     else:
#         situacao = "Reprovado"

#     # Mostra o resultado final
#     print(f"\nAluno: {nome}")
#     print(f"Média: {media:.2f}")
#     print(f"Situação: {situacao}")


# # Chama a função
# sistema_notas()


#atividade 01
# def consumo_combustivel():
#     motorista = input("Digite o nome do motorista: ")
#     km = float(input("Digite a quantidade de quilômetros percorridos: "))
#     litros = float(input("Digite a quantidade de litros de combustível gastos: "))

#     consumo = km / litros

#     if consumo >= 15:
#         categoria = "Econômico"
#     elif consumo >= 10:
#         categoria = "Regular"
#     else:
#         categoria = "Alto Consumo"

#     print(f"\nMotorista: {motorista}")
#     print(f"Consumo médio: {consumo:.2f} km/l")
#     print(f"Categoria: {categoria}")

# consumo_combustivel()


# ##atividade 02
# # Programa: Calculadora de IMC
# # Solicita o nome da pessoa
# nome = input("Digite o nome da pessoa: ")

# # Solicita peso e altura
# peso = float(input("Digite o peso em kg: "))
# altura = float(input("Digite a altura em metros: "))

# # Calcula o IMC
# imc = peso / (altura ** 2)

# # Classifica o resultado
# if imc < 18.5:
#     classificacao = "Abaixo do peso"
# elif imc < 25:
#     classificacao = "Peso normal"
# elif imc < 30:
#     classificacao = "Sobrepeso"
# else:
#     classificacao = "Obesidade"

# # Mostra o resultado final
# print(f"\nNome: {nome}")
# print(f"IMC: {imc:.2f}")
# print(f"Classificação: {classificacao}")


# ###atividade 03
# # Função para verificar velocidade
# def verificar_velocidade():
#     # Solicita o nome do motorista
#     motorista = input("Digite o nome do motorista: ")

#     # Solicita a velocidade registrada
#     velocidade = float(input("Digite a velocidade em km/h: "))

#     # Verifica a classificação da velocidade
#     if velocidade <= 80:
#         classificacao = "Dentro do limite"
#     elif velocidade <= 100:
#         classificacao = "Acima do limite (leve)"
#     else:
#         classificacao = "Acima do limite (grave)"

#     # Mostra o resultado final
#     print(f"\nMotorista: {motorista}")
#     print(f"Velocidade registrada: {velocidade:.1f} km/h")
#     print(f"Classificação: {classificacao}")

# # Chama a função
# verificar_velocidade()


#atividade 04
# Função que recebe dois números e retorna a soma
def somar(a, b):
    return a + b


# Programa principal
print("=== Soma de dois números ===")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chama a função e guarda o resultado
resultado = somar(num1, num2)

# Mostra o resultado
print(f"\nA soma de {num1} + {num2} = {resultado}")


