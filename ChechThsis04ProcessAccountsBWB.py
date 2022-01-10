# Day 4 Exercise (will be counted as Programing Assignment 2)

"""
Add the 04ProcessAccounts.py file and BankAccount.py file to the same project.
Also add the accounts.txt file to the project.

Each line of that file contains one account with format:
<FirstName>, <LastName> $<AccountBalance>

Read in all the bank accounts, creating a corresponding BankAccount object and putting it in a list.

1.      Have your program "ProcessAccounts" find and print the average balance of all of the accounts.

2.      Find and print the account with the biggest balance.

3.      Find and print the account with the smallest balance.

4.      The account(s) with the median balance.
        Print one account if there are odd number of accounts in the file; otherwise, print the two accounts in the middle
        after you have the accounts sorted by the balance.
        How do you sort a list of objects based on one of its attributes? try:
        bank_accounts.sort(key=lambda x: x.balance, reverse=True)
        to sort a list of BankAccount object in place with the balance from large to small

5.      Assume that one year has passed and there is no new deposits/withdraws from each account. Update each account's
        balance by adding the interest rate (1.5% to the account balance).
        Print out the average of all the accounts after this update.

6.      The account with the lowest (alphabetically) first name. ("Aaron" is lower than "Zachary", for example).
        You should print the account information with the updated balance after one year.

7.      The account with the lowest (alphabetically) last name.
        You should print the account information with the updated balance after one year.

Hint 1: we will test your program with another input file with the same format.
Hint 2: you need to create a list of BankAccount objects, you should get rid of the spaces and dollar signs from the
accounts.txt before constructing your BankAccount objects. Each bank account should have the balance as a float.
Hint 3: to test your program by yourself, you can create a much smaller version of accounts.txt file.
"""

from BankAccount4BWB import *
bank_accounts = []
Stank_accounts = []
total = 0
ListOBala=[]
ListOFNames = []
ListOLNames = []
OpenAccount= open("accounts.txt", "r")
Numberof = 0
LunerTotal = 0
for line in OpenAccount:
    DesList= line.split()
    Sol = BankAccount(DesList[0],DesList[1],int(DesList[2][1:]))
    Luna = BankAccount(DesList[0],DesList[1],int(DesList[2][1:]))
    Luna.deposit(int(Luna.calculateInterest()))
    #Moona =Sol.deposit(Sol.calculateInterest())
    print(Sol)
    print(Luna)

    total += Sol.balance
    bank_accounts.append(Sol)
    Stank_accounts.append(Luna)
    ListOBala.append(Sol.balance)
    ListOFNames.append(Luna.firstName)
    ListOLNames.append(Luna.lastName)
    Numberof +=1
    LunerTotal += Luna.balance

BalaSorted = ListOBala
ListOFNames.sort()
ListOLNames.sort()
BalaSorted.sort()
if Numberof % 2 == 1:
    # print("odd")
    Mathma=int(BalaSorted-(BalaSorted//2)-1)
    Midnumber=(Mathma)
    print(Midnumber)
    print(BalaSorted [Midnumber])
else:
    # print ("even")
    Mathnam= (Numberof//2)
    Mathka= (Numberof//2)-1
    Mathcha= ((BalaSorted[Mathnam])+(BalaSorted[Mathka]))/2
    #print (Mathcha)

#print(bank_accounts)
print("average",total/Numberof)
print("interest average",LunerTotal/Numberof)
# print (min(ListOBala))
# print (max(ListOBala))
OpenAccount.close()

OpenAccount= open("accounts.txt", "r")
for line in OpenAccount:
    DesList= line.split()
    Sol = BankAccount(DesList[0],DesList[1],int(DesList[2][1:]))
    if Sol.balance == min(ListOBala):
        Answer1 = Sol
    if Sol.balance == max(ListOBala):
        Answer2 = Sol
    if Sol.balance == BalaSorted[Mathnam]:
        Answer3 = Sol
    if Sol.balance == BalaSorted [Mathka]:
        Answer4 = Sol
    if Sol.firstName == ListOFNames [0]:
        Answer5 = Sol
    if Sol.lastName == ListOLNames [0]:
        Answer6 = Sol
print("min",Answer1)
print("max",Answer2)
print("Median high",Answer3)
print("median low",Answer4)
print("Alpha first",Answer5)
print("Alpha last",Answer6)

OpenAccount.close()
# work on order printed