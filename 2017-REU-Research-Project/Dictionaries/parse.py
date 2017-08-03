from sys import argv
import xml.etree.ElementTree as ET
f = open('batch_search_result.html','r')
st = f.read();
tables = []

def getTag(tag,endtag,st):
    i = 0
    all_strings = []
    while i < len(st) - len(tag) :
        if( cmp(st[i:i+len(tag)],tag) == 0) :
            first = i
            while( cmp(st[i:i+len(endtag)],endtag) != 0 ) :
                i+=1
            last = i+len(endtag)
            all_strings.append(st[first:last])
        i+=1
    return all_strings

def output( inputmass, adduct, data ) :
	mass,dppm,name,formula,cas,msms = [ t[4:-5] for t in getTag("<td","</td>",r) ]
	cas = getTag(">","<",cas + "<")[0][1:-1]
	molid = getTag("<a","</a>",data)[0]
	molid = getTag(">","<",molid)[0][1:-1]
	kegg = "kegg"
	msms = "msms"
	lnk = "lnk"
	print( "\t".join([molid,inputmass,adduct,mass,dppm,name,formula,cas,kegg,msms,lnk]) )

# find tables
tables = getTag("<table","</table>",st)
for t in tables :
    rows = getTag("<tr","</tr>",t)
    header = getTag("<h4","</h4>",t)
    adduct = getTag("Metabolites [","]",t)
    if header :
    	m = getTag(">","m/z",header[0])[0][1:-3]
    if adduct :
	    a = adduct[-1][len("Metabolites"):]
    for r in rows :
	    if  len( getTag("<td","</td>",r) )  == 6 :
		    output( m , a, r )
f.close()
