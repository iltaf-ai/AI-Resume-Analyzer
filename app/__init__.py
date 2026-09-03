from flask import Flask , Blueprint
from flask_sqlalchmy import SQLALchemy

db = SQLALchemy()

app = Flask(__name__)
def create_app():
    app.config['SQLALchemy-DATABASE-URI'] = 'sqlite:///Resume.db'
    app.config['SQLALchemy-TRACK-MODIFICATIONS'] = False

    db.init_app(app)

    from.app.routes import auth_bp
    from app.models import User , Resume
    from app.services import ai_bp
    from app.routes.dashborad import dashborad_bp
    
    
    app.Blueprint(auth_bp)
    app.Blueprint(ai_bp)
    app.Blueprint(dashborad_bp)

return app



