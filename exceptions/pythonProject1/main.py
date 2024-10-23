# #KeyError, TypeError, IndexError. ZeroError, FileError
#
# try:
#     file =  open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     # file.close()
#     # print("File closed")
#     raise KeyError("This is an error")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height must not be over 2 metres tall.")

bmi = weight / (height ** 2)

