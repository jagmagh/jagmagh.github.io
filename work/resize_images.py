from PIL import Image
import os

img_dir = r'D:\www.jagmagh.com\jagmagh.github.io\img'

# SA hero: resize to 1400px wide, convert PNG -> JPEG
src = os.path.join(img_dir, '2026-06-10-image1.png')
dst = os.path.join(img_dir, '2026-06-10-image1.jpg')
with Image.open(src) as img:
    w, h = img.size
    new_w = 1400
    new_h = int(h * new_w / w)
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    resized = resized.convert('RGB')
    resized.save(dst, 'JPEG', quality=85, optimize=True)
    print(f'SA hero: {w}x{h} -> {new_w}x{new_h}, {os.path.getsize(dst)//1024}KB')

# image3: resize to 1000px wide, stay PNG
src3 = os.path.join(img_dir, '2026-07-18-image3.png')
with Image.open(src3) as img:
    w, h = img.size
    new_w = 1000
    new_h = int(h * new_w / w)
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    resized.save(src3, 'PNG', optimize=True)
    print(f'image3: {w}x{h} -> {new_w}x{new_h}, {os.path.getsize(src3)//1024}KB')
