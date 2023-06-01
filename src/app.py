from flask import Flask
from models import db

app = Flask(__name__)

from controllers import *

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/2455248_facturacion'
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
app_context = app.app_context()
app_context.push()   
db.init_app(app)
db.create_all()