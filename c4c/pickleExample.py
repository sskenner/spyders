import pickle

with open("./responseFromCodeforcash", "rb") as f:
	file_name = pickle.load(f)
print(file_name)

# import base64 
# image = open('./responseFromCodeforcash', 'rb') #open binary file in read mode
# image_read = image.read()
# image_64_encode = base64.encodestring(image_read)
# print(image_64_encode)

# import codecs

# encodings = ['utf-8', 'windows-1250', 'windows-1252', 'ascii', 'base64_codec']
# for e in encodings:
#     try:
#         fh = codecs.open('./responseFromCodeforcash', 'r', encoding=e)
#         fh.readlines()
#         fh.seek(0)
#     except UnicodeDecodeError:
#         print('got unicode error with %s , trying different encoding' % e)
#     else:
#         print('opening the file with encoding:  %s ' % e)
#         break   

# print(fh)

# import libmagic

# blob = open('./responseFromCodeforcash').read()
# m = magic.Magic(mime_encoding=True)
# encoding = m.from_buffer(blob)
# print(encoding)


# import io

# def read_binary_from_file(file_name):
# 	with io.open(file_name, 'rb') as binary_file:
# 		data = binary_file.read
# 	print(data)

# if __name__ == '__main__':
# 	read_binary_from_file('./responseFromCodeforcash')

# import os
# import glob

# path = './'
# for infile in glob.glob(os.path.join(path, 'responseFromCodeforcash*')):
# 	file = open(infile, 'r').read()
# 	print(file)

