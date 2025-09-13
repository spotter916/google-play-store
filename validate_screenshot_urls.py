#!/usr/bin/env python3

import requests
import json
import time
from urllib.parse import urljoin

# App URL
BASE_URL = "http://localhost:5000"

# Screenshot pages to validate
SCREENSHOT_PAGES = [
    {
        "name": "Dashboard Hero",
        "url": f"{BASE_URL}/",
        "expected_title_keywords": ["My Branches", "Dashboard", "Family"],
        "description": "Family dashboard with stats and activity"
    },
    {
        "name": "Groups Overview", 
        "url": f"{BASE_URL}/groups",
        "expected_title_keywords": ["Groups", "My Branches"],
        "description": "Family groups listing"
    },
    {
        "name": "Event Planning",
        "url": f"{BASE_URL}/events", 
        "expected_title_keywords": ["Events", "My Branches"],
        "description": "Event creation/management interface"
    },
    {
        "name": "Group Chat",
        "url": f"{BASE_URL}/chat",  # Try without specific ID first
        "expected_title_keywords": ["Chat", "My Branches"],
        "description": "Family chat with messages and photos"
    },
    {
        "name": "Premium Labels",
        "url": f"{BASE_URL}/labels",  # Try general labels endpoint
        "expected_title_keywords": ["Labels", "My Branches"],
        "description": "Mailing label generation (premium feature)"
    },
]

def check_url_accessibility(url, timeout=10):
    """Check if a URL is accessible and return status info"""
    try:
        response = requests.get(url, timeout=timeout)
        return {
            "accessible": True,
            "status_code": response.status_code,
            "content_length": len(response.text),
            "title_found": any(keyword.lower() in response.text.lower() 
                             for keyword in ["my branches", "family", "dashboard", "groups", "events", "chat", "labels"])
        }
    except requests.exceptions.RequestException as e:
        return {
            "accessible": False,
            "error": str(e),
            "status_code": None,
            "content_length": 0,
            "title_found": False
        }

def validate_all_pages():
    """Validate all screenshot pages are accessible"""
    print("🔍 Validating My Branches App Pages for Screenshot Capture")
    print("=" * 60)
    
    results = {}
    all_good = True
    
    for page in SCREENSHOT_PAGES:
        print(f"\n📄 Testing: {page['name']}")
        print(f"   URL: {page['url']}")
        
        result = check_url_accessibility(page['url'])
        results[page['name']] = result
        
        if result['accessible'] and result['status_code'] == 200:
            print(f"   ✅ Status: {result['status_code']} - Content: {result['content_length']} chars")
            if result['title_found']:
                print(f"   ✅ App content detected")
            else:
                print(f"   ⚠️  App-specific content not clearly detected")
        else:
            print(f"   ❌ Status: {result.get('status_code', 'ERROR')} - Error: {result.get('error', 'Unknown')}")
            all_good = False
    
    print(f"\n🎯 Summary:")
    print(f"   📱 App base URL: {BASE_URL}")
    
    working_pages = [name for name, result in results.items() 
                    if result['accessible'] and result['status_code'] == 200]
    
    print(f"   ✅ Working pages: {len(working_pages)}/{len(SCREENSHOT_PAGES)}")
    
    if working_pages:
        print(f"   📝 Ready for screenshots:")
        for page_name in working_pages:
            page = next(p for p in SCREENSHOT_PAGES if p['name'] == page_name)
            print(f"      • {page_name}: {page['url']}")
    
    if not all_good:
        print(f"\n⚠️  Some pages may not be accessible. Consider:")
        print(f"   • Checking if authentication is required")
        print(f"   • Verifying the app routes are properly configured")
        print(f"   • Testing alternative URL paths")
    
    return results

