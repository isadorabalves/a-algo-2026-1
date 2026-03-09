import time
import sys

sys.setrecursionlimit(2000)

def fatorial(n):

    if n <= 1:
        return 1

    return n * fatorial(n - 1)

valores = [10, 100, 500, 1000]

for numero in valores:

    inicio = time.time()
    resultado = fatorial(numero)
    fim = time.time()
    tempo_execucao = fim - inicio

    print("Número:", numero)
    print("Tempo de execução:", tempo_execucao)
    print()

    # Resultados do tempo de execução do programa:

    # Número: 10
    # Tempo de execução: 3.0994415283203125e-06

    # Número: 100
    # Tempo de execução: 2.3126602172851562e-05

    # Número: 500
    # Tempo de execução: 0.00019621849060058594

    # Número: 1000
    # Tempo de execução: 0.0003948211669921875

   # Conforme se observa pelos resultados obtidos, à medida que o valor da entrada aumenta,
   # o tempo de execução do algoritmo também cresce.
   
   # No presente exercício, que calcula o fatorial utilizando recursão, a cada chamada da
   # função o valor de n é reduzido em 1 até alcançar o caso base (n <= 1).
   
   # Dessa forma, o número de chamadas da função depende diretamente do valor de n.
   # Assim, quanto maior o valor de n, maior será a quantidade de chamadas realizadas
   # pela função recursiva.
   
   # Portanto, a complexidade assintótica do algoritmo é O(n), pois o tempo de execução
   # cresce de forma linear em relação ao tamanho da entrada.
   
   # Ressalta-se que, ao testar o valor n = 1000, foi necessário utilizar a biblioteca
   # sys para aumentar o limite de chamadas recursivas, uma vez que o Python possui
   # um limite padrão para esse tipo de chamada..