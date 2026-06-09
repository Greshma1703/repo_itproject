# WearItright

> WearItRight is a smart, web-based styling application designed to simplify daily outfit planning. It helps users — from fashion beginners to enthusiasts — create appropriate looks by combining real-time weather, occasion, personal style, and items from their own digital closet. Unlike apps that focus on shopping or inspiration, WearItRight solves the “I have clothes but nothing to wear” problem with fast, personalized recommendations tailored to what users already own. The platform is mobile and desktop friendly, with an intuitive interface that makes styling accessible for everyone.

## Team

| Role | Name |
|---|---|
| Product Owner | Lalit |
| Scrum Master | Sandrin|
| Developer | Brinda(Vaishnavi) |
| Developer |Greshma |


## Project Overview

WearItRight solves daily outfit anxiety for students, professionals, and fashion users of all levels by turning clothes they already own into smart recommendations. Using weather, occasion, and personal style, it delivers complete outfits — cutting decision fatigue and promoting sustainable, practical styling.

## Architecture

_Add your architecture diagram here (C4 Context or Container diagram). Update this as the project evolves._

```
service-a  ──►  service-b
    │
    ▼
  database
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | |
| Backend | |
| Database | |
| Deployment | |

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed
- Git

### Run locally

```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>
cp .env.example .env   # fill in your values
docker compose up --build
```

The app will be available at `http://localhost:3000`.

### Run with Flask

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Repository Structure

```
├── README.md
├── .gitignore
├── docs/
│   └── vision.md            # Product vision, personas, user stories
├── services/
│   ├── service-a/           # First microservice
│   └── service-b/           # Second microservice
└── docker-compose.yml
```

## Documentation

- [Vision Document](docs/vision.md)


## License

MIT
