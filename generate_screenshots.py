import os
from PIL import Image, ImageDraw, ImageFont
import json

# My Branches brand colors
PURPLE = '#7c3aed'
WHITE = '#ffffff'
GRAY_100 = '#f3f4f6'
GRAY_800 = '#1f2937'
BLUE = '#3b82f6'

def create_screenshot(width, height, title, filename):
    # Create image with white background
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Try to use a reasonable font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Draw header bar with My Branches branding
    draw.rectangle([(0, 0), (width, 120)], fill=PURPLE)
    draw.text((width//2, 60), "My Branches", font=header_font, anchor="mm", fill=WHITE)
    
    # Draw main title
    draw.text((width//2, 200), title, font=title_font, anchor="mm", fill=GRAY_800)
    
    # Draw feature boxes based on the screen type
    if "dashboard" in title.lower():
        # Dashboard layout
        boxes = [
            ("👨‍👩‍👧‍👦 8 Family Members", 300),
            ("👥 3 Active Groups", 400),
            ("📅 2 Upcoming Events", 500),
            ("✅ 4 Pending Tasks", 600)
        ]
        for text, y in boxes:
            draw.rectangle([(50, y), (width-50, y+80)], fill=GRAY_100, outline=PURPLE, width=2)
            draw.text((width//2, y+40), text, font=text_font, anchor="mm", fill=GRAY_800)
            
    elif "groups" in title.lower():
        # Groups layout
        groups = [
            ("Extended Family", "12 members", 300),
            ("Summer Reunion", "8 members", 450),
            ("Weekly Dinners", "4 members", 600)
        ]
        for group_name, members, y in groups:
            draw.rectangle([(50, y), (width-50, y+100)], fill=GRAY_100, outline=PURPLE, width=2)
            draw.text((width//2, y+30), group_name, font=text_font, anchor="mm", fill=GRAY_800)
            draw.text((width//2, y+70), members, font=text_font, anchor="mm", fill=BLUE)
            
    elif "event" in title.lower():
        # Event planning layout
        draw.rectangle([(50, 350), (width-50, 550)], fill=GRAY_100, outline=PURPLE, width=3)
        draw.text((width//2, 380), "Johnson Family Reunion 2025", font=text_font, anchor="mm", fill=GRAY_800)
        draw.text((width//2, 420), "📅 July 15, 2025", font=text_font, anchor="mm", fill=BLUE)
        draw.text((width//2, 460), "📍 Riverside Park", font=text_font, anchor="mm", fill=GRAY_800)
        draw.text((width//2, 500), "✅ 12 RSVPs confirmed", font=text_font, anchor="mm", fill=PURPLE)
        
    elif "chat" in title.lower():
        # Chat layout with message bubbles
        messages = [
            ("Sarah: Can't wait to see everyone! ✈️", 350, True),
            ("Mike: What do you think of this venue?", 420, False),
            ("Mom: Perfect! Kids will love it 👨‍👩‍👧‍👦", 490, True),
            ("Dad: I'll handle catering 🍔", 560, False)
        ]
        for msg, y, is_right in messages:
            bubble_x = width - 300 if is_right else 50
            bubble_width = 250
            color = PURPLE if is_right else GRAY_100
            text_color = WHITE if is_right else GRAY_800
            draw.rounded_rectangle([(bubble_x, y), (bubble_x + bubble_width, y + 50)], 
                                 radius=15, fill=color)
            draw.text((bubble_x + bubble_width//2, y + 25), msg, font=text_font, anchor="mm", fill=text_color)
            
    elif "labels" in title.lower() or "premium" in title.lower():
        # Premium mailing labels layout
        draw.rectangle([(50, 300), (width-50, 200)], fill='#ffd700', outline=PURPLE, width=3)
        draw.text((width//2, 150), "⭐ PREMIUM FEATURE ⭐", font=header_font, anchor="mm", fill='#d97706')
        
        # Label preview
        labels = [
            "Johnson Family", "123 Oak Street", "Portland, OR 97201"
        ]
        for i, label in enumerate(labels):
            draw.rectangle([(100, 400 + i*60), (width-100, 450 + i*60)], fill=WHITE, outline=GRAY_800, width=1)
            draw.text((width//2, 425 + i*60), label, font=text_font, anchor="mm", fill=GRAY_800)
    
    # Add footer with app name
    draw.text((width//2, height-80), "Family Collaboration Made Simple", 
             font=text_font, anchor="mm", fill=GRAY_800)
    
    # Save image
    img.save(filename, 'PNG')
    print(f"Created {filename} ({width}x{height})")

# Screenshot specifications
screenshots = [
    # iPhone screenshots
    {"width": 1290, "height": 2796, "title": "Family Dashboard", "path": "app-store-assets/screenshots/iphone/6.7-inch/dashboard-hero-iphone67.png"},
    {"width": 1290, "height": 2796, "title": "Groups Overview", "path": "app-store-assets/screenshots/iphone/6.7-inch/groups-overview-iphone67.png"},
    {"width": 1290, "height": 2796, "title": "Event Planning", "path": "app-store-assets/screenshots/iphone/6.7-inch/event-planning-iphone67.png"},
    {"width": 1290, "height": 2796, "title": "Group Chat", "path": "app-store-assets/screenshots/iphone/6.7-inch/group-chat-iphone67.png"},
    {"width": 1290, "height": 2796, "title": "Premium Labels", "path": "app-store-assets/screenshots/iphone/6.7-inch/premium-labels-iphone67.png"},
    
    # iPhone 6.5"
    {"width": 1284, "height": 2778, "title": "Family Dashboard", "path": "app-store-assets/screenshots/iphone/6.5-inch/dashboard-hero-iphone65.png"},
    {"width": 1284, "height": 2778, "title": "Groups Overview", "path": "app-store-assets/screenshots/iphone/6.5-inch/groups-overview-iphone65.png"},
    
    # iPhone 5.5"
    {"width": 1242, "height": 2208, "title": "Family Dashboard", "path": "app-store-assets/screenshots/iphone/5.5-inch/dashboard-hero-iphone55.png"},
    {"width": 1242, "height": 2208, "title": "Groups Overview", "path": "app-store-assets/screenshots/iphone/5.5-inch/groups-overview-iphone55.png"},
    
    # iPad screenshots
    {"width": 2048, "height": 2732, "title": "Family Dashboard", "path": "app-store-assets/screenshots/ipad/12.9-inch/dashboard-hero-ipad129.png"},
    {"width": 2048, "height": 2732, "title": "Event Planning", "path": "app-store-assets/screenshots/ipad/12.9-inch/event-planning-ipad129.png"},
    
    # Android screenshots
    {"width": 1080, "height": 1920, "title": "Family Dashboard", "path": "app-store-assets/screenshots/android/phone/dashboard-hero-android.png"},
    {"width": 1080, "height": 1920, "title": "Groups Overview", "path": "app-store-assets/screenshots/android/phone/groups-overview-android.png"},
    {"width": 1200, "height": 1920, "title": "Family Dashboard", "path": "app-store-assets/screenshots/android/tablet-7/dashboard-hero-tablet7.png"},
]

# Generate all screenshots
for screenshot in screenshots:
    create_screenshot(screenshot["width"], screenshot["height"], screenshot["title"], screenshot["path"])

print("All screenshots generated successfully!")
