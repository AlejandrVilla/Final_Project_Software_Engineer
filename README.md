# Practica 9: Estilos de programación

## Things
Constraints:
- The larger problem is decomposed into 'things' that make sense for the problem domain
- Each 'thing' is a capsule of data that exposes procedures to the rest of the world
- Data is never accessed directly, only through these procedures
- Capsules can reappropriate procedures defined in other capsules

La declaracion de la clase evento que se usará como una entidad en la lógica del dominio
```
class Evento:
    def __init__(evento, detalles_, link_, id_, nombre_, fecha_, hora_inicio_, hora_fin_):
        evento.detalles = detalles_
        evento.link = link_
        evento.id = id_
        evento.nombre = nombre_
        evento.fecha = fecha_
        evento.hora_inicio = hora_inicio_
        evento.hora_fin = hora_fin_
    
    def getDetalles(evento):
        return evento.detalles
    def getLink(evento):
        return evento.link
    def getId(evento):
        return evento.id
    def getNombre(evento):
        return evento.nombre
    def getFecha(evento):
        return evento.fecha
    def getHoraInicio(evento):
        return evento.hora_inicio
    def getHoraFin(evento):
        return evento.hora_fin

    def setDetalles(evento, detalles_):
        evento.detalles = detalles_
    def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_
    def getId(evento, id_):
        evento.id = id_
    def getNombre(evento, nombre_):
        evento.nombre = nombre_
    def getFecha(evento, fecha_):
        evento.fecha = fecha_
    def getHoraInicio(evento, hora_inicio_):
        evento.hora_inicio = hora_inicio_
    def getHoraFin(evento, hora_fin_):
        evento.hora_fin = hora_fin_

```

## Declared intentions
Constraints:
- Existence of a run-time typechecker
- Procedures and functions declare what types of arguments they expect
- If callers send arguments of types that are't expected, the procedures/functions are not executed

Cuando un nuevo link se va añadir a la entidad evento, esta debe contener la "www" dentro de la cadena, sinó esta no sería válida
```
def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
```

## Cook book
Constraints:
- Larger problem decomposed in procedural abstractions
- Larger problem solved as a sequence of commands, each corresponding to a procedure

Users es una variable global que se usa dentro de varias funciones 
```
users = []

list_log = modelLogin.get_all_usuario()
list_user = modelUser.get_all_usuarios()

n = 1
for x, y in zip(list_log,list_user):
    users.append(User(
        id=n, contrasenia=x.get('contrasenia'),corre=x.get('correo'),
        nombre=x.get('nombre'), apellido=x.get('apellido'),
        nombres=y.get('nombres'), apellidos=y.get('apellidos'),
        correo=y.get('correo'), lista=y.get('listaEventos'),))
    n += 1


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

```

# Práctica 10: Codificación legible

## Comenting and documentation
Comenta la logica necesaria mas no cada acción realizada dentro de cada función
```
    def createUsuario(self, id, contrasenia):   #crear usuario a traves de json    
        params = {
            'id' : id,
            'contrasenia' : contrasenia
        }  
        query = """insert into login(id, contrasenia) 
            values (%(id)s, %(contrasenia)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': id, 'contrasenia': contrasenia}
        return data

    def deleteUsuario(self, id):    #borra usuario de la base de datos  
        params = {'id' : id}      
        query = """delete from login where id = %(id)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
```
## Avoid obvius comemnts
Se podría comentar que hace cada función, pero esto resultaría en redundancias innecesarias
```
    def getLink(evento):
        return evento.link
    def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_

    def getId(evento):
        return evento.id
    def getId(evento, id_):
        evento.id = id_
```

## Code grouping
Cada grupo de funciones set y get estan separadas 
```
# modulo evento
class Evento:
    def __init__(evento, detalles_, link_, 
                id_, nombre_, fecha_, 
                hora_inicio_, hora_fin_):
        evento.detalles = detalles_
        evento.link = link_
        evento.id = id_
        evento.nombre = nombre_
        evento.fecha = fecha_
        evento.hora_inicio = hora_inicio_
        evento.hora_fin = hora_fin_
    
    def getDetalles(evento):
        return evento.detalles
    def setDetalles(evento, detalles_):
        evento.detalles = detalles_

    def getLink(evento):
        return evento.link
    def setLink(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_

    def getId(evento):
        return evento.id
    def getId(evento, id_):
        evento.id = id_

    def getNombre(evento):
        return evento.nombre
    def getNombre(evento, nombre_):
        evento.nombre = nombre_

    def getFecha(evento):
        return evento.fecha
    def getFecha(evento, fecha_):
        evento.fecha = fecha_

    def getHoraInicio(evento):
        return evento.hora_inicio
    def getHoraInicio(evento, hora_inicio_):
        evento.hora_inicio = hora_inicio_

    def getHoraFin(evento):
        return evento.hora_fin
    def getHoraFin(evento, hora_fin_):
        evento.hora_fin = hora_fin_

```
## Consistent naming scheme
Para cada función se utiliza mayúsculas a partir de la segunda palabra, además por cada parámetro que pide la función se usa un sub-guión al final (menos evento que es el identificador de la clase)
```
    def getFecha(evento):
        return evento.fecha
    def getFecha(evento, fecha_):
        evento.fecha = fecha_
```
## Capitalize SQL special words
Se usa mayúsculas en las palabras reservadas al hacer uso de sentencias SQL, con la finalidad de mejorar el entendimiento del código
```
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
```
