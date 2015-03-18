#!/usr/bin/env python2

import json
import uuid
import random
import NodoAeropuerto
import NodoUsuario
import NodoVuelo
import ListaAeropuerto
import ListaUsuario
import ArbolAvlVuelos
import ArbolAvlUsuario

from flask import Flask, session, request, render_template, jsonify, Response

app = Flask("pruebas")


miArbolUsuario = ArbolAvlUsuario.ArbolAvlUsuario()
miListaAeropuerto = ListaAeropuerto.ListaAeropuerto()
miListaUsuario = ListaUsuario.ListaUsuario()
miArbolVuelos = ArbolAvlVuelos.ArbolAvlVuelos()

@app.route('/bienvenido')
def saludarme():
  return "Hola mundo!"

@app.route('/aeropuerto/insertar', methods=['POST'])
def crearAeropuerto():
    nombre_aeropuerto_sent = request.form['NombreAeropuerto']
    pais_sent = request.form['Pais']
    contra_sent = request.form['Contrasenia']
    aeroppuertoo = NodoAeropuerto.NodoAeropuerto(nombre_aeropuerto_sent, pais_sent,contra_sent)
    app.logger.debug(unicode(aeroppuertoo.verNodoAeropuerto()))
    miListaAeropuerto.insertarFinal(aeroppuertoo)
    return jsonify(aeroppuertoo.verNodoAeropuerto())


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
