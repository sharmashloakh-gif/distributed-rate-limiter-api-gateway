# SentinelGate — Distributed API Gateway & Rate Limiter

A lightweight, high-throughput API gateway and distributed rate limiter built with **Django**, **MySQL**, and **Python** (token-bucket & sliding-window algorithms) without relying on heavy third-party proxies.

## Why This Matters to Engineering Teams
At scale (Google/Microsoft workloads), protecting downstream microservices from traffic spikes and noisy neighbors is critical. SentinelGate implements atomic sliding-window counters, dynamic IP/API-key throttling, circuit breakers, and real-time traffic analytics.

## Core Architecture
- **Backend:** Python, Django REST architecture, Thread-safe Token Bucket engine
- **Storage:** MySQL (Indexed sliding window logs, API key quotas, audit trails)
- **Dashboard:** HTML5, CSS3, Vanilla JS + Bootstrap 5 live telemetry UI

## Quick Start
```bash
pip install django mysqlclient
python manage.py migrate
python manage.py runserver
```
