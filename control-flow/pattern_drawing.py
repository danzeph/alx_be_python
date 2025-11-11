while True:
    try:
        pattern = int(input("Enter the size of the pattern: "))
        if pattern > 0:
            break
        else:
            print("Please enter a positive integer only.\n")
    except ValueError:
        print("Please enter a positive integer only.\n")

for x in range(pattern):       
    for y in range(pattern):   
        print("*", end="")
        
    print("\n")
