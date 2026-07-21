import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

qr_url = "https://rocky-2qx.pages.dev/"
output_path = os.path.join(os.path.dirname(__file__), "images", "rocky-website-qr.png")
photo_path = os.path.join(os.path.dirname(__file__), "images", "photo4.jpg")

bg_img = None
if os.path.exists(photo_path):
    try:
        bg_img = Image.open(photo_path).convert("RGBA")
    except:
        bg_img = None

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=16,
    border=2,
)
qr.add_data(qr_url)
qr.make(fit=True)

qr_pil = qr.make_image(fill_color="#d4a853", back_color="white").convert("RGBA")
qr_w, qr_h = qr_pil.size

card_padding = 60
text_area_h = 120
card_w = qr_w + card_padding * 2
card_h = qr_h + card_padding * 2 + text_area_h

outer_margin = 40
total_w = card_w + outer_margin * 2
total_h = card_h + outer_margin * 2

canvas = Image.new("RGBA", (total_w, total_h), (10, 10, 15, 255))
draw = ImageDraw.Draw(canvas)

gold = (212, 168, 83)
gold_light = (240, 200, 120)
dark_bg = (20, 20, 30)
white = (245, 245, 247)

if bg_img:
    bg_crop = bg_img.copy()
    target_ratio = total_w / total_h
    bg_ratio = bg_crop.width / bg_crop.height
    if bg_ratio > target_ratio:
        new_h = bg_crop.height
        new_w = int(new_h * target_ratio)
        left = (bg_crop.width - new_w) // 2
        bg_crop = bg_crop.crop((left, 0, left + new_w, new_h))
    else:
        new_w = bg_crop.width
        new_h = int(new_w / target_ratio)
        top = (bg_crop.height - new_h) // 3
        bg_crop = bg_crop.crop((0, top, new_w, top + new_h))
    bg_crop = bg_crop.resize((total_w, total_h), Image.LANCZOS)
    enhancer = ImageEnhance.Brightness(bg_crop)
    bg_crop = enhancer.enhance(0.25)
    overlay = Image.new("RGBA", (total_w, total_h), (10, 10, 15, 200))
    bg_crop = Image.alpha_composite(bg_crop, overlay)
    canvas = Image.alpha_composite(canvas, bg_crop)
    draw = ImageDraw.Draw(canvas)

card_x1 = outer_margin
card_y1 = outer_margin
card_x2 = total_w - outer_margin
card_y2 = total_h - outer_margin
draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=40, fill=(20, 20, 30, 240), outline=gold, width=5)

for i in range(3):
    alpha = 80 - i * 25
    draw.rounded_rectangle([card_x1 - 4 + i, card_y1 - 4 + i, card_x2 + 4 - i, card_y2 + 4 - i], 
                           radius=42 + i, outline=(*gold, alpha), width=1)

qr_x = card_x1 + card_padding
qr_y = card_y1 + card_padding

qr_bg_padding = 20
draw.rounded_rectangle([qr_x - qr_bg_padding, qr_y - qr_bg_padding, 
                        qr_x + qr_w + qr_bg_padding, qr_y + qr_h + qr_bg_padding],
                       radius=20, fill=(255, 255, 255, 245))

canvas.paste(qr_pil, (qr_x, qr_y), qr_pil)

logo_size = 90
logo_x = qr_x + qr_w//2 - logo_size//2
logo_y = qr_y + qr_h//2 - logo_size//2

circle_padding = 12
draw.ellipse([logo_x - circle_padding, logo_y - circle_padding, 
              logo_x + logo_size + circle_padding, logo_y + logo_size + circle_padding], 
             fill=(255, 255, 255, 255), outline=gold, width=4)
draw.ellipse([logo_x, logo_y, logo_x + logo_size, logo_y + logo_size], fill=dark_bg)

try:
    font_r = ImageFont.truetype("arialbd.ttf", 52)
except:
    try:
        font_r = ImageFont.truetype("arial.ttf", 52)
    except:
        font_r = ImageFont.load_default()
bbox = draw.textbbox((0, 0), "R", font=font_r)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text((logo_x + logo_size//2 - tw//2 - bbox[0], logo_y + logo_size//2 - th//2 - bbox[1] - 3), 
          "R", fill=gold, font=font_r)

text_y = card_y1 + card_padding + qr_h + 25
try:
    font_title = ImageFont.truetype("arialbd.ttf", 48)
    font_sub = ImageFont.truetype("msyh.ttc", 26)
except:
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_sub = ImageFont.truetype("arial.ttf", 26)
    except:
        font_title = font_sub = ImageFont.load_default()

title = "ROCKY"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
for dx, dy in [(1,1), (-1,-1), (1,-1), (-1,1)]:
    draw.text((total_w//2 - tw//2 + dx, text_y + dy), title, fill=(0,0,0,180), font=font_title)
draw.text((total_w//2 - tw//2, text_y), title, fill=gold_light, font=font_title)

subtitle = "扫码访问个人网站"
try:
    bbox_s = draw.textbbox((0, 0), subtitle, font=font_sub)
    tw_s = bbox_s[2] - bbox_s[0]
    draw.text((total_w//2 - tw_s//2, text_y + 62), subtitle, fill=white, font=font_sub)
except:
    pass

url_text = "rocky-2qx.pages.dev"
try:
    font_url = ImageFont.truetype("arial.ttf", 18)
    bbox_u = draw.textbbox((0, 0), url_text, font=font_url)
    tw_u = bbox_u[2] - bbox_u[0]
    draw.text((total_w//2 - tw_u//2, text_y + 92), url_text, fill=(*gold, 180), font=font_url)
except:
    pass

canvas.save(output_path, "PNG", quality=95)
print(f"二维码已保存到: {output_path}")
print(f"文件大小: {os.path.getsize(output_path) / 1024:.1f} KB")
