from database.db import get_connection #Conexion 
from .entities.Account import Account #Clase del modelado


class AccountModel():
    
    #Para llamar el metodo sin necesidad de instanciar la clase
    @classmethod
    def get_accounts(self):
        '''
    Obtiene las cuentas almacenadas en la base de datos
    Args:
        None
    Returns:
        array: regresa todas las cuentas obtenidas por la consulta
        objecto: regresa un objeto de exception
    '''
        try:
            connection = get_connection()
            accounts=[] # Lista de cuentas bancarias 
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM bank_accounts ORDER BY full_name ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    account = Account(row[0], row[1], row[2], row[3],row[4],row[5])
                    accounts.append(account.to_JSON())#Anexar
            
            connection.close()
            
            return accounts
                
            
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo get por id
    #Para llamar el metodo sin necesidad de instanciar la clase
    @classmethod
    def get_account(self,id):
        '''
    Obtiene una cuenta obtenida de las cuentas de banco
    Args:
        id(string): El identificador de las cuentas de usuario, es decir el numero de cuenta
    Returns:
        objeto: regresa un objeto json que representa una cuenta
        objeto: regresa un objeto de exception
    '''
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM bank_accounts WHERE account_number=%s",(id,))
                row = cursor.fetchone()
                
                account=None
                if row != None:
                    account = Account(row[0], row[1], row[2], row[3],row[4],row[5])
                    account = account.to_JSON()
            
            connection.close()
            
            return account                
            
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo post (create)
    @classmethod
    def add_account(self,account):
        '''
    Crea una nueva cuenta de usuario
    Args:
        objeto: un objeto que representa una cuenta de banco
    Returns:
        objeto: regresa las filas afectadas por la consulta
        objecto: regresa un objeto de exception
    '''
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO bank_accounts(id,full_name,birthdate,account_number,user_password,user_cash) 
                                    VALUES (%s, %s, %s, %s, %s, %s)""", (account.id, account.full_name, account.birthdate, account.account_number,account.user_password,account.user_cash))
                #Verificar cuantas filas han sido insertadas
                affected_rows=cursor.rowcount
                connection.commit()                
            
            connection.close()            
            return affected_rows                
            
        except Exception as ex:
            raise Exception(ex)
        
    #Metodo patch (update)
    @classmethod
    def update_account(self,account):
     '''
    Actualiza el nombre de usuario de una cuenta de banco
    Args:
        objeto: un objeto que representa una cuenta de banco
    Returns:
        objeto: regresa las filas afectadas por la consulta
        objecto: regresa un objeto de exception
    '''
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE bank_accounts SET full_name = %s 
                                    WHERE (account_number = %s)""", (account.full_name,account.account_number))
                #Verificar cuantas filas han sido insertadas
                affected_rows=cursor.rowcount
                connection.commit()                
            
            connection.close()            
            return affected_rows                
            
        except Exception as ex:
            raise Exception(ex)
        
    #Metodo DELETE (DELETE ROW)
    @classmethod
    def delete_account(self,account):
      '''
    Elimina una cuenta de usuario
    Args:
        objeto: un objeto que representa una cuenta de banco
    Returns:
        objeto: regresa las filas afectadas por la consulta
        objecto: regresa un objeto de exception
    '''
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM bank_accounts  
                                    WHERE account_number = '{0}'""".format(account.account_number))
                #Verificar cuantas filas han sido insertadas
                affected_rows=cursor.rowcount
                connection.commit()                
            
            connection.close()            
            return affected_rows                
            
        except Exception as ex:
            raise Exception(ex)