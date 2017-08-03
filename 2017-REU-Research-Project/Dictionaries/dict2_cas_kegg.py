"""
  get the dictionary between cas and kegg
  and the pickled
"""
import pickle

with open("casID.txt","rb") as myfile:
  cas_id_list = myfile.read().splitlines()
print "cas_id_lidt",cas_id_list

with open("keggID.txt","rb") as myfile:
  kegg_id_list = myfile.read().splitlines()
print "kegg_id_list",kegg_id_list

cas_kegg_dict = dict(zip(cas_id_list,kegg_id_list))
print "cas_kegg_dict",cas_kegg_dict

pickle.dump(cas_kegg_dict,open("cas_kegg_dict_save.pickle","wb"))

with open("cas_kegg_dict_txt.txt","wb") as myfile:
  for kv in cas_kegg_dict.items():
    print >>myfile, kv[0],'\t',kv[1]

