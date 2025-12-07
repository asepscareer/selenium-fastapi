# Selenium FastAPI

Deploy a lightweight Selenium + FastAPI scraper on Railway: headless Chromium, optimized Chrome flags, clean FastAPI service, and ready-to-extend blueprint for web scraping.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/selenium-fastapi?referralCode=asepsp&utm_medium=integration&utm_source=template&utm_campaign=generic)

## Features

* Headless Chromium + Chromedriver preinstalled
* Optimized Chrome flags for low-memory Railway environments
* Simple FastAPI endpoint (`/scrape`) as Selenium scraping example
* BS4 for fast HTML parsing
* Minimal, reproducible Dockerfile
* `$PORT`-aware FastAPI server

## Endpoints

| Route     | Description                                               |
| --------- | --------------------------------------------------------- |
| `/`       | Basic health/status check                                 |
| `/scrape` | Example scraper using Selenium → BS4 (scrapethissite.com) |

## File Structure

```
.
├── Dockerfile
├── main.py
└── requirements.txt
```

## How It Works

* Chromium & Chromedriver installed through `apt`
* Headless Chrome launched with safe container flags
* Selenium retrieves page HTML
* BeautifulSoup handles parsing for performance
* FastAPI exposes clean HTTP endpoints for triggering scrapes

## Notes

* Suitable as a base template for any Selenium scraping workflow
* Recommended to add request queueing if scraping becomes heavy
* For production scraping, consider disabling large asset loading (images, fonts)