# Polymarket 5M BTC Predictor

Production-oriented foundation for analysing Polymarket BTC 5-minute Up/Down markets.

## Current stage

Stage 1:
- project structure
- configuration
- environment variables
- Docker
- Render skeleton
- tests

## Run locally

```bash
python -m venv .venv
pip install -r requirements.txt
python -m app.main
```

## Tests

```bash
pytest
```

## Environment

Copy `.env.example` to `.env` and configure the required variables.

## Important

This project does not guarantee prediction accuracy or profitability.
Future stages must validate every model with historical out-of-sample data.
