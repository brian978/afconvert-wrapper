import os


def lookup_files(directory: str, extension: str):
    paths = os.listdir(directory)
    for path in paths:
        full_path = os.path.join(directory, path)
        if os.path.isdir(full_path):
            yield from lookup_files(full_path, extension)
        else:
            file = full_path.split('.')
            ext = str(file[-1:][0])
            if ext.lower() == extension.lower():
                filename = '.'.join(file[:-1])
                yield (filename, ext, filename.split('/')[-1:][0])
