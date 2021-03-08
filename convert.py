import os
import sys

i = 1
# f = open("train.tsv","r", encoding='utf8')
# copy = open("train1.tsv","wt",encoding='utf8')
f = open("dev.tsv","r", encoding='utf8')
copy = open("dev1.tsv","wt",encoding='utf8')
# f = open("test.tsv","r", encoding='utf8')
# copy = open("test1.tsv","wt",encoding='utf8')
#loop that copies file line by line and terminates loop when i reaches 10
lines= f.readlines()
for line in lines:
     new = f"vietnamese	twenties	1	0	male	wav	{line[:-1]}	1\n"
     copy.write(new,)
f.close()
copy.close()
