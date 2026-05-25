
import pandas as pnd
import matplotlib.pyplot as plt

# Leer archivo CSV
leer = pnd.read_csv("datos/ventas.csv")

# Crear columna total
leer["total"] = leer["cantidad"] * leer["precio"]

# Calcular ventas totales
ventas_totales = leer["total"].sum()

print("Ventas totales:", ventas_totales)

# Agrupar ventas por producto
ventas_producto = leer.groupby("producto")["cantidad"].sum()

# Crear gráfico
ventas_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad vendida")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")
