# 📊 Proyecto de Ingesta de Datos - Panadería

Proyecto de **pipeline de ingesta y carga** de datos que extrae información de productos desde un archivo CSV, la almacena en la zona *raw* y la carga en una base de datos **Oracle**.

---

## ✨ Objetivo del Proyecto

Automatizar el proceso de ingesta de datos de productos de una panadería, aplicando buenas prácticas de **Data Engineering**:
- Extracción de fuente original
- Almacenamiento en zona *raw*
- Carga (Load) hacia base de datos relacional Oracle

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **oracledb** (conexión a Oracle)
- **shutil** y **os** (manejo de archivos)
- **logging** (trazabilidad)
- **CSV** (formato de origen)

---

## 📁 Estructura del Proyecto

```bash
proyecto_ingesta/
├── origen/
│   └── productos.csv          # Fuente original de datos
├── data/
│   └── raw/
│       └── productos.csv      # Zona raw (copia)
├── ingesta-main/
│   └── ingesta.py             # Script principal del pipeline
├── .vscode/                   # Configuración de VS Code
└── README.md
