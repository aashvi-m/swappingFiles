def swapFileData():
    file1 = input("name of file 1: ")
    file2 = input("name of file 2: ")

    data_a = open(file1, "r")
    data_a.read()

    data_b = open(file2, "r")
    data_b.read()

    data_a = open(file1, "w")
    data_a.write(data_b)

    data_b = open(file2, "w")
    data_b.write(data_a)

swapFileData()
