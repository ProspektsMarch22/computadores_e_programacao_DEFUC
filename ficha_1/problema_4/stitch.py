# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stitch.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 15:21:31 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 15:28:31 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def is_primo(n):
    if (n < 2 or type(n) != type(1)):
        return (False)
    i = 2
    while (i <= math.sqrt(n)):
        if (n % i == 0):
            return (False)
        i += 1
    return (True)

def n_primos(N):
    i = 0
    n = 2
    while (i < N):
        if (is_primo(n)):
            print(n)
            i += 1
        n += 1

def main():
    N = int(input("Defina N: "))
    n_primos(N)

if __name__ == '__main__':
    main()
