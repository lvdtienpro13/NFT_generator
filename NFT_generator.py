import os
import random
from PIL import Image

# Đường dẫn tới các thư mục/chứa ảnh
template_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/"
folder1_path = template_path + "1_HERO_MODELS"
folder2_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/2_SKILL_ICONS"
folder3_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/3_SKILL_GLOW"
folder4_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/4_ROLE_TAGS"
folder5_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/5_ELEMENT_ICONS"
folder6_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/6_CARD_FRAMES"
folder7_path = "C:/Users/KimAnh/Desktop/nft_generator/templates/7_STAR_ICONS"

bottom_shadow_overlay = Image.open(template_path+"BOTTOM_SHADOW_OVERLAY.png").convert('RGBA')

# Đường dẫn đến thư mục lưu ảnh kết quả
output_folder = 'C:/Users/KimAnh/Desktop/nft_generator/output1'
# Lặp qua tất cả các ảnh trong các thư mục
for file1 in os.listdir(folder1_path):
    for file2 in os.listdir(folder2_path):
        for file3 in os.listdir(folder3_path):
            for file4 in os.listdir(folder4_path):
                for file5 in os.listdir(folder5_path):
                    for file6 in os.listdir(folder6_path):
                        for file7 in os.listdir(folder7_path):
                            # Lấy tên của các ảnh
                            file1_name = os.path.splitext(file1)[0]
                            file2_name = os.path.splitext(file2)[0]
                            file3_name = os.path.splitext(file3)[0]
                            file4_name = os.path.splitext(file4)[0]
                            file5_name = os.path.splitext(file5)[0]
                            file6_name = os.path.splitext(file6)[0]
                            file7_name = os.path.splitext(file7)[0]

                            # Đọc 7 ảnh
                            img1 = Image.open(os.path.join(folder1_path, file1))
                            img2 = Image.open(os.path.join(folder2_path, file2))
                            img3 = Image.open(os.path.join(folder3_path, file3))
                            img4 = Image.open(os.path.join(folder4_path, file4))
                            img5 = Image.open(os.path.join(folder5_path, file5))
                            img6 = Image.open(os.path.join(folder6_path, file6))
                            img7 = Image.open(os.path.join(folder7_path, file7))

                            # Tạo ảnh mới
                            new_img = Image.new('RGBA', (img6.width, img6.height),(0,0,0,0))

                            # Chồng ảnh lên nhau
                            new_img.paste(img6, (0, 0))
                            new_img.paste(bottom_shadow_overlay, (99,1215), mask=bottom_shadow_overlay)

                            new_img.paste(img1, (0, 0), mask=img1)
                            new_img.paste(img2, (402, 1860), mask=img2)
                            new_img.paste(img3, (390, 1851), mask=img3)
                            new_img.paste(img4, (506, 141), mask=img4)
                            new_img.paste(img5, (130, 79), mask=img5)
                            new_img.paste(img7, (224, 2142,), mask=img7)

                            # Lưu ảnh với tên theo định dạng NFT_CARD
                            output_file_name = f'NFT_CARD_{file1_name}_{file2_name}_{file3_name}{file4_name}_{file5_name}{file6_name}_{file7_name}.png'
                            output_file_path = os.path.join(output_folder, output_file_name)
                            new_img.save(output_file_path)