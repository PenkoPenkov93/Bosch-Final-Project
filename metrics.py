from prometheus_client import CollectorRegistry, Counter, Gauge, Info, push_to_gateway
import psutil

# Create a custom registry
registry = CollectorRegistry()

# Unregister the existing 'github_runner_status' metric, if it exists
if 'github_runner_status' in registry._names_to_collectors:
    registry.unregister(registry._names_to_collectors['github_runner_status'])

# Create Prometheus metrics with the custom registry
workflow_duration = Gauge('github_workflow_run_duration_ms', 'Duration of the GitHub Actions workflow in milliseconds', registry=registry)
workflow_status = Gauge('github_workflow_run_status', 'Status of the GitHub Actions workflow (0 for success, 1 for failure)', registry=registry)
runner_status = Info('runner_status', 'Operating system of the GitHub Actions runner', registry=registry)

# Get process time and memory usage
process = psutil.Process()
process_time = process.cpu_percent()
memory_usage = process.memory_info().rss / 1024 / 1024

# Get disk usage
disk_usage = psutil.disk_usage('/').total / 1024 / 1024 / 1024

# Update the Prometheus metrics
workflow_duration.set(100)  # Replace with the actual duration of the workflow
workflow_status.set(0)  # Replace with the actual status of the workflow (0 for success, 1 for failure)
runner_status.info({'os': 'Linux'})

# Push the metrics to the Pushgateway
push_to_gateway('104.214.223.114:9091', job='metrics_exporter', registry=registry)
