# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 15:01:20 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 15:19:18 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#A esse ponto você já percebeu que estamos usando várias vezes a função "fatorial(n)".
#E se tivesse um jeito de ->importar<- essa função de um outro arquivo?

def fatorial(n):
    if (n == 0):
        return (1)
    fat = n
    while (n > 1):
        n -= 1
        fat *= n
    return (fat)

def somatorio(N, x):
    n = 0
    soma = 0
    while (n <= N):
        soma += (((-1) ** n) * (x ** ((2 * n) + 1)))/(fatorial((2 * n) + 1))
        n += 1
    return (soma)

def main():
    N = int(input("Defina 'N'\n Pelo o amor de deus coloque N entre 1 e 10 senao o computador explode: "))
    x = float(input("Defina 'x': "))
    soma = somatorio(N, x)
    print(soma)

if __name__ == '__main__':
    main()
