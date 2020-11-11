from itertools import combinations
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
from adjacency_matrix import *
from PIL import ImageTk, Image
from random import randint

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from pprint import pprint


def handle_reset_adjacency_maxtrix_button(vars_checkbox):
    def inner():
        for row in vars_checkbox:
            for col in row:
                col.set(0)

    return inner

def handle_set_random_button(vars_checkbox):
    def inner():
        for row in vars_checkbox:
            for col in row:
                col.set(randint(1,10))

    return inner

def handle_adjacency_maxtrix_button(root, var_dimention, vars_checkbox):
    def inner():
        master = Toplevel(root)
        master.title("")
        root.resizable(width=False, height=False)

        for i in range(var_dimention.get()):
            for j in range(var_dimention.get()):
                # Checkbutton(master, variable=vars_checkbox[i][j], onvalue=1, offvalue=0).grid(row=i + 1, column=j + 1)
                Entry(master, textvariable=vars_checkbox[i][j], width=2).grid(row=i + 1, column=j + 1)
                if i == 0:
                    Label(master,text=ascii_uppercase[j]).grid(row=i, column=j + 1)
                if j == 0:
                    Label(master, text=ascii_uppercase[i]).grid(row=i + 1, column=j)

        Button(master, text="Cбросить", command=handle_reset_adjacency_maxtrix_button(vars_checkbox)).grid(columnspan=var_dimention.get() + 1)
        Button(master, text="Задать случайно", command=handle_set_random_button(vars_checkbox)).grid(columnspan=var_dimention.get() + 1)

        master.mainloop()

    return inner

def handle_start_button(root, var_dimention, vars_checkbox):
    def inner():
        master = Toplevel(root)
        master.title("Алгоритм")
        master.resizable(width=False, height=False)

        vertices = set()
        edge_labels = {}
        labels_for_G = {}
        adjacency_matrix = [] # матрица связности

        G = nx.DiGraph() # создаём граф

        for j in vars_checkbox[0:var_dimention.get()]:
            adjacency_matrix.append([k.get() for k in j[0:var_dimention.get()]])

        if adjacency_matrix_is_empty(adjacency_matrix):
            messagebox.showerror("Ошибка", "Матрица весов не заполнена.")
            return

        for j in range(var_dimention.get()):
            labels_for_G[j] = f"${ascii_uppercase[j]}$"

        adjacency_matrix = np.array(adjacency_matrix)


        for x, i in enumerate(adjacency_matrix):
            for y, j in enumerate(i):
                if j != 0:
                    vertices.add(y)
                    G.add_edge(x, y, weight=j)
                    edge_labels[(x, y)] = j

        try:
            max_path = nx.algorithms.dag.dag_longest_path(G, weight='weight')
        except:
            messagebox.showerror("Ошибка", "В графе есть цикл!")

        max_path_letters = map(lambda x: ascii_uppercase[x], max_path)

        # flow_value, flow_dict = nx.maximum_flow(G, 0, var_dimention.get() - 1)

        # for x, v in flow_dict.items():
        #     for y, w in v.items():
        #         edge_labels[(x, y)] = f"{edge_labels[(x, y)]}"

        # pprint(flow_dict)

        # result = []
        # for x, y in combinations(vertices, 2):
        #     try:
        #         all_paths = [p for p in nx.all_shortest_paths(G, source=int(x), weight='weight', target=int(y))]
        #         all_paths = map(lambda p: [ ascii_uppercase[x] for x in p ], all_paths)
        #         all_paths = map(lambda p: "->".join(p), all_paths)
        #         result.append(f"{ascii_uppercase[x]} -> {ascii_uppercase[y]}: { list(all_paths) }\n")
        #     except nx.exception.NetworkXNoPath:
        #         pass

        plt.figure(1)
        plt.clf()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500, node_color='pink', alpha=0.9, labels=labels_for_G)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        # pos = nx.get_node_attributes(G, 'pos')
        # labels_weight = nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_edge_labels(G, pos, with_labels=True, node_color='r', labels=labels_for_G, edge_labels=labels_weight)
        # nx.draw_networkx_edge_labels(G, pos, labels=labels_for_G, edge_labels=labels_weight)
        plt.savefig("input.png", dpi=75)

        input_obj = Image.open("input.png")
        img_input = ImageTk.PhotoImage(input_obj)
        panel_input = Label(master, image=img_input)
        panel_comp = Label(master, text=f"Максимальный путь: {'->'.join(max_path_letters)}", justify=LEFT)
        panel_input.pack(side="top", fill="both", expand="yes")
        panel_comp.pack()

        master.protocol('WM_DELETE_WINDOW', master.destroy)
        master.mainloop()

    return inner