Minin=int(input("minimum number of people:"))
Maxin=int(input("maximum number of people:"))
OMG=1
print("                   Probability of ")
print("                  Two People Having")
print("Number of People  the Same Birthday ")
print("----------------  ----------------- ")
for j in range(Minin , Maxin+1):
    i=0
    MatList = []
    while i < j:
        mep=(365-i)/365
        MatList.append(mep)
        i+=1
    else:
        # needs to call all values in list and * them
        OMG=1
        for t in range(len(MatList)):
            OMG=OMG*MatList[t]
        else:
            ECKD = 1-OMG
            print("%10.d  %20.4f"% (i,ECKD))

