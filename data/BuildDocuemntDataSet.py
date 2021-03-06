import json
import pymongo
from xml.dom.minidom import parse
import xml.dom.minidom,re
import jieba
class DateEncoder(json.JSONEncoder ):  
    def default(self, obj):  
        if isinstance(obj,dict):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj) 




def sampleData():
	datas=[]
	for i in range(20):
		data={"id":i,"query":"query"+str(i),"discription":(" discription"+str(i))*5,"document1":(" documentOne"+str(i))*30,"document2":(" documentTwo"+str(i))*30}
		datas.append(data)
	return datas

def appDatas(datas):
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	docs=db.docs
	docs.insert(datas)
	# for doc in docs.find():
	# 	print doc["id"]



def clear(collection_name):
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	if collection_name in db.collection_names():
		db.drop_collection(collection_name)
	
	db.create_collection(collection_name,)
	return db[collection_name]
def createDatas(datas):
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	if "docs" in db.collection_names():
		db.drop_collection("docs")
	
	db.create_collection("docs",)
	docs=db.docs
	
	docs.insert(datas)
	for doc in docs.find():
		print doc["id"]
	# with open('measurements.json', 'w') as f:
	# 	f.write(json.dumps(datas,cls=DateEncoder)) 

def createCollection(collection_name):
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	if collection_name in db.collection_names():
		db.drop_collection(collection_name)
	
	db.create_collection(collection_name,)


def getinfo(collection_name):
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	for doc in db[collection_name].find():
		print doc
def check_contain_chinese(check_str):
	count=0
	for ch in check_str:
		if u'\u4e00' <= ch <= u'\u9fff':
			count+=1
	if count*0.1/len(check_str) >0.3:
		return True
	return False


def filter(text):
	text, numeber = re.subn(r"\[\d*\]", "", text) 
	text, numeber = re.subn(r"[\n]+", "<br/>&nbsp;&nbsp;", text)
	return text
def addLabel(text): 
	text=filter( text) 
	labeledText="&nbsp;&nbsp;"
	if check_contain_chinese(text):
		tokens=jieba.cut(text)
		
		for token in tokens:
			labeledText +="<a>"+token+"</a>"
		return labeledText
	else:
		tokens=text.split()
<<<<<<< HEAD
		print "*".join(tokens)
=======
		#print "*".join(tokens)
>>>>>>> origin/master
		for token in tokens:
			labeledText +="<a>"+token+" </a>"
		return labeledText



		
	


def dataFromXml(filename):
	DOMTree = xml.dom.minidom.parse( filename )
	collection = DOMTree.documentElement
	records = collection.getElementsByTagName("record")
	print len(records)
	datas=[]
	id=0
	for record in records:
		#id=record.getElementsByTagName("id") [0].childNodes[0].data
		query=record.getElementsByTagName("query") [0].childNodes[0].data
		desicription=record.getElementsByTagName("desicription") [0].childNodes[0].data.strip()
		
		document1=record.getElementsByTagName("d1") [0].childNodes[0].data.strip()
<<<<<<< HEAD
		print document1
=======
		#
		#print d1_title
		
>>>>>>> origin/master
		document2=record.getElementsByTagName("d2") [0].childNodes[0].data.strip()
		title1=record.getElementsByTagName("d1") [0].getAttribute("title")
		title2=record.getElementsByTagName("d2") [0].getAttribute("title")
		data={"id":id,"query":query,"discription":addLabel(desicription),"title1":title1,"document1":addLabel(document1),"title2":title2,"document2":addLabel(document2)}
		#print desicription
<<<<<<< HEAD
		print 
		datas.append(data)
	return datas

=======
		print "%s & %s & %s & tobeCoverd\\\\" % (query,title1,title2)
		print "\hline"
		id+=1 
		datas.append(data)
	return datas

def calMeanLength(filename):

	DOMTree = xml.dom.minidom.parse( filename )
	collection = DOMTree.documentElement
	records = collection.getElementsByTagName("record")
	print len(records)
	
	counter=[]
	for record in records:
		
		
		document1=record.getElementsByTagName("d1") [0].childNodes[0].data.strip()
		counter.append(len(document1.split()))
		document2=record.getElementsByTagName("d2") [0].childNodes[0].data.strip()
		counter.append(len(document2.split()))
		
	return counter


>>>>>>> origin/master
def loadData():
	files={"dataSet.xml"}
	clear("docs")
	for f in files:
		datas=dataFromXml(f)
		appDatas(datas);
	
<<<<<<< HEAD

=======
def count():
	counter=calMeanLength("dataSet.xml")
	sum=0;
	print counter
	for c in counter:
		sum+=c
	print sum*1.0/len(counter)
>>>>>>> origin/master
def main():
	# str="[1]  hello,world [2]"
	# for s in  re.findall(r"\[\d*\]",str):
	# 	print s
	# result, number = re.subn(r"\[\d*\]", "", str) 
	# print result+"$"
	files={"dataSet.xml"}
	for f in files:
		datas=dataFromXml(f)
<<<<<<< HEAD
	appDatas(datas)
if __name__=="__main__":
	#main()
	#loadData()
	#clear("label")
	getinfo("label")
=======

	appDatas(datas)


if __name__=="__main__":
	main()
	#loadData()
	#clear("label")
	#getinfo("label")

>>>>>>> origin/master
