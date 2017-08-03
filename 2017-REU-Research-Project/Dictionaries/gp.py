"""
useage: python gp.py f
f is a file that contains the feedback from kegg, e.g. for 
curl http://rest.kegg.jp/get/compound:C00002

prints out what the pathways are for this metabolite
can read standard input in addition to a file given as argument
"""

def get_pathways(lines):
	result = []
	for l in lines :
		if( l.split()[0] == "PATHWAY" ) :
			print(l.split()[1])
			g = (m for m in lines if 'map' in m)
			for m in g :
				print(m.split()[0])
			break

if __name__ == "__main__" :
	import fileinput
	get_pathways(fileinput.input())
