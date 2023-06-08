# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script_color.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skasmi <skasmi@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/08 17:58:16 by skasmi            #+#    #+#              #
#    Updated: 2023/06/08 17:58:19 by skasmi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)