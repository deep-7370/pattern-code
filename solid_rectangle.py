def solid_rectangle(length,breath):
    for i in range(length):
        for j in range(breath):
            print("* ",end="")
        print()
print(solid_rectangle(6,4))