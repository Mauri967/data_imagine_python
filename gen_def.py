import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Ruta al Escritorio, es necesario en Windows 11 por sus conexiones directas a OneDrive
escritorio = "C:/Users/raro9/OneDrive/Escritorio"
os.chdir(escritorio)

# Número de registros
n_registros = 200000

# Función para generar ID de registro
def generar_id(n):
    return f"MECMTUV{n:05d}"

# Fecha de inicio y fin (de todas formas, el out put será mm/dd/aaaa)
fecha_inicio = datetime(2000, 1, 1)
fecha_fin = datetime(2025, 12, 31)

# lista de conceptos
conceptos = ["Sales", "Cost of Sales", "Total Expense", "Financial Cost(income)"]
# lista de productos
productos = ["Kappa", "Lambda", "Phi", "Rho"]

# Estados de EEUU
estados_eeuu = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
    "Wisconsin", "Wyoming"]

# Crear lista para almacenar los datos
data = []
for i in range(n_registros):
    id_registro = generar_id(i + 1)
    
    # fecha aleatoria
    tiempo_transcurrido = random.randint(0, int((fecha_fin - fecha_inicio).total_seconds()))
    fecha_aleatoria = fecha_inicio + timedelta(seconds=tiempo_transcurrido)
    fecha_formateada = fecha_aleatoria.strftime("%d/%m/%Y")  # Formato dd/mm/aaaa

    concepto = random.choice(conceptos)

    # Generar montos condicionados (usando distribución normal, pero puede ser cualquier distribución y jugar con los parametros
    if concepto == "Sales":
        monto_total = round(np.random.normal(70, 40), 2)  # Media 50, desviación estándar 20
        monto_total = max(0, monto_total) # Evitar valores negativos
    elif concepto == "Cost of Sales":
        monto_total = round(np.random.normal(25, 10), 2)  # Media 25, desviación estándar 10
        monto_total = max(0, monto_total) # Evitar valores negativos
    elif concepto == "Total Expense":
        monto_total = round(np.random.normal(15, 5), 2)  # Media 15, desviación estándar 5
        monto_total = max(0, monto_total) # Evitar valores negativos
    else:
        monto_total = round(np.random.normal(7, 3), 2)  # Media 7, desviación estándar 3
        monto_total = max(0, monto_total) # Evitar valores negativos

    # Generar productos y estados solo para "Ventas totales", en el producto final, cuando el concepto es diferente de "Sales", es un registro vacio (o null)
    if concepto == "Sales":
        producto = random.choice(productos)
        estado = random.choice(estados_eeuu)
    else:
        producto = None
        estado = None

    data.append([id_registro, fecha_formateada, concepto, monto_total, producto, estado])

# Crear DataFrame con pandas
df = pd.DataFrame(data, columns=["ID registro", "Fecha", "Concepto", "Monto total", "Productos", "Estado"])

# Guardar DataFrame en formato CSV en el Escritorio, insisto, Windows 11 tiene ciertos "detalles" por tener todo integrado a One Drive, debe ser en una carpeta local
ruta_completa = os.path.join(escritorio, "base_de_datos_imaginaria.csv")
df.to_csv(ruta_completa, index=False)

print(f"Base de datos generada y guardada en: {ruta_completa}")