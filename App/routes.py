from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import LoginForm, VehicleForm, RepairForm
from app.models import User, Client, Vehicle, Repair
from app import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and u.check_password(form.password.data):
            login_user(u)
            return redirect(url_for("main.index"))
        flash("Usuario o contraseña incorrectos", "danger")
    return render_template("login.html", form=form)

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main_bp.route("/")
@login_required
def index():
    vehicles = Vehicle.query.all()
    return render_template("index.html", vehicles=vehicles)

@main_bp.route("/vehicles")
@login_required
def vehicles():
    vehicles = Vehicle.query.all()
    return render_template("vehicles.html", vehicles=vehicles)

@main_bp.route("/vehicle/new", methods=["GET","POST"])
@login_required
def new_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        client = Client.query.get(form.client_id.data)
        if not client:
            flash("Cliente no encontrado (usa el ID).", "danger")
            return redirect(url_for("main.vehicles"))
        v = Vehicle(plate=form.plate.data.upper(), brand=form.brand.data, model=form.model.data, client=client)
        db.session.add(v); db.session.commit()
        flash("Vehículo creado", "success")
        return redirect(url_for("main.index"))
    return render_template("vehicle_detail.html", form=form)

@main_bp.route("/vehicle/<int:vid>", methods=["GET","POST"])
@login_required
def vehicle_detail(vid):
    vehicle = Vehicle.query.get_or_404(vid)
    form = RepairForm()
    if form.validate_on_submit():
        r = Repair(description=form.description.data, cost=form.cost.data or 0.0, vehicle=vehicle)
        db.session.add(r); db.session.commit()
        flash("Reparación registrada", "success")
        return redirect(url_for("main.vehicle_detail", vid=vid))
    return render_template("vehicle_detail.html", vehicle=vehicle, form=form)
