##############################################
# Manual open/close
##############################################
f = open("data.txt", "r", encoding="utf-8")
try:
    text = f.read()
finally:
    f.close()


##############################################
# Auto Close
##############################################
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
# file is auto-closed here

