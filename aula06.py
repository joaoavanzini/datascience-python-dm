# -*- coding: utf-8 -*-

# visualização de dados em Python

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

titulo = "Scatterplot: gráfico de dispersão (ou gráfico de pontos)"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="k", linestyle=":")
plt.scatter(x, y, label="Meus pontos", color='r', marker='.', s=200)
plt.legend();
plt.show()

'''
cores (color):

'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white

marcadores (marker):

'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	

estilo da linha (linestyle):

'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style

'''