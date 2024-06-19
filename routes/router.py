from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.facturaDaoControl import FacturaDaoControl  # Importamos el nuevo controlador
from flask_cors import CORS
from models.factura import Factura
from controls.tda.linked.linkedList import Linked_List


router = Blueprint('router', __name__)
CORS(router)
fc = FacturaDaoControl() 

@router.route('/')
def home():
    return render_template('template.html')

# RENDERS A LOS TEMPLATES
@router.route('/facturas')
def ver_facturas():
    fc = FacturaDaoControl()  # Usamos el nuevo controlador FacturaDaoControl
    return render_template('facturas/lista.html', lista=fc.to_dict())

@router.route('/facturas/formulario')
def ver_guardar():
    return render_template('facturas/guardar.html')

@router.route('/facturas/<metodo>/<criterio>/<ordenar>')
def ver_facturas_ordenar(metodo, criterio, ordenar):
    fc = FacturaDaoControl() 
     # Usamos el nuevo controlador FacturaDaoControl
    fc.sort_models(metodo, criterio, ordenar)
    return render_template('facturas/lista.html', lista=fc.to_dict(fc))

@router.route('/facturas/editar/<pos>')
def ver_editar(pos):
    fc = FacturaDaoControl()  # Usamos el nuevo controlador FacturaDaoControl
    factura = fc._list[int(pos) - 1]
    print(factura)
    return render_template('facturas/editar.html', data=factura)

# LOGICAS
# GUARDAR FACTURA POST
@router.route('/facturas/guardar', methods=['POST'])
def guardar_factura():
    data = request.form

    if 'usuario' not in data or 'ruc' not in data or 'monto' not in data or 'tiporuc' not in data:
        abort(400)

    # Crear instancia de Factura y asignar valores
    factura = Factura()
    factura.usuario = data['usuario']
    factura.ruc = data['ruc']
    factura.monto = float(data['monto'])
    factura.tiporuc = float(data['tiporuc'])

    try:
        # Asignar factura al controlador y guardarla
        fc._factura = factura
        fc.save()
    except Exception as e:
        abort(500, f"Error al guardar la factura: {str(e)}")

    return redirect('/facturas', code=302)

@router.route('/facturas/modificar', methods=['POST'])
def modificar_factura():
    fc = FacturaDaoControl()  # Usamos el nuevo controlador FacturaDaoControl
    data = request.form
    pos = int(data['id']) - 1
    factura = fc._lista[pos]

    if 'usuario' not in data.keys() or 'ruc' not in data.keys() or 'monto' not in data.keys() or 'tiporuc' not in data.keys():
        abort(400)
    
    fc._factura = factura
    fc._factura._usuario = data['usuario']
    fc._factura._ruc = data['ruc']
    fc._factura._monto = float(data['monto'])
    fc._factura._tiporuc = float(data['tiporuc'])
    fc.merge(pos)
    return redirect('/facturas', code=302)
