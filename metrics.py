import psutil
import requests
import json
import os

# Get process time and memory usage
process = psutil.Process()
process_time = process.cpu_percent()
memory_usage = process.memory_info().rss / 1024 / 1024

# Get disk usage
disk_usage = psutil.disk_usage('/').total / 1024 / 1024 / 1024

# Get GitHub Actions environment variables
workflow_run_duration = os.environ.get('GITHUB_WORKFLOW_RUN_DURATION')
workflow_run_status = os.environ.get('GITHUB_WORKFLOW_RUN_STATUS')
runner_status = os.environ.get('RUNNER_OS')

# Define Prometheus metrics payload
metrics = {
    'process_time': process_time,
    'memory_usage': memory_usage,
    'disk_usage': disk_usage,
    'github_workflow_run_duration_ms': workflow_run_duration,
    'github_workflow_run_status': workflow_run_status,
    'github_runner_status': runner_status
}

# Send metrics to Prometheus
url = 'http://104.214.223.114:9100/metrics/job/metrics_exporter'
response = requests.post(url, data=json.dumps(metrics))
