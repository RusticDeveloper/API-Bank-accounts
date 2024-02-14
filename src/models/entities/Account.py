from utils.DateFormat import DateFormat

class Account():
    
    def __init__(self, id, full_name=None, birthdate=None,account_number=None,user_password=None,user_cash=None) -> None:
        '''
    Constructor de la clase Account
    Args:
        id(string): identificador de la clase
        fullname(string): nombre del usuario de la cuenta bancaria
        birthdate(date): fecha de nacimiento del usuario
        account_number(string): numero de cuenta del usuario
        user_password(char): contraseña del usuario
        user_cash(float): dinero en la cuenta de un usurio
    Returns:
        None
    '''
        #Estructura de la tabla
        self.id=id
        self.full_name = full_name
        self.birthdate = birthdate
        self.account_number = account_number  
        self.user_password = user_password  
        self.user_cash = user_cash  
    
    #Definir una clase para el retorno de un JSON
    def to_JSON(self):
        '''
    Transforma los campos del constructo en formato JSON
    Args:
        self: obtiene el constructor de la  clase
    Returns:
        json: retorna un objeto json con los campos de la clase
    '''
        return {
            'id': self.id,
            'full name': self.full_name,
            'birthdate': DateFormat.convert_date(self.birthdate),
            'user cash': self.user_cash,
            'account number': self.account_number
        }
        
        