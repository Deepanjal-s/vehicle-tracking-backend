from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.me import router as me_router
from app.mqtt.subscriber import start_mqtt


app = FastAPI(
    title="Vehicle Tracking System",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(me_router)

mqtt_client = None


@app.on_event("startup")
def startup():
    global mqtt_client
    mqtt_client = start_mqtt()


@app.on_event("shutdown")
def shutdown():
    global mqtt_client

    if mqtt_client:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()


@app.get("/")
def root():
    return {
        "message": "Vehicle Tracking API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }