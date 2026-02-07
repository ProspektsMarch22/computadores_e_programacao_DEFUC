# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fatorial.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: icezar-s <icezar-s@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 14:08:10 by icezar-s          #+#    #+#              #
#    Updated: 2026/02/07 14:15:26 by icezar-s         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fatorial(n):
    fat = n;
    while ( n > 1 ):
        n -= 1
        fat *= n
    return (fat)

def main():
    n = int(input("Defina N: "))
    fat = fatorial(n)
    print(f"Fatorial de N é: {fat}")

if __name__ == "__main__":
    main()
