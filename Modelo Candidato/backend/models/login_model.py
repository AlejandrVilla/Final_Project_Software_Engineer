from flask.templating import render_template
from backend.models.connection_pool import MySQLPool

class LoginModel:
    def __init__(self): 
        self.mysql_pool = MySQLPool()

    def get_usuario(self, id_): #retorna el usuario dependiendo del ID que se pasa a traves de json    
        params = {'id' : id_}      
        rv = self.mysql_pool.execute("SELECT * FROM login WHERE id=%(id_)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'contrasenia': result[1]
                }
            data.append(content)
            content = {}
        return data

    def get_all_usuario(self): #retorna todos los usuarios que existen en la tabla "login"
        rv = self.mysql_pool.execute("SELECT * FROM login ORDER BY id")  
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0], 
                'contrasenia': result[1]
                }
            data.append(content)
            content = {}
        return data

    def create_usuario(self, id_, contrasenia_):       
        params = {
            'id' : id_,
            'contrasenia' : contrasenia_
            }  
        query = """INSERT INTO login(id, contrasenia) 
                    VALUES (%(id_)s, %(contrasenia_)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {
            'id': id_, 
            'contrasenia': contrasenia_
            }
        return data

    def delete_usuario(self, id_):     
        params = {'id' : id_}      
        query = """DELETE FROM login WHERE id = %(id_)s"""    
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