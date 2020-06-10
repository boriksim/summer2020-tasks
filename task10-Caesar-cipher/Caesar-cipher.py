import sys

try:
    src_file = open(sys.argv[1], "rb")
    dst_file = open(sys.argv[2], "wb")
    shift = int(sys.argv[3])
except IndexError:
    print("please use {python Caesar-cipher.py [file name to be encrypted] [destination file name] [shift coefficient (use - to decrypt)]}")
    sys.exit()
while byte := src_file.read(1):
    byte = bytes([(ord(byte) + shift) % 256])
    dst_file.write(byte)
src_file.close()
dst_file.close()
