#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "SewellDinG"

"""
typecho pages 提取 md 并另存到本地
"""

import time
import codecs
import pymysql


db = pymysql.connect(host="ip", user="root", password="pass", database="typecho")
cursor = db.cursor()
sql = "SELECT * FROM typecho_contents WHERE typecho_contents.type = 'post';"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        title = row[1]
        created = row[3]
        text = row[5]
        title = title.replace("/", " ")
        title = title.replace("&amp;", "&")
        ctime = time.strftime("%Y-%m-%d", time.localtime(created))
        file_name = ctime + '-' + title + '.md'
        fw = codecs.open(file_name, "wb", "utf-8")
        fw.write(text)
        fw.close()
        print(file_name)
        # print("title=%s,created=%s,text=%s" % (title, created, text ))
except:
    print("Error: unable to fetch data")
db.close()
