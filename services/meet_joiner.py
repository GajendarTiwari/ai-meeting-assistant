# services/meet_joiner.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def join_meet(meet_url):
    print("🚀 Launching Google Meet...")

    try:
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(meet_url)

        print("⏳ Waiting for Meet page to load...")
        time.sleep(10)  # wait for the page to load completely

        # Retry loop to find and click join button
        for i in range(4):
            try:
                join_button = driver.find_element(
                    By.XPATH, "//span[contains(text(), 'Join now') or contains(text(), 'Ask to join') or contains(text(), 'Join meeting')]"
                )
                join_button.click()
                print("✅ Joined the meeting.")
                break
            except Exception as e:
                print(f"🔁 Retry {i+1}: Join button not found yet. Waiting 5s...")
                time.sleep(5)
        else:
            print("⚠️ Join button still not found.")

        # Keep the browser open while recording
        return driver

    except Exception as e:
        print(f"⚠️ Error joining meet: {e}")
        return None
