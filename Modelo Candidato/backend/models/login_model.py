from flask.templating import render_template
from backend.models.connection_pool import MySQLPool

class LoginModel:
    def __init__(self): 
        self.mysql_pool = MySQLPool()

    def getUsuario(self, id): #retorna el usuario dependiendo del ID que se pasa a traves de json    
        params = {'id' : id}      
        rv = self.mysql_pool.execute("SELECT * FROM login WHERE id=%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'contrasenia': result[1]}
            data.append(content)
            content = {}
        return data

    def getAllUsuario(self): #retorna todos los usuarios que existen en la tabla "login"
        rv = self.mysql_pool.execute("SELECT * FROM login ORDER BY cui")  
        data = []
        content = {}
        for result in rv:
            content = {'cui': result[0], 'contrasenia': result[1]}
            data.append(content)
            content = {}
        return data

    def createUsuario(self, cui, contrasenia): #crear usuario a traves de json    
        params = {
            'cui' : cui,
            'contrasenia' : contrasenia
        }  
        query = """insert into login(cui, contrasenia) 
            values (%(cui)s, %(contrasenia)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'cui': cui, 'contrasenia': contrasenia}
        return data

    def deleteUsuario(self, cui):#borra usuario de la base de datos  
        params = {'cui' : cui}      
        query = """delete from login where cui = %(cui)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    um = LoginModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(um.delete_usuario(67))
    #print(um.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))