# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0

def day_in_month(month,year):
    if month==4 or month==6 or month==9 or month==11:
        return 30
    elif month==2:
        return 29   if leap_year(year) else  28
    else:
        return 31

def day_in_year(year):
    return 366 if leap_year(year) else 365

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here..
    if year1>year2 or (year1==year2 and month1>month2) or (year1==year2 and month1==month2 and day1>day2) or month1>12 or month1<1 or month2 >12 or month2<1 or (day_in_month(month1,year1)-day1<0) or day1<1 or (day_in_month(month2,year2)-day2<0) or day2<1 :
# ex: from 2017 to 2015     from Sep/2017 to Jan/2017             from Feb 25th 2017 to Feb 11th 2017                       Ther are 12 months                           Feb 29th 2017 or Jan 35th 2017 or Dec 0th 2016  "some examples of errors we can get as input"
        return 'Error' 
    else:
        m,y,b,c = 0,0,0,0
        saveYear = year1    # save the value of year1 , we gonna need it later
        while year1 < year2 :
            y = y + day_in_year(year1) #***
            year1 = year1 + 1 
        if year1 == year2 : 
            year1 = saveYear # back the real value of year1 to year1 (if it was modify...)
            while month1 != 12 :
                b = b + day_in_month(month1,year1) #DaysInAllMonths from birth month to the end of the birth year
                month1 = month1 + 1
            while month2  != 12 :
                c = c + day_in_month(month2,year2) #DaysInAllMonths from the current month to the end of the year
                month2 = month2 + 1
        if year1==year2:
            m = b - c   #***
        else:
            m =  b - day_in_year(year1)  +  day_in_year(year2) - c  
        d = day2 - day1 #***
        return y + m + d #*** their sum
    ##
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,8,3), day_in_month(1,2012)-1 + day_in_month(2,2012)+day_in_month(3,2012)+day_in_month(4,2012)+day_in_month(5,2012)+day_in_month(6,2012)+day_in_month(7,2012)+3),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30),366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed",result," != ",answer
        else:
            print "Test case passed!",result," = ",answer

test()