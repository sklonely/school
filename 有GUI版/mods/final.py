import math
import re
def mydata(my1,my2):
	#my1="+CGPSINFO: 2242.484940,N,12021.608459,E,150518,101255.0,,54.6,180.4"
	#my2="+CGPSINFO: 2242.559644,N,12021.609622,E,150518,101250.0,,51.1,179.6"
	#my1:第二次座標 my2:第一次座標
	mylast=[]
	mynext=[]
	mylastGPS=''
	mynextGPS=''
	a=my2.find(" ")
	b=my2.find("N",10)
	c=my2.find("E")
	for i in range(a+1,b-1):
		mylastGPS=mylastGPS+my2[i]
	mylastGPS=mylastGPS+","
	for j in range(b+2,c-1):
		mylastGPS=mylastGPS+my2[j]
	mylastGPS=mylastGPS+","
	for k in range(c+9,c+15):
		mylastGPS=mylastGPS+my2[k]
	a=my1.find(" ")
	b=my1.find("N",10)
	c=my1.find("E")
	for i in range(a+1,b-1):
		mynextGPS=mynextGPS+my1[i]
	mynextGPS=mynextGPS+","
	for j in range(b+2,c-1):
		mynextGPS=mynextGPS+my1[j]
	mynextGPS=mynextGPS+","
	for k in range(c+9,c+15):
		mynextGPS=mynextGPS+my1[k]
	mylastdata=re.findall(r'\d+',mylastGPS)
	mynextdata=re.findall(r'\d+',mynextGPS)
	if(len(mylastdata)!=5 or len(mynextdata)!=5 or (mylastdata[4]==mynextdata[4])):
		s=-1
		f=''
	elif (len(mylastdata)==5 or len(mynextdata)==5):
		t=mylastdata[0]+'.'+mylastdata[1]
		if len(mylastdata[0])<3:
			anlast=float(t)/60
		elif len(mylastdata[0])==3:
			anlast=float(t[0])+float(t[1:])/60
		elif len(mylastdata[0])==4:
			anlast=float(t[0:2])+float(t[2:])/60
		elif len(mylastdata[0])==5:
			anlast=float(t[0:3])+float(t[3:])/60
		mylast.insert(0,anlast)
		t=mylastdata[2]+'.'+mylastdata[3]
		if len(mylastdata[2])<3:
			aelast=float(t)/60
		elif len(mylastdata[2])==3:
			aelast=float(t[0])+float(t[1:])/60
		elif len(mylastdata[2])==4:
			aelast=float(t[0:2])+float(t[2:])/60
		elif len(mylastdata[2])==5:
			aelast=float(t[0:3])+float(t[3:])/60
		mylast.insert(1,aelast)
		t=mynextdata[0]+'.'+mynextdata[1]
		if len(mynextdata[0])<3:
			annext=float(t)/60
		elif len(mynextdata[0])==3:
			annext=float(t[0])+float(t[1:])/60
		elif len(mynextdata[0])==4:
			annext=float(t[0:2])+float(t[2:])/60
		elif len(mynextdata[0])==5:
			annext=float(t[0:3])+float(t[3:])/60
		mynext.insert(0,annext)
		t=mynextdata[2]+'.'+mynextdata[3]
		if len(mynextdata[2])<3:
			aenext=float(t)/60
		elif len(mynextdata[2])==3:
			aenext=float(t[0])+float(t[1:])/60
		elif len(mynextdata[2])==4:
			aenext=float(t[0:2])+float(t[2:])/60
		elif len(mynextdata[2])==5:
			aenext=float(t[0:3])+float(t[3:])/60
		mynext.insert(1,aenext)
		t1=mylastdata[4]
		t2=mynextdata[4]
		if int(t2[4:]) > int(t1[4:]):
			z=int(t2[4:])-int(t1[4:])
		elif int(t2[4:])<int(t1[4:]):
			z=int(t2[4:])+60-int(t1[4:])
		x=float(mylast[0])-float(mynext[0])
		y=float(mylast[1])-float(mynext[1])
		xk=x*111
		yk=y*111
		d=math.sqrt(xk**2+yk**2)
		s=round((d/z)*3600,3)
		if mynext[1]-mylast[1] == 0 and mynext[0]-mylast[0] != 0:
			if mynext[0]-mylast[0] > 0:
				f='北'
			elif mynext[0]-mylast[0] < 0:
				f='南'
		elif mynext[1]-mylast[1] == 0 and mynext[0]-mylast[0] == 0:
			f='靜止'
		elif mynext[1]-mylast[1] != 0:
			if mynext[0]-mylast[0] > 0:
				if ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) >= 2.5 or ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) <= -2.5:
					f='北'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > 0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < 2.5:
					f='東北'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < 0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) >= 0:
					f='東'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < -0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > -2.5:
					f='西北'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > -0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) <= 0:
					f='西'
			elif mynext[0]-mylast[0] < 0:
				if ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) >= 2.5 or ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) <= -2.5:
					f='南'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > 0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < 2.5:
					f='西南'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < 0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > 0:
					f='西'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < -0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > -2.5:
					f='東南'
				elif ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) > -0.5 and ((mynext[0]-mylast[0])/(mynext[1]-mylast[1])) < 0:
					f='東'
	return s,f
