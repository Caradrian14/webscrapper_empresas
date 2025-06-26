from playwright.sync_api import sync_playwright

def scrape_job_listings(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state()
        # Ajusta los selectores según la página
        job_listings = page.query_selector_all('.notion-page-block')

        for job in job_listings:
            # si en el titulo existen una serie de palabras clave, que se muestre
            title = job.inner_text()
            print(f'Title: {title}')

        browser.close()
