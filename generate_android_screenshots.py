#!/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont
import math

# My Branches brand colors (from index.css)
PRIMARY_BLUE = '#4f8ef7'  # hsl(217, 91%, 60%)
PURPLE_BG = '#a78bfa'     # hsl(260.87, 37.3%, 63.73%)  
WHITE = '#ffffff'
GRAY_100 = '#f3f4f6'
GRAY_800 = '#1f2937'
GRAY_600 = '#4b5563'
GREEN = '#10b981'
ORANGE = '#f59e0b'
RED = '#ef4444'

def get_font(size):
    """Get font with fallback to default"""
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except:
        return ImageFont.load_default()

def get_regular_font(size):
    """Get regular font with fallback to default"""
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def draw_header(draw, width, title="My Branches"):
    """Draw the app header bar"""
    # Header background
    draw.rectangle([(0, 0), (width, 120)], fill=PRIMARY_BLUE)
    
    # App title
    header_font = get_font(min(40, width // 20))
    draw.text((width//2, 60), title, font=header_font, anchor="mm", fill=WHITE)

def draw_card(draw, x, y, width, height, title, value, icon="", border_color=GRAY_100):
    """Draw a stats card"""
    # Card background
    draw.rounded_rectangle([(x, y), (x + width, y + height)], radius=12, fill=WHITE, outline=border_color, width=2)
    
    # Card content
    title_font = get_regular_font(24)
    value_font = get_font(36)
    
    # Icon (if provided)
    if icon:
        icon_font = get_font(32)
        draw.text((x + width - 40, y + 30), icon, font=icon_font, anchor="mm", fill=PRIMARY_BLUE)
    
    # Title and value
    draw.text((x + 20, y + 25), title, font=title_font, anchor="lm", fill=GRAY_600)
    draw.text((x + 20, y + height - 35), value, font=value_font, anchor="lm", fill=GRAY_800)

def create_dashboard_screenshot(width, height, filename):
    """Create family dashboard screenshot"""
    img = Image.new('RGB', (width, height), GRAY_100)
    draw = ImageDraw.Draw(img)
    
    # Header
    draw_header(draw, width, "My Branches")
    
    # Welcome text
    welcome_font = get_font(min(48, width // 15))
    subtitle_font = get_regular_font(min(32, width // 25))
    
    draw.text((width//2, 180), "Welcome back!", font=welcome_font, anchor="mm", fill=GRAY_800)
    draw.text((width//2, 220), "Here's what's happening in your family network", font=subtitle_font, anchor="mm", fill=GRAY_600)
    
    # Stats cards
    card_width = (width - 60) // 2
    card_height = 120
    start_y = 280
    
    # Row 1
    draw_card(draw, 20, start_y, card_width, card_height, "Family Members", "8", "👨‍👩‍👧‍👦")
    draw_card(draw, 40 + card_width, start_y, card_width, card_height, "Active Groups", "3", "👥")
    
    # Row 2
    draw_card(draw, 20, start_y + 140, card_width, card_height, "Upcoming Events", "2", "📅")
    draw_card(draw, 40 + card_width, start_y + 140, card_width, card_height, "Pending Tasks", "4", "✅")
    
    # Upcoming Birthdays section
    section_y = start_y + 300
    section_font = get_font(min(36, width // 18))
    draw.text((30, section_y), "🎁 Upcoming Birthdays", font=section_font, anchor="lm", fill=GRAY_800)
    
    # Birthday card
    bday_y = section_y + 60
    draw.rounded_rectangle([(30, bday_y), (width - 30, bday_y + 80)], radius=8, fill=WHITE, outline=ORANGE, width=2)
    
    name_font = get_font(28)
    date_font = get_regular_font(24)
    draw.text((50, bday_y + 25), "Emma Johnson", font=name_font, anchor="lm", fill=GRAY_800)
    draw.text((50, bday_y + 55), "July 25th", font=date_font, anchor="lm", fill=GRAY_600)
    draw.text((width - 50, bday_y + 40), "3 days", font=name_font, anchor="rm", fill=ORANGE)
    
    # Recent Activity section
    activity_y = bday_y + 120
    draw.text((30, activity_y), "🕐 Recent Activity", font=section_font, anchor="lm", fill=GRAY_800)
    
    # Activity items
    activities = [
        "Sarah shared photos in Summer Planning",
        "Mike created BBQ event for next weekend", 
        "Mom added reunion tasks"
    ]
    
    for i, activity in enumerate(activities):
        item_y = activity_y + 60 + (i * 60)
        draw.rounded_rectangle([(30, item_y), (width - 30, item_y + 50)], radius=6, fill=WHITE)
        activity_font = get_regular_font(22)
        draw.text((50, item_y + 25), activity, font=activity_font, anchor="lm", fill=GRAY_800)
    
    img.save(filename, 'PNG')
    print(f"✅ Created dashboard screenshot: {filename}")

def create_groups_screenshot(width, height, filename):
    """Create groups overview screenshot"""
    img = Image.new('RGB', (width, height), GRAY_100)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, width, "Family Groups")
    
    # Page title
    title_font = get_font(min(42, width // 16))
    draw.text((30, 160), "Your Family Groups", font=title_font, anchor="lm", fill=GRAY_800)
    
    groups = [
        ("Extended Family", "12 members", "Plan family reunions and gatherings", PRIMARY_BLUE),
        ("Summer Reunion", "8 members", "Organizing the 2025 family reunion", GREEN),  
        ("Weekly Dinners", "4 members", "Weekly dinner coordination", ORANGE),
        ("Holiday Planning", "6 members", "Coordinate holiday celebrations", RED)
    ]
    
    card_height = 140
    start_y = 220
    
    for i, (name, members, desc, color) in enumerate(groups):
        y = start_y + (i * (card_height + 20))
        
        # Group card
        draw.rounded_rectangle([(30, y), (width - 30, y + card_height)], radius=12, fill=WHITE, outline=color, width=3)
        
        # Group content
        name_font = get_font(32)
        members_font = get_regular_font(24)
        desc_font = get_regular_font(20)
        
        draw.text((50, y + 30), name, font=name_font, anchor="lm", fill=GRAY_800)
        draw.text((50, y + 70), members, font=members_font, anchor="lm", fill=color)
        draw.text((50, y + 100), desc, font=desc_font, anchor="lm", fill=GRAY_600)
        
        # Join button
        btn_x = width - 120
        draw.rounded_rectangle([(btn_x, y + 25), (btn_x + 80, y + 60)], radius=6, fill=color)
        btn_font = get_regular_font(18)
        draw.text((btn_x + 40, y + 42), "View", font=btn_font, anchor="mm", fill=WHITE)
    
    # Create new group button
    new_y = start_y + (len(groups) * (card_height + 20))
    draw.rounded_rectangle([(30, new_y), (width - 30, new_y + 80)], radius=12, fill=PRIMARY_BLUE, outline=PRIMARY_BLUE, width=2)
    new_font = get_font(28)
    draw.text((width//2, new_y + 40), "+ Create New Group", font=new_font, anchor="mm", fill=WHITE)
    
    img.save(filename, 'PNG')
    print(f"✅ Created groups screenshot: {filename}")

def create_events_screenshot(width, height, filename):
    """Create event planning screenshot"""
    img = Image.new('RGB', (width, height), GRAY_100)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, width, "Event Planning")
    
    # Page title
    title_font = get_font(min(42, width // 16))
    draw.text((30, 160), "Johnson Family Reunion 2025", font=title_font, anchor="lm", fill=GRAY_800)
    
    # Event details card
    card_y = 220
    card_height = 300
    draw.rounded_rectangle([(30, card_y), (width - 30, card_y + card_height)], radius=15, fill=WHITE, outline=PRIMARY_BLUE, width=3)
    
    # Event info
    detail_font = get_font(28)
    label_font = get_regular_font(24)
    
    details = [
        ("📅", "Date", "July 15, 2025"),
        ("📍", "Location", "Riverside Park"),
        ("👥", "RSVPs", "12 confirmed, 3 pending"),
        ("💰", "Budget", "$2,500 / $3,000")
    ]
    
    for i, (icon, label, value) in enumerate(details):
        y = card_y + 40 + (i * 60)
        draw.text((50, y), icon, font=detail_font, anchor="lm", fill=PRIMARY_BLUE)
        draw.text((90, y), label, font=label_font, anchor="lm", fill=GRAY_600)
        draw.text((200, y), value, font=detail_font, anchor="lm", fill=GRAY_800)
    
    # Tasks section
    tasks_y = card_y + card_height + 40
    draw.text((30, tasks_y), "Event Tasks", font=title_font, anchor="lm", fill=GRAY_800)
    
    tasks = [
        ("Book catering", "Dad", True),
        ("Send invitations", "Sarah", True), 
        ("Reserve pavilion", "Mike", False),
        ("Plan activities", "Mom", False)
    ]
    
    for i, (task, person, done) in enumerate(tasks):
        task_y = tasks_y + 60 + (i * 50)
        
        # Task item
        task_bg = GREEN if done else WHITE
        task_border = GREEN if done else GRAY_100
        draw.rounded_rectangle([(30, task_y), (width - 30, task_y + 40)], radius=6, fill=task_bg, outline=task_border, width=2)
        
        # Checkbox
        check_color = WHITE if done else GRAY_600
        draw.text((45, task_y + 20), "✓" if done else "○", font=label_font, anchor="mm", fill=check_color)
        
        # Task text
        task_color = WHITE if done else GRAY_800
        person_color = WHITE if done else GRAY_600
        draw.text((75, task_y + 12), task, font=label_font, anchor="lm", fill=task_color)
        draw.text((75, task_y + 32), f"Assigned to {person}", font=get_regular_font(18), anchor="lm", fill=person_color)
    
    img.save(filename, 'PNG')
    print(f"✅ Created events screenshot: {filename}")

def create_chat_screenshot(width, height, filename):
    """Create group chat screenshot"""
    img = Image.new('RGB', (width, height), GRAY_100)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, width, "Summer Reunion Planning")
    
    # Chat messages
    messages = [
        ("Sarah", "Can't wait to see everyone! Just booked our flights ✈️", False, "2 hours ago"),
        ("You", "That's awesome! I'm working on the venue details", True, "1 hour ago"),
        ("Mike", "What do you think of this venue? *Photo*", False, "45 min ago"),
        ("Mom", "Perfect! The kids will love the playground nearby 👨‍👩‍👧‍👦", False, "30 min ago"),
        ("Dad", "I'll handle the catering arrangements 🍔", False, "15 min ago"),
        ("You", "Sounds great! Let me know if you need the guest count", True, "5 min ago")
    ]
    
    start_y = 150
    msg_font = get_regular_font(22)
    name_font = get_font(20)
    time_font = get_regular_font(16)
    
    for i, (sender, text, is_sent, time) in enumerate(messages):
        msg_y = start_y + (i * 90)
        
        # Message bubble
        bubble_width = min(width - 120, len(text) * 12 + 40)
        bubble_x = width - bubble_width - 30 if is_sent else 30
        
        bubble_color = PRIMARY_BLUE if is_sent else WHITE
        text_color = WHITE if is_sent else GRAY_800
        
        draw.rounded_rectangle([(bubble_x, msg_y), (bubble_x + bubble_width, msg_y + 60)], 
                             radius=15, fill=bubble_color, outline=bubble_color if is_sent else GRAY_100, width=1)
        
        # Sender name (for received messages)
        if not is_sent:
            draw.text((bubble_x + 15, msg_y - 25), sender, font=name_font, anchor="lm", fill=GRAY_600)
        
        # Message text
        draw.text((bubble_x + 15, msg_y + 30), text, font=msg_font, anchor="lm", fill=text_color)
        
        # Timestamp
        time_x = bubble_x + bubble_width - 10 if is_sent else bubble_x + bubble_width + 10
        draw.text((time_x, msg_y + 70), time, font=time_font, anchor="rm" if is_sent else "lm", fill=GRAY_600)
    
    # Message input at bottom
    input_y = height - 100
    draw.rounded_rectangle([(30, input_y), (width - 30, input_y + 60)], radius=25, fill=WHITE, outline=GRAY_100, width=2)
    
    input_font = get_regular_font(20)
    draw.text((50, input_y + 30), "Type a message...", font=input_font, anchor="lm", fill=GRAY_600)
    
    # Send button
    send_x = width - 80
    draw.rounded_rectangle([(send_x, input_y + 10), (send_x + 40, input_y + 50)], radius=20, fill=PRIMARY_BLUE)
    draw.text((send_x + 20, input_y + 30), "→", font=get_font(24), anchor="mm", fill=WHITE)
    
    img.save(filename, 'PNG')
    print(f"✅ Created chat screenshot: {filename}")

def create_premium_labels_screenshot(width, height, filename):
    """Create premium mailing labels screenshot"""
    img = Image.new('RGB', (width, height), GRAY_100)
    draw = ImageDraw.Draw(img)
    
    draw_header(draw, width, "Mailing Labels")
    
    # Premium badge
    badge_y = 140
    draw.rounded_rectangle([(30, badge_y), (width - 30, badge_y + 60)], radius=8, fill='#ffd700', outline='#f59e0b', width=2)
    badge_font = get_font(min(32, width // 20))
    draw.text((width//2, badge_y + 30), "⭐ PREMIUM FEATURE ⭐", font=badge_font, anchor="mm", fill='#d97706')
    
    # Description
    desc_y = badge_y + 80
    desc_font = get_regular_font(24)
    draw.text((width//2, desc_y), "Generate professional Avery 5160 mailing labels", font=desc_font, anchor="mm", fill=GRAY_600)
    draw.text((width//2, desc_y + 30), "Perfect for holiday cards and family events", font=desc_font, anchor="mm", fill=GRAY_600)
    
    # Label preview section
    preview_y = desc_y + 80
    preview_font = get_font(min(36, width // 18))
    draw.text((30, preview_y), "Label Preview:", font=preview_font, anchor="lm", fill=GRAY_800)
    
    # Sample labels
    labels = [
        ("Mike & Sarah Johnson", "123 Oak Street", "Portland, OR 97201"),
        ("Pat Johnson (Grandparent)", "456 Pine Avenue", "Seattle, WA 98101"),
        ("Chris & Alex Miller", "789 Maple Drive", "Vancouver, WA 98661"),
        ("The Williams Family", "321 Cedar Lane", "Beaverton, OR 97005")
    ]
    
    label_width = (width - 60) // 2
    label_height = 100
    
    for i, (name, street, city) in enumerate(labels):
        row = i // 2
        col = i % 2
        
        x = 30 + col * (label_width + 30)
        y = preview_y + 60 + row * (label_height + 20)
        
        # Label background
        draw.rounded_rectangle([(x, y), (x + label_width, y + label_height)], radius=6, fill=WHITE, outline=GRAY_800, width=1)
        
        # Label text
        name_font = get_font(20)
        addr_font = get_regular_font(16)
        
        draw.text((x + 10, y + 15), name, font=name_font, anchor="lm", fill=GRAY_800)
        draw.text((x + 10, y + 40), street, font=addr_font, anchor="lm", fill=GRAY_600)
        draw.text((x + 10, y + 65), city, font=addr_font, anchor="lm", fill=GRAY_600)
    
    # Export buttons
    btn_y = preview_y + 60 + 2 * (label_height + 20) + 40
    btn_width = (width - 90) // 2
    
    # Download PDF button
    draw.rounded_rectangle([(30, btn_y), (30 + btn_width, btn_y + 50)], radius=8, fill=PRIMARY_BLUE)
    btn_font = get_font(24)
    draw.text((30 + btn_width//2, btn_y + 25), "📄 Download PDF", font=btn_font, anchor="mm", fill=WHITE)
    
    # Print button
    draw.rounded_rectangle([(60 + btn_width, btn_y), (60 + 2*btn_width, btn_y + 50)], radius=8, fill=GREEN)
    draw.text((60 + btn_width + btn_width//2, btn_y + 25), "🖨️ Print Labels", font=btn_font, anchor="mm", fill=WHITE)
    
    img.save(filename, 'PNG')
    print(f"✅ Created premium labels screenshot: {filename}")

def generate_android_screenshots():
    """Generate all Android screenshots for Google Play Store"""
    
    # Android device configurations
    configs = [
        {
            "name": "Android Phone",
            "width": 1080,
            "height": 1920,
            "folder": "app-store-assets/screenshots/android/phone/"
        },
        {
            "name": "Android 7-inch Tablet", 
            "width": 1200,
            "height": 1920,
            "folder": "app-store-assets/screenshots/android/tablet-7/"
        },
        {
            "name": "Android 10-inch Tablet",
            "width": 1600, 
            "height": 2560,
            "folder": "app-store-assets/screenshots/android/tablet-10/"
        }
    ]
    
    # Screenshot functions
    screenshots = [
        ("dashboard-hero", create_dashboard_screenshot),
        ("groups-overview", create_groups_screenshot), 
        ("event-planning", create_events_screenshot),
        ("group-chat", create_chat_screenshot),
        ("premium-labels", create_premium_labels_screenshot)
    ]
    
    print("🚀 Generating Android Screenshots for Google Play Store")
    print("=" * 60)
    
    total_generated = 0
    
    for config in configs:
        print(f"\n📱 Generating {config['name']} screenshots ({config['width']}x{config['height']})")
        
        # Create directory
        os.makedirs(config["folder"], exist_ok=True)
        
        for screenshot_name, screenshot_func in screenshots:
            # Generate device-specific filename
            device_suffix = config["name"].lower().replace(" ", "").replace("-", "")
            if "phone" in device_suffix:
                device_suffix = "android"
            elif "7inch" in device_suffix:
                device_suffix = "tablet7"
            elif "10inch" in device_suffix:
                device_suffix = "tablet10"
                
            filename = f"{config['folder']}{screenshot_name}-{device_suffix}.png"
            
            # Generate screenshot
            screenshot_func(config["width"], config["height"], filename)
            total_generated += 1
    
    print(f"\n🎉 Successfully generated {total_generated} Android screenshots!")
    print("📂 Screenshots saved in app-store-assets/screenshots/android/")
    print("\n✅ Ready for Google Play Store upload!")

if __name__ == "__main__":
    generate_android_screenshots()