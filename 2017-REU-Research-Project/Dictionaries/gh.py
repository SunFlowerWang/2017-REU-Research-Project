"""
usage: python gh.py a b
a: kegg id of metabolite
b: pathways (line by line) it belongs to, b can also be piped through standard input.
makes a pickled dictionary; meant to be used for batch processing of mutliple metabolite/pathways pairs
"""
def add_to_dictionary(d,key,lines) :
	for l in lines :
		d[key].add(l.rstrip())

if __name__ == "__main__" :
	from sys import argv, stdin
	from collections import defaultdict as df
	import pickle as p

	met = argv[1]

	lines = stdin
	if len(argv) > 2 :
		lines = open(argv[2],'r')
	
	dic = df(set)
	try :
		f = open('pathway')
		dic = p.load(f)
		f.close()
	except IOError :
		pass
	add_to_dictionary(dic,met,lines)
	f = open('pathway','w')
	p.dump(dic,f)
