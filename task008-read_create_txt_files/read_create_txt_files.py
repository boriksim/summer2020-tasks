# 2020-06-07
# Построчное чтение и запись текстовых файлов
import sys

try:
    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w+")
except IndexError:
    print("please input 2 file names")
    sys.exit()
except FileNotFoundError as e:
    print("file \"{}\" not found".format(e.filename))
    sys.exit()
try:
    for line in file1.readlines():
        try:
            file2.write("{}\n".format(max(list(map(int, line.split())))))
        except ValueError:
            print("file contains non-integers")
            sys.exit()
except UnicodeDecodeError:
    print("something went wrong")
file1.close()
file2.close()
