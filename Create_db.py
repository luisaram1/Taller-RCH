from app import create_app, db
from app.models import User, Client
app = create_app()
app.app_context().push()

db.create_all()
# Crear admin demo si no existe
if not User.query.filter_by(username="admin").first():
    u = User(username="admin", role="admin")
    u.set_password("admin123")
    db.session.add(u)
# Crear cliente demo
if not Client.query.filter_by(name="Cliente RCH").first():
    c = Client(name="Cliente RCH")
    db.session.add(c)
db.session.commit()
print("Base de datos creada. Usuario admin/admin123 y cliente demo añadidos.")
