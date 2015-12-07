#coding=utf-8
import pandas as pd

robish=["Eyetracker Status","选项卡行","最大化","Baigle Search","启动眼动仪","开始实验","本次查询还需要看","您完成了一次查询，休息一下开始下一个查询","结束","下一个","这次查询对应1个文档","查询","irrelevance","localhost","SDK - Basic Eyetracking Sample","结束","选项卡行","最大化","Stop Tracking"]

def loadData():
	df = pd.read_csv("8.txt", header=None, sep='\t',names=["word","count","time","left","right","timestamp"],encoding='utf-8')#,keep_date_col =True
	print df
	
	

	validatedData=df[~df["word"].isin(robish)].dropna()

	for index, row in validatedData.iterrows():
		print row["word"]+"*"
	#print validatedData["word"]
	# for row in df.iterrows():
	# 	print row[1]

def main():
	loadData();
if __name__=="__main__":
	main()