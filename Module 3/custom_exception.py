def check_file(filename):
    if not filename.endswith(".txt"):
        raise ValueError("Not a txt file")
    print("Valid File")

try:
    check_file("text.tt")
except Exception as e:
    print(e)