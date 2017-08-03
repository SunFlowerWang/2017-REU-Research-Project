In the Dictionary directory, run command "source main.sh"
In the main.sh, a series of action will be excuted:
No.1: Parse the data from METLIN, and save the data into METLINDATA.txt
NO.2: Extract m/z values from the METLINDATA.txt
NO.3: Extract name of metabolites from METLINDATA.txt
No.4: Extract casID.txt from the MEtLINDATA.txt
NO.5: Using regular expression to get kegg ids correspend to the cas ids and save the data into casTOkegg.txt
NO.6: Run dict1_mz_cas.py and get a pickle dictionary and mz to cas text file
NO.7: Run dict2_cas_kegg.py and get a picke dictionary and cas to kegg text file
NO.8: Run mi.sh to get pathway
NO.9: Run dict3_kegg_pathway.py to get a pickle dictionary and pathway to kegg text file and a pathway to kegg.txt

Run python dictionary4 for futrue research

In the Cplex_java directory, we implement the colored set cover problem uinginteger linear programming.

In Cplex_java, we have 3 test cases, according to these test cases you can change the constraints. 

