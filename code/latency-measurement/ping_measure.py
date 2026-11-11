#!/usr/bin/env python3
"""Measure round-trip latency to a host and save the samples to a CSV file.

Requests go out at a fixed interval rather than back-to-back, so we sample the
latency distribution honestly instead of hiding slow requests (coordinated
omission). Replies slower than the interval time out and are dropped, which is
fine for a quick look at the tail.
"""
import argparse
import csv
import time

from ping3 import ping

INTERVAL = 1  # seconds between requests

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("samples", type=int)
args = parser.parse_args()

latencies = []
for _ in range(args.samples):
    rtt = ping(args.host, timeout=INTERVAL)
    if not rtt:
        print("warning: ping timed out, outlier not recorded")
        continue
    latencies.append(rtt)
    time.sleep(max(0, INTERVAL - rtt))

with open(f"ping-{args.host}.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Latency_secs"])
    writer.writerows([value] for value in latencies)
