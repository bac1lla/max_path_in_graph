from tkinter import *

from handlers import *

AUTHOR = "Васильев Александр М80-105Б-19"
ROOT_TITLE = "Нахождение максимального пути в нагруженном графе"

ROOT_WIDTH = 420
ROOT_HEGHT = 120
ROOT_DIMENTION = f"{ROOT_WIDTH}x{ROOT_HEGHT}"

MIN_MATRIX_DIMENTION = 2
MAX_MATRIX_DIMENTION = 8

root = Tk()
root.title(ROOT_TITLE) # задаём название окна

# задаём размер окна
root.geometry(ROOT_DIMENTION)
root.resizable(width=False, height=False)

var_dimention = IntVar()
vars_checkbox = [[IntVar() for i in range(MAX_MATRIX_DIMENTION)] for j in range(MAX_MATRIX_DIMENTION)]

label_author = Label(root, text=AUTHOR)
label_dimention_matrix = Label(root, text="Размер матрицы весов:")
dimention_maxtrix_spinbox = Spinbox(root, from_=MIN_MATRIX_DIMENTION, to=MAX_MATRIX_DIMENTION, increment=1, width=2, textvariable=var_dimention)
adjacency_maxtrix_button = Button(root, text="Задать матрицу весов", command=handle_adjacency_maxtrix_button(root, var_dimention, vars_checkbox))
start_button = Button(root, text="Запустить алгоритм", command=handle_start_button(root, var_dimention, vars_checkbox))

label_author.place(x=(ROOT_WIDTH / 2) - 70, y=ROOT_HEGHT - 25)
label_dimention_matrix.pack()
dimention_maxtrix_spinbox.place(x=(ROOT_WIDTH / 2) + 120, y=0)
adjacency_maxtrix_button.pack()
adjacency_maxtrix_button.pack()
start_button.pack()

root.protocol('WM_DELETE_WINDOW', exit)
root.mainloop()