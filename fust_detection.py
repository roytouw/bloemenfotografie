from PIL import Image

im = Image.open('fust2.jpg')
im = im.resize((300, 300))
pix = im.load()

r = 0
g = 0
b = 0

for i in range(0, 300, 6):
    for j in range(0, 300, 6):
        r += pix[i, j][0]
        g += pix[i, j][1]
        b += pix[i, j][2]
        pix[i, j] = (255,0, 0)

brightness = (r + g + b) / 3

print(r, g, b, brightness)
im.save('fust2d.jpg')
