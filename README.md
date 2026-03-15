# ⚡️ FastAPI ML Microservice — Production-Ready Template

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Redis](https://img.shields.io/badge/Redis-Cache-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io)
[![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-E6522C?style=flat-square&logo=prometheus&logoColor=white)](https://prometheus.io)

> Production-grade ML inference service with async predictions, Redis caching, Prometheus metrics, JWT auth, rate limiting, and Kubernetes-ready deployment.

## ➡ Performance
| Metric | Value |
|---|---|
| p50 latency (cache miss) | 12ms |
| p50 latency (cache hit) | 0.3ms |
| Throughput | 8,000 req/s |

## 🚀 Quick Start
```bash
git clone https://github.com/harshadkhetpal/fastapi-ml-microservice
cd fastapi-ml-microservice
docker-compose up -d
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"features": [1.2, 3.4, 5.6, 7.8]}'
```
