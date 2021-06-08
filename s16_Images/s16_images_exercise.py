from PIL import Image

matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

# print(matrix.size)  # (1015, 559)
# print(mask.size)  # (505, 251)

# Should do some resize work
mask = mask.resize((1015, 559))

# Then change opacity
mask.putalpha(128)

# Paste
matrix.paste(im=mask, box=(0, 0), mask=mask)

# Show
matrix.show()
