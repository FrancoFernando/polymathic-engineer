#!/usr/bin/env python3
"""Plot latency by percentile using HdrHistogram."""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from hdrh.histogram import HdrHistogram

path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("ping-sample.csv")
latencies_ms = np.genfromtxt(path, delimiter=",", skip_header=1) * 1000

histogram = HdrHistogram(1, 1000, 4)  # track 1 ms .. 1000 ms, 4 significant digits
for value in latencies_ms:
    histogram.record_value(value)

percentiles = [25.0, 50.0, 90.0, 99.0, 99.9, 99.99]
values = [histogram.get_value_at_percentile(p) for p in percentiles]

fig, ax = plt.subplots()
ax.plot([p / 100 for p in percentiles], values)
ax.set_xscale("logit")
ax.set_xticks([0.25, 0.5, 0.9, 0.99, 0.999, 0.9999])
ax.xaxis.set_major_formatter(
    ticker.FixedFormatter(["25%", "50%", "90%", "99%", "99.9%", "99.99%"])
)
ax.xaxis.set_minor_formatter(ticker.NullFormatter())
ax.set_xlabel("Percentile")
ax.set_ylabel("Latency (milliseconds)")
ax.set_title("Latency by percentile")
ax.grid(True)
fig.savefig("percentiles.png", dpi=300)
