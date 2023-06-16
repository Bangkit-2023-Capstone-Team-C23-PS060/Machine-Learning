import os
#How many images on each class
def list_dir():
    # base_dir = r'E:\Nanda\Pekerjaan Rumah\Kuliah D3 TE Poltek\Bangkit_Academy\Capstone\data\train'
    base_dir = r'E:\path\data'

    # arduino_dir = os.path.join(base_dir, 'arduino_uno')
    # esp32_dir = os.path.join(base_dir, 'esp32')
    ic_dir = os.path.join(base_dir, 'ic')
    # ic_dir = os.path.join(base_dir, 'IC')
    resistor_dir = os.path.join(base_dir, 'resistor')
    transistor_dir = os.path.join(base_dir, 'transistor')
    capasitor_dir = os.path.join(base_dir, 'capacitor')
    # transformator_dir = os.path.join(base_dir, 'transformator')
    # inductor_dir = os.path.join(base_dir, 'inductor')
    # dioda_dir = os.path.join(base_dir, 'diode')

    # print('total training arduino images:', len(os.listdir(arduino_dir)))
    # print('total training esp32 images:', len(os.listdir(esp32_dir)))
    print('total training ic images:', len(os.listdir(ic_dir)))
    print('total training resistor images:', len(os.listdir(resistor_dir)))
    print('total training transistor images:', len(os.listdir(transistor_dir)))
    print('total training capasitor images:', len(os.listdir(capasitor_dir)))
    # print('total training transformator images:', len(os.listdir(transformator_dir)))
    # print('total training inductor images:', len(os.listdir(inductor_dir)))
    # print('total training dioda images:', len(os.listdir(dioda_dir)))

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

# capasitor_files = os.listdir(capasitor_dir)
# print(capasitor_files[:10])

# transformator_files = os.listdir(transformator_dir)
# print(transformator_files[:10])
# print(os.listdir(base_dir))


if __name__ == '__main__':
    list_dir()