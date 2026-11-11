#!/usr/bin/env python3
"""Plot the latency distribution as a histogram."""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("ping-sample.csv")
latencies_ms = np.genfromtxt(path, delimiter=",", skip_header=1) * 1000

plt.hist(latencies_ms, bins="auto")
plt.xlabel("Latency (milliseconds)")
plt.ylabel(f"Frequency (N = {len(latencies_ms)})")
plt.savefig("histogram.png", dpi=300)
