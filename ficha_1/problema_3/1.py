# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    1.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 14:31:25 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 14:42:24 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def somatorio(N, a):
    soma = 0
    n = 0
    while (n <= N):
        soma += (a**n)
        n += 1
    return (soma)

def main():
    a = float(input("Indique 'a'.\n Lembrando que -1 < a < 1: "))
    N = int(input("Indique 'N'.\n Aproxime 'N' o máximo que conseguir de INT_MAX: "))
    print("Se voce por um numero muito grande o programa vai demorar a executar mesmo.")
    soma = "%.2f" % somatorio(N, a)
    print(soma)
    return

if __name__ == '__main__':
    main()
