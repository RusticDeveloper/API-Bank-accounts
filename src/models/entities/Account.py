from utils.DateFormat import DateFormat

class Account():
    
    def __init__(self, id, full_name=None, birthdate=None,account_number=None,user_password=None,user_cash=None) -> None:
        #Estructura de la tabla
        self.id=id
        self.full_name = full_name
        self.birthdate = birthdate
        self.account_number = account_number  
        self.user_password = user_password  
        self.user_cash = user_cash  
    
    #Definir una clase para el retorno de un JSON
    def to_JSON(self):
        return {
            'id': self.id,
            'full name': self.full_name,
            'birthdate': DateFormat.convert_date(self.birthdate),
            'user cash': self.user_cash,
            'account number': self.account_number
        }
        
        