def create_manual_guide():
    """Create a comprehensive manual screenshot guide"""
    guide_content = """# My Branches Manual Screenshot Capture Guide

## Quick Start Instructions

### Prerequisites ✅
- Chrome browser (latest version recommended)
- My Branches app running at http://localhost:5000
- All app pages validated and accessible

### Step-by-Step Process

#### 1. Open Chrome Developer Tools
1. Open Chrome and navigate to `http://localhost:5000`
2. Press `F12` to open Developer Tools
3. Click the "Toggle device toolbar" icon (📱) or press `Ctrl+Shift+M`
4. Select "Responsive" from the device dropdown

#### 2. Configure Device Dimensions

For each screenshot size, set these exact dimensions:

**iPhone 6.7-inch (iPhone 14 Pro Max, 15 Pro Max)**
- Dimensions: `430 x 932` pixels  
- Device Pixel Ratio: `3x`
- Final screenshot: `1290 x 2796` pixels

**iPhone 6.5-inch (iPhone 14 Plus, 15 Plus)**
- Dimensions: `428 x 926` pixels
- Device Pixel Ratio: `3x`  
- Final screenshot: `1284 x 2778` pixels

**iPhone 5.5-inch (iPhone 8 Plus)**
- Dimensions: `414 x 736` pixels
- Device Pixel Ratio: `3x`
- Final screenshot: `1242 x 2208` pixels

**iPad 12.9-inch (iPad Pro)**
- Dimensions: `1024 x 1366` pixels
- Device Pixel Ratio: `2x`
- Final screenshot: `2048 x 2732` pixels

**Android Phone**  
- Dimensions: `360 x 640` pixels
- Device Pixel Ratio: `3x`
- Final screenshot: `1080 x 1920` pixels

**Android 7-inch Tablet**
- Dimensions: `600 x 960` pixels  
- Device Pixel Ratio: `2x`
- Final screenshot: `1200 x 1920` pixels

**Android 10-inch Tablet**
- Dimensions: `800 x 1280` pixels
- Device Pixel Ratio: `2x` 
- Final screenshot: `1600 x 2560` pixels

#### 3. Capture Screenshots for Each Page

**Page 1: Dashboard Hero** (`http://localhost:5000/`)
- Navigate to home page
- Wait for all content to load (stats cards, activity feed)
- Look for: Family statistics, recent activity, upcoming events
- Screenshot filename pattern: `dashboard-hero-[device].png`

**Page 2: Groups Overview** (`http://localhost:5000/groups`)  
- Navigate to groups page
- Wait for group cards to load
- Look for: Group listings, member counts, "Create Group" button
- Screenshot filename pattern: `groups-overview-[device].png`

**Page 3: Event Planning** (`http://localhost:5000/events`)
- Navigate to events page  
- Wait for event content to load
- Look for: Event listings, create event form, RSVPs
- Screenshot filename pattern: `event-planning-[device].png`

**Page 4: Group Chat** (`http://localhost:5000/chat`)
- Navigate to chat page
- Wait for messages to load
- Look for: Message bubbles, member avatars, input field
- Screenshot filename pattern: `group-chat-[device].png`

**Page 5: Premium Labels** (`http://localhost:5000/labels`) 
- Navigate to mailing labels page
- Wait for label interface to load  
- Look for: "Premium Feature" indicator, address list, print preview
- Screenshot filename pattern: `premium-labels-[device].png`

#### 4. Capture Process
1. Set the device dimensions as specified above
2. Navigate to the target URL
3. Wait 3-5 seconds for full page load
4. Ensure My Branches purple theme is visible
5. Right-click in the viewport → "Capture screenshot" → "Capture full size screenshot"  
6. Save with the correct filename in the appropriate folder

### File Organization

Save all screenshots in this structure:
```
app-store-assets/screenshots/
├── iphone/
│   ├── 6.7-inch/
│   ├── 6.5-inch/  
│   └── 5.5-inch/
├── ipad/
│   └── 12.9-inch/
└── android/
    ├── phone/
    ├── tablet-7/
    └── tablet-10/
```

### Quality Checklist ✅
- [ ] Screenshot shows real My Branches app content (not placeholder)
- [ ] Purple theme clearly visible
- [ ] Text is crisp and readable
- [ ] No loading spinners or error messages
- [ ] Correct dimensions (verify in image properties)
- [ ] File size under 8MB
- [ ] Proper filename with device suffix

### Device Filename Suffixes
- iPhone 6.7": `iphone67`
- iPhone 6.5": `iphone65` 
- iPhone 5.5": `iphone55`
- iPad 12.9": `ipad129`
- Android Phone: `android`
- Android 7" Tablet: `tablet7`
- Android 10" Tablet: `tablet10`

### Complete File List Needed (35 total):

**iPhone 6.7-inch (5 files):**
- dashboard-hero-iphone67.png
- groups-overview-iphone67.png  
- event-planning-iphone67.png
- group-chat-iphone67.png
- premium-labels-iphone67.png

**iPhone 6.5-inch (5 files):**
- dashboard-hero-iphone65.png
- groups-overview-iphone65.png
- event-planning-iphone65.png  
- group-chat-iphone65.png
- premium-labels-iphone65.png

**iPhone 5.5-inch (5 files):**
- dashboard-hero-iphone55.png
- groups-overview-iphone55.png
- event-planning-iphone55.png
- group-chat-iphone55.png  
- premium-labels-iphone55.png

**iPad 12.9-inch (5 files):**
- dashboard-hero-ipad129.png
- groups-overview-ipad129.png
- event-planning-ipad129.png
- group-chat-ipad129.png
- premium-labels-ipad129.png

**Android Phone (5 files):**
- dashboard-hero-android.png
- groups-overview-android.png
- event-planning-android.png  
- group-chat-android.png
- premium-labels-android.png

**Android 7-inch Tablet (5 files):**
- dashboard-hero-tablet7.png
- groups-overview-tablet7.png
- event-planning-tablet7.png
- group-chat-tablet7.png
- premium-labels-tablet7.png

**Android 10-inch Tablet (5 files):**
- dashboard-hero-tablet10.png
- groups-overview-tablet10.png
- event-planning-tablet10.png
- group-chat-tablet10.png  
- premium-labels-tablet10.png

---

## Troubleshooting

**If pages don't load properly:**
- Check that the app is running at localhost:5000
- Verify user authentication if required
- Try refreshing the page
- Check browser console for errors

**If screenshots look wrong:**
- Verify device pixel ratio is set correctly
- Ensure purple My Branches theme is active
- Check that content has fully loaded before capturing
- Verify dimensions match requirements exactly

**Time Estimate:** 45-60 minutes for all 35 screenshots
"""
    
    with open("MANUAL_SCREENSHOT_GUIDE.md", "w") as f:
        f.write(guide_content)
    
    print("✅ Created comprehensive manual guide: MANUAL_SCREENSHOT_GUIDE.md")

def main():
    """Main validation and guide creation function"""
    print("🚀 My Branches Screenshot Preparation Tool")
    print("=" * 50)
    
    # Validate all pages
    results = validate_all_pages()
    
    # Create manual guide
    print(f"\n📋 Creating comprehensive manual guide...")
    create_manual_guide()
    
    # Final recommendations
    working_pages = sum(1 for result in results.values() 
                       if result['accessible'] and result['status_code'] == 200)
    
    print(f"\n🎯 Next Steps:")
    if working_pages == len(SCREENSHOT_PAGES):
        print(f"   ✅ All {working_pages} pages validated successfully!")
        print(f"   📖 Follow the manual guide in MANUAL_SCREENSHOT_GUIDE.md")
        print(f"   ⏱️  Estimated time: 45-60 minutes for all 35 screenshots")
    else:
        print(f"   ⚠️  Only {working_pages}/{len(SCREENSHOT_PAGES)} pages accessible")
        print(f"   🔧 Fix page accessibility issues first")
        print(f"   📖 Then follow the manual guide for working pages")
    
    print(f"\n📁 Screenshots should be saved to: app-store-assets/screenshots/")
    return working_pages == len(SCREENSHOT_PAGES)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)