#!/usr/bin/env python3

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# App URL
BASE_URL = "http://localhost:5000"

# Screenshot configurations for each device/platform
SCREENSHOT_CONFIGS = [
    # iPhone 6.7-inch (1290 x 2796)
    {
        "name": "iPhone 6.7-inch",
        "width": 1290,
        "height": 2796,
        "device_width": 430,
        "device_height": 932,
        "pixel_ratio": 3,
        "folder": "app-store-assets/screenshots/iphone/6.7-inch/"
    },
    # iPhone 6.5-inch (1284 x 2778) 
    {
        "name": "iPhone 6.5-inch",
        "width": 1284,
        "height": 2778,
        "device_width": 428,
        "device_height": 926,
        "pixel_ratio": 3,
        "folder": "app-store-assets/screenshots/iphone/6.5-inch/"
    },
    # iPhone 5.5-inch (1242 x 2208)
    {
        "name": "iPhone 5.5-inch", 
        "width": 1242,
        "height": 2208,
        "device_width": 414,
        "device_height": 736,
        "pixel_ratio": 3,
        "folder": "app-store-assets/screenshots/iphone/5.5-inch/"
    },
    # iPad 12.9-inch (2048 x 2732)
    {
        "name": "iPad 12.9-inch",
        "width": 2048,
        "height": 2732,
        "device_width": 1024,
        "device_height": 1366,
        "pixel_ratio": 2,
        "folder": "app-store-assets/screenshots/ipad/12.9-inch/"
    },
    # Android Phone (1080 x 1920)
    {
        "name": "Android Phone",
        "width": 1080,
        "height": 1920,
        "device_width": 360,
        "device_height": 640,
        "pixel_ratio": 3,
        "folder": "app-store-assets/screenshots/android/phone/"
    },
    # Android 7-inch Tablet (1200 x 1920)
    {
        "name": "Android 7-inch Tablet",
        "width": 1200,
        "height": 1920,
        "device_width": 600,
        "device_height": 960,
        "pixel_ratio": 2,
        "folder": "app-store-assets/screenshots/android/tablet-7/"
    },
    # Android 10-inch Tablet (1600 x 2560)
    {
        "name": "Android 10-inch Tablet",
        "width": 1600,
        "height": 2560,
        "device_width": 800,
        "device_height": 1280,
        "pixel_ratio": 2,
        "folder": "app-store-assets/screenshots/android/tablet-10/"
    },
]

# Screenshot pages with their routes and filenames
SCREENSHOT_PAGES = [
    {
        "name": "Dashboard Hero",
        "url": f"{BASE_URL}/",
        "filename_suffix": "dashboard-hero",
        "wait_selector": "[data-testid='dashboard-stats']",  # Wait for dashboard to load
        "description": "Family dashboard with stats and activity"
    },
    {
        "name": "Groups Overview", 
        "url": f"{BASE_URL}/groups",
        "filename_suffix": "groups-overview",
        "wait_selector": "[data-testid='groups-list']",  # Wait for groups to load
        "description": "Family groups listing"
    },
    {
        "name": "Event Planning",
        "url": f"{BASE_URL}/events", 
        "filename_suffix": "event-planning",
        "wait_selector": "[data-testid='events-list']",  # Wait for events to load
        "description": "Event creation/management interface"
    },
    {
        "name": "Group Chat",
        "url": f"{BASE_URL}/chat/1",  # Assuming group ID 1 exists
        "filename_suffix": "group-chat",
        "wait_selector": "[data-testid='chat-messages']",  # Wait for chat to load
        "description": "Family chat with messages and photos"
    },
    {
        "name": "Premium Labels",
        "url": f"{BASE_URL}/groups/1/labels",  # Assuming group ID 1 exists
        "filename_suffix": "premium-labels", 
        "wait_selector": "[data-testid='mailing-labels']",  # Wait for labels to load
        "description": "Mailing label generation (premium feature)"
    },
]

