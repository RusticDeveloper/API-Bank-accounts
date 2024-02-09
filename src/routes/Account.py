from flask import Blueprint, jsonify, request
import uuid

import bcrypt


#Entities
from models.entities.Account import Account

#Models
from models.AccountModel import AccountModel



main = Blueprint('account_blueprint',__name__)

@main.route('/')
def get_accounts():
    try:
        accounts = AccountModel.get_accounts()
        return jsonify(accounts)
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
#Para get con id
@main.route('/<id>')
def gat_account(id):
    try:
        account = AccountModel.get_account(id)
        if account != None:
            return jsonify(account)
        else:
            return jsonify({}),404
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
    
#Metodo post
@main.route('/add', methods= ['POST'])
def add_account():
    try:
        full_name= request.json['fullname']
        birthdate= request.json['birthdate']
        user_password= request.json['password']
        #codificar
        user_password=user_password.encode()
        #generar sal
        salt=bcrypt.gensalt()
        #encriptar la contraseña
        secure_password=bcrypt.kdf(user_password,salt,15,100)
        # secure_password=bcrypt.hashpw(user_password,salt)
        
        print("hashed password: ",secure_password)
        print("longitude of password: ",len(secure_password))
        
        user_cash= request.json['cash']
        account_number=request.json['account']
        id= uuid.uuid4()
        #print(id)
        account = Account(str(id),full_name, birthdate,account_number,secure_password,user_cash)
        
        affected_rows = AccountModel.add_account(account)
        
        if affected_rows == 1:
            return jsonify(account.id)  
        else:
            return jsonify({'message':"Error on insert"}),500  
        
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
    
# edit method
@main.route('/edit', methods= ['PATCH'])
def edit_account():
    try:
        #print(request.json)
        full_name= request.json['fullname']
        account_number= request.json['account']
        
        account = Account('',full_name,'',account_number,'','')
        
        affected_rows = AccountModel.update_account(account)
        
        if affected_rows == 1:
            return jsonify('Cuenta actualizada, nombre cambiado a: ', full_name)  
        else:
            return jsonify({'message':"Error on insert"}),500  
        
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
    
    
# DELETE method
@main.route('/delete', methods= ['DELETE'])
def delete_account():
        try:
            
            account_number= request.json['account']
            
            account = Account('','','',account_number,'','')
            
            affected_rows = AccountModel.delete_account(account)
            
            if affected_rows == 1:
                return jsonify('Cuenta eliminada, ten un bonito dia')  
            else:
                return jsonify({'message':"El numero de cuenta ingresado no existe"}),500  
            
        except Exception as ex: 
            return jsonify({'message':str(ex)}),500

