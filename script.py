# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skasmi <skasmi@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/08 17:42:24 by skasmi            #+#    #+#              #
#    Updated: 2023/06/08 17:44:43 by skasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
                    math.cos(3*k)-\
                    math.cos(4*k)
speed(100)
bgcolor("black")
for i in range(10000):
    goto(hearta (i)*20,heartb(i)*20)
    for i in range(1):
        color("#ff0000")
        goto(0,0)
done()