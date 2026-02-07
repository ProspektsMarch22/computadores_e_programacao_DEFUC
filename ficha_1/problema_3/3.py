# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 14:48:45 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 14:56:28 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fatorial(n):
    if (n == 0):
        return (1)
    fat = n;
    while (n > 1):
        n -= 1
        fat *= n
    return (fat)

def somatorio(N, x):
    soma = 0
    n = 0
    while (n <= N):
        soma += ((x ** n)/(fatorial(n)))
        n += 1
    return (soma)

def main():
    N = int(input("Defina 'N': "))
    x = float(input("Defina 'x': "))
    #Você pode remover a parte entre o sinal de '=' e '%' caso queira a resposta inteira
    soma = "%.2f" % somatorio(N, x)
    print(soma)

if __name__ == '__main__':
    main()
