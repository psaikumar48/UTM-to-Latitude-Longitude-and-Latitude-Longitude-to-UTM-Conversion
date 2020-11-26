import utm
import pandas as pd
no_of_decimals_in_dms=4 #INPUT:decimal values in Degree, Minutes and secounds can be adjusted
no_of_decimals_in_UTM=4 #INPUT:decimal values in Easting and Northing can be adjusted

def decdeg2dms(dd,Longitude=True):
    minutes,seconds = divmod(abs(dd)*3600,60)
    degrees,minutes = divmod(minutes,60)
    DIR='E' if Longitude & (dd>0) else 'W' if Longitude & (dd<0) else 'N' if (not Longitude) & (dd>0) else 'S'
    return "{:02d}".format(int(degrees))+'° '+"{:02d}".format(int(minutes))+"' "+format(seconds,f".{no_of_decimals_in_dms}f")+'" '+DIR

IP=pd.read_excel(io='from_dd.xlsx',sheet_name='Sheet1')
lat=list(IP.latitude)
long=list(IP.longitude)
lat=[x for x in lat if str(x) != 'nan']
long=[x for x in long if str(x) != 'nan']
n=min(len(lat),len(long))
Lat_dms,Long_dms,E,N,Z=[],[],[],[],[]
for i in range(n):
    (e,n,z1,z2)=utm.from_latlon(lat[i],long[i])
    E.append(e),N.append(n),Z.append(str(z1)+z2)
    Lat_dms.append(decdeg2dms(lat[i],False))
    Long_dms.append(decdeg2dms(long[i]))

E,N=[format(_,f".{no_of_decimals_in_UTM}f") for _ in E],[format(_,f".{no_of_decimals_in_UTM}f") for _ in N]
OP={'longitude(dd)':long,'latitude(dd)':lat,'longitude(dms)':Long_dms,'latitude(dms)':Lat_dms,'Esting':E,'Northing':N,'Zone':Z}
OP=pd.DataFrame(OP)
print(OP.head())
OP.to_excel("from_dd.xlsx")