for decimal in range(0, 128):
    binary = bin(decimal)[2:]
    print(" " * (3-len(str(decimal))) + str(decimal), "0" * (8-len(binary)) + binary)
