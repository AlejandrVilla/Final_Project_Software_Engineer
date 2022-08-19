#!/usr/bin/python
#-*- coding: utf-8 -*-

# modulo evento_
class Evento_:
    def __init__(evento_, detalles_, link_, 
                id_, nombre_, fecha_, 
                hora_inicio_, hora_fin_):
        evento_.detalles = detalles_
        evento_.link = link_
        evento_.id = id_
        evento_.nombre = nombre_
        evento_.fecha = fecha_
        evento_.hora_inicio = hora_inicio_
        evento_.hora_fin = hora_fin_
    
    def get_detalles(evento_):
        return evento_.detalles
    def setDetalles(evento_, detalles_):
        evento_.detalles = detalles_

    def get_link(evento_):
        return evento_.link
    def set_link(evento_, link_):
        if not "www" in link_:
            raise("Expected a www in ", link_)
        evento_.link = link_

    def get_id(evento_):
        return evento_.id
    def get_id(evento_, id_):
        evento_.id = id_

    def get_nombre(evento_):
        return evento_.nombre
    def get_nombre(evento_, nombre_):
        evento_.nombre = nombre_

    def get_fecha(evento_):
        return evento_.fecha
    def get_fecha(evento_, fecha_):
        evento_.fecha = fecha_

    def get_hora_inicio(evento_):
        return evento_.hora_inicio
    def get_hora_inicio(evento_, hora_inicio_):
        evento_.hora_inicio = hora_inicio_

    def getHora_fin(evento_):
        return evento_.hora_fin
    def getHora_fin(evento_, hora_fin_):
        evento_.hora_fin = hora_fin_
