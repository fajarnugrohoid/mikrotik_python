#!/usr/bin/env python

from RosAPI import Core

def prettify(data):
	for x in data:
		for y in x.keys():
			print "%-20s: %50s" % (y, x[y])

if __name__ == "__main__":
	a = Core("192.168.101.254")
	a.login("user1", "user")
	#a.run_interpreter()
	#prettify(a.response_handler(a.talk(["/tool/torch","=interface=ether2 - Lokal","=src-address=192.168.101.160","=dst-address=218.45.174.214"])))
	prettify(a.response_handler(a.talk(["/tool/torch","=interface=ether2 - Lokal","=src-address=192.168.101.160","=dst-address=0.0.0.0/0"])))
	#prettify(a.response_handler(a.talk(["/tool/torch","=interface=ether2 - Lokal","=src-address=192.168.101.160"])))