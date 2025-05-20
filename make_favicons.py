from PIL import Image

# 1. Load your logo
im = Image.open('e14f5866-8e67-46a0-b23a-08b3917f428b.png').convert('RGBA')

# 2. Center-crop to a square (ensures no distortion)
w, h = im.size
side = min(w, h)
left = (w - side) // 2
top  = (h - side) // 2
im = im.crop((left, top, left + side, top + side))

# 3. Save a multi-size ICO file:
im.save('favicon.ico',
        format='ICO',
        sizes=[(16,16),(32,32),(48,48),(64,64)])

# 4. (Optional) Save larger PNGs for mobile/PWA:
for size in [128, 192, 256, 512]:
    im.resize((size, size), Image.LANCZOS) \
      .save(f'favicon-{size}x{size}.png')
