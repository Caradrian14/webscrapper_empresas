from playwright.sync_api import sync_playwright

def scrape_job_listings(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # Ajusta los selectores según la página
        page.wait_for_selector('.job-listing')
        job_listings = page.query_selector_all('.job-listing')

        for job in job_listings:
            title = job.query_selector('.job-title').inner_text()
            company = job.query_selector('.company-name').inner_text()
            print(f'Title: {title}, Company: {company}')

        browser.close()
