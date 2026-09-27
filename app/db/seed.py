from app.db.database import SessionLocal
from app.models import User, Route, Vehicle
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

db = SessionLocal()

route_a = Route(
    name="Route A",
    description="NIT Sikkim Route A"
)

route_b = Route(
    name="Route B",
    description="NIT Sikkim Route B"
)

db.add_all([route_a, route_b])
db.commit()

db.refresh(route_a)
db.refresh(route_b)

vehicle_a = Vehicle(
    vehicle_number="BUS-001",
    status="active",
    route_id=route_a.id
)

vehicle_b = Vehicle(
    vehicle_number="BUS-002",
    status="active",
    route_id=route_b.id
)

db.add_all([vehicle_a, vehicle_b])
db.commit()

db.refresh(vehicle_a)
db.refresh(vehicle_b)

user_a = User(
    email="a@test.com",
    password_hash=password_hash.hash("password123"),
    route_id=route_a.id,
    vehicle_id=vehicle_a.id
)

user_b = User(
    email="b@test.com",
    password_hash=password_hash.hash("password123"),
    route_id=route_b.id,
    vehicle_id=vehicle_b.id
)

db.add_all([user_a, user_b])
db.commit()

db.close()

print("Seed data created.")