print("Welcome to the tip calculator.")

Total = input("What was the total of the bill? ")

TipPer = input("What percentage tip would you like to give? 10, 12, or 15? ")

split = input("How many people to split the bill? ")

#converts tip value to a percentage
TipPerConv =  int(TipPer) / 100

#Multiplies total of bill by percentage if tip. 
shit = int(Total) * float(TipPerConv)

#This is the total of the bill after the tip has been applied
TotalBill = shit + int(Total)

#This splits the bill for each person
FinalTotal_ForEach = TotalBill / int(split)
