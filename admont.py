import os
import time
# Convert a number into a string that is fixed size in length. In case the number is smaller in lenght then 0 will be put in front of the number. E.g. 0001 where lenght is 4 input number is 1.
def properzero(input,length):
	pstr=str(input)
	# print "A string: %s"%pstr
	inputlenght=len(pstr)
	zeros=""
	while (inputlenght < length):
		zeros += "0"
		inputlenght+=1
	pstr=zeros+pstr
	return pstr

count=0
# for m range (4, 4)
for dt in range(1, 5):
	for t in range(0, 24):
		for min in xrange(0, 60, 10):
			count+=1
			pdt=properzero(dt,2)
			ptime=properzero(t,2)
			pmin=properzero(min,2)
			pcount=properzero(count,5)
			# url =  "http://www.webcams.schultz.at/webcam/ankogel-nord/2016/04/%s/%s%s_hu.jpg"%(pdt,ptime,pmin)
			url =  "http://www.webcams.schultz.at/webcam/ankogel-sued/2016/04/%s/%s%s_hu.jpg"%(pdt,ptime,pmin)
			# fname = "pic/admont_%s.jpg"%pcount
			fname = "picsued/admont_sued_%s.jpg"%pcount
			# print url
			# print fname
			cmd = "wget '%s' -O '%s'"%(url,fname)
			# print cmd
			os.system(cmd)
			time.sleep(4)


year=2016
month=03
day=21
hh=0
mm=0

yd=8765.81277
md=730.484398
od=24

range=165

y=int(range/yd)
range=range-(y*yd)
m=int(range/md)
range=range-(m*md)
d=range/od

print "y %d m %d d %d" %(y, m, d)

#Added an extra comment line just to test github commits.
