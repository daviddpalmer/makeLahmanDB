#! /usr/bin/python

# import os
import MySQLdb

# have already run these in shell:
# mysqld_safe --max_allowed_packet=128M &
# mysql -uroot
# CREATE DATABASE lahmandb
# USE lahmandb

# lahman2013.sql is in this dir

# connect to db
db = MySQLdb.connect("localhost","root","","lahmandb")
cursor = db.cursor()

# read in lahman2013 sql file and execute
for line in open('lahman2013.sql').read().split(';\n'):
    if line is not "":
        cursor.execute(line)
#        print '-->',line,'<--'

# uncomment here to test it
#cursor.execute("SELECT * FROM AllstarFull")
#vals = cursor.fetchall()
#print vals[1]
#

cursor.close()
