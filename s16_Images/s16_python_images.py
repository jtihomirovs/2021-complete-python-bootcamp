from PIL import Image

mac = Image.open('example.jpg')
# print type
print(type(mac))
# open file in OS
# mac.show()
# print size
print(mac.size)
# print filename
print(mac.filename)
# print format description
print(mac.format_description)

# Cropping - top
pencils = Image.open('pencils.jpg')
x = 0
y = 0

w = 1950 / 3
h = 1300 / 10

pencils.crop((x, y, w, h))
pencils.show()

# Cropping bottom
x = 0
y = 1100
w = 1950 / 3
h = 1300

pencils.crop((x, y, w, h))

# Crop mac
halfway = 1993 / 2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
mac.crop((x, y, w, h))

# Copying and Pasting s16_Images
computer = mac.crop((x, y, w, h))
mac.paste(im=computer, box=(0, 0))
mac.paste(im=computer, box=(796, 0))
# mac.show()
mac.resize((3000, 50))
mac.rotate(90)
# mac.show()


red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
red.putalpha(128)
blue.putalpha(128)
red.show()
blue.show()

blue.paste(im=red, box=(0, 0), mask=red)
blue.show()
blue.save('purple.png')
