#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def verifica_fibonacci(num):
    a = 0
    b = 1
    while b < num:
        temp = a
        a = b
        b = temp + b
        
    if b == num:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")

# Exemplos de uso:
verifica_fibonacci(34)  # Exibe: 21 pertence à sequência de Fibonacci.
verifica_fibonacci(100)  # Exibe: 30 não pertence à sequência de Fibonacci.
