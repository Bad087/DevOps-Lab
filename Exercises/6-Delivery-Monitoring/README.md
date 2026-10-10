# Exercise 6 - Delivery Monitoring

## Objective
Build a containerized delivery monitoring system that exposes application metrics and visualizes them using Prometheus and Grafana.

## Tools Used
- Python
- Docker
- Docker Compose
- Prometheus
- Grafana

## Components

### Delivery Metrics
The Python metrics application exposes delivery-related metrics through an HTTP metrics endpoint for Prometheus to scrape.

### Prometheus
Prometheus collects metrics from the delivery metrics service using the configuration in `prometheus.yml`.

### Alert Rules
The `alert_rules.yml` file contains the configured Prometheus alerting rules.

### Grafana
Grafana connects to Prometheus as a data source and displays metrics in dashboards.

### Docker Compose
The `compose.yaml` file defines the services needed to run the monitoring stack.

## Project Structure
```text
Exercises/
└── 6-Delivery-Monitoring/
    ├── alert_rules.yml
    ├── compose.yaml
    ├── delivery_metrics.py
    ├── Dockerfile
    ├── prometheus.yml
    ├── requirements.txt
    ├── README.md
    └── screenshots/
```

## Running the Project
From this directory, start the services with:

```bash
docker compose up -d --build
```

Check service status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop the services:

```bash
docker compose down
```

## Verification
- Confirm that the delivery metrics endpoint responds.
- Confirm that Prometheus can scrape the metrics.
- Confirm that Grafana can query Prometheus and display the configured dashboard.

## Screenshots
The `screenshots/` directory contains evidence of the monitoring application, Prometheus, and Grafana setup.
