# Profile Intelligence Service

A REST API that accepts a name and enriches it using Genderize, Agify, and Nationalize APIs.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Endpoints

- `POST /api/profiles` — create a profile
- `GET /api/profiles` — get all profiles
- `GET /api/profiles/<id>` — get a profile by id
- `DELETE /api/profiles/<id>` — delete a profile

## Base URL
coming soon