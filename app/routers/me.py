from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models import User, Route, Vehicle, GPSRecord

router = APIRouter(prefix="/me", tags=["User"])


@router.get("/")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "route_id": current_user.route_id,
        "vehicle_id": current_user.vehicle_id,
    }


@router.get("/route")
def get_my_route(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    route = db.query(Route).filter(Route.id == current_user.route_id).first()

    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    return {
        "id": route.id,
        "name": route.name,
        "description": route.description,
    }


@router.get("/vehicle")
def get_my_vehicle(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    vehicle = db.query(Vehicle).filter(
        Vehicle.id == current_user.vehicle_id
    ).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return {
        "id": vehicle.id,
        "vehicle_number": vehicle.vehicle_number,
        "status": vehicle.status,
        "route_id": vehicle.route_id,
    }


@router.get("/vehicle/location")
def get_current_location(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    gps = (
        db.query(GPSRecord)
        .filter(GPSRecord.vehicle_id == current_user.vehicle_id)
        .order_by(GPSRecord.timestamp.desc())
        .first()
    )

    if not gps:
        return {
            "message": "No GPS data available",
            "location": None,
        }

    return {
        "vehicle_id": gps.vehicle_id,
        "latitude": gps.latitude,
        "longitude": gps.longitude,
        "speed": gps.speed,
        "timestamp": gps.timestamp,
    }


@router.get("/vehicle/history")
def get_vehicle_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    records = (
        db.query(GPSRecord)
        .filter(GPSRecord.vehicle_id == current_user.vehicle_id)
        .order_by(GPSRecord.timestamp.desc())
        .limit(100)
        .all()
    )

    return [
        {
            "vehicle_id": r.vehicle_id,
            "latitude": r.latitude,
            "longitude": r.longitude,
            "speed": r.speed,
            "timestamp": r.timestamp,
        }
        for r in records
    ]


@router.get("/vehicle/{vehicle_id}")
def access_vehicle(
    vehicle_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if vehicle_id != current_user.vehicle_id:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to access this vehicle"
        )

    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return {
        "id": vehicle.id,
        "vehicle_number": vehicle.vehicle_number,
        "status": vehicle.status,
        "route_id": vehicle.route_id,
    }