# Bangladeshi News Scraper & Analyser 🔴

> **Python-powered scraper that pulls headlines from major Bangladeshi news outlets and performs keyword frequency analysis.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-dc143c?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-111111?style=for-the-badge&logo=python&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/)
[![License: MIT](https://img.shields.io/badge/License-MIT-dc143c?style=for-the-badge)](LICENSE)
[![Portfolio](https://img.shields.io/badge/Portfolio-tawhidur.github.io-111111?style=for-the-badge&logo=github&logoColor=white)](https://tawhidur.github.io/)

---

## Overview

**newsScraper** collects headlines from leading Bangladeshi news sources — including Prothom Alo and The Daily Star — and performs keyword-based frequency analysis to surface trending topics and entities across the Bangladeshi media landscape.

Designed as a practical demonstration of Python web scraping, HTML parsing, and basic NLP pipeline construction in a real-world multilingual news context.

---

## Features

- 📰 **Multi-source scraping** — targets Prothom Alo, The Daily Star, and more
- 🔍 **Keyword filtering** — configurable watchlist for entities, topics, and names
- 📊 **Frequency analysis** — headline tokenisation and word frequency ranking
- ⚙️ **Modular site-scraper functions** — one function per news outlet, easy to extend
- 🕒 **Polite crawling** — request delays to avoid rate-limit bans

---

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3.8+-dc143c?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.x-111111?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2.x-dc143c?style=for-the-badge)](https://requests.readthedocs.io/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-111111?style=for-the-badge)](https://www.nltk.org/)

---

## Project Structure

```
newsScraper/
├── newsAnalysis.py     # Core scraper + analysis logic
├── config.py           # Keyword watchlist & site URLs (add yours here)
├── requirements.txt    # Python dependencies
├── .env.example        # Template for any API-gated sources
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.8+
- pip
- Stable internet connection

---

## Installation

```bash
# Clone the repository
git clone https://github.com/tawhidur/newsScraper.git
cd newsScraper

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
# Run the scraper and analysis
python newsAnalysis.py
```

**Example output:**

```
[Prothom Alo] Fetching headlines...  ✔  23 headlines retrieved
[Daily Star]  Fetching headlines...  ✔  18 headlines retrieved

--- Top Keywords (last 24h) ---
1. Economy       → 14 mentions
2. Election      → 11 mentions
3. Dhaka         → 9 mentions
...
```

### Customise the keyword watchlist

Edit `config.py` to add or remove tracked entities:

```python
KEYWORDS = [
    "Economy",
    "Election",
    "Climate",
    # Add your own
]

NEWS_SOURCES = {
    "prothom_alo": "https://www.prothomalo.com/",
    "daily_star":  "https://www.thedailystar.net/",
    # Add more outlets
}
```

---

## ⚠️ Ethical Use Notice

This tool is for **research and educational purposes only**. Always check a site's `robots.txt` and Terms of Service before scraping. The scraper includes request delays to be a polite client. Do not use this tool to circumvent paywalls or violate site policies.

---

## Roadmap

- [ ] Add Bengali-language (Bangla) headline support
- [ ] Export results to CSV / JSON
- [ ] Sentiment analysis on headlines using HuggingFace Transformers
- [ ] Schedule via cron for daily digest
- [ ] Add a simple CLI with `argparse` for keyword and date range flags

---

## Contributing

This is a personal portfolio project. Issues and feature suggestions are welcome via GitHub Issues.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

**Tawhidur Rahman** — Senior SQA Lead | CSM  
🌐 [Portfolio](https://tawhidur.github.io/) · 💼 [LinkedIn](https://www.linkedin.com/in/tawhidur/) · 🐦 [@Tawhid_CSE](https://twitter.com/Tawhid_CSE) · ✉️ tawhid.cse@gmail.com

---

*Built by [Tawhidur Rahman](https://tawhidur.github.io/) — 14+ years in SQA | Samsung Research · Progoti Systems*
