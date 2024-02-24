# s = "Shree is a good guy"

# ************************************* Writing to a file *****************************************
# with open("test.txt", "w") as f:
#     f.write(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

# ************************************* Reading from a file *******************************************
# with open("test.txt", "r") as f:
#     s = f.read()
#     print(s)

# fp = open("test.txt", "r")
# s = fp.read()
# print(s)
# fp.close()


# ************************************* Appending to a file *******************************************
with open("test.txt", "a") as f:
    f.write(" Add this to previous text")

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()