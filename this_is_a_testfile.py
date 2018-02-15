"""
Created 20180215

@author: MrFuppes
"""
def julday(ymd_hms):
    """
    input: vector "ymd_hms"; [year,month,day,hour,minute,second]
    output: julian day + day fraction as floating point number
    
    note: day fraction seems to be correct
        BUT: julian day number calculation doesn't match IDL julday function
            result (only correct for current date)
            source: https://en.wikipedia.org/wiki/Julian_day
    """
    year = ymd_hms[0]
    month = ymd_hms[1]
    day = ymd_hms[2]
    hour = ymd_hms[3]
    minute = ymd_hms[4]
    second = ymd_hms[5]
    
    jdn = (1461*(year+4800+(month-14)/12))/4+(367*(month-2-12*((month-14)/12)))/12-(3*((year+4900+(month-14)/12)/100))/4+day-32075
    
    jdn = math.ceil(jdn)
    print("jdn: ",jdn)
    
    day_fraction = (hour-12)/24+minute/1440+second/86400
    print("day frac: ", day_fraction)
    
    return jdn+day_fraction
