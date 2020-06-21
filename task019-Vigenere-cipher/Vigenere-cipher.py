# 2020-06-19
# Шифр Виженера
import argparse
import os.path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("srcfile", metavar="src", type=str, help="source filename")
parser.add_argument("dstfile", metavar="dst", type=str, help="destination filename")
parser.add_argument("--pwd", metavar="password", type=str, help="password", required=True)
parser.add_argument("--force", default=False, action="store_true", help="please mention to have existing file overwritten")
args = parser.parse_args()
pwd = args.pwd

bufsize = 1024

if os.path.exists(args.srcfile):
    src = open(args.srcfile, "rb")
else:
    print("srcfile not found")
    exit()

if args.force or not os.path.exists(args.dstfile):
    dst = open(args.dstfile, "wb")
else:
    print("dstfile already exists. Use \"--force\" to overwrite it")
    exit()

pos = 0
while True:
    block = src.read(bufsize)
    if not block:
        break
    block2 = [ord('-')]*len(block)
    i = 0
    for b in block:
        pwd_char = pwd[pos % len(pwd)]
        dst_char = b ^ ord(pwd_char)
        # block2.append(dst_char)
        block2[i] = dst_char
        i += 1
        pos += 1

    dst.write(bytes(block2))

src.close()
dst.close()
