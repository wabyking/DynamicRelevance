import json
import pymongo
from xml.dom.minidom import parse
import xml.dom.minidom
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

def dataFromXml(filename):
	DOMTree = xml.dom.minidom.parse("dataSet.xml")
	collection = DOMTree.documentElement
	records = collection.getElementsByTagName("record")
	print len(records)
	datas=[]
		
	for record in records:
		id=record.getElementsByTagName("id") [0].childNodes[0].data
		query=record.getElementsByTagName("query") [0].childNodes[0].data
		desicription=record.getElementsByTagName("desicription") [0].childNodes[0].data
		document1=record.getElementsByTagName("d1") [0].childNodes[0].data
		document2=record.getElementsByTagName("d2") [0].childNodes[0].data
		data={"id":id,"query":query,"discription":desicription,"document1":document1,"document2":document2}
		print desicription
		datas.append(data)
	return datas


if __name__=="__main__":
	datas=dataFromXml("dataSet.xml")
	appDatas(datas);
	#getinfo("docs")