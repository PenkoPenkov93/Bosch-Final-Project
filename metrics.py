from prometheus_client import Counter, Gauge, Info, start_http_server, REGISTRY
import psutil
import time

# Unregister the existing 'github_runner_status' metric, if it exists
if 'github_runner_status' in REGISTRY._names_to_collectors:
    REGISTRY.unregister(REGISTRY._names_to_collectors['github_runner_status'])

# Create Prometheus metrics
workflow_duration = Gauge('github_workflow_run_duration_ms', 'Duration of the GitHub Actions workflow in milliseconds')
workflow_status = Gauge('github_workflow_run_status', 'Status of the GitHub Actions workflow (0 for success, 1 for failure)')

# Create the new 'runner_status' Info metric
runner_status = Info('runner_status', 'Operating system of the GitHub Actions runner')

# Start the Prometheus metrics server
start_http_server(addr='104.214.223.114', port=8000)

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

# Wait for the Prometheus metrics server to receive the metrics
time.sleep(1)
