# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 14:45:01 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 14:48:11 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def somatorio(N):
    n = 0
    soma = 0
    while (n <= N):
        soma += n
        n += 1
    return (soma)

def main():
    N = int(input("Indique 'N'.\n O que é esperado confirmar é simplesmente Gauss: "))
    soma = somatorio(N)
    print(soma)

if __name__ == '__main__':
    main()
