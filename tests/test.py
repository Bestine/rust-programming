# Using Chromium browser

# from playwright.sync_api import sync_playwright

# def access_homepage():
#     with sync_playwright() as p:
#         # Launch the browser in headless mode
#         browser = p.chromium.launch(headless=False)  # Set to True if you don't want to see the browser window
#         page = browser.new_page()

#         # Go to the homepage
#         url = "https://www.docinfo.org/"
#         page.goto(url)

#         # Wait for the page content to load fully
#         page.wait_for_load_state("networkidle")

#         # Extract general information from the homepage
#         # Example: Get the main heading or any intro text if available
#         heading = page.query_selector("h1").inner_text() if page.query_selector("h1") else "Heading not found"
#         intro_text = page.query_selector(".intro-text").inner_text() if page.query_selector(".intro-text") else "Intro text not found"

#         # Print or return the extracted information
#         print(f"Heading: {heading}")
#         print(f"Intro Text: {intro_text}")

#         # You can further explore and extract other elements as needed
#         # For example, listing links in the footer or navigation
#         links = page.query_selector_all("a")
#         for link in links:
#             link_text = link.inner_text()
#             link_url = link.get_attribute("href")
#             print(f"Link: {link_text} - URL: {link_url}")

#         # Close the browser
#         browser.close()

# # Run the function to test accessing the homepage
# access_homepage()

# Using Firefox
from playwright.sync_api import sync_playwright

def access_homepage():
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.firefox.launch(headless=False)  # Set to True if you don't want to see the browser window
        page = browser.new_page()

        # Go to the homepage
        url = "https://www.docinfo.org/"
        page.goto(url)

        # Wait for the page content to load fully
        page.wait_for_load_state("networkidle")

        # Extract general information from the homepage
        # Example: Get the main heading or any intro text if available
        heading = page.query_selector("h1").inner_text() if page.query_selector("h1") else "Heading not found"
        intro_text = page.query_selector(".intro-text").inner_text() if page.query_selector(".intro-text") else "Intro text not found"

        # Print or return the extracted information
        print(f"Heading: {heading}")
        print(f"Intro Text: {intro_text}")

        # You can further explore and extract other elements as needed
        # For example, listing links in the footer or navigation
        links = page.query_selector_all("a")
        for link in links:
            link_text = link.inner_text()
            link_url = link.get_attribute("href")
            print(f"Link: {link_text} - URL: {link_url}")

        # Close the browser
        browser.close()

# Run the function to test accessing the homepage
access_homepage()
