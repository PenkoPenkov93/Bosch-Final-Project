#!/bin/bash

# Install Docker and Docker Compose
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

# Create Docker Compose file for SonarQube, Prometheus, and Grafana
sudo tee docker-compose.yml > /dev/null <<EOF
version: '3'

services:
  sonarqube:
    image: sonarqube:8.5-community
    ports:
      - "9000:9000"
    networks:
      - sonarnet
    environment:
      - SONARQUBE_JDBC_URL=jdbc:postgresql://sonarqube-db:5432/sonar
      - SONARQUBE_JDBC_USERNAME=sonar
      - SONARQUBE_JDBC_PASSWORD=sonar

  sonarqube-db:
    image: postgres:13
    networks:
      - sonarnet
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
      - POSTGRES_DB=sonar

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - sonarnet

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    networks:
      - sonarnet

networks:
  sonarnet:

EOF

# Create Prometheus configuration file
sudo tee prometheus.yml > /dev/null <<EOF
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'sonarqube'
    metrics_path: '/sonarqube-prometheus-exporter/metrics'
    static_configs:
      - targets: ['sonarqube:9000']
EOF

# Start Docker Compose
sudo docker-compose up -d
