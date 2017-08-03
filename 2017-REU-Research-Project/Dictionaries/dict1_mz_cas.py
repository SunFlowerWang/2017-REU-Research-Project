"""
This script is for map the connections between m/z and cas
get a pickled dictionary from m/z to cas
get a text file with two columns, one is the m/z values and the other is cas ids
"""
import pickle

# put all the m/z values into mz_list
with open("mz_value.txt","r") as myfile:
  mz_list = myfile.read().splitlines()
print ("mz_list: ", mz_list)
print()

# put all the cas ids into cas_ids_list
with open("casID.txt","r") as myfile:
  cas_ids_list = myfile.read().splitlines()
print ("cas_ids_list: ", cas_ids_list)
print()

# create the dictionary key as m/z values and values as cas ids
mz_cas_dict = dict(zip(mz_list,cas_ids_list))
print ("mz_cas_dict: ", mz_cas_dict)

#save the mz_cas_dict into a pickle dictionary
pickle.dump(mz_cas_dict,open("mz_cas_dict_save.pickle","wb"))

# put this dictionary into a formated txt file
with open("mz_cas_dict_txt.txt","wb") as myfile:
  for k, v in mz_cas_dict.iteritems():
    print >>myfile, k+"\t",v

