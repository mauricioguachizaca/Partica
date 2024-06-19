from models.factura import Factura
class Retencion:
    def __init__(self, factura: Factura):
        self.factura = factura
        self.retencion = self.calcular_retencion()

    def calcular_retencion(self):
        if self.factura.tiporuc == 'educativo':
            return self.factura.monto * 0.08
        elif self.factura.tiporuc == 'profesional':
            return self.factura.monto * 0.10
        else:
            return 0

    def serialize(self):
        return {
            'factura': self.factura.serialize,
            'retencion': self.retencion
        }

    @staticmethod
    def deserializar(data):
        factura = Factura.deserializar(data['factura'])
        return Retencion(factura)

    def __repr__(self):
        return f"Factura ID: {self.factura.id}, RUC: {self.factura.ruc}, Monto: {self.factura.monto}, Retención: {self.retencion}"
