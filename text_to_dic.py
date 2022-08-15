a =  """Device1,Int1,1%
Router1,Int2,1%
Router1,Int3,1%
Router1,Int4,1%
Router2,Int1,5%
Router2,Int2,10%
Router2,Int3,1%
Router2,Int4,1%"""

devices = {}
lines = a.splitlines()
for line in lines:
    columns = line.split(",")
    print(columns)
    key = f"{columns[0]}_{columns[1]}"
    devices[key] = int(columns[2].replace("%",""))

print(max(devices,key=devices.get))
