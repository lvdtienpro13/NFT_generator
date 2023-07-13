from PIL import Image

# Đường dẫn tới file ảnh
image_path = 'C:/Users/KimAnh/Desktop/nft_generator/templates/BOTTOM_SHADOW_OVERLAY.png'

# Đọc ảnh
image = Image.open(image_path)

# Lấy kích thước của ảnh
width, height = image.size

# In kích thước của ảnh
print(f'Kích thước của ảnh: {width} x {height}')

#6: 1350 x 2400