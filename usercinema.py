import mysql.connector
from argon2 import PasswordHasher
import secrets

# Función para agregar un usuario a la base de datos
def agregar_usuario(username, password):
    # Configuración de la conexión a la base de datos
    config = {
        'user': 'root',
        'password': '123456789',
        'host': 'localhost',
        'database': 'pos_cinema',
    }

    # Crear la conexión
    conn = mysql.connector.connect(**config)

    # Instanciar el hasher Argon2
    hasher = PasswordHasher()

    # Generar un salt aleatorio
    salt = secrets.token_hex(15)

    # Combinar la contraseña con el salt y realizar el hash con Argon2
    password_hash = hasher.hash(password + salt)

    # Crear un cursor
    cursor = conn.cursor()

    try:
        # Crear la consulta de inserción para el usuario
        consulta = "INSERT INTO Users (username, password_hash, salt) VALUES (%s, %s, %s)"
        
        # Ejecutar la consulta
        cursor.execute(consulta, (username, password_hash, salt))

        # Confirmar la transacción
        conn.commit()
        print("Usuario agregado exitosamente.")
    except Exception as e:
        print("Error al agregar usuario:", e)
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de usuario
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    # Llamar a la función para agregar usuario
    agregar_usuario(username, password)
