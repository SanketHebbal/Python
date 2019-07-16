
import pprint
#implementation of setdefalut() method....

message = 'Its to cold outside , stay inside the room and spend whole day in front of heater'

count = {}

for ch in message:
    count.setdefault(ch,0)
    count[ch] = count[ch] + 1

#for key,value in count.items():
 #   print(key+" "+str(value))

#pprint.pprint(count)
print(pprint.pformat(count))
