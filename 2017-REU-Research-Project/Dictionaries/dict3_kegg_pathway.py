from collections import defaultdict
"""
This script is to get the dict from kegg to pathway
"""
import pickle

file_name = "pathway"
file_object = open(file_name,'rb')
pathway = pickle.load(file_object)
print "Pathway dictionary: ", pathway

with open("kegg_pathway_txt.txt","wb") as myfile:
  for kv in pathway.items():
    for item in kv[1]:
      print >>myfile, kv[0],'\t',("\t".join(str(item) for item in kv[1]))

inv_kegg_pathway_d3 = defaultdict(set)
# make a reversed dictionaryinv_kegg_pathway_d3 = defaultdict(set)
for k,v in pathway.items():
  for i in v:
    inv_kegg_pathway_d3[i].add(k)
print inv_kegg_pathway_d3
pickle.dump(inv_kegg_pathway_d3,open("kegg_pathway_d3.pickle","wb"))
# make a file to store pathway to kegg
with open("pathway_to_kegg.txt","wb") as myfile:
  for kv in inv_kegg_pathway_d3.items():
    for item in kv[1]:    
      print >> myfile, kv[0],'\t',("\t".join(str(item) for item in kv[1]))
