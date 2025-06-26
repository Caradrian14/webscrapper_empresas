from playwright.sync_api import sync_playwright
from datetime import datetime
from .constantes import programming_keywords
def scrape_job_listings(empresa, url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()
        # Ajusta los selectores según la página
        if page.get_by_text("Backend"):
            page.get_by_text("Backend").click()


        browser.close()