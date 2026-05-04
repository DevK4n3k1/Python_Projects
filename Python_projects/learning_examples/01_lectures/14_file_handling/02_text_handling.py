##############################################
# Read the whole file (small files)
##############################################
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

##############################################
# Read line by line (memory-friendly)
##############################################
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# f.read(100)     # first 100 chars
# f.readline()    # one line
# f.readlines()   # list of lines


##############################################
# Write (create/overwrite)
##############################################
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")


##############################################
# Append (add to the end)
##############################################
with open("data.txt", "a", encoding="utf-8") as f:
    f.write("New line\n")

