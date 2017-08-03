CFILE=$1
for i in $(cat $CFILE); do
	curl http://rest.kegg.jp/get/compound:$i | python gp.py | python gh.py $i
done
