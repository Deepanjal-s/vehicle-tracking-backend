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

## Test Users

### User A

Email: `a@test.com`

Password: `password123`

Vehicle: `BUS-001`

Route: `Route A`

### User B

Email: `b@test.com`

Password: `password123`

Vehicle: `BUS-002`

Route: `Route B`

## Run with Docker

```bash
docker compose up -d --build
