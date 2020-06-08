# 2020-06-08
# Разбор строк текстового файла
# сортировать файл по зарплате/имени
import re
import sys

list = []
dlist = []
sum = 0
file = open(sys.argv[2], "r", encoding="utf-8")
for line in file.readlines():
    m = re.search(r"^([\w\s]+)\s(\d+)$", line, re.IGNORECASE)
    list.append([m.group(1), int(m.group(2))])
    sum += int(m.group(2))

if sys.argv[1] == "--sort=name":
    list = sorted(list, key=lambda a: a[0])
elif sys.argv[1] == "--sort=salary":
    list = sorted(list, key=lambda a: a[1], reverse=True)
else:
    print("please use --sort=name|salary")

for l in list:
    print("%(name)30s %(salary)6d" % {"name": l[0], "salary": l[1]})
print("%(name)30s %(salary)d" % {"name": "ИТОГО", "salary": sum})
