def fibonacci(n):
    """
    Função que gera a sequência de Fibonacci até o número informado.
    
    Args:
        n (int): Número até o qual a sequência de Fibonacci será gerada.
    
    Returns:
        list: Sequência de Fibonacci até o número informado.
    """
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci(n):
    """
    Função que verifica se um número pertence à sequência de Fibonacci.
    
    Args:
        n (int): Número a ser verificado.
    
    Returns:
        bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    fib_sequence = fibonacci(n)
    return n in fib_sequence

def main():
    # Número a ser verificado (pode ser alterado para qualquer valor)
    num = 13
    
    if check_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()