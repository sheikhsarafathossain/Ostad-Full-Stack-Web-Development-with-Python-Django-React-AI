import os
import pathlib

# try:
#     file = "texbook.txt"
#     if os.path.exists(file):
#         print("File Exist")
#         print(os.path.abspath(file))
#     else:
#         print("File not found")


#     file_path = pathlib.Path(file)

#     if file_path.exists():
#         print("File Exists")
#     print(os.path.abspath(file))
#     print(os.path.getsize(file) / 8 , "MB")
# except Exception:
#     print("File not found")
# else:
#     print("code executed")

# finally:
#     print("Always print")
f = "sss.tt"

def checkFile(f):
    if not f.endswith('.txt'):
        raise ValueError("only .txt approved")
    print("valid file")
try:
    checkFile(f)
except ValueError as e:
    print(e)

