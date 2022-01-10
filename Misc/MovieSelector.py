
def list_movies():
    fileRef=open("movies.txt","r")
    for line in fileRef:
        stuff=line.split("\t")
        print(stuff[0])
    fileRef.close()
#L
def list_by_year():
    fileRef = open("movies.txt", "r")
    askYear=int(input("Year (1880-2050)"))
    #FunDict={}
    #timeYear =[]
    if askYear < 1880 or askYear > 2050:
        print("invalid year")
        quit(TheStartOfCode())
    for line in fileRef:
        stuff=line.split("\t")
        #timeYear.append(int(stuff[1]))
        #FunDict[(stuff[0])] = int(stuff[1])
        if int(stuff[1])==askYear:
            print(stuff[0])
    # timeYear.sort()
    #for i in timeYear:
        #if i == askYear:
            #edit to look for value connected to the key
    fileRef.close()
#Y, i belive it works now
def search_by_title():
    fileRef = open("movies.txt", "r")
    searchUser=input("Title (is/contains):")
    realList=[]
    for line in fileRef:
        stuff=line.split("\t")
        realList.append(stuff[0])
    for i in realList:
        if searchUser in i:
            print(i)
    fileRef.close()
#T
def Search():
    fileRef = open("movies.txt", "r")
    GenerAsk= input("Genre (Action(A), Animation(N), Comedy(C), Drama(D), Documentary(O), Romance(R)):")
    RatingAsk = input("Rating (G, PG, PG-13, R, NC-17, NR):")
    LengthAsk = int(input("Maximum length (min):"))
    GeneraDict={}
    RatingDict={}
    LenthDict={}
    THeList=[]
    if GenerAsk not in "AaNnCcDdOoRr":
        print("invalid response")
        quit(Search())
    elif RatingAsk not in "G,g PG,pg PG-13,pg-13 R,r NC-17,nc-17 NR,nr":
        print("invalid response")
        quit(Search())
    for line in fileRef:
        stuff=line.split("\t")
        THeList.append(stuff[0])
        Jenera=stuff[4].split()  # need to convert what the txt says to something that can work
        RatingDict[stuff[0]]=stuff[3]
        numberL=int(stuff[2])
        LenthDict[stuff[0]]= numberL
        GeneraDict[stuff[0]] = Jenera
        if (RatingAsk.upper() == RatingDict[stuff[0]].upper()) or RatingAsk.lower() == RatingDict[stuff[0]].lower(): #this can be tricky
            if LengthAsk <= 0:
                print("invalid lenght")
                break
            elif LengthAsk >= numberL:
                if (GenerAsk in ("Aa")) and Jenera[0][0]=="1":
                    print(stuff[0])
                elif(GenerAsk in ("Cc")) and Jenera[0][2] == "1":
                    print(stuff[0])
                elif (GenerAsk in ("Dd")) and Jenera[0][3] == "1":
                    print(stuff[0])
                elif (GenerAsk in ("0o")) and Jenera[0][4] == "1":
                    print(stuff[0])
                elif (GenerAsk in ("Rr")) and Jenera[0][5] == "1":
                    print(stuff[0])


    #for i in THeList:
        #if LenthDict[i] >= LengthAsk and RatingDict[i]== RatingAsk and GenerAsk in GeneraDict[i]:
            #print(i)
        # Length:if LenthDict[i]>= lengthAsk
        # print(i)
        #Rating: if RatingDict[i]== RatingAsk
        #genera: if generaAsk in GeneraDict[i]
def TheStartOfCode():
    while True:
        UserIn = input("""Movie Selector - Please enter an option below:
    L - List all movies
    Y - List movies by year
    T - Search by title
    S - Search by genre, rating, and maximum length
    Q - Quit the program""")
        if UserIn in "lL":
            list_movies()
            quit()
        elif UserIn in "Yy":
            list_by_year()
            quit()
        elif UserIn in "Tt":
            search_by_title()
            quit()
        elif UserIn in "Ss":
            Search()
            quit()
        elif UserIn in "Qq":
            print("Goodbye")
            quit()
        else:
            print("invalid entry")
            continue
TheStartOfCode()

