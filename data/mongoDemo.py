#encoding=utf-8
import pymongo,os

def connect_mongodb():
	# servers="mongodb://localhost:27017"
	# conn = pymongo.Connection(servers)
	# print conn.database_names()
	# db = conn.my_mongodb            #连接库
	client = pymongo.MongoClient("localhost", 27017)
	print client.database_names()
	db=client.test
	print db.collection_names()
	if "docs" in db.collection_names():
		db.drop_collection("docs")
	
	db.create_collection("docs",)
	docs=db.docs
	for doc in docs.find():
		print doc

	restaurants=db.restaurants
	print restaurants.find().count()

	restaurant={"sb":"test"}
	restaurants.insert(restaurant)

	restaurants.find_one({u"sb":u"test"}) # please use "u" for the unicode
	print restaurants.find().count()
	
	return 
	

	
	return client.test
	#return db
def str_process(string,db):
	d={}
	if string == '\n':
		return
	string2=str(string)
	print '-----'+string
	string2=string2.split(' ')
	print '---------------'
	print string2
	for i in string2:
		print i
		print '------------'
		string2[3].split('\n')
		d['projectcode']=string2[0]
		d['pagename']=string2[1]
		d['pageview']=string2[2]
		d['bytes']=string2[3][:-1]
		db.user.insert(d)
def file_process(source_file,db):
	string2=''
	f=open(source_file,'r')
	print 'file name :'+source_file
	while True:
		string2=f.readline()
		if string2 == '':
			break
		string2=str_process(string2,db)
		print string2
def get_dir_list(dir):  #input the dir ,will output the all filename
	dat0=[]
	for i in os.listdir(dir):
		dat0.append(i)
	return dat0
def all_file_process():
	dir_file_name=''
	dir_list=[]
	dir_file_name=raw_input('please input the dir name:')
	dir_list=get_dir_list(dir_file_name)
	print dir_list
	db=connect_mongodb()
	for i in dir_list:
		if str(i) != 'log_file_process.py':
			file_process(str(i),db)
	all_file_process()
def main():
	connect_mongodb()


if __name__=="__main__":
	main()