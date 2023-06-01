from models import db

class Productos(db.Model):
    id = db.Column(db.Integer(128), unique=True, nullable=False)
    descripcion = db.Column(db.String(128), unique=True, nullable=False)
    valor_unitario = db.Column(db.Float(10,8))
    unidad_medida = db.Column(db.String(3), nullable=False)
    cantidad_stock = db.Column(db.Float(10,8))
    categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    facturas = db.relationship('facturas', secondary='facturas_productos', back_populates='productos')