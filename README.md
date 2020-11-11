# Нахождение максимального пути в нагруженном графе

# Алгоритм Форда — Фалкерсона

=== Формальное описание ===
Дан граф <math>G(V,E)</math> с пропускной способностью <math>c(u,v)</math> и потоком <math>f(u,v)=0</math> для рёбер из ''u'' в ''v''. Необходимо найти максимальный поток из источника ''s'' в сток ''t''. На каждом шаге алгоритма действуют те же условия, что и для всех потоков:

* <math> f(u,v) \leqslant c(u,v)</math>. Поток из <math>u</math> в <math>v</math> не превосходит пропускной способности.
* <math> f(u,v) = - f(v,u)</math>.
* <math> \sum_v f(u,v) = 0 \Longleftrightarrow f_{in}(u) = f_{out}(u)</math> для всех узлов <math>u</math>, кроме <math>s</math> и <math>t</math>. Поток не изменяется при прохождении через узел.

'''Остаточная сеть''' <math>G_f(V,E_f)</math> — сеть с пропускной способностью <math>c_f(u,v) = c(u,v) - f(u,v)</math> и без потока.

'''Вход''' Граф <math>G</math> с пропускной способностью <math>c</math>, источник <math>s</math> и сток <math>t</math><br />
'''Выход''' Максимальный поток <math>f</math> из <math>s</math> в <math>t</math><br />
   <math>f(u,v) := 0</math> для всех рёбер <math>(u,v)</math>
   Пока есть путь <math>p</math> из <math>s</math> в <math>t</math> в <math>G_f</math>, такой что <math>c_f(u,v) > 0</math> для всех рёбер <math>(u,v) \in p</math>:
    Найти <math>c_f(p) = \min\{c_f(u,v) \;|\; (u,v) \in p\}</math>
    Для каждого ребра <math>(u,v) \in p</math>
     <math>f(u,v) := f(u,v) + c_f(p)</math>
     <math>f(v,u) := f(v,u) - c_f(p)</math>
