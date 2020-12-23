"""with block in file open"""
with open("Harry.txt") as f :
    print(f.read(4))
""" If we use with block then file will automatically closed after reading so no need to use close """