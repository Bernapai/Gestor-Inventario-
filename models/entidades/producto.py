
from models.entidades.categoria import Categoria
from models.entidades.proveedor import Proveedor
from datetime import datetime
from config import db


class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock_actual = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'), nullable=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id_proveedor'), nullable=True)
    fecha_creacion =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)


    def __init__(self, nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock_actual = stock_actual
        self.categoria_id = categoria_id
        self.proveedor_id = proveedor_id

    def serialize(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock_actual': self.stock_actual,
            'categoria_id': self.categoria_id,
            'proveedor_id': self.proveedor_id,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }

   