def AMBdata(amb1,amb2):
	amblast=[]
	ambnext=[]
	amblastGPS=''
	ambnextGPS=''
	a=amb2.find(" ")
	b=amb2.find("N",10)
	c=amb2.find("E")
	for i in range (a+1,b-1):
		amblastGPS=amblastGPS+amb2[i]
	amblastGPS=amblastGPS+","
	for j in range (b+2,c-1):
		amblastGPS=amblastGPS+amb2[j]
	amblastGPS=amblastGPS+","
	for k in range (c+9,c+15):
		amblastGPS=amblastGPS+amb2[k]
	a=amb1.find(" ")
	b=amb1.find("N",10)
	c=amb1.find("E")
	for i in range (a+1,b-1):
		ambnextGPS=ambnextGPS+amb1[i]
	ambnextGPS=ambnextGPS+","
	for j in range (b+2,c-1):
		ambnextGPS=ambnextGPS+amb1[j]
	ambnextGPS=ambnextGPS+","
	for k in range (c+9,c+15):
		ambnextGPS=ambnextGPS+amb1[k]
	amblastdata=re.findall(r'\d+',amblastGPS)
	ambnextdata=re.findall(r'\d+',ambnextGPS)
	if (len(amblastdata) != 5 or len(ambnextdata) != 5 or (amblastdata[4] == ambnextdata[4])):
		s=-1
		F=''
	elif (len(amblastdata) == 5 or len(ambnextdata) == 5):
		t = amblastdata[0] + '.' +amblastdata[1]
		if len(amblastdata[0]) < 3:
			anlast = float(t)/60
		elif len(amblastdata[0]) == 3:
			anlast = float(t[0]) + float(t[1:])/60
		elif len(amblastdata[0]) == 4:
			anlast = float(t[0:2]) + float(t[2:])/60
		elif len(amblastdata[0]) == 5:
			anlast = float(t[0:3]) + float(t[3:])/60
		amblast.insert(0,anlast)
		t=amblastdata[2] + '.' + amblastdata[3]
		if	len(amblastdata[2]) < 3:
			aelast = float(t)/60
		elif len(amblastdata[2]) == 3:
			aelast = float(t[0]) + float(t[1:])/60
		elif len(amblastdata[2]) == 4:
			aelast = float(t[0:2]) + float(t[2:])/60
		elif len(amblastdata[2]) == 5:
			aelast = float(t[0:3]) + float(t[3:])/60
		amblast.insert(1,aelast)
		t=ambnextdata[0] + '.' + ambnextdata[1]
		if len(ambnextdata[0]) < 3:
			annext = float(t)/60
		elif len(ambnextdata[0]) == 3:
			annext = float(t[0]) + float(t[1:])/60
		elif len(ambnextdata[0]) == 4:
			annext = float(t[0:2]) + float(t[2:])/60
		elif len(ambnextdata[0]) == 5:
			annext = float(t[0:3]) + float(t[3:])/60
		ambnext.insert(0,annext)
		t=ambnextdata[2] + '.' +ambnextdata[3]
		if len(ambnextdata[2])<3:
			aenext = float(t)/60
		elif len(ambnextdata[2]) == 3:
			aenext = float(t[0]) + float(t[1:])/60
		elif len(ambnextdata[2]) == 4:
			aenext = float(t[0:2]) + float(t[2:])/60
		elif len(ambnextdata[2]) == 5:
			aenext = float(t[0:3]) + float(t[3:])/60
		ambnext.insert(1,aenext)
		t1=amblastdata[4]
		t2=ambnextdata[4]
		if int(t2[4:]) > int(t1[4:]):
			z=int(t2[4:])-int(t1[4:])
		elif int(t2[4:])<int(t1[4:]):
			z=int(t2[4:])+60-int(t1[4:])
		x=float(amblast[0])-float(ambnext[0])
		y=float(amblast[1])-float(ambnext[1])
		xk=x*111
		yk=y*111
		d=math.sqrt(xk**2+yk**2)
		s=round((d/z)*3600,3)
		if ambnext[1]-amblast[1] == 0 and ambnext[0]-amblast[0] != 0:
			if ambnext[0]-amblast[0] > 0:
				f='北'
			elif ambnext[0]-amblast[0] < 0:
				f='南'
		elif ambnext[1]-amblast[1] == 0 and ambnext[0]-amblast[0] == 0:
			f='靜止'
		elif ambnext[1]-amblast[1] != 0:
			if ambnext[0]-amblast[0] > 0:
				if ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) >= 2.5 or ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) <= -2.5:
					f='北'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > 0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < 2.5:
					f='東北'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < 0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) >= 0:
					f='東'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < -0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > -2.5:
					f='西北'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > -0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) <= 0:
					f='西'
			elif ambnext[0]-amblast[0] < 0:
				if ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) >= 2.5 or ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) <= -2.5:
					f='南'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > 0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < 2.5:
					f='西南'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < 0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > 0:
					f='西'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < -0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > -2.5:
					f='東南'
				elif ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) > -0.5 and ((ambnext[0]-amblast[0])/(ambnext[1]-amblast[1])) < 0:
					f='東'
	return s,f
