from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import math

# from sqlalchemy.schema import Sequence
# from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False


db = SQLAlchemy(app)
# migrate = Migrate(app, db)


class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(30), nullable=False)
    sender_number = db.Column(db.String(10), nullable=False)
    sender_loc = db.Column(db.String(15))
    item_name = db.Column(db.String(50), nullable=False)
    item_weight = db.Column(db.String(5), nullable=False)
    receiver_name = db.Column(db.String(30), nullable=False)
    receiver_number = db.Column(db.String(10), nullable=False)
    receiver_loc = db.Column(db.String(15))
    cost = db.Column(db.Integer, nullable=False)
    payment_status = db.Column(db.String(5), nullable=False, default="False")
    delivered = db.Column(db.String(5), nullable=False, default="False")

    def __repr__(self):
        return f"<Cargo {self.id}>"


@app.route("/")
def index():
    cargo = Cargo.query.order_by(Cargo.id).all()
    return render_template("index.html", cargo=cargo)


@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        # id = request.form['id']
        sender_name = request.form["sender_name"]
        sender_number = request.form["sender_number"]
        sender_loc = request.form["sender_loc"]
        item_name = request.form["item_name"]
        item_weight = request.form["item_weight"]
        receiver_name = request.form["receiver_name"]
        receiver_number = request.form["receiver_number"]
        receiver_loc = request.form["receiver_loc"]

        if (sender_loc == "Chennai" and receiver_loc == "Trichy") or (
            sender_loc == "Trichy" and receiver_loc == "Chennai"
        ):
            distance = 330
            price_multiplier = 1.5
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Chennai" and receiver_loc == "Salem") or (
            sender_loc == "Salem" and receiver_loc == "Chennai"
        ):
            distance = 344
            price_multiplier = 1.6
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Chennai" and receiver_loc == "Madurai") or (
            sender_loc == "Madurai" and receiver_loc == "Chennai"
        ):
            distance = 455
            price_multiplier = 2.1
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Chennai" and receiver_loc == "Pondichery") or (
            sender_loc == "Pondichery" and receiver_loc == "Chennai"
        ):
            distance = 151
            price_multiplier = 0.7
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Trichy" and receiver_loc == "Salem") or (
            sender_loc == "Salem" and receiver_loc == "Trichy"
        ):
            distance = 140
            price_multiplier = 0.6
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Trichy" and receiver_loc == "Madurai") or (
            sender_loc == "Madurai" and receiver_loc == "Trichy"
        ):
            distance = 138
            price_multiplier = 0.5
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Trichy" and receiver_loc == "Pondichery") or (
            sender_loc == "Pondichery" and receiver_loc == "Trichy"
        ):
            distance = 208
            price_multiplier = 1.1
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Salem" and receiver_loc == "Madurai") or (
            sender_loc == "Madurai" and receiver_loc == "Salem"
        ):
            distance = 234
            price_multiplier = 1.3
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Salem" and receiver_loc == "Pondichery") or (
            sender_loc == "Pondichery" and receiver_loc == "Salem"
        ):
            distance = 220
            price_multiplier = 1.2
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        if (sender_loc == "Madurai" and receiver_loc == "Pondichery") or (
            sender_loc == "Pondichery" and receiver_loc == "Madurai"
        ):
            distance = 340
            price_multiplier = 1.6
            rate_per_km = 0.5
            cost = math.ceil(
                (int(item_weight) * 1000 * price_multiplier) + (distance * rate_per_km)
            )

        # delivered = False

        cargo = Cargo(
            sender_name=sender_name,
            sender_number=sender_number,
            sender_loc=sender_loc,
            item_name=item_name,
            item_weight=item_weight,
            receiver_name=receiver_name,
            receiver_number=receiver_number,
            receiver_loc=receiver_loc,
            cost=cost,
        )
        db.session.add(cargo)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("create.html")

    # @app.route('/update/<int:id>')
    # def update(id):
    pass

    # @app.route('/edit/<int:id>')
    # def edit(id):
    pass


@app.route("/delete/<int:id>", methods=("GET", "POST"))
def delete(id):
    if request.method == "POST" and request.form["candelete"] == "yes":
        cargo = Cargo.query.get(int(id))
        db.session.delete(cargo)
        db.session.commit()
        cargos = Cargo.query.order_by(Cargo.id).all()
        return render_template("viewall.html", cargo=cargos)
    else:
        cargo = Cargo.query.get(int(id))
        return render_template("delete.html", cargo=cargo)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/admin/", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = "admin"
        password = "password"
        if (
            request.form["username"] == username
            and request.form["password"] == password
        ):
            cargo = Cargo.query.order_by(Cargo.id).all()
            return render_template("viewall.html", cargo=cargo)
        else:
            flash("Wrong Credentials")

    return render_template("admin.html")


@app.route("/update/<int:id>")
def update(id):
    cargo = Cargo.query.get_or_404(id)
    return render_template("status.html", cargo=cargo)


@app.route("/status/<int:id>", methods=["POST"])
def status(id):
    # id = request.form['id']
    delivered = request.form["delivered"]
    existing_cargo = Cargo.query.get(id)
    existing_cargo.delivered = delivered
    db.session.commit()
    cargos = Cargo.query.order_by(Cargo.id).all()
    return render_template("viewall.html", cargo=cargos)


@app.route("/payupdate/<int:id>")
def payupdate(id):
    cargo = Cargo.query.get_or_404(id)
    return render_template("paystatus.html", cargo=cargo)


@app.route("/paystatus/<int:id>", methods=["POST"])
def paystatus(id):
    payment_status = request.form["payment_status"]
    existing_cargo = Cargo.query.get(id)
    existing_cargo.payment_status = payment_status
    db.session.commit()
    cargos = Cargo.query.order_by(Cargo.id).all()
    return render_template("viewall.html", cargo=cargos)
