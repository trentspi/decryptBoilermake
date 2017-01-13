alpha = "abcdefghijklmnopqrstuvwxyz"
key = [0,5,2,2,5,2,8,4,3,4,0,5,2,2,5,2,
       8,4,3,0,5,2,2,5,2,8,4,3,4,0,5,2,
       2,5,2,8,4,3,0,5,2,2,5,2,8,4,3,4,
       0,5,2,2,5,2,8,4,3,0,5,2,2,5,2,8,
       4,3,4,0,5,2, 2,5,2,8,4,3]
cipher = input("enter your text: ")
keepGoing = True

while keepGoing:
    for i in range(len(cipher)):
        cipher = cipher.lower()
        foo = alpha[alpha.find(cipher[i]) - key[i]]
        print(foo, end = "")
    print("")

    keepup = input("keep going >> y/n : ")
    if keepup == "y":
        cipher = input("enter your text : ")
    if keepup == "n":
        keepGoing = False
