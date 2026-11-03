# Dexscreener Solana Token Monitor

A lightweight Python CLI tool for tracking, filtering, and analyzing newly created trading pairs on the Solana blockchain using the Dexscreener REST API.

---

## Features

- **Public REST API Integration:** Fetches real-time market data from Dexscreener's search endpoints using `requests`.
- **Targeted Chain & Age Filtering:** Isolates Solana pairs created within the last 24 hours.
- **Volume Threshold Validation:** Filters out low-liquidity pairs, displaying only tokens with a 24-hour trading volume exceeding $10,000.
- **Multi-Level Sorting:** Sorts extracted pairs dynamically by age and trading volume.
- **Formatted Terminal Output:** Displays clean tabular data with precise column alignment and floating-point formatting.

---

## Prerequisites

- Python 3.8+
- `requests` library

```bash
pip install requests
