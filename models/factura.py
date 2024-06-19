class Factura:
    def __init__(self):
        self._id = ''
        self._usuario = ''
        self._ruc = ''
        self._monto = 0.0
        self._tiporuc = 0.0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def ruc(self):
        return self._ruc

    @ruc.setter
    def ruc(self, value):
        self._ruc = value

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, value):
        self._monto = value

    @property
    def tiporuc(self):
        return self._tiporuc

    @tiporuc.setter
    def tiporuc(self, value):
        self._tiporuc = value
    
    @property
    def serialize(self):
        return {
            'id': self._id,
            'usuario': self._usuario,
            'ruc': self._ruc,
            'monto': self._monto,
            'tiporuc': self._tiporuc
        }

    def deserializar(self, data):
        factura = Factura()
        factura.id = data['id']
        factura.usuario = data['usuario']
        factura.ruc = data['ruc']
        factura.monto = data['monto']
        factura.tiporuc = data['tiporuc']
        return factura

