




'''CREATE TABLE IF NOT EXISTS staging_US_flights_data    (
TRANSACTIONID	
FLIGHTDATE	
AIRLINECODE	
AIRLINENAME
TAILNUM	
FLIGHTNUM	
ORIGINAIRPORTCODE	
ORIGAIRPORTNAME	
ORIGINCITYNAME	
ORIGINSTATE	
ORIGINSTATENAME	
DESTAIRPORTCODE	
DESTAIRPORTNAME	
DESTCITYNAME	
DESTSTATE	
DESTSTATENAME	
CRSDEPTIME	
DEPTIME	
DEPDELAY	
TAXIOUT	
WHEELSOFF	
WHEELSON	
TAXIIN	
CRSARRTIME	
ARRTIME	
ARRDELAY	
CRSELAPSEDTIME	
ACTUALELAPSEDTIME	
CANCELLED	
DIVERTED	
DISTANCE
        '''


def get_date_dimension(date_df):
    
    date_df['YEAR'], date_df['QUARTER'] =  date_df['FLIGHTDATE'].dt.year, date_df['FLIGHTDATE'].dt.quarter
    date_df['MONTH'], date_df['MONTHNAME'] =  date_df['FLIGHTDATE'].dt.month, date_df['FLIGHTDATE'].dt.month_name()
    date_df['DAYSINMONTH'] =  date_df['FLIGHTDATE'].dt.days_in_month
    date_df['WEEK'], date_df['WEEKDAY'] =  date_df['FLIGHTDATE'].dt.week, date_df['FLIGHTDATE'].dt.day_name()
    date_df['DAY'], date_df['YEARDAY'] =  date_df['FLIGHTDATE'].dt.day, date_df['FLIGHTDATE'].dt.dayofyear
    return date_df



'FLIGHTDATE',
'TAILNUM',	
'FLIGHTNUM',	
'DEPTIME',	
'DEPDELAY',	
'TAXIOUT',		
'TAXIIN',		
'ARRTIME',	
'ARRDELAY',	
'DISTANCE'