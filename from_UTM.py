import utm
import pandas as pd
no_of_decimals_in_dms=8 #INPUT:decimal values in Degree, Minutes and secounds can be adjusted
no_of_decimals_in_dd=8  #INPUT:decimal values in Desimals Degree can be adjusted
loop=True
while loop:
    Zone=(input("Enter Zone ID [default:44P] : ") or "44 P")
    if (Zone[:-1].isdigit() or Zone[:-2].isdigit()) & isinstance(Zone[-1],str):
        Ezone,Nzone=int(Zone[:-1]),Zone[-1]
        loop=False    
    else:
        print('Wrong input......., Zone ID be like "1A" "36Q"')
def decdeg2dms(dd,Longitude=True):
    minutes,seconds = divmod(abs(dd)*3600,60)
    degrees,minutes = divmod(minutes,60)
    DIR='E' if Longitude & (dd>0) else 'W' if Longitude & (dd<0) else 'N' if (not Longitude) & (dd>0) else 'S'
    return "{:02d}".format(int(degrees))+'° '+"{:02d}".format(int(minutes))+"' "+format(seconds,f".{no_of_decimals_in_dms}f")+'" '+DIR

IP=pd.read_excel(io='from_utm.xlsx',sheet_name='Sheet1')
Esting=list(IP.E)
Northing=list(IP.N)
Esting=[x for x in Esting if str(x) != 'nan']
Northing=[x for x in Northing if str(x) != 'nan']
n=min(len(Esting),len(Northing))
Lat_dd,Long_dd,Lat_dms,Long_dms=[],[],[],[]
for i in range(n):
    (lat,long)=utm.to_latlon(Esting[i],Northing[i],Ezone,Nzone)
    Lat_dd.append(lat),Long_dd.append(long)
    Lat_dms.append(decdeg2dms(lat,False))
    Long_dms.append(decdeg2dms(long))

Lat_dd,Long_dd=[format(_,f".{no_of_decimals_in_dd}f") for _ in Lat_dd],[format(_,f".{no_of_decimals_in_dd}f") for _ in Long_dd]
OP={'E':Esting,'N':Northing,'latitude(dd)':Lat_dd,'longitude(dd)':Long_dd,'latitude(dms)':Lat_dms,'longitude(dms)':Long_dms}
OP=pd.DataFrame(OP)
OP.to_excel("from_UTM.xlsx")