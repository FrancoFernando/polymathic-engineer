# Measuring network latency

Code for the "Hands-on" section of *Where Latency Comes From and How to Measure It*.

Measure the round-trip latency to a host, then look at the distribution three
ways: a histogram, a percentile chart, and an eCDF.

## Setup

```sh
pip3 install ping3 numpy matplotlib hdrhistogram
```

## Measure your own network

```sh
python3 ping_measure.py google.com 100
```

This runs for about 100 seconds (one request per second) and writes
`ping-google.com.csv`.

## Plot the distribution

Each plotting script takes a CSV path and defaults to the included
`ping-sample.csv`, so you can try them before collecting your own data:

```sh
python3 plot_histogram.py    ping-google.com.csv   # -> histogram.png
python3 plot_percentiles.py  ping-google.com.csv   # -> percentiles.png
python3 plot_ecdf.py         ping-google.com.csv   # -> ecdf.png
```

`ping-sample.csv` holds 100 sample round trips: a tight body around 40 ms plus a
handful of isolated tail samples out to ~80 ms (p50 ≈ 40 ms, p99 ≈ 79 ms), so the
plots show a realistic tail.


[Read the newsletter issue: Latency: What It Is and What Limits It (Part II)](https://newsletter.francofernando.com/p/latency-what-it-is-and-what-limits).
