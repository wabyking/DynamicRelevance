#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("dataSet.xml")
collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")

# 在集合中获取所有电影
records = collection.getElementsByTagName("record")
print len(records)
# 打印每部电影的详细信息
for record in records:
   print "record"
   print record
   # if movie.hasAttribute("title"):
   #    print "Title: %s" % movie.getAttribute("title")

   # type = movie.getElementsByTagName('type')[0]
   # print "Type: %s" % type.childNodes[0].data
   # format = movie.getElementsByTagName('format')[0]
   # print "Format: %s" % format.childNodes[0].data
   # rating = movie.getElementsByTagName('rating')[0]
   # print "Rating: %s" % rating.childNodes[0].data
   # description = movie.getElementsByTagName('description')[0]
   # print "Description: %s" % description.childNodes[0].data
   print str( record.getElementsByTagName("id") [0].childNodes[0].data)+": query" +record.getElementsByTagName("query")[0].childNodes[0].data#+ " description"+record.getElementsByTagName("description")[0].data+ " d1:"+ record.getElementsByTagName("d1")[0].data+"d2:"+record.getElementsByTagName("d2")[0].data