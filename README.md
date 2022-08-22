# Practica 9: Estilos de programación

## Things
Constraints:
- The larger problem is decomposed into 'things' that make sense for the problem domain.
- Each 'thing' is a capsule of data that exposes procedures to the rest of the world.
- Data is never accessed directly, only through these procedures.
- Capsules can reappropriate procedures defined in other capsules.

La declaracion de la clase evento que se usará como una entidad en la lógica del dominio.
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
    
    def get_detalles(evento):
        return evento.detalles
    def setDetalles(evento, detalles_):
        evento.detalles = detalles_

    def get_link(evento):
        return evento.link
    def set_link(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_

    def get_id(evento):
        return evento.id
    def get_id(evento, id_):
        evento.id = id_

    def get_nombre(evento):
        return evento.nombre
    def get_nombre(evento, nombre_):
        evento.nombre = nombre_

    def get_fecha(evento):
        return evento.fecha
    def get_fecha(evento, fecha_):
        evento.fecha = fecha_

    def get_hora_inicio(evento):
        return evento.hora_inicio
    def get_hora_inicio(evento, hora_inicio_):
        evento.hora_inicio = hora_inicio_

    def getHora_fin(evento):
        return evento.hora_fin
    def getHora_fin(evento, hora_fin_):
        evento.hora_fin = hora_fin_

```

## Declared intentions
Constraints:
- Existence of a run-time typechecker.
- Procedures and functions declare what types of arguments they expect.
- If callers send arguments of types that are't expected, the procedures/functions are not executed.

Cuando un nuevo link se va añadir a la entidad evento, esta debe contener la "www" dentro de la cadena, sinó esta no sería válida.
```
def set_link(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_
```

## Cook book
Constraints:
- Larger problem decomposed in procedural abstractions.
- Larger problem solved as a sequence of commands, each corresponding to a procedure.

Users es una variable global que se usa dentro de varias funciones .
```
users = []

# extrae datos usuario
list_log = modelLogin.get_all_usuario()
# extrae todos los usuarios
list_user = modelUser.get_all_usuarios()


id_usuario = 1
# guarda usuarios
for x, y in zip(list_log,list_user):
    users.append(User(
        id=id_usuario, contrasenia=x.get('contrasenia'),corre=x.get('correo'),
        nombre=x.get('nombre'), apellido=x.get('apellido'),
        nombres=y.get('nombres'), apellidos=y.get('apellidos'),
        correo=y.get('correo'), lista=y.get('listaEventos'),))
    id_usuario += 1


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

```

# Práctica 10: Codificación legible

## Limit line length
Largas líneas de código pueden resultar tediosas de leer, mejor es acomodarlas en columnas.
```
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
```
## Avoid obvius comemnts
Se podría comentar que hace cada función, pero esto resultaría en redundancias innecesarias.
```
    def get_link(evento):
        return evento.link
    def set_link(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_

    def get_id(evento):
        return evento.id
    def get_id(evento, id_):
        evento.id = id_
```

## Code grouping
Cada grupo de funciones set y get estan separadas.
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
    
    def get_detalles(evento):
        return evento.detalles
    def setDetalles(evento, detalles_):
        evento.detalles = detalles_

    def get_link(evento):
        return evento.link
    def set_link(evento, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento.link = link_

    def get_id(evento):
        return evento.id
    def get_id(evento, id_):
        evento.id = id_

    def get_nombre(evento):
        return evento.nombre
    def get_nombre(evento, nombre_):
        evento.nombre = nombre_

    def get_fecha(evento):
        return evento.fecha
    def get_fecha(evento, fecha_):
        evento.fecha = fecha_

    def get_hora_inicio(evento):
        return evento.hora_inicio
    def get_hora_inicio(evento, hora_inicio_):
        evento.hora_inicio = hora_inicio_

    def getHora_fin(evento):
        return evento.hora_fin
    def getHora_fin(evento, hora_fin_):
        evento.hora_fin = hora_fin_


```
## Consistent naming scheme
Para cada función se utiliza sub-guión para separar palabras, además por cada parámetro que pide la función se usa un sub-guión al final (menos evento que es el identificador de la clase).
```
    def get_fecha(evento):
        return evento.fecha
    def get_fecha(evento, fecha_):
        evento.fecha = fecha_
```
## Capitalize SQL special words
Se usa mayúsculas en las palabras reservadas al hacer uso de sentencias SQL, con la finalidad de mejorar el entendimiento del código.
```
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
```

# Práctica 11: princios SOLID

## Single Responsability
A class should have a single responsibility
[Diagrama de casos de uso](./evidencias/S_SOLID.png)

## Open Closed
Classes should be open for extension, but closed for modification
```
```
## Interface segregation
Clients should not be forced to depend on methods that they do not use.



