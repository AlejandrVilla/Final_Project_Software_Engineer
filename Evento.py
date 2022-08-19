#!/usr/bin/python
#-*- coding: utf-8 -*-

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
