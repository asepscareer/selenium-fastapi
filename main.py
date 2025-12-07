from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import uvicorn
import os
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_driver():
    service = Service(os.environ.get("CHROMEDRIVER_PATH"))
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    driver = webdriver.Chrome(service=service, options=options)
    return driver


@app.get("/")
def root():
    return {"message": "Selenium FastAPI on Railway - OK"}


@app.get("/scrape")
def scrape():
    title = None
    url = "https://www.scrapethissite.com/"
    driver = init_driver()
    try:
        logger.info(f"Scraping URL: {url}")
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else "No title found"

        logger.info(f"Scraped Title: {title}")
    except Exception as e:
        logger.error(f"Error during scraping: {e}")
    finally:
        driver.quit()
        return {"title": title, "url": url}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)