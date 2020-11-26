import utm
import pandas as pd
no_of_decimals_in_dd=4   #INPUT:decimal values in Desimals Degree can be adjusted
no_of_decimals_in_UTM=4  #INPUT:decimal values in Easting and Northing can be adjusted

def dms2decdeg(dms):
    dms=dms[1:] if dms[0]==' ' else dms[:-1] if dms[-1]==' ' else dms
    dms=dms if dms[-1] not in ['N','E','S','W'] else '-' + dms[:-1] if ['N','E','S','W'].index(dms[-1])>1 else dms[:-1]
    degree=int(dms.split('°')[0])
    minutes=int(dms.split("'")[0][-2:])
    seconds=float(dms.split("'")[1][:-2]) if dms[-1]==' ' else float(dms.split("'")[1][:-1])
    minutes_desimales=((minutes*60)+seconds)/3600
    dd=degree-minutes_desimales if dms[0] =='-' else degree+minutes_desimales
    return dd

IP=pd.read_excel(io='D:\PYTHON\\from_dms.xlsx',sheet_name='Sheet1')
lat=list(IP.latitude)
long=list(IP.longitude)
lat=[x for x in lat if str(x) != 'nan']
long=[x for x in long if str(x) != 'nan']
n=min(len(lat),len(long))
Lat_dd,Long_dd,E,N,Z=[],[],[],[],[]
for i in range(n):
    la,lo=dms2decdeg(lat[i]),dms2decdeg(long[i])
    (e,n,z1,z2)=utm.from_latlon(la,lo)
    E.append(e),N.append(n),Z.append(str(z1)+z2)
    Lat_dd.append(la)
    Long_dd.append(lo)
E,N=[format(_,f".{no_of_decimals_in_UTM}f") for _ in E],[format(_,f".{no_of_decimals_in_UTM}f") for _ in N]
Long_dd,Lat_dd=[format(_,f".{no_of_decimals_in_dd}f") for _ in Long_dd],[format(_,f".{no_of_decimals_in_dd}f") for _ in Lat_dd]
OP={'longitude':long,'latitude':lat,'longitude(dd)':Long_dd,'latitude(dd)':Lat_dd,'Esting':E,'Northing':N,'Zone':Z}
OP=pd.DataFrame(OP)
print(OP.head())
OP.to_excel("from_dms.xlsx")