#!/bin/bah
#keep refreshing casID.txt
cat /dev/null > casID.txt

# command for parse the metlin website
python2 parse.py .*html > METLINDATA.txt
#this program's goal is to get cas ids from the METLIN webpage
sed 's/[\t ][\t ]*/ /g' < METLINDATA.txt | cut -d' ' -f2 > mz_value.txt

sed 's/[\t ][\t ]*/ /g' < METLINDATA.txt | cut -d' ' -f6 > name.txt


sed 's/[\t ][\t ]*/ /g' < METLINDATA.txt | cut -d' ' -f8 > casID.txt


#> casID.txt
#-d' ' -mean, use space as a delimiter
#-f -take and print 8th column
# cut is much faster for large files as a pure shell solution
# sed will replace any tab or space characters with a single space
#cut -d' ' -f8 dataOutput.txt > casID.txt

#cas id to kegg id
cat /dev/null >casTOkegg.txt
#regularEpression to get kegg id
regEpress1=".result.:[[:space:]]+[^]]+"
regEpress2="(.C[0-9]+.[[:space:]]+)+"
regEpress3="(C[0-9]+)"
for i in $(cat casID.txt); do
if [[ $(curl http://cts.fiehnlab.ucdavis.edu/service/convert/cas/kegg/$i) =~ $regEpress1 ]]; then
        if [[ ${BASH_REMATCH[0]} =~ $regEpress2 && ${BASH_REMATCH[0]} =~ $regEpress3 ]]; then
            echo $i, ${BASH_REMATCH[0]} >> casTOkegg.txt #save kegg id to a file
        fi
    fi
done 

#make the dictionary 1
python dict1_mz_cas.py

#get kegg ids
sed 's/[\t ][\t ]*/ /g' < casTOkegg.txt | cut -d' ' -f2 > keggID.txt

#make the dictionary2
python dict2_cas_kegg.py

# run mi.sh 
#source mi.sh

#make the dictionary3
python dict3_kegg_pathway.py

