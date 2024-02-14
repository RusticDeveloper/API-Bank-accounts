from flask import Flask
from config import config #importar 

#Importar rutas, ojo hay que agregar el archico __init.py__
from routes import Account

app = Flask(__name__)


#para las paginas no encontradas
def page_not_found():
    '''
    Muestra la pagina "no encontrado", si no existe la url dentro del api
    Args:
        None
    Returns:
        page: regresa una pagina html con el codigo 404     
    '''
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    help(page_not_found)
    #Blueprints, para asignar mis rutas
    app.register_blueprint(Account.main, url_prefix='/api/accounts')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
