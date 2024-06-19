from controls.tda.linked.linkedList import Linked_List
from models.factura import Factura
import json, os

class FacturaControl:
    def __init__(self):
        self.__factura = None
        self.__lista = Linked_List()

    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
        return self.__factura
    
    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    @property
    def _lista(self):
        return self.__lista
    
    @_lista.setter
    def _lista(self, value):
        self.__lista = value
    
    @property
    def save(self):
        self.__factura._id = self.__lista._length + 1
        print('Factura Control:')
        print(self.__factura.serialize)
        self.__lista.add(self.__factura, self.__lista._length)