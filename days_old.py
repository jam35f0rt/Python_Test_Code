# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def month(mois,year):
    if year % 4 == 0 : #annees bissextiles
        bisex = 1 
    else:
        bisex = 0
    if mois==4 or mois==6 or mois==9 or mois==11  :
        return 30
    elif mois==2:
        return 28 + bisex
    else:
        return 31
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    y = 0 #days in year
    b = 0 #DaysInAllMonths to birth at the end of the year
    c = 0 #DaysInAllMonths to today at the end of the year
    m = 0

    while year1 < year2 :
        if year1 % 4 == 0 :
            y = y + 366 # jr nan ane a complet bissextille
        else:
            y = y + 365
        year1 = year1 + 1 
        
    
    if year1 == year2 : 
            if month1 < month2:
                while month1 != 12 :
                    b = b + month(month1,year1) #mois fet
                    month1 = month1 + 1
                while month2 != 12 :
                    c = c + month(month2,year2) #mois today
                    month2 = month2 + 1
                m = b - c
            elif month1 > month2 :
                while month1 != 12 :
                     b = b + month(month1,year1) #mois fet
                     month1 = month1 + 1
                while month2  != 0 :
                     c = c + month(month2,year2) #mois today
                     month2 = month2 - 1
                m = b + c
            elif year2 % 4 == 0  : #deux annes consecutifs , le 2eme est bissextille et le meme mois
                y = y + 1
    d = day2 - day1 #day
    return y + m + d
            
    ##


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed",result
        else:
            print "Test case passed!",result

test()














                if month1 < month2 :
                    while month1 != 12 :
                        b = b + day_in_month(month1,year1) #birth month
                        month1 = month1 + 1
                    while month2 != 12 :
                        c = c + day_in_month(month2,year2) #current month
                        month2 = month2 + 1
                    m = b - c
                elif month1 > month2 :
                    while month1 != 12 :
                        b = b + day_in_month(month1,year1) #birth month
                        month1 = month1 + 1
                    while month2  != 0 :
                        c = c + day_in_month(month2,year2) #current month
                        month2 = month2 - 1
                    m = b + c
                elif (year2 % 4 == 0 and year2 %100 !=0 or year2 % 400 == 0) and ( month1 <= 2  ):
                    m = m + 1