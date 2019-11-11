import os
import shutil
import struct
import subprocess

import yaml

from filesystem.directory import lookup_files

with open('config.yml', 'r') as yaml_file:
    config = yaml.load(yaml_file, Loader=yaml.FullLoader)

for filename in lookup_files(config['lookup']['folder'], config['lookup']['extension']):
    file = filename[0]
    basename = filename[2]

    input_file = f'{file}.wav'
    output_file = f'{file}.aiff'

    fh = open(input_file, 'rb')
    fh.seek(34)
    bits_per_sample = struct.unpack('H', fh.read(2))[0]

    data_format = 'BEI8'
    if 16 == bits_per_sample:
        data_format = 'BEI16'
    elif 16 == bits_per_sample:
        data_format = 'BEI32'

    print(filename)
    print(subprocess.run(f'afconvert -f AIFF -d {data_format} "{file}.wav" "{file}.aiff"', shell=True, check=True))

    if os.path.isfile(output_file):
        print(f"Removing file {input_file}")
        shutil.move(input_file, config['trash']['folder'] + f'/{basename}.wav')
