import app
from app import *

with app.app_context():
    db.drop_all()
    db.create_all()
    #db.session.execute("INSERT INTO Cargo (id) VALUES (1000)")