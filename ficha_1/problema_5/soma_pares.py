# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    soma_pares.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 15:40:39 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 15:47:33 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#NOTA: estou PRESSUPONDO que o intervalo entre n e m é fechado!

def soma_pares(n, m):
    if (n <= m):
        menor = n
        maior = m
    else:
        menor = m
        maior = n
    soma = 0
    for i in range(menor, (maior + 1)):
        if (i % 2 == 0):
            soma += i
    return (soma)

def main():
    n = int(input("Defina n: "))
    m = int(input("Defina m: "))
    print(soma_pares(n, m))

if __name__ == '__main__':
    main()
