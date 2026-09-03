from flask import (
    session,
    flash,
    redirect,
    url_for,
    Blueprint,
    request
)
from app.models import User
from werkzeug.security import generate_password_hash , check_password_hash
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.dashboard"))


@auth_bp.route('/register' , methods = ["GET" , "POST"])
def register():
    if "id" in session:
        return redirect(url_for("auth.dashboard"))

        if request.method == "POST":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            hash_password = generate_password_hash(password)

            user_exit = User.query.filter_by(email=email).first()
            if user_exit:
                flash("Email already exists", "error")
                return redirect(url_for("auth.login"))

            new_user = User(username = username , email = email , password = hash_password)
            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for("auth.login"))



