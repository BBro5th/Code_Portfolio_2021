Stair="""*
*   0
*  /|\\
* /   \\
* * * * """
Stair="""*
*   0
*  /|\\
*  / \\
* * * * """
top1="*"
art2="* 0"
art3="*/|\\"
art4="*/ \\"
art5="* * * *"
space="      "
Dspace="\n"
n=int(input("how many steps?"))
for i in range(n):
    if i <=0:
        print((space*i)+top1)
        print((space * i) + art2)
        print((space * i) + art3)
        print((space * i) + art4)
        print((space * i) + art5)
    else:
        print((space * i) + art2)
        print((space * i) + art3)
        print((space * i) + art4)
        print((space * i) + art5)