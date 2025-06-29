import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from services.obs_controller import start_obs_recording, stop_obs_recording


# === CONFIGURABLE ===
MEET_URL = "https://meet.google.com/your-meeting-code"  # Change to your actual Meet link
RECORDING_DURATION = 300  # In seconds (e.g. 300 = 5 minutes)
CHROMEDRIVER_PATH = r"C:\Users\Admin\chromedriver-win64\chromedriver.exe"

print("🚀 Launching Chrome and joining Google Meet...")

# Setup Chrome options
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-blink-features=AutomationControlled")

# Optional: auto login using a profile
# options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
driver.get(MEET_URL)

# Wait and click "Join now"
time.sleep(10)
try:
    join_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Join now')]")
    join_btn.click()
    print("✅ Joined meeting.")
except Exception as e:
    print("⚠️ Couldn't find Join button:", e)

time.sleep(5)

# === START RECORDING ===
print("🎥 Recording session...")
start_obs_recording()

time.sleep(RECORDING_DURATION)

# === STOP RECORDING ===
print("🛑 Stopping recording...")
stop_obs_recording()

print("✅ Meeting session complete. Closing browser...")
driver.quit()
