import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Một khí cầu bay lên từ mặt đất v0. Gió truyền v_x=ay. Cho v0, a
#a. Xác định phương trình chuyển động của vật
#b. Xác định phương trình quỹ đạo của vật.
#c. Vẽ quỹ đạo của vật trong khoảng thời gian từ t=0 đến t=5s.

# Input vận tốc đầu (v_0) và gia tốc (a)
v_0 = int(input("Nhập vận tốc đầu v_0: "))
a = int(input("Nhập gia tốc đầu a: "))

# Define biến
t = sp.symbols('t')
y = sp.symbols('y')

# a. Xác định phương trình chuyển động y(t) and x(t)
y_t = v_0 * t                                        # Chuyển động theo phương thằng đứng ( trục Oy )
vx_t = a * y_t                                       # Chuyển động theo phương nằm ngang ( trục Ox ) 
x_t = sp.integrate(vx_t, t)
print("a) Phương trình chuyển động của vật: \nx(t) = ", x_t, "\ny(t) = ", y_t)

# b. Xác định phương trình quỹ đạo x(y)
x_y = x_t.subs(t, y / v_0)                           # Thay t = y / v_0 vào x(t) để biểu diễn x theo y:
print("b) Phương trình quỹ đạo của vật: \nx(y) = ", x_y)

# Convert và Plot bằng LaTeX label
plt.text(0.5, 0.8, f"câu $a)$", fontsize=18, ha='center')
plt.text(0.5, 0.65, f"$x(t) = {sp.latex(x_t)}$", fontsize=18, ha='center')
plt.text(0.5, 0.5, f"$y(t) = {sp.latex(y_t)}$", fontsize=18, ha='center')
plt.text(0.5, 0.35, f"câu $b)$", fontsize=18, ha='center')
plt.text(0.5, 0.2, f"$x(y) = {sp.latex(x_y)}$", fontsize=18, ha='center')
plt.axis('off')
plt.show()

# c. Vẽ quỹ đạo của vật trong khoảng thời gian từ t=0 đến t=5s
# Define lambdified 
y_plot = np.linspace(0, v_0 * 5, 400)               # y từ y(t=0)=0 đến y(t=5) va convert y(t) tu <'sympy.core.xxx.xxx'> thanh ndarray
x_y_plot = sp.lambdify(y, x_y, "numpy")             # convert x(y) từ <'sympy.core.xxx.xxx'> thành function
x_plot = x_y_plot(y_plot)                           # x thanh ndarray

# Plot quỹ đạo của vật
plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, label=f'$x(y) = {sp.latex(x_y)}$')
plt.title("Quỹ đạo của vật")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

"""
print(type(y), type(t))
print(type(x_y), type(x_t), type(y_t))
print(type(x_plot))
print(type(y_plot))
"""