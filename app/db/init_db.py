from app.db.database import Base, engine
from app.models import User, Route, Vehicle, GPSRecord

Base.metadata.create_all(bind=engine)

print("Database tables created.")