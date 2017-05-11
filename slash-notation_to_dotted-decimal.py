#!/usr/bin/env python

from sys import argv

slash_notation = ['/1','/2','/3','/4','/5','/6','/7','/8','/9','/10','/11','/12','/13','/14','/15','/16','/17','/18','/19','/20','/21','/22','/23','/24','/25','/26','/27','/28','/29','/30','/31','/32']
dotted_decimal_notation = [' 128.0.0.0',' 192.0.0.0',' 224.0.0.0',' 240.0.0.0',' 248.0.0.0',' 252.0.0.0',' 254.0.0.0',' 255.0.0.0',' 255.128.0.0',' 255.192.0.0',' 255.224.0.0',' 255.240.0.0',' 255.248.0.0',' 255.252.0.0',' 255.254.0.0',' 255.255.0.0',' 255.255.128.0',' 255.255.192.0',' 255.255.224.0',' 255.255.240.0',' 255.255.248.0',' 255.255.252.0',' 255.255.254.0',' 255.255.255.0',' 255.255.255.128',' 255.255.255.192',' 255.255.255.224',' 255.255.255.240',' 255.255.255.248',' 255.255.255.252',' 255.255.255.254',' 255.255.255.255']


def conversion(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            for x in reversed(range(32)):
                if slash_notation[x] in line:
                    print(line.strip().replace(slash_notation[x],dotted_decimal_notation[x]))
                    break
def single_ip(ip):
	for x in reversed(range(32)):
        	if slash_notation[x] in ip:
                	print(ip.strip().replace(slash_notation[x],dotted_decimal_notation[x]))
			break


if len(argv) == 2 and len(argv) < 3:
	script, file_name = argv
	try:
		conversion(file_name)
	except Exception as e:
		print "Please enter a valid file name"
elif len(argv) == 3:
	script, ip, ip_address = argv
	if argv[1] == "-ip":
		try:
			single_ip(ip_address)	
		except Exception as e:
			print e
else:  
	print "Requires an argument"
