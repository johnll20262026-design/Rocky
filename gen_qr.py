# -*- coding: utf-8 -*-
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
qr_url = "https://rocky-2qx.pages.dev/"
out_path = os.path.join(base_dir, "images", "rocky-website-qr.png")
poster_path = os.path.join(base_dir, "images", "rocky-poster.jpg")

qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=18, border=2)
qr.add_data(qr_url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="#1a1a25", back_color="white").convert("RGBA")
qw, qh = qr_img.size

data = qr_img.getdata()
new_data = []
for item in data:
    if item[0] < 50 and item[3] > 0:
        new_data.append((212, 168, 83, 255))
    else:
        new_data.append(item)
qr_img.putdata(new_data)

pad = 70
text_h = 140
cw = qw + pad * 2
ch = qh + pad * 2 + text_h
margin = 50
tw = cw + margin * 2
th = ch + margin * 2

canvas = Image.new("RGBA", (tw, th), (8, 8, 12, 255))
draw = ImageDraw.Draw(canvas)

GOLD = (212, 168, 83)
GLIGHT = (240, 200, 120)
DARK = (20, 20, 30)
WHITE = (245, 245, 247)
PINK = (255, 105, 180)
PINK_LIGHT = (255, 150, 200)

if os.path.exists(poster_path):
    try:
        poster = Image.open(poster_path).convert("RGBA")
        tr = tw / th
        br = poster.width / poster.height
        if br > tr:
            nh = poster.height
            nw = int(nh * tr)
            l = (poster.width - nw) // 2
            poster = poster.crop((l, 0, l + nw, nh))
        else:
            nw = poster.width
            nh = int(nw / tr)
            t = (poster.height - nh) // 4
            poster = poster.crop((0, t, nw, t + nh))
        poster = poster.resize((tw, th), Image.LANCZOS)
        poster = ImageEnhance.Brightness(poster).enhance(0.25)
        poster = poster.filter(ImageFilter.GaussianBlur(radius=3))
        overlay = Image.new("RGBA", (tw, th), (8, 8, 12, 210))
        poster = Image.alpha_composite(poster, overlay)
        canvas = Image.alpha_composite(canvas, poster)
        draw = ImageDraw.Draw(canvas)
    except Exception as e:
        print("bg error:", e)

cx1, cy1, cx2, cy2 = margin, margin, tw - margin, th - margin
draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=45, fill=(12, 12, 20, 250), outline=GOLD, width=6)

for i in range(5):
    a = 90 - i * 18
    draw.rounded_rectangle([cx1-6+i, cy1-6+i, cx2+6-i, cy2+6-i], radius=51+i, outline=(GLIGHT[0], GLIGHT[1], GLIGHT[2], a), width=1)

qx, qy = cx1 + pad, cy1 + pad
qp = 25
draw.rounded_rectangle([qx-qp, qy-qp, qx+qw+qp, qy+qh+qp], radius=25, fill=(255,255,255,252))

qr_pos = (qx, qy)
canvas.paste(qr_img, qr_pos, qr_img)

logo_size = 130
lx = qx + qw // 2 - logo_size // 2
ly = qy + qh // 2 - logo_size // 2
cp = 16

oring = Image.new("RGBA", (logo_size + cp*2, logo_size + cp*2), (0,0,0,0))
od = ImageDraw.Draw(oring)
od.ellipse([0, 0, logo_size+cp*2-1, logo_size+cp*2-1], fill=(255,255,255,255), outline=GOLD, width=6)
for t in range(4):
    od.ellipse([t+2, t+2, logo_size+cp*2-3-t, logo_size+cp*2-3-t], outline=(PINK[0], PINK[1], PINK[2], 120-t*25), width=1)
canvas.paste(oring, (lx-cp, ly-cp), oring)

mask = Image.new("L", (logo_size, logo_size), 0)
md = ImageDraw.Draw(mask)
md.ellipse([0, 0, logo_size-1, logo_size-1], fill=255)

