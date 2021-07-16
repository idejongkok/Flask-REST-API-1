from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return f"{self.name} - {self.email}"

@app.route('/')
def index():
    return 'Mari Nyoba bikin REST API'

@app.route('/users')
def get_users():
    users = Users.query.all()

    output = []
    for user in users:
        user_data = {'name': user.name, 'email':user.email}

        output.append(user_data)
    return {"users" : output}

@app.route('/users/<id>')
def get_user(id):
    user = Users.query.get_or_404(id)
    return {"id": user.id, "name" : user.name, "email" : user.email}


@app.route('/users', methods=['POST'])
def add_user():
    user = Users(name=request.json['name'], email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    return {"message": "udah di tambah","id": user.id, "name" : user.name, "email" : user.email}

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "mamam tuh diapus"}

@app.route('/users/<id>', methods=['PUT'])
def edit_user(id):
    user = Users.query.get_or_404(id)
    update = Users.query.filter_by(id=id).first()
    update.name = request.json['name']
    update.email = request.json['email']
    db.session.flush()
    db.session.commit()
    return {"message": "udah di edit","id": user.id, "name" : user.name, "email" : user.email}
