import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

'''for i in files:
    start = time.time()
    read_info(i)
    print('time taken:', time.time() - start)'''

if __name__ == '__main__':
    start = time.time()
    with Pool() as pool:
        pool.map(read_info, files)
    print('time taken:', time.time() - start)
