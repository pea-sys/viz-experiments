import flask
import flask_sqlalchemy
import flask_restless

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/nobel_prize.db"

db = flask_sqlalchemy.SQLAlchemy(app)


class Winners(db.Model):
    __tablename__ = "winners"
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    category = db.Column(db.Unicode)
    year = db.Column(db.Unicode)
    country = db.Column(db.Unicode)
    gender = db.Column(db.Unicode)


db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Winners, method=["GET"], max_results_per_page=1000)

app.run()