def setup_chrome_driver():
    """Setup Chrome WebDriver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--force-device-scale-factor=1")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Use system chromium binary
    chrome_options.binary_location = "/nix/store/zi4f80l169xlmivz8vja8wlphq74qqk0-chromium-125.0.6422.141/bin/chromium"
    
    try:
        # Try using system chromedriver first
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Failed with system chromedriver: {e}")
        # Fallback to ChromeDriverManager
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            return driver
        except Exception as e2:
            print(f"Failed with ChromeDriverManager: {e2}")
            raise e2

def create_directories():
    """Create all necessary directories for screenshots"""
    for config in SCREENSHOT_CONFIGS:
        os.makedirs(config["folder"], exist_ok=True)
        print(f"Created directory: {config['folder']}")

def wait_for_page_load(driver, wait_selector, timeout=10):
    """Wait for a specific element to load on the page"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, wait_selector))
        )
        return True
    except Exception as e:
        print(f"Warning: Could not find selector {wait_selector}: {e}")
        # Still proceed with screenshot even if selector not found
        return False

def capture_screenshot(driver, config, page, skip_existing=True):
    """Capture a screenshot for a specific device configuration and page"""
    
    # Generate filename based on device and page
    device_suffix = config["name"].lower().replace(" ", "").replace("-", "").replace(".", "")
    if "iphone67" in device_suffix:
        device_suffix = "iphone67"
    elif "iphone65" in device_suffix:
        device_suffix = "iphone65"
    elif "iphone55" in device_suffix:
        device_suffix = "iphone55"
    elif "ipad" in device_suffix:
        device_suffix = "ipad129"
    elif "androidphone" in device_suffix:
        device_suffix = "android"
    elif "android7" in device_suffix:
        device_suffix = "tablet7"
    elif "android10" in device_suffix:
        device_suffix = "tablet10"
    
    filename = f"{page['filename_suffix']}-{device_suffix}.png"
    filepath = os.path.join(config["folder"], filename)
    
    # Skip if file exists and skip_existing is True
    if skip_existing and os.path.exists(filepath):
        print(f"Skipping existing screenshot: {filepath}")
        return True
    
    try:
        # Set window size to device dimensions
        driver.set_window_size(config["device_width"], config["device_height"])
        
        # Navigate to the page
        print(f"Navigating to: {page['url']}")
        driver.get(page["url"])
        
        # Wait for page to load
        print(f"Waiting for page to load...")
        wait_for_page_load(driver, page["wait_selector"])
        
        # Additional wait for any animations or async content
        time.sleep(3)
        
        # Take screenshot
        print(f"Capturing screenshot: {filepath}")
        success = driver.save_screenshot(filepath)
        
        if success:
            print(f"✅ Successfully captured: {filename} ({config['width']}x{config['height']})")
            return True
        else:
            print(f"❌ Failed to capture: {filename}")
            return False
            
    except Exception as e:
        print(f"❌ Error capturing {filename}: {e}")
        return False

def verify_app_accessibility():
    """Verify the app is running and accessible"""
    import requests
    try:
        response = requests.get(BASE_URL, timeout=10)
        if response.status_code == 200:
            print(f"✅ App is accessible at {BASE_URL}")
            return True
        else:
            print(f"❌ App returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot access app: {e}")
        return False

def main():
    """Main function to generate all screenshots"""
    print("🚀 Starting My Branches Screenshot Generation")
    print("=" * 50)
    
    # Verify app is running
    if not verify_app_accessibility():
        print("❌ App is not accessible. Please ensure it's running at localhost:5000")
        return False
    
    # Create directories
    create_directories()
    
    # Setup Chrome driver
    print("\n📱 Setting up Chrome WebDriver...")
    driver = setup_chrome_driver()
    
    try:
        total_screenshots = 0
        successful_screenshots = 0
        
        # Generate screenshots for each configuration and page
        for config in SCREENSHOT_CONFIGS:
            print(f"\n🔧 Configuring for {config['name']} ({config['width']}x{config['height']})")
            
            for page in SCREENSHOT_PAGES:
                print(f"\n📸 Capturing {page['name']} for {config['name']}")
                success = capture_screenshot(driver, config, page)
                total_screenshots += 1
                if success:
                    successful_screenshots += 1
        
        print(f"\n🎉 Screenshot generation complete!")
        print(f"📊 Results: {successful_screenshots}/{total_screenshots} screenshots captured successfully")
        
        if successful_screenshots == total_screenshots:
            print("✅ All screenshots generated successfully!")
            return True
        else:
            print(f"⚠️  {total_screenshots - successful_screenshots} screenshots failed")
            return False
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
        
    finally:
        driver.quit()
        print("🔧 WebDriver closed")

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)