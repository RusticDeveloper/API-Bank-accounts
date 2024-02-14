import psycopg2 #Conexion a la base de datos
from psycopg2 import DatabaseError #Manejo de errores
from decouple import config # obtener las variables de entorno

def get_connection ():
    '''
    Se conecta con la base de datos usando la libreria psycopg2
    Args:
        None
    Returns:
        page: regresa un objeto de coneccion con la bse de datos.
    '''
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex

