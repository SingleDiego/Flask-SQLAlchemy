from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # 自定义 __init__() 方法，使其具有默认的 username 和 email
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        
        self.username = kwargs.get('username', 'default_name')
        self.email = kwargs.get('email', 'default_email@flask.com')


    def __repr__(self):
        return '<User %r>' % self.username

new_user = User()
db.session.add(new_user)
db.session.commit()