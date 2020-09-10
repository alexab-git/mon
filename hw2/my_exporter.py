from prometheus_client import start_http_server, Summary, Gauge, Histogram
import time

# Create a metric to track seconds in current time.
SECONDS_GAUGE = Gauge('my_seconds_gauge', 'seconds gauge')

# Create a metric to track seconds sum
SECONDS_SUM = Summary('my_seconds', 'seconds sum')


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    # collect metrics
    while True:
        sec = time.localtime().tm_sec
        SECONDS_GAUGE.set(sec)
        SECONDS_SUM.observe(sec)
        time.sleep(1)
