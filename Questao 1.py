def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def test_fibonacci(n):
  contador = 0

  while True:
      resposta = fibonacci(contador)

      if resposta == n:
          return f"O numero {n} pertence a sequencia de Fibonacci"
      if resposta > n:
          return f"O numero {n} não pertence a sequencia de Fibonacci"
      contador += 1
    
def main():
    n = int(input('Digite um número: '))
    print(test_fibonacci(n))

if __name__ == '__main__':
    main()
