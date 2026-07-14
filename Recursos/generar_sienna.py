"""
Generador de dataset POS para la cafetería ficticia "Sienna" (Costa Rica).
- Periodo: 2024-12-01 a 2026-05-31 (18 meses)
- Granularidad: una fila por producto vendido (línea de ticket)
- Moneda: colón costarricense (CRC), IVA 13% incluido en el precio
- Realismo: estacionalidad mensual, día de semana, hora pico, crecimiento, SINPE Móvil
"""

import numpy as np
import pandas as pd
from datetime import date, timedelta

rng = np.random.default_rng(42)

START = date(2024, 12, 1)
END = date(2026, 5, 31)
CERRADOS = {date(2024, 12, 25), date(2025, 1, 1), date(2025, 12, 25), date(2026, 1, 1)}

DIAS_ES = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
CAJEROS = ["María Jiménez", "José Vargas", "Daniela Mora", "Carlos Rojas", "Andrea Solís", "Luis Castro"]
PAGOS = ["Efectivo", "Tarjeta", "SINPE Móvil"]
PAGOS_P = [0.33, 0.42, 0.25]
ORDEN = ["Para llevar", "En sucursal"]
ORDEN_P = [0.57, 0.43]

# ---- Catálogo: (producto, {tamaño: precio_CRC}) ----
CAFE_CALIENTE = [
    ("Café Americano", {"Pequeño": 1200, "Mediano": 1500, "Grande": 1800}),
    ("Café Chorreado", {"Pequeño": 1100, "Mediano": 1400, "Grande": 1700}),
    ("Espresso", {"Único": 1100}),
    ("Espresso Doble", {"Único": 1500}),
    ("Cappuccino", {"Pequeño": 1700, "Mediano": 2100, "Grande": 2500}),
    ("Latte", {"Pequeño": 1800, "Mediano": 2200, "Grande": 2600}),
    ("Mocha", {"Pequeño": 2000, "Mediano": 2400, "Grande": 2800}),
    ("Cortado", {"Único": 1500}),
    ("Flat White", {"Pequeño": 1900, "Mediano": 2300}),
    ("Macchiato", {"Único": 1400}),
]
CAFE_FRIO = [
    ("Cold Brew", {"Mediano": 2200, "Grande": 2600}),
    ("Latte Helado", {"Mediano": 2100, "Grande": 2500}),
    ("Frappé de Café", {"Mediano": 2600, "Grande": 3000}),
    ("Affogato", {"Único": 2400}),
    ("Café Helado", {"Mediano": 1700, "Grande": 2000}),
]
BEBIDAS = [
    ("Té Caliente", {"Pequeño": 1300, "Mediano": 1600}),
    ("Chai Latte", {"Mediano": 2000, "Grande": 2400}),
    ("Matcha Latte", {"Mediano": 2400, "Grande": 2800}),
    ("Chocolate Caliente", {"Pequeño": 1900, "Mediano": 2300}),
    ("Agua Embotellada", {"Único": 900}),
    ("Jugo Natural", {"Único": 1800}),
    ("Limonada", {"Mediano": 1700, "Grande": 2000}),
]
REPOSTERIA = [
    ("Croissant", {"Único": 1500}),
    ("Croissant de Almendra", {"Único": 1900}),
    ("Muffin de Arándano", {"Único": 1600}),
    ("Brownie", {"Único": 1700}),
    ("Galleta de Chocolate", {"Único": 1000}),
    ("Cheesecake", {"Único": 2500}),
    ("Pan Casero", {"Único": 1200}),
    ("Empanada de Queso", {"Único": 1300}),
    ("Empanada de Frijol", {"Único": 1300}),
    ("Tres Leches", {"Único": 2400}),
]
COMIDA = [
    ("Sándwich Jamón y Queso", {"Único": 3200}),
    ("Bagel con Queso Crema", {"Único": 2800}),
    ("Quiche", {"Único": 3000}),
    ("Tostada de Aguacate", {"Único": 3500}),
    ("Wrap de Pollo", {"Único": 3600}),
    ("Ensalada César", {"Único": 3800}),
    ("Gallo Pinto", {"Único": 2900}),
]
RETAIL = [
    ("Bolsa de Café 340g", {"Único": 5500}),
    ("Bolsa de Café 1kg", {"Único": 12000}),
    ("Taza Sienna", {"Único": 4500}),
]

CATALOGO = {
    "Café Caliente": CAFE_CALIENTE,
    "Café Frío": CAFE_FRIO,
    "Bebidas": BEBIDAS,
    "Repostería": REPOSTERIA,
    "Comida": COMIDA,
    "Retail": RETAIL,
}
CATS = list(CATALOGO.keys())

# Probabilidad de categoría para el 1er ítem (sesgo a café) y para ítems adicionales
P_CAT_PRIMERO = {"Café Caliente": 0.50, "Café Frío": 0.12, "Bebidas": 0.12,
                 "Repostería": 0.16, "Comida": 0.08, "Retail": 0.02}
P_CAT_EXTRA = {"Café Caliente": 0.18, "Café Frío": 0.07, "Bebidas": 0.12,
               "Repostería": 0.40, "Comida": 0.18, "Retail": 0.05}

# Tamaño: preferencia por Mediano cuando hay opciones
def elegir_tamano(precios):
    tams = list(precios.keys())
    if tams == ["Único"]:
        return "Único", precios["Único"]
    pesos = {"Pequeño": 0.28, "Mediano": 0.50, "Grande": 0.22}
    w = np.array([pesos.get(t, 0.3) for t in tams], dtype=float)
    w /= w.sum()
    t = rng.choice(tams, p=w)
    return t, precios[t]

