# Vehicle Tracking System - Backend

A GPS-based vehicle tracking backend built with FastAPI, PostgreSQL, MQTT and Docker.

## Features

- JWT authentication
- Multiple users
- Route and vehicle assignment
- GPS data ingestion through MQTT
- Latest vehicle location
- GPS history
- User-level vehicle authorization
- PostgreSQL database
- Docker Compose setup

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- MQTT
- Docker

## API Endpoints

### Authentication

POST `/auth/login`

### User

GET `/me/`

GET `/me/route`

GET `/me/vehicle`

GET `/me/vehicle/location`

GET `/me/vehicle/history`

GET `/me/vehicle/{vehicle_id}`

## Local accounts

Use accounts configured in your local development database. Keep passwords out of public documentation and use unique credentials for any deployed instance.

## Run with Docker

```bash
docker compose up -d --build
```

## Companion application

The [Flutter client](https://github.com/Deepanjal-s/vehicle-tracking-flutter) displays assigned routes, vehicle details, latest location, and GPS history. See its README for client setup and local API connection limitations.
