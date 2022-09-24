from flask import Flask

from welcome import welcome
from gql.gql import gql
from database.pgsql import db
from commands import cmd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://twnlfjmu:6j6O1boBzYBL8SKSCNj2AfSMgkuyD5CU@tiny.db.elephantsql.com/twnlfjmu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
# commands.init_app(app)

app.register_blueprint(gql)
app.register_blueprint(welcome)
app.register_blueprint(cmd)
