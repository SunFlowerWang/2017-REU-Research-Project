import pickle
from collections import defaultdict

file_name1 = "mz_cas_dict_save.pickle"
file_name2 = "cas_kegg_dict_save.pickle"
file_name3 = "kegg_pathway_d3.pickle"

file_object1 = open(file_name1,'r')
file_object2 = open(file_name2,'r')
file_object3 = open(file_name3,'r')

mz_cas_d1 = pickle.load(file_object1)
cas_kegg_d2 = pickle.load(file_object2)
kegg_pathway_d3 = pickle.load(file_object3)

print kegg_pathway_d3

invert_cas_mz_d1 = {v:k for k,v in mz_cas_d1.items()}
print "invert_cas_mz_d1:"
for k,v in invert_cas_mz_d1.items():
  print k, v
print
invert_kegg_cas_d2 = {v:k for k,v in cas_kegg_d2.items()}
print "cas to kegg d2:"
for k,v in cas_kegg_d2.items():
  print k,v
print "invert_kegg_cas_d2:"
for k,v in invert_kegg_cas_d2.items():
  print k,v
invert_pathway_kegg_d3 = defaultdict(set)
for k, v in kegg_pathway_d3.items():
  for i in v:
    invert_pathway_kegg_d3[i].add(k)

print "invert_pathway_kegg_d3:"
for k,v in invert_pathway_kegg_d3.items():
  print k,v
    

print "kegg to pathway:"
for k,v in kegg_pathway_d3.items():
  print k,v
#get the keys of the invert_pathway_kegg_d3
keys = invert_pathway_kegg_d3.keys()
print "the pathway: ", keys

#when geting a list of kegg ids
value = invert_pathway_kegg_d3.values()
print "keggID", value
value1_list = [] # a list of kegg ids
for item in value:
  element = list(item)
  value1_list.append(element[0])
print "keggID from invert_pathway_kegg_d3: ", value1_list

holding_list = []
for i in value1_list:
  if i in holding_list:
    pass
  else:
    holding_list.append(i)
print "holding_list", holding_list

wanted_cas = []
match_mz = []
for kv in invert_kegg_cas_d2.items():
  for j in holding_list:
    if kv[0] == j:
      print kv[0],'\t',kv[1]
      wanted_cas.append(kv[1])
print "wanted cas: ", wanted_cas

wanted_mz = []
for kv in invert_cas_mz_d1.items():
  for cas in wanted_cas:
    if kv[0] == cas:
      print kv[0],'\t',kv[1]
      wanted_mz.append(kv[1])
print "matached mz values: ", wanted_mz


