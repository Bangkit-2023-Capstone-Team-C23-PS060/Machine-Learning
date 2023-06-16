import os

base_dir = 'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\Capstone\data\train'

arduino_dir = os.path.join(base_dir, 'arduino_uno')
esp32_dir = os.path.join(base_dir, 'esp32')
ic_dir = os.path.join(base_dir, 'ic')
resistor_dir = os.path.join(base_dir, 'resistor')
transistor_dir = os.path.join(base_dir, 'transistor')
capasitor_dir = os.path.join(base_dir, 'capasitor')

print('total training arduino images:', len(os.listdir(arduino_dir)))
print('total training esp32 images:', len(os.listdir(esp32_dir)))
print('total training ic images:', len(os.listdir(ic_dir)))
print('total training resistor images:', len(os.listdir(resistor_dir)))
print('total training transistor images:', len(os.listdir(transistor_dir)))
print('total training capasitor images:', len(os.listdir(capasitor_dir)))
# arduino_files = os.listdir(arduino_dir)
# print(arduino_files[:10])

# esp32_files = os.listdir(esp32_dir)
# print(esp32_files[:10])

# ic_files = os.listdir(ic_dir)
# print(ic_files[:10])

# resistor_files = os.listdir(resistor_dir)
# print(resistor_files[:10])

# transistor_files = os.listdir(transistor_dir)
# print(transistor_files[:10])
# # print(os.listdir(base_dir))


# %matplotlib inline

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# pic_index = 2

# next_arduino = [os.path.join(arduino_dir, fname) 
#                 for fname in arduino_files[pic_index-2:pic_index]]
# next_esp32 = [os.path.join(esp32_dir, fname) 
#                 for fname in esp32_files[pic_index-2:pic_index]]
# next_ic = [os.path.join(ic_dir, fname) 
#                 for fname in ic_files[pic_index-2:pic_index]]
# next_resistor = [os.path.join(resistor_dir, fname) 
#                 for fname in resistor_files[pic_index-2:pic_index]]
# next_transistor = [os.path.join(transistor_dir, fname) 
#                 for fname in transistor_files[pic_index-2:pic_index]]
# for i, img_path in enumerate(next_arduino + next_esp32 + next_ic next_resistor + next_transistor):
#   img = mpimg.imread(img_path)
#   plt.imshow(img)
#   plt.axis('Off')
#   plt.show()