def AMBandmy(my1,amb1):
	mylast=[]
	ambnext=[]
	mylastGPS=''
	ambnextGPS=''
	a=my1.find(" ")
	b=my1.find("N",10)
	c=my1.find("E")
	for i in range (a+1,b-1):
		mylastGPS=mylastGPS+my1[i]
	mylastGPS=mylastGPS+","
	for j in range (b+2,c-1):
		mylastGPS=mylastGPS+my1[j]
	mylastGPS=mylastGPS+","
	for k in range (c+9,c+15):
		mylastGPS=mylastGPS+my1[k]
	a=amb1.find(" ")
	b=amb1.find("N",10)
	c=amb1.find("E")
	for i in range (a+1,b-1):
		ambnextGPS=ambnextGPS+amb1[i]
	ambnextGPS=ambnextGPS+","
	for j in range (b+2,c-1):
		ambnextGPS=ambnextGPS+amb1[j]
	ambnextGPS=ambnextGPS+","
	for k in range (c+9,c+15):
		ambnextGPS=ambnextGPS+amb1[k]
	mylastdata=re.findall(r'\d+',mylastGPS)
	ambnextdata=re.findall(r'\d+',ambnextGPS)
	if (len(mylastdata) != 5 or len(ambnextdata) != 5 or (mylastdata[4] == ambnextdata[4])):
		s=-1
		F=''
	elif (len(mylastdata) == 5 or len(ambnextdata) == 5):
		t = mylastdata[0] + '.' +mylastdata[1]
		if len(mylastdata[0]) < 3:
			anlast = float(t)/60
		elif len(mylastdata[0]) == 3:
			anlast = float(t[0]) + float(t[1:])/60
		elif len(mylastdata[0]) == 4:
			anlast = float(t[0:2]) + float(t[2:])/60
		elif len(mylastdata[0]) == 5:
			anlast = float(t[0:3]) + float(t[3:])/60
		mylast.insert(0,anlast)
		t=mylastdata[2] + '.' + mylastdata[3]
		if	len(mylastdata[2]) < 3:
			aelast = float(t)/60
		elif len(mylastdata[2]) == 3:
			aelast = float(t[0]) + float(t[1:])/60
		elif len(mylastdata[2]) == 4:
			aelast = float(t[0:2]) + float(t[2:])/60
		elif len(mylastdata[2]) == 5:
			aelast = float(t[0:3]) + float(t[3:])/60
		mylast.insert(1,aelast)
		t=ambnextdata[0] + '.' + ambnextdata[1]
		if len(ambnextdata[0]) < 3:
			annext = float(t)/60
		elif len(ambnextdata[0]) == 3:
			annext = float(t[0]) + float(t[1:])/60
		elif len(ambnextdata[0]) == 4:
			annext = float(t[0:2]) + float(t[2:])/60
		elif len(ambnextdata[0]) == 5:
			annext = float(t[0:3]) + float(t[3:])/60
		ambnext.insert(0,annext)
		t=ambnextdata[2] + '.' +ambnextdata[3]
		if len(ambnextdata[2])<3:
			aenext = float(t)/60
		elif len(ambnextdata[2]) == 3:
			aenext = float(t[0]) + float(t[1:])/60
		elif len(ambnextdata[2]) == 4:
			aenext = float(t[0:2]) + float(t[2:])/60
		elif len(ambnextdata[2]) == 5:
			aenext = float(t[0:3]) + float(t[3:])/60
		ambnext.insert(1,aenext)
		x=float(mylast[0])-float(ambnext[0])
		y=float(mylast[1])-float(ambnext[1])
		xm=x*111
		ym=y*111
		d=round(math.sqrt(xm**2+ym**2),3)
		if mylast[1]-ambnext[1] == 0 and mylast[0]-ambnext[0] != 0:
			if mylast[0]-ambnext[0] > 0:
				f='北'
			elif mylast[0]-ambnext[0] < 0:
				f='南'
		elif mylast[1]-ambnext[1] == 0 and mylast[0]-ambnext[0] == 0:
			f='靜止'
		elif mylast[1]-ambnext[1] != 0:
			if mylast[0]-ambnext[0] > 0:
				if ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) >= 2.5 or ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) <= -2.5:
					f='南'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > 0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < 2.5:
					f='西南'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < 0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) >= 0:
					f='西'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < -0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > -2.5:
					f='東南'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > -0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) <= 0:
					f='東'
			elif mylast[0]-ambnext[0] < 0:
				if ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) >= 2.5 or ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) <= -2.5:
					f='北'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > 0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < 2.5:
					f='東北'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < 0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > 0:
					f='東'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < -0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > -2.5:
					f='西北'
				elif ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) > -0.5 and ((mylast[0]-ambnext[0])/(mylast[1]-ambnext[1])) < 0:
					f='西'

	return d,f