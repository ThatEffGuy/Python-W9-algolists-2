#Client Lists Program

#fill lists
lastNameList = ["Gumm", "Mann","Garden", "Dare", "Turner", "Friend", "Seek"]
firstNameList = ["Chuann", "Saad", "Rose", "Colin", "Paige", "Fiona", "Hayden"]
owedList     = [100, 0, 2000, 3500, 6000, 456]

#find the average 
def findAvg(owedList):
    avgOwed = 0
    total = 0
    totalCount = 0

    if len(owedList) > 0:
        totalCount = len(owedList)
        for item in owedList:
            total += item
        #end for
        if total > 0:
            avgOwed = total / totalCount
        else:
            avgOwed = 0
        #end if
    #end if
    return avgOwed
#end avgOwed

#find the maximum amount owed
def findMax(owedList):
    maxOwed = None
    position = None
    if len(owedList) > 0:
        maxOwed = owedList[0]  # maxOwed = first item in list
        for item in owedList:
            if maxOwed < item:
                maxOwed = item
                position = owedList.index(item) # get index value
            #end if
        #end for
    #end if
    return maxOwed, position
#end findMax

#find the minimum amount owed
def findMin(owedList):
    minOwed = None
    position = None
    if len(owedList) > 0:
        minOwed = owedList[0]  # minOwed = first item in list
        for item in owedList:
            if minOwed > item:
                minOwed = item
                position = owedList.index(item) # get index value
            #end if
        #end for
    #end if
    return minOwed, position
#end findMin

#main program
avgOwed = findAvg(owedList)
#find who owes the most money
maxOwed, positionMax  = findMax (owedList)
minOwed, positionMin  = findMin (owedList)

#print results
print ("Average amount owed : £", format(avgOwed, "6.2f"))
client = firstNameList[positionMax] + " " + lastNameList[positionMax] 
print (client,"owes Maximum Amount: £", format(maxOwed, "6.2f"))
client = firstNameList[positionMax] + " " + lastNameList[positionMax] 
print (client,"owes Minimum Amount: £", format(minOwed, "6.2f"))
