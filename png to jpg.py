import os
from PIL import Image


def read_directory(directory_name):
    i = 1
    for filename in os.listdir(directory_name):
        filepath = os.path.join(directory_name, filename)
        try:
            im = Image.open(filepath)
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")  # 轉換為 RGB 模式
            output_filename = os.path.join(directory_name, f"{i}.jpg")
            im.save(output_filename, "JPEG")
            # print(f"Saved: {output_filename}")
            i += 1
        except Exception as e:
            print(f"Failed to process {filename}: {e}")


file = input("請輸入資料夾路徑 (如 D:\\images): ")
read_directory(file)
# 轉換JPG
