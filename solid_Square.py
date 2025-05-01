def solid_square(side):
    for i in range(side):
        for j in range(side):
            print("* ",end="")
        print()
print(solid_square(6))