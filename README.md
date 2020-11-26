UTM: universal transverse mercator
dd: Decimal degrees
dms: Degree,minutes and seconds

1) About form_UTM.py
1.1) This code takes the excel as input with the name 'from_UTM.xlsx', consist of Easting and Northing with a header as 'E' and 'N' [in Sheet1] and converts to Latitude and Longitudes in both decimal degrees(DD) and Degrees, Minutes and seconds(DMS).
1.2) Number of decimal values in output can be adjusted in 3rd and 4th line of the code
1.3) Output is stored in same excel with Headers as longitude(dd), latitude(dd), longitude(dms) and latitude(dms)

2) About form_dd.py
2.1) This code takes the excel as input with the name 'from_dd.xlsx', consist of longitude in dd, latitude in dd with a header as longitude and latitude [in Sheet1] and converts to Latitude/Longitudes in Degrees, Minutes and seconds(DMS) and Eastin/Northing/zone.
2.2) Number of decimal values in output can be adjusted in 3rd and 4th line of the code
2.3) Output is stored in same excel with Headers as longitude(dms),latitude(dms), Easting, Northing and Zone

3) About form_dms.py
3.1) This code takes the excel as input with the name 'from_dms.xlsx', consist of longitude in dms, latitude in dms with a header as longitude and latitude [in Sheet1] and converts to Latitude/Longitudes in Desimals Degrees and Eastin/Northing/zone.
3.2) Number of decimal values in output can be adjusted in 3rd and 4th line of the code
3.3) Output is stored in same excel with Headers as longitude(dd),latitude(dd), Easting, Northing and Zone
3.4) Input dms may be like 30°41'34.11"S or -30°41'34.11" any thing accepted