def elegir_producto(prob_cat):
    cats = list(prob_cat.keys())
    p = np.array([prob_cat[c] for c in cats]); p /= p.sum()
    cat = rng.choice(cats, p=p)
    prods = CATALOGO[cat]
    prod, precios = prods[rng.integers(len(prods))]
    tam, precio = elegir_tamano(precios)
    return cat, prod, tam, precio

# Distribución horaria (apertura 6:00 - 20:00)
HORAS = list(range(6, 21))
W_SEMANA = np.array([2, 7, 11, 10, 7, 5, 7, 6, 5, 5, 5, 5, 4, 3, 2], dtype=float)
W_FINDE  = np.array([1, 3, 6, 9, 10, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2], dtype=float)
W_SEMANA /= W_SEMANA.sum(); W_FINDE /= W_FINDE.sum()

DOW_FACTOR = {0: 0.95, 1: 0.95, 2: 1.00, 3: 1.05, 4: 1.18, 5: 1.32, 6: 1.12}
MONTH_FACTOR = {1: 1.10, 2: 1.10, 3: 1.15, 4: 1.10, 5: 0.95, 6: 0.90,
                7: 1.00, 8: 0.95, 9: 0.85, 10: 0.85, 11: 0.98, 12: 1.22}
BASE_TICKETS = 78

total_dias = (END - START).days + 1
filas = []
tid = 0

dia = START
idx = 0
while dia <= END:
    idx += 1
    if dia in CERRADOS:
        dia += timedelta(days=1)
        continue
    dow = dia.weekday()
    growth = 0.85 + 0.33 * (idx / total_dias)          # crecimiento del negocio
    noise = float(np.clip(rng.normal(1.0, 0.08), 0.75, 1.25))
    n_tickets = max(20, int(round(BASE_TICKETS * DOW_FACTOR[dow] * MONTH_FACTOR[dia.month] * growth * noise)))

    wh = W_FINDE if dow >= 5 else W_SEMANA
    for _ in range(n_tickets):
        tid += 1
        id_ticket = f"S-{tid:06d}"
        hora = int(rng.choice(HORAS, p=wh))
        minuto = int(rng.integers(0, 60)); seg = int(rng.integers(0, 60))
        ts = pd.Timestamp(dia.year, dia.month, dia.day, hora, minuto, seg)
        cajero = CAJEROS[rng.integers(len(CAJEROS))]
        pago = rng.choice(PAGOS, p=PAGOS_P)
        orden = rng.choice(ORDEN, p=ORDEN_P)

        n_items = int(rng.choice([1, 2, 3, 4], p=[0.42, 0.34, 0.18, 0.06]))
        for j in range(n_items):
            prob = P_CAT_PRIMERO if j == 0 else P_CAT_EXTRA
            cat, prod, tam, precio = elegir_producto(prob)
            qty = int(rng.choice([1, 2, 3], p=[0.86, 0.11, 0.03]))
            filas.append((
                id_ticket, ts, dia.isoformat(), f"{hora:02d}:{minuto:02d}",
                DIAS_ES[dow], cat, prod, tam, qty, precio, qty * precio,
                pago, orden, cajero,
            ))
    dia += timedelta(days=1)

cols = ["id_ticket", "fecha_hora", "fecha", "hora", "dia_semana", "categoria",
        "producto", "tamano", "cantidad", "precio_unitario", "subtotal",
        "metodo_pago", "tipo_orden", "cajero"]
df = pd.DataFrame(filas, columns=cols)
df = df.sort_values(["fecha_hora", "id_ticket"]).reset_index(drop=True)
df["fecha_hora"] = df["fecha_hora"].dt.strftime("%Y-%m-%d %H:%M:%S")

import os
# El CSV se escribe en la carpeta hermana "Data Set" (estructura del proyecto Sienna)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out = os.path.normpath(os.path.join(BASE_DIR, "..", "Data Set", "sienna_ventas_pos.csv"))
os.makedirs(os.path.dirname(out), exist_ok=True)
df.to_csv(out, index=False, encoding="utf-8")

# -------- Verificación --------
dias_abiertos = df["fecha"].nunique()
es_cafe = df["categoria"].isin(["Café Caliente", "Café Frío"])
cafes_lineas_dia = es_cafe.sum() / dias_abiertos
cafes_tazas_dia = df.loc[es_cafe, "cantidad"].sum() / dias_abiertos
integridad = bool((df["subtotal"] == df["cantidad"] * df["precio_unitario"]).all())

print("=== RESUMEN SIENNA ===")
print(f"Filas (líneas de ticket): {len(df):,}")
print(f"Tickets únicos: {df['id_ticket'].nunique():,}")
print(f"Rango de fechas: {df['fecha'].min()} a {df['fecha'].max()}")
print(f"Días abiertos: {dias_abiertos} (cerrados: {len(CERRADOS)})")
print(f"Cafés/día promedio (líneas): {cafes_lineas_dia:.1f}")
print(f"Cafés/día promedio (tazas):  {cafes_tazas_dia:.1f}")
print(f"Ingreso total (CRC): {df['subtotal'].sum():,}")
print(f"Ticket promedio (CRC): {df.groupby('id_ticket')['subtotal'].sum().mean():,.0f}")
print(f"Integridad subtotal=cant*precio: {integridad}")
print(f"Nulos por columna:\n{df.isnull().sum().to_string()}")
print("\nMix por categoría (%):")
print((df['categoria'].value_counts(normalize=True) * 100).round(1).to_string())
print("\nMétodos de pago (%):")
print((df['metodo_pago'].value_counts(normalize=True) * 100).round(1).to_string())
