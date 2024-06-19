from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.retencion import Retencion
from models.factura import Factura

class RetencionController(DaoAdapter):
    def __init__(self):
        super().__init__(Retencion)
        self.__retencion = None

    @property
    def _retencion(self):
        if self.__retencion is None:
            factura = Factura()
            self.__retencion = Retencion(factura)
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        # Asegurar que la factura esté correctamente inicializada
        if self.__retencion.factura is None:
            raise ValueError("La factura no está correctamente inicializada en la retención.")
        
        # Asignar el ID basado en la longitud de la lista
        self.__retencion.factura._id = self._lista._length + 1
        print('Retencion Dao Control:')
        print(self.__retencion.serialize())
        
        # Guardar la retención en el adaptador DAO
        self._save(self.__retencion)

    def merge(self, pos):
        self._merge(self.__retencion, pos)
