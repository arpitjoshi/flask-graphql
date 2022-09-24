from flask import Blueprint
from database.pgsql import db
from datetime import datetime
from api.models import Post
import time

cmd = Blueprint('db-ops', __name__)


@cmd.cli.command("create-db")
def create_db():
    """Creates database"""
    print("create-db")
    db.create_all()


@cmd.cli.command("drop-db")
def drop_db():
    """Cleans database"""
    print("drop-db")
    db.drop_all()


@cmd.cli.command("add-posts")
def add_posts():
    """Insert mock data in database"""
    posts = {
        "A new morning": "A new morning details",
        "Ankita Bhandari": "Ankita Bhandari called Rishikesh resort staffer 'crying' before",
        "News Highlights": "News Highlights: ‘Kremlin is leading a hybrid war’: European Council president at UNGA",
        "Mumbai news Live": "Mumbai news Live: Rain lashes Mumbai, transport services remain unaffected",
        "Man of the system": "Man of the system: How Jagdish Chandra uses news to"
    }
    for title, desc in posts.items():
        current_date = datetime.today().date()
        new_post = Post(title=title, description=desc, created_at=current_date)
        db.session.add(new_post)
        time.sleep(2)

    db.session.commit()
