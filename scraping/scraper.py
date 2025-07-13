from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os

URL = "https://en.wikisource.org/wiki/The_Adventures_of_Sherlock_Holmes/Adventure_I"

def scrape_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Screenshot
        screenshot_path = "../screenshots/chapter1.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path)
        print(f"✅ Screenshot saved to {screenshot_path}")

        # Scrape content
        html = page.content()
        soup = BeautifulSoup(html, "lxml")
        content_div = soup.find("div", class_="mw-parser-output")
        paragraphs = content_div.find_all("p")

        text = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        # Save to file
        output_path = "../output/chapter1.txt"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Chapter text saved to {output_path}")

        # RL Reward (basic)
        reward = 1 if len(text) > 1000 else -1
        print(f"🎯 RL Reward Score: {reward}")

        browser.close()

if __name__ == "__main__":
    scrape_chapter(URL)
