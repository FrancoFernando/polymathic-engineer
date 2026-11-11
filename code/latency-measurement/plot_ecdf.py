#!/usr/bin/env python3
"""Plot the latency distribution as an empirical CDF (eCDF).

The eCDF answers questions like "what fraction of requests finish under 45 ms?"
by sorting the samples and plotting the running fraction from 0 to 1.
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("ping-sample.csv")
latencies_ms = np.genfromtxt(path, delimiter=",", skip_header=1) * 1000

x = np.sort(latencies_ms)
y = np.arange(1, len(x) + 1) / len(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Latency (milliseconds)")
ax.set_ylabel("Cumulative fraction")
ax.set_yticks(np.arange(0, 1.1, 0.1))
ax.grid(True)
fig.savefig("ecdf.png", dpi=300)
