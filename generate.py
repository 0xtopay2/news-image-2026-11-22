from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1024, 1024
BG_COLOR = '#FDFBF7' # warm newsprint background
TEXT_COLOR = '#111111'
ACCENT_COLOR = '#8B0000' # dark red
NAVY_COLOR = '#000080'

FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

img = Image.new('RGB', (WIDTH, HEIGHT), color=BG_COLOR)
draw = ImageDraw.Draw(img)

# Fonts
font_masthead = ImageFont.truetype(FONT_BOLD, 68)
font_date = ImageFont.truetype(FONT_REG, 24)
font_kicker = ImageFont.truetype(FONT_BOLD, 18)
font_head = ImageFont.truetype(FONT_BOLD, 34)
font_sub = ImageFont.truetype(FONT_REG, 22)
font_footer = ImageFont.truetype(FONT_REG, 24)

# Masthead (y 0-170)
draw.text((WIDTH//2, 60), "WORLD CHRONICLE", fill=TEXT_COLOR, font=font_masthead, anchor='mm')
draw.text((WIDTH//2, 120), "Sunday, 22 November 2026  •  Global Edition  •  Daily Briefing", fill=TEXT_COLOR, font=font_date, anchor='mm')
draw.line([(50, 155), (WIDTH-50, 155)], fill=TEXT_COLOR, width=3)

# Tiles Data: 2 columns x 3 rows
# Left x=50, right x=545, tile inner width 430
# Starting y=210, each row 240px tall
tiles = [
    ("MEXICO", "Cartel boss 'El Chapo Isidro' captured", "Sinaloa raid arrests Beltran Leyva leader; 11 killed", "badge"),
    ("GULF", "Iran-US clash claims over Gulf waters", "Iran says missile damaged US F-16; US denies", "jet"),
    ("USA", "Democrats sweep House in historic win", "At least 258 seats, largest since 1992", "dome"),
    ("LIBYA", "Russian warship sinks in Benghazi port", "Suspected Ukrainian drone attack", "ship"),
    ("INDONESIA", "Factory fire kills 3, dozens missing", "Confectionery plant blaze", "flame"),
    ("SOUTH KOREA", "Minister quits in AI exam-cheating scandal", "University tests engulfed", "cap")
]

def wrap_text(draw, text, font, max_width, max_lines=2):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if draw.textlength(test_line, font=font) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines[:max_lines]

def draw_icon(draw, icon_type, x, y):
    # icon area box: x to x+55, y to y+70
    cx, cy = x + 27, y + 35
    if icon_type == "flame":
        # Flame icon in dark red
        draw.polygon([(cx, cy-25), (cx+18, cy+20), (cx-18, cy+20)], fill=ACCENT_COLOR)
        draw.polygon([(cx, cy-10), (cx+10, cy+15), (cx-10, cy+15)], fill=BG_COLOR)
    elif icon_type == "ship":
        # Ship hull + wave
        draw.polygon([(cx-22, cy+5), (cx+22, cy+5), (cx+16, cy+22), (cx-16, cy+22)], fill=NAVY_COLOR)
        draw.arc([cx-25, cy+15, cx+25, cy+30], 0, 180, fill=NAVY_COLOR, width=3)
    elif icon_type == "jet":
        # Jet triangle with wings
        draw.polygon([(cx, cy-20), (cx+15, cy+20), (cx-15, cy+20)], fill=NAVY_COLOR)
        draw.polygon([(cx-22, cy+10), (cx, cy+5), (cx+22, cy+10), (cx, cy+20)], fill=NAVY_COLOR)
    elif icon_type == "dome":
        # Capitol dome
        draw.arc([cx-16, cy-15, cx+16, cy+15], 180, 0, fill=NAVY_COLOR, width=3)
        draw.rectangle([cx-18, cy+15, cx+18, cy+22], fill=NAVY_COLOR)
        draw.rectangle([cx-12, cy+22, cx+12, cy+25], fill=NAVY_COLOR)
    elif icon_type == "badge":
        # Star badge
        draw.ellipse([cx-20, cy-20, cx+20, cy+20], outline=ACCENT_COLOR, width=3)
        # draw a small star/cross inside
        draw.line([cx, cy-12, cx, cy+12], fill=ACCENT_COLOR, width=3)
        draw.line([cx-12, cy, cx+12, cy], fill=ACCENT_COLOR, width=3)
    elif icon_type == "cap":
        # Graduation cap
        draw.polygon([(cx, cy-18), (cx+24, cy-5), (cx, cy+8), (cx-24, cy-5)], fill=NAVY_COLOR)
        draw.rectangle([cx-8, cy+6, cx+8, cy+18], fill=NAVY_COLOR)

col_coords = [50, 545]
row_y = [210, 450, 690]
tile_w = 430
tile_h = 240

for i, (kicker, head, sub, icon) in enumerate(tiles):
    c = i % 2
    r = i // 2
    x = col_coords[c]
    y = row_y[r]
    
    # Draw icon in left area (x to x+60)
    draw_icon(draw, icon, x, y + 10)
    
    # Text area starts at x + 65
    text_x = x + 65
    text_w = tile_w - 65
    
    # Kicker
    draw.text((text_x, y + 8), kicker, fill=ACCENT_COLOR, font=font_kicker)
    
    # Headline (max 2 lines, max_width = text_w)
    head_lines = wrap_text(draw, head, font_head, text_w, max_lines=2)
    current_y = y + 32
    for line in head_lines:
        draw.text((text_x, current_y), line, fill=TEXT_COLOR, font=font_head)
        current_y += 38
        
    # Subhead (max 2 lines)
    sub_lines = wrap_text(draw, sub, font_sub, text_w, max_lines=2)
    current_y += 2
    for line in sub_lines:
        draw.text((text_x, current_y), line, fill='#444444', font=font_sub)
        current_y += 26
        
    # Thin rule line between rows (except last row bottom)
    if r < 2:
        draw.line([(50, y + tile_h + 5), (WIDTH - 50, y + tile_h + 5)], fill='#D0D0D0', width=1)

# Footer (single centered line, DejaVuSans 24, within 974px)
footer_text = "Climate talks break down | UNIFIL hands over Lebanon posts | Leeds 4-1 Chelsea"
draw.line([(50, HEIGHT - 70), (WIDTH - 50, HEIGHT - 70)], fill=TEXT_COLOR, width=2)
draw.text((WIDTH // 2, HEIGHT - 35), footer_text, fill=TEXT_COLOR, font=font_footer, anchor='mm')

img.save('entry.png', 'PNG', optimize=True)
