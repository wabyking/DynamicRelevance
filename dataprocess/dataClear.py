#encoding=utf-8
import simplejson,re
from pandas import DataFrame
from pandas import Panel
from xml.dom.minidom import parse
import xml.dom.minidom
def prepare():
	print "start"
	datas=[]
	with open("demo.text") as f:
		while 1:
			line=f.readline()
			if not line:
				break;
			try:
				line=line.replace("u\'","\'")
				line=line.replace("\'","\"")
				
				#line=re.sub(r", \"_id\": ObjectId(\"[0-9a-f]*\")","",line)
				line=re.sub(r", \"_id\": ObjectId\(\"[0-9a-f]{24}\"\)","",line)
				data= simplejson.loads(line)
				#print data
				datas.append(data)
			except:
				print line

	return datas


def dataFromXml(filename):
	DOMTree = xml.dom.minidom.parse( filename )
	collection = DOMTree.documentElement
	records = collection.getElementsByTagName("record")
	print len(records)
	datas={}
	
	for record in records:
		id=record.getElementsByTagName("id") [0].childNodes[0].data
		query=record.getElementsByTagName("query") [0].childNodes[0].data
		desicription=record.getElementsByTagName("desicription") [0].childNodes[0].data.strip()
		
		document1=record.getElementsByTagName("d1") [0].childNodes[0].data.strip()
		#
		#print d1_title
		
		document2=record.getElementsByTagName("d2") [0].childNodes[0].data.strip()
		title1=record.getElementsByTagName("d1") [0].getAttribute("title")
		title2=record.getElementsByTagName("d2") [0].getAttribute("title")
		data={"id":id,"query":query,"discription":(desicription),"title1":title1,"document1":(document1),"title2":title2,"document2":(document2)}
		#print desicription
		
		datas[str(id)]=data

	return datas
if __name__=="__main__":
	datas=prepare()
	df=DataFrame(datas)#.dropna(axis=0, how='any', thresh=None)
	# for  row in df["0"]:
	# 	print row
	# 	if row.has_key("order1") and row["order1"]==-1:
	# 		del row
	# print df["0"]
	print df[:][4:17]
	datas=dataFromXml("oringalData.xml")
	print datas.keys()
	
	validate=set([4,6,8,9,10,11,12,13,14,15,16,17])
	flag=[ i in validate for i in range(0,len(df))]
	print flag
	for i in range(0,21):
		print str(i)+" "+datas[str(i)]["query"]+"  :  "+datas[str(i)]["title1"]+"  ->  "+datas[str(i)]["title2"]
		c10=[]
		c0=[]
		c1=[]
		for d in df[str(i)][flag]:
			if len(d)==1:
				c10.append(d["order1"])
			else:
				c0.append(d["order0"])
				c1.append(d["order1"])
		print "no interference group: "+datas[str(i)]["title2"]+str(c10)
		print "interference group   : "+datas[str(i)]["title2"]+str(c1)
		print "interference group   : "+datas[str(i)]["title1"]+str(c0)
	

		print 