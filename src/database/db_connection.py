import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Tu clave aquí
        database="cerpint_db",
    )

    if conexion.is_connected():
        cursor = conexion.cursor()
        # Le pedimos a Python que nos diga qué tablas hay
        cursor.execute("SHOW TABLES")

        print("--- CONEXIÓN EXITOSA, MANUEL ---")
        print("Las tablas que rescatamos de la base de datos son:")

        for (tabla,) in cursor:
            print(f"--- Tabla encontrada: {tabla}")

        conexion.close()

except Exception as e:
    print(f"Hubo un detalle: {e}")
