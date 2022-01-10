print(""" Welcome to the Diagnosis Decision Support System
 When prompted, please enter today's month and day (e.g., 3 14),
  the patient's full name, temperature, and whether the patient
   is experiencing congestion, aches, and/or a rash.
    A diagnosis of Healthy, Cold, Flu, Measles, or Uncertain will be output as well as a return date,
     if the diagnosis is Measles or Uncertain
""")
# input
name = input("enter name")
month = int(input("enter numerical month"))
day = int(input("enter numerical day"))
patTem = float(input("enter patient temperature"))
cong = input("enter y or n if suffering congestion")
aches = input("enter y or n if suffering aches")
rash = input("enter y or n if suffering rashes")
# error checking
if cong not in "YynN":
    print("invalid response")
    exit(1)
if aches not in "YynN":
    print("invalid response")
    exit(1)
if rash not in "yYnN":
    print("invalid response")
    exit(1)
# variables
yES= "yY"
nO="nN"
healthy = "Healthy"
cold = "Cold"
flu = "Flu"
measles = "Measles"
unCert="Uncertain"
patStat= " "
if (patTem < 99.0) and (cong in nO) and (aches in nO) and(rash in nO) :
    patStat = healthy
elif patTem < 100.0:
    if (cong in yES) and (aches in nO) and (rash in nO):
        patStat = cold
    else:
        patStat = unCert
elif patTem >= 100.0:
    if (cong in nO) and (aches in yES) and (rash in nO):
        patStat = flu
    elif (cong in nO) and (aches in nO) and (rash in yES):
        patStat = measles
    else:
        patStat = unCert
else:
    patStat = unCert

# date
if month ==0 or month > 12:
    print ("invalid date")
    exit(1)
if month == 2:
    if day ==0 or day > 28:
        print ("invalid date")
        exit(1)
elif month in [1,3,5,7,8,10,12]:
    if day ==0 or day > 31:
        print ("invalid date")
        exit(1)
else:
    if day ==0 or day > 30:
        print("invalid date")
        exit(1)
# return date
returnDay = day+3
returnMonth= month
returnYear=2018

if (returnDay > 28)and(month == 2):
    returnDay = returnDay - 28
    returnMonth += 1
    if month == 12:
        returnMonth = 1
        returnYear = 2019
elif (returnDay > 30) and (month in [1, 3, 5, 7, 8, 10, 12]):
    returnDay = returnDay - 30
    returnMonth += 1
    if month == 12:
        month = 1
        returnYear = 2019
elif (returnDay > 31) and month in [4, 6, 9, 11]:
    returnDay = returnDay - 31
    returnMonth += 1
    if month == 12:
        returnMonth = 1
        returnYear = 2019

print("Patient:",name)
print("Date:{0}/{1}/2018".format(month,day))
print("Diagnosis:",patStat)
if patStat == measles or unCert:
    print("Return Date:{0}/{1}/{2}".format(returnDay, returnMonth, returnYear))

