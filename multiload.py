import glob

def load_files(file_pattern):
    file_list = glob.glob(file_pattern)
    data = []
    for file in file_list:
        with open(file, 'r') as f:
            data.append(f.read())
    return data


pattern = '*.dat'
if __name__ == '__main__':
    data = load_files(pattern)
    print(data)