logo_ok = False
if os.path.exists(poster_path):
    try:
        limg = Image.open(poster_path).convert("RGBA")
        w, h = limg.size
        min_wh = min(w, h)
        left = (w - min_wh) // 2
        top = 0
        limg = limg.crop((left, top, left + min_wh, top + min_wh))
        limg = limg.resize((logo_size, logo_size), Image.LANCZOS)
        
        lb = Image.new("RGBA", (logo_size, logo_size), (0,0,0,0))
        lbd = ImageDraw.Draw(lb)
        lbd.ellipse([3, 3, logo_size-4, logo_size-4], outline=(GOLD[0], GOLD[1], GOLD[2], 220), width=3)
        limg.paste(lb, (0,0), lb)
        
        canvas.paste(limg, (lx, ly), mask)
        logo_ok = True
    except Exception as e:
        print("logo error:", e)

if not logo_ok:
    lc = Image.new("RGBA", (logo_size, logo_size), (0,0,0,0))
    lcd = ImageDraw.Draw(lc)
    lcd.ellipse([0, 0, logo_size-1, logo_size-1], fill=DARK)
    try:
        fr = ImageFont.truetype("arialbd.ttf", 72)
    except:
        fr = ImageFont.load_default()
    bb = lcd.textbbox((0,0), "R", font=fr)
    ww = bb[2] - bb[0]
    hh = bb[3] - bb[1]
    lcd.text((logo_size//2 - ww//2 - bb[0], logo_size//2 - hh//2 - bb[1] - 4), "R", fill=GOLD, font=fr)
    canvas.paste(lc, (lx, ly), mask)

ty = cy1 + pad + qh + 35
try:
    ft = ImageFont.truetype("arialbd.ttf", 58)
    fs = ImageFont.truetype("msyh.ttc", 28)
    fu = ImageFont.truetype("arial.ttf", 18)
except:
    try:
        ft = ImageFont.truetype("arial.ttf", 58)
        fs = fu = ImageFont.truetype("arial.ttf", 24)
    except:
        ft = fs = fu = ImageFont.load_default()

title = "ROCKY"
bb = draw.textbbox((0,0), title, font=ft)
wt = bb[2] - bb[0]
for dx, dy in [(3,3),(-3,-3),(3,-3),(-3,3),(0,3),(3,0),(-3,0),(0,-3)]:
    draw.text((tw//2 - wt//2 + dx, ty+dy), title, fill=(0,0,0,180), font=ft)
draw.text((tw//2 - wt//2, ty), title, fill=PINK, font=ft)

glow = Image.new("RGBA", (tw, th), (0,0,0,0))
gd = ImageDraw.Draw(glow)
bbox_glow = gd.textbbox((0,0), title, font=ft)
gd.text((tw//2 - (bbox_glow[2]-bbox_glow[0])//2, ty), title, fill=PINK_LIGHT, font=ft)
glow = glow.filter(ImageFilter.GaussianBlur(radius=8))
canvas = Image.alpha_composite(canvas, glow)
draw = ImageDraw.Draw(canvas)
draw.text((tw//2 - wt//2, ty), title, fill=PINK, font=ft)

sub = "扫码访问个人网站"
try:
    bs = draw.textbbox((0,0), sub, font=fs)
    ws = bs[2] - bs[0]
    draw.text((tw//2 - ws//2, ty+72), sub, fill=WHITE, font=fs)
except:
    pass

utxt = "rocky-2qx.pages.dev"
try:
    bu = draw.textbbox((0,0), utxt, font=fu)
    wu = bu[2] - bu[0]
    draw.text((tw//2 - wu//2, ty+108), utxt, fill=(GLIGHT[0], GLIGHT[1], GLIGHT[2], 220), font=fu)
except:
    pass

canvas.save(out_path, "PNG", quality=95)
print("OK:", out_path)
print("Size:", round(os.path.getsize(out_path)/1024, 1), "KB")
