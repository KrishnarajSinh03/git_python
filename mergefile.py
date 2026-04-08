with open("file1.txt", "r") as f1,
 open("file2.txt", "r") as f2,
 open("merged.txt", "w") as mf:
    mf.write(f1.read())
    mf.write(f2.read())

print("Files merged successfully!")