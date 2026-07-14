<div align="center">

# Business Intelligence Aplicado
### Sienna Coffee Shop | SQL · DuckDB · Excel

Proyecto de análisis de datos de punta a punta sobre una **cafetería ficticia de Costa Rica**. Convierte **90.756 líneas de ventas POS**, 18 meses de operación y un catálogo de costos por SKU en una lectura ejecutiva del negocio: crecimiento, demanda, productos, rentabilidad y operación. El resultado final es una narrativa visual profesional orientada a portafolio, LinkedIn y procesos de reclutamiento para Analista de Datos / BI.

<br>

![SQL](https://img.shields.io/badge/SQL-DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=000000)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Business Intelligence](https://img.shields.io/badge/Business_Intelligence-435152?style=for-the-badge)
![Data Visualization](https://img.shields.io/badge/Data_Visualization-638579?style=for-the-badge)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Completado-success?style=for-the-badge)

</div>

---

## Tabla de contenidos

- [Resumen del proyecto](#resumen-del-proyecto)
- [Objetivo y preguntas de negocio](#objetivo-y-preguntas-de-negocio)
- [Datasets](#datasets)
- [Stack y herramientas](#stack-y-herramientas)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Metodología y flujo de trabajo](#metodología-y-flujo-de-trabajo)
- [Análisis realizado](#análisis-realizado)
- [Hallazgos clave](#hallazgos-clave)
- [Visualizaciones](#visualizaciones)
- [Cómo reproducir](#cómo-reproducir)
- [Habilidades demostradas](#habilidades-demostradas)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Resumen del proyecto

Análisis integral de **Sienna**, una cafetería ficticia construida como caso de negocio para practicar el flujo real de un Analista de Datos. El proyecto parte de transacciones POS a nivel de línea de ticket y conecta cuatro perspectivas:

1. **Desempeño comercial:** ingresos, tickets, unidades y evolución mensual.
2. **Comportamiento de la demanda:** días, horas, métodos de pago y tipo de orden.
3. **Portafolio de productos:** ranking, Pareto e ingeniería de menú.
4. **Rentabilidad y operación:** costos directos, margen de contribución y carga por cajero.

> Proyecto de portafolio orientado a un perfil de **Analista de Datos Junior / Business Intelligence**.

La idea central es demostrar que un análisis profesional no termina al calcular métricas: debe validar los datos, mantener definiciones consistentes y convertir los resultados en una historia que facilite decisiones.

---

## Objetivo y preguntas de negocio

Transformar los datos operativos de Sienna en recomendaciones accionables:

- ¿Cómo evolucionan el **ingreso, los tickets y el ticket promedio**?
- ¿El crecimiento proviene de mayor gasto por cliente o de **más volumen**?
- ¿Qué días y horas concentran la demanda?
- ¿Cuáles SKU lideran por **ingreso, unidades y margen**?
- ¿El menú sigue realmente una distribución **Pareto 80/20**?
- ¿Qué categorías combinan escala y rentabilidad?
- ¿Cómo se distribuyen los pagos, tipos de orden y carga entre cajeros?
- ¿Qué acciones debería priorizar la gerencia?

---

## Datasets

### `sienna_ventas_pos.csv`

Dataset sintético con **90.756 filas**. La granularidad es una línea de producto dentro de un ticket.

| Columna | Tipo | Descripción |
|---|---|---|
| `id_ticket` | texto | Identificador del ticket |
| `fecha_hora` | fecha-hora | Momento exacto de la transacción |
| `fecha` | fecha | Día de la venta |
| `hora` | hora | Hora de la venta |
| `dia_semana` | categoría | Día de lunes a domingo |
| `categoria` | categoría | Familia comercial del producto |
| `producto` | texto | Nombre del producto |
| `tamano` | categoría | Pequeño, mediano, grande o único |
| `cantidad` | entero | Unidades vendidas en la línea |
| `precio_unitario` | número (₡) | Precio por unidad |
| `subtotal` | número (₡) | `cantidad × precio_unitario` |
| `metodo_pago` | categoría | Tarjeta, efectivo o SINPE Móvil |
| `tipo_orden` | categoría | Para llevar o en sucursal |
| `cajero` | categoría | Cajero responsable del ticket |

### `sienna_catalogo_costos.csv`

Catálogo con **62 SKU únicos**, utilizado para incorporar la dimensión económica del menú.

| Columna | Descripción |
|---|---|
| `categoria` | Categoría comercial |
| `producto` | Nombre del producto |
| `tamano` | Tamaño del SKU |
| `precio_venta` | Precio unitario |
| `costo_directo` | Costo de insumos por unidad |
| `margen_contribucion` | `precio_venta − costo_directo` |
| `pct_margen` | Margen de contribución porcentual |

**Cobertura:** diciembre de 2024 a mayo de 2026, 18 meses completos, 48.384 tickets y 106.223 unidades.

> Calidad del dato: el catálogo cubre el 100% de los SKU vendidos y el cruce conserva exactamente las 90.756 filas. Las líneas idénticas se mantienen porque la granularidad permite artículos repetidos dentro del mismo ticket; no se aplicó una deduplicación automática.

---

## Stack y herramientas

| Herramienta | Uso en el proyecto |
|---|---|
| **DuckDB CLI** | Consultas directas sobre CSV sin cargar una base de datos |
| **SQL** | Agregaciones, `COUNT(DISTINCT)`, CTE, joins y funciones de ventana |
| **Microsoft Excel para Mac** | Tablas dinámicas, porcentajes acumulados, gráficos y análisis exploratorio |
| **Catálogo de costos** | Cálculo de costo directo y margen de contribución por SKU |
| **Diseño de información** | Carrusel ejecutivo de seis imágenes para LinkedIn |

Python aparece únicamente como recurso para generar el dataset sintético; **el análisis fue realizado con SQL y Excel**.

---

## Estructura del repositorio

```text
Sienna/
├── Data Set/
│   ├── sienna_ventas_pos.csv
│   └── sienna_catalogo_costos.csv
├── Modulos/
│   ├── Analisis_Siennaa.xlsx
│   ├── Modulo 2/
│   │   ├── comparacion_compra.csv
│   │   ├── productos_juntos_top5.csv
│   │   └── tickets_solos.csv
│   ├── Modulo 3/
│   │   ├── productos_tipo_pedido.csv
│   │   └── tickets_promedio.csv
│   ├── Modulo 4/
│   │   └── pareto_sku.csv
│   └── Modulo 6/LinkedIn/
│       ├── 01_resumen_ejecutivo.png
│       ├── 02_evolucion_comercial.png
│       ├── 03_patron_demanda.png
│       ├── 04_concentracion_sku.png
│       ├── 05_rentabilidad_menu.png
│       ├── 06_operacion_decisiones.png
│       └── texto_linkedin.md
├── Recursos/
│   ├── generar_sienna.py
│   └── sienna_diccionario.md
└── README.md
```

---

## Metodología y flujo de trabajo

El proyecto separa datos, análisis y comunicación:

**Datos POS + catálogo de costos  →  SQL / DuckDB  →  Excel  →  Validación  →  Storytelling ejecutivo**

1. **Comprensión y validación.** Revisión de granularidad, tipos, nulos, llaves y reconciliación de totales.
2. **Diagnóstico comercial.** Ingreso, tickets únicos, ticket promedio, unidades, evolución mensual y horas pico.
3. **Comportamiento de compra.** Productos comprados juntos, tickets individuales, métodos de pago y tipo de orden.
4. **Análisis de producto.** Ranking por SKU, porcentaje del ingreso y curva acumulada de Pareto.
5. **Rentabilidad.** Cruce con costos, margen de contribución y matriz de ingeniería de menú.
6. **Operación.** Distribución temporal, carga por cajero y composición de pagos y órdenes.
7. **Comunicación.** Síntesis de las métricas en seis visualizaciones con una narrativa lineal.

---

## Análisis realizado

| Bloque | Técnica | Qué resuelve |
|---|---|---|
| Diagnóstico del negocio | Agregaciones y tablas dinámicas | Escala, tendencia, ticket promedio y horas pico |
| Canasta de compra | Autojoin por ticket y conteos | Productos que aparecen juntos y tickets individuales |
| Segmentación | Agrupación categórica | Diferencias por pago y tipo de orden |
| Pareto de SKU | Ventanas y porcentaje acumulado | Concentración del ingreso dentro del menú |
| Rentabilidad | Join POS–costos | Margen unitario y margen total por SKU |
| Ingeniería de menú | Popularidad × margen unitario | Stars, Plow Horses, Puzzles y Dogs |
| Operación | Tickets únicos por día, hora y cajero | Distribución de la carga observada |
| Storytelling | KPIs, línea, barras, heatmap y scatter | Lectura ejecutiva para una audiencia no técnica |

**Definiciones principales:**

- **Ticket:** `COUNT(DISTINCT id_ticket)`; una fila no equivale a un ticket.
- **SKU:** combinación de `producto + tamano`.
- **Ticket promedio:** ingreso total dividido entre tickets únicos.
- **Margen de contribución:** ingreso menos costo directo; no representa utilidad neta.
- **Carga por cajero:** tickets únicos por día activo; no equivale a productividad por hora porque no existen horas trabajadas.

---

## Hallazgos clave

### Escala del negocio

- **Ingreso total:** ₡228.240.000.
- **Tickets únicos:** 48.384.
- **Ticket promedio:** ₡4.717,26.
- **Unidades vendidas:** 106.223.
- **Margen de contribución:** ₡150.601.028, equivalente a **65,98%** del ingreso.

### Crecimiento

- Entre enero y mayo, el ingreso de **2026 creció 25,8%** frente al mismo periodo de 2025.
- Los tickets crecieron **25,2%**, mientras el ticket promedio aumentó solo **0,5%**.
- El crecimiento observado proviene principalmente de **mayor volumen**, no de un aumento importante del gasto por ticket.

### Demanda temporal

- **Viernes, sábado y domingo** concentran 48,4% del ingreso.
- La franja de **08:00 a 10:00** representa 31,9% de los tickets.
- La hora con mayor volumen es **09:00–09:59**, con 5.590 tickets.
- El sábado es el día con mayor intensidad operativa; con 18 meses se habla de patrones observados, no de estacionalidad estructural.

### Menú y concentración

- Se necesitan **36 de 62 SKU** para alcanzar 80% del ingreso acumulado.
- Esos 36 SKU representan **58,1% del catálogo**: Sienna no sigue un Pareto 80/20 clásico.
- El SKU líder por ingreso es **Bolsa de Café 1 kg**, con ₡14.112.000 y 6,18% del ingreso.
- El SKU líder por unidades es **Cortado**, con 3.754 unidades.

### Rentabilidad

- **Café Caliente** combina escala y rentabilidad: 28,06% del ingreso y 74,76% de margen.
- **Retail** aporta 11,38% del ingreso, pero registra el menor margen: 42,08%.
- La diferencia entre liderazgo por ingreso, unidades y margen demuestra por qué vender más no siempre significa aportar más rentabilidad.

### Operación y comportamiento

- **Tarjeta** representa 42,23% del ingreso; efectivo 33,09% y SINPE Móvil 24,68%.
- Las órdenes **para llevar** concentran 57,28% del ingreso.
- La carga por cajero está equilibrada: la diferencia entre el mayor y menor volumen de tickets es aproximadamente 4,65%.

### Recomendación

> Proteger capacidad e inventario durante viernes–domingo y la franja de 08:00–10:00; revisar precio y costo de Retail, cuyo margen está 23,9 puntos porcentuales por debajo del total; y evitar atribuir diferencias de desempeño a los cajeros sin información de horas trabajadas.

---

## Visualizaciones

Las seis imágenes forman una narrativa continua: panorama general, evolución, demanda, productos, rentabilidad y operación.

<p align="center">
  <img src="Modulos/Modulo%206/LinkedIn/01_resumen_ejecutivo.png" alt="Resumen ejecutivo de Sienna" width="48%">
  <img src="Modulos/Modulo%206/LinkedIn/02_evolucion_comercial.png" alt="Evolución comercial de Sienna" width="48%">
</p>

<p align="center">
  <img src="Modulos/Modulo%206/LinkedIn/03_patron_demanda.png" alt="Patrón de demanda de Sienna" width="48%">
  <img src="Modulos/Modulo%206/LinkedIn/04_concentracion_sku.png" alt="Concentración de ingresos por SKU" width="48%">
</p>

<p align="center">
  <img src="Modulos/Modulo%206/LinkedIn/05_rentabilidad_menu.png" alt="Rentabilidad e ingeniería de menú" width="48%">
  <img src="Modulos/Modulo%206/LinkedIn/06_operacion_decisiones.png" alt="Operación y recomendaciones de Sienna" width="48%">
</p>

---

## Cómo reproducir

1. **Clonar el repositorio** y entrar en su carpeta.
2. **Abrir DuckDB** desde Terminal:

```bash
duckdb
```

3. **Crear vistas sobre los CSV**, sin cargar una base de datos:

```sql
CREATE VIEW ventas AS
SELECT *
FROM read_csv_auto('Data Set/sienna_ventas_pos.csv');

CREATE VIEW costos AS
SELECT *
FROM read_csv_auto('Data Set/sienna_catalogo_costos.csv');
```

4. **Validar los principales totales:**

```sql
SELECT
    COUNT(*) AS lineas,
    COUNT(DISTINCT id_ticket) AS tickets,
    SUM(cantidad) AS unidades,
    SUM(subtotal) AS ingreso
FROM ventas;
```

Resultado esperado: 90.756 líneas, 48.384 tickets, 106.223 unidades y ₡228.240.000 de ingreso.

5. Abrir `Modulos/Analisis_Siennaa.xlsx` para revisar las tablas dinámicas y análisis en Excel.
6. Consultar `Modulos/Modulo 4/pareto_sku.csv` para el ranking y porcentaje acumulado por SKU.
7. Revisar el entregable visual en `Modulos/Modulo 6/LinkedIn/`.

---

## Habilidades demostradas

- SQL analítico con **DuckDB**, CTE, joins, agregaciones y funciones de ventana.
- Modelado de métricas con la granularidad correcta: líneas, tickets, productos y SKU.
- Excel analítico: tablas dinámicas, porcentajes acumulados y gráficos combinados.
- Análisis de Pareto e **ingeniería de menú**.
- Cruce de ventas y costos para calcular **margen de contribución**.
- Validación de calidad: cobertura de joins, consistencia de precios y reconciliación de totales.
- Diseño de KPIs y selección de gráficos según la pregunta de negocio.
- Comunicación ejecutiva y **data storytelling** orientado a decisiones.

---

## Autor

**Ale (Daniel Raudes)**, Analista de Datos Junior (Costa Rica).  
GitHub: [@ADRaudes](https://github.com/ADRaudes)

---

## Licencia

Distribuido bajo licencia **MIT**. Ver el archivo [`LICENSE`](LICENSE).
