# -*- coding: utf-8 -*-

import csv


print "| Label id | Chinese label | English label |"
print "|   ---:   | ------------- | ------------- |"
print "| 999 | 非以下分类 | none_of_below |"

with open('original/scene_classes.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
        print "| %s | %s | %s |" % (row[0], row[1], row[2])

