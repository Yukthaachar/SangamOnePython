import mod_findlucky as mf
from datetime import date,timedelta
result=mf.findlucky(10)
lucky=result[0]
unlucky=result[1]

today=date.today()
later=today+timedelta(weeks=4)

s1="Honourable Prime Minister of India, the following are the list of lucky prisoners who are releasing on "
f1=open("lucky.txt",'w')
f1.write(s1+str(today)+"\n")
f1.write(str(lucky))
f1.close()

s1="Honourable Prime Minister of India, the following are the list of unlucky prisoners who are releasing on "
f1=open("unlucky.txt",'w')
f1.write(s1+str(later)+"\n")
f1.write(str(unlucky))
f1.close()
