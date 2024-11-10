import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        file.close()
    print(f'Завершилась запись в файл {file_name}')

start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end = time.time()
print(f'Работа потока 0:00:{round((end - start), 2)}')

t1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

start1 = time.time()
t1.join()
t2.join()
t3.join()
t4.join()
end1 = time.time()
print(f'Работа потоков 0:00:{round((end1 - start1), 2)}')