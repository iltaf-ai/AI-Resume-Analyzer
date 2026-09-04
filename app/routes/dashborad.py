from app import db
from flask import(
    Flask,
    redirect,
    render_template, 
    session,
    Blueprint,
    url_for

)

dashborad_bp = Blueprint("dashborad" , __name__)

@dashborad_bp.route("/dashborad")
def dashboard():
    if "id" not in session:
        return redirect(url_for("auth.login"))


    return render_template("dasboard.dashboard")