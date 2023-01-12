#!/usr/bin/python

import sys

f = open('vpcflow.txt', 'r')
logs = f.readlines()
f.close()

# Get headers row
headers_row = logs[0]
fields = headers_row.split()

# Build out dictionary to reference logs
logs_dictionaries = []
for l in logs[1:]:
    record = {}
    line = l.split()
    col_count = 0
    for field in fields:
        record[field] = line[col_count]
        col_count = col_count + 1
    logs_dictionaries.append(record)

# Build out NACLs
