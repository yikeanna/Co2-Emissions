#Anna Zhang
#260985734

def get_iso_codes_by_continent(filename):
    
    """
    (str)->dict
    
    The function returns a
    dictionary mapping continents’ names (all upper case) to a list of ISO codes (strings) of countries
    that belongs to that continent.
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> len(d['ASIA'])
    50
    >>> len(d['NORTH AMERICA'])
    23
    >>> d['AFRICA'][0]
    'NGA'
    >>> d['EUROPE'][2]
    'BLR'

    >>> len(d)
    6
    >>> d["EUROPE"][-1]
    'LVA'
    >>> d["SOUTH AMERICA"][:3]
    ['URY', 'COL', 'BRA']
    """
    fobj=open(filename, 'r', encoding="utf-8") #open file
    dct={}
    
    for line in fobj: #go line by line
        line_upper=line.upper().strip("\n") #change everything in the line to upper case, remove \n
        lst=line_upper.split("\t") #split the line by tabs into a list
        if lst[1]  in dct: #if the continent is already in the dictionary, add the country 
            dct[lst[1]].append(lst[0])
        else:
            dct[lst[1]]=list() #assign the continent ot a list
            
            dct[lst[1]].append(lst[0]) #add the continent to the list
    
    fobj.close() #close the file
    
    return dct

def add_continents_to_data(input_filename, continents_filename, output_filename):
    
    """
    (str,str,str)->int
    The function will read the input_filename, make changes to each of the
    lines and write the new version to output_filename. Don’t forget to open your files using the ’utf-8’
    encoding.
    The only change that should happen to the data is that in the output file a column should be added
    with the continent to which each country belongs. This should be the third column in the file, the
    one right after the name of the country. Note that there are some countries that are considered to
    be part of two continents. For these countries, write both continents separated by a comma.
    
    >>> add_continents_to_data("Anna_small_clean_co2_data.tsv", "iso_codes_by_continent.tsv","Anna_small_co2_data.tsv")
    10
    >>> add_continents_to_data("Anna_large_clean_co2_data.tsv", "iso_codes_by_continent.tsv","Anna_large_co2_data.tsv")
    17452
    
    >>> add_continents_to_data("ivoire_small_clean_co2_data.tsv", "iso_codes_by_continent.tsv","ivoire_small_co2_data.tsv")
    15
    
    >>> add_continents_to_data("owid_small_clean_co2_data.tsv", "iso_codes_by_continent.tsv","owid_small_co2_data.tsv")
    11
    
    """
    fobj=open(input_filename, 'r', encoding="utf-8") #open files
    fobj2=open(output_filename, 'w', encoding="utf-8")
    d=get_iso_codes_by_continent(continents_filename) #get dict of continent to list of countries(iso)
    count=0
    for line in fobj:
       lst_new_line=line.split("\t") #split the list into tabs
       iso_code=lst_new_line[0] #get the iso code
       cont=""
       for continent in d:# going through each continent
           if iso_code in d[continent]: #if the iso code is in the list of the continent
               if cont=="": #first continent in the list
                   cont+=continent
               else:
                   cont+=","+continent #follows after another continent(ASIA, EUROPE)
       lst_cont=[]
       lst_cont.append(cont) #add the list of continents
       lst_new_line[2:2]=lst_cont #add continent to list at index 2
       fobj2.write("\t".join(lst_new_line)) #write line including the continents this time
       count+=1 #count number of liens
    
    
    fobj.close() #close the files
    fobj2.close()
    return count

if __name__=="__main__":
    import doctest
    doctest.testmod()