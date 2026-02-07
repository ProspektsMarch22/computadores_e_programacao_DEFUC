# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pi_sobre_dois.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 15:51:40 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 16:07:42 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def p(n):
    produto = 1
    for i in range(1, n + 1):
        produto *= (((2 * i) * (2 * i))/(((2 * i) - 1) * ((2 * i) + 1)))
    return (produto)

def pi_sobre_dois():
    n = 1
    while (abs((math.pi / 2) - p(n)) >= 0.0001):
        n += 1
    return (n)

def main():
    print(pi_sobre_dois())

if __name__ == '__main__':
    main()
