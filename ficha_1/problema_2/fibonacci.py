# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fibonacci.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 14:19:49 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 14:29:36 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fibonacci(n):
    seq = [0]
    nbr = 1
    if (n == 0):
        return (print(0))
    print(0)
    for i in range(1, n):
        print(nbr)
        seq.append(nbr)
        nbr = seq[i] + seq[i - 1]

def main():
    n = int(input("Indique o numero de elementos a serem impressos: "))
    fibonacci(n)
    return

if __name__ == '__main__':
    main()
