# Sienna — Dataset POS (diccionario de datos)

Cafetería ficticia en Costa Rica. Datos de ventas a nivel **línea de ticket** (una fila por producto vendido). Moneda: **colón (CRC)**, IVA 13% incluido en el precio.

## Cobertura
- Periodo: **2024-12-01 a 2026-05-31** (18 meses)
- Filas: **90,756** | Tickets: **48,384** | Días abiertos: **543** (cerrado 25-dic y 1-ene)
- Promedio: **~75 líneas de café/día (~87 tazas/día)** — supera el mínimo de 40
- Ingreso total: ₡228,240,000 | Ticket promedio: ₡4,717

## Columnas
| Columna | Tipo | Descripción |
|---|---|---|
| id_ticket | texto | ID de la venta. Se repite en cada línea del mismo ticket (clave para `groupby`). |
| fecha_hora | datetime | Marca de tiempo de la venta (`YYYY-MM-DD HH:MM:SS`). |
| fecha | fecha | Fecha (`YYYY-MM-DD`). |
| hora | texto | Hora:minuto (`HH:MM`). |
| dia_semana | texto | Lunes…Domingo. |
| categoria | texto | Café Caliente, Café Frío, Bebidas, Repostería, Comida, Retail. |
| producto | texto | Nombre del producto. |
| tamano | texto | Pequeño/Mediano/Grande, o `Único` si no aplica. |
| cantidad | entero | Unidades de esa línea. |
| precio_unitario | entero | Precio por unidad en CRC (IVA incl.). |
| subtotal | entero | `cantidad * precio_unitario`. |
| metodo_pago | texto | Efectivo, Tarjeta, SINPE Móvil. |
| tipo_orden | texto | Para llevar / En sucursal. |
| cajero | texto | Empleado que registró la venta. |

## Patrones incluidos (para que el análisis tenga señal)
- **Día de semana**: pico fin de semana (sáb +32%, vie +18%); lun-mar más bajos.
- **Hora**: pico mañana 7–10h; segundo pico almuerzo 12–14h; tarde/noche menor.
- **Estacionalidad**: alza en temporada seca/diciembre (dic +22%, mar +15%); baja set-oct (−15%).
- **Crecimiento**: tendencia ascendente del negocio a lo largo de los 18 meses.

## Ejercicios sugeridos
1. Ingresos por mes y serie de tiempo; identifica estacionalidad y tendencia.
2. Top 10 productos por unidades y por ingreso (no siempre coinciden).
3. Ticket promedio por `tipo_orden` y por `metodo_pago`.
4. Heatmap día_semana × hora (conteo de tickets).
5. Mix de categorías por mes; participación del café.
6. Reconstruye ventas por ticket: `df.groupby('id_ticket').agg(...)`.

Reproducible con `generar_sienna.py` (semilla fija = 42). Cambia `END` para simular la actualización mensual.
