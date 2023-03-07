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