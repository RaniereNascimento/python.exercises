#Programa que calcula o índice de massa corporal(IMC)
#Inserirdo dados no programa
altura = float(input("insira sua altura: "))
peso = float(input("insira seu peso: "))
#Processamento de dados
imc = peso/altura**2
# Retornando o valor processado e imprimindo o resultado na tela
print("O valor de seu IMC é: ", imc,".")
