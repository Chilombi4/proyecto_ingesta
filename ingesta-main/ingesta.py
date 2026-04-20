import shutil
import logging
import os
import csv
import oracledb 

# Paso 4: Configuración de trazabilidad [cite: 73, 74]
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Definición de rutas del proyecto [cite: 69, 76]
origen = "../origen/productos.csv"
destino_raw = "../data/raw/productos.csv"

# Configuración de tu base de datos Oracle
db_config = {
    "user": "santiago",
    "password": "Pax.,ytrG231", # Reemplaza con tu clave real de SQL Developer
    "dsn": "localhost:1521/xe" 
}

def ejecutar_pipeline():
    logging.info("Iniciando pipeline: Ingesta -> Carga Oracle")
    
    try:
        # 1. Ingesta: Asegurar carpeta y mover archivo (Automatización) [cite: 65, 72]
        if not os.path.exists("../data/raw"):
            os.makedirs("../data/raw")
        
        shutil.copy(origen, destino_raw)
        logging.info("Archivo copiado a data/raw correctamente")

        # 2. Carga: Conexión a Oracle (Nivel Avanzado) [cite: 84]
        connection = oracledb.connect(
            user=db_config["user"], 
            password=db_config["password"], 
            dsn=db_config["dsn"]
        )
        cursor = connection.cursor()

        # 3. Lectura e Inserción de datos [cite: 88, 96]
        with open(destino_raw, mode='r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                cursor.execute(
                    "INSERT INTO productos (id_producto, nombre, precio) VALUES (:1, :2, :3)",
                    (fila['id_producto'], fila['nombre'], fila['precio'])
                )
        
        connection.commit()
        logging.info("Exito: Datos de la panaderia cargados en Oracle")

    except Exception as e:
        logging.error(f"Error en el pipeline: {e}")
    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    ejecutar_pipeline()