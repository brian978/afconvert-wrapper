import os
import shutil
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

    print(filename)
    print(subprocess.run(f'afconvert -f AIFF -d BEI16 "{file}.wav" "{file}.aiff"', shell=True, check=True))

    if os.path.isfile(output_file):
        print(f"Removing file {input_file}")
        shutil.move(input_file, config['trash']['folder'] + f'/{basename}.wav')
