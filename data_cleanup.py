#Anna Zhang
#260985734

def find_delim(txt):
    
    """
    (str)-> str
    
    returns the most commonly used delimiter in the input string
    
    >>> find_delim("0 1 2 3,4")
    ' '
    >>> find_delim("cat\\tdog bat\\tcrab-cod")
    '\\t'
    
    >>> find_delim(", -\\t-")
    '-'
    >>> find_delim(", -\\t-    \\t")
    ' '
    >>> find_delim(", -\\t-aaa\\ta\\t")
    '\\t'
    
    """
    delim_lst=["\t", ",", " ", "-"]
    lst=[]
    for delim in delim_lst: #iterate through each delimiter
        if delim in txt:
            lst.append(txt.count(delim)) #count the occurence of the delimiter
        else:
            lst.append(0) #if the delimiter is not in the text
            
    max_num=max(lst) #find the most common delimiter with occurence
    if max_num==0: #if theres no common delimiter
        raise AssertionError('no tab/comma/space/dash in the string')
    return delim_lst[lst.index(max_num)] #return the delimiter using index 

def clean_one(filename1, filename2):
    
    """
    (str, str) -> int
    
    read the input_filename, make changes to each of the lines and write the new
    version to output_filename.The only change that should happen to the data is that in
    the output file all lines should have a tab as a delimiter in place of which ever
    delimiter each line originally had.The function should return an integer indicating
    the number of lines written to output_filename.
    
    >>> clean_one('small_raw_co2_data.txt', 'Anna_small_tab_sep_co2_data.tsv')
    10
    >>> clean_one('large_raw_co2_data.txt', 'Anna_large_tab_sep_co2_data.tsv')
    17452
    
    >> clean_one('owid_small_raw_co2_data.txt', 'owid_small_tab_sep_co2_data.tsv')
    15
    >>> clean_one('RUS_small_raw_co2_data.txt', 'RUS_small_tab_sep_co2_data.tsv')
    15
    >>> clean_one('ivoire_small_raw_co2_data.txt', 'ivoire_small_tab_sep_co2_data.tsv')
    5
    
    """
    fobj=open(filename1, 'r', encoding="utf-8") #open files
    fobj2=open(filename2, 'w', encoding="utf-8")
    count=0
    for line in fobj: #go line by line in file 1
        delim=find_delim(line) #find the delimiter of the line
        new_line=line.replace(delim, "\t") #replace the delimiter by a tab
        fobj2.write(new_line) #write the new line seperated with a tab in the new file 2
        count+=1 #count the number of lines
     
    fobj.close()
    fobj2.close()
    
    return count #return the number of lines in file 2


def final_clean(filename1, filename2):
    """
    (str, str) -> int
    The function will read the input_filename, make changes to each of the lines and write the new
    version to output_filename.
    
    – All lines should have exactly 5 columns. From the changes that took place in the previous
    function we now might have lines with more than 5 columns. For examples, lines in which the
    co2 emissions were reported using commas and the delimiter was also a comma will now have
    6 columns instead of 5. To find other cases in which the columns might have increased, please
    check the files provided and make sure to account for all of them. The only ways in which a
    line might end up with more than 5 columns are all found in the files provided
    -All commas which are used to indicate decimal numbers should be replaced with dots.
    
    The function should return an integer indicating the number of lines written to output_filename.
    
    >>> final_clean('Anna_small_tab_sep_co2_data.tsv', 'Anna_small_clean_co2_data.tsv')
    10
    >>> final_clean('Anna_large_tab_sep_co2_data.tsv', 'Anna_large_clean_co2_data.tsv')
    17452
    
    
    >>> final_clean('owid_small_tab_sep_co2_data.tsv', 'owid_small_clean_co2_data.tsv')
    11
    >>> final_clean('RUS_small_tab_sep_co2_data.tsv', 'RUS_small_clean_co2_data.tsv')
    15
    >>> final_clean('ivoire_small_tab_sep_co2_data.tsv', 'ivoire_small_clean_co2_data.tsv')
    15
    """
    fobj=open(filename1, 'r', encoding="utf-8") #open files
    fobj2=open(filename2, 'w', encoding="utf-8")
    count=0
    for line in fobj:
        if line!="\n": #if its not the last line 
            new_line=line.replace(",", ".") #replace the commas with a dot
            lst_new_line=new_line.split() #seperate the words in the line into a list
            lst_fin=[]
            lst_alpha_num=[]
            #add iso
            lst_fin.append(lst_new_line[0])
            
            #CHECKS AFTER 2 INDEX TO SEE IF COUNTRY CONTAINS MORE THAN TWO WORDS(3RD COLUMN)
            for word in lst_new_line[2:]:
                    if not word[0].isdecimal(): #if its a word
                        lst_alpha_num.append(1)
                    else: #if its a number
                        lst_alpha_num.append(0)

            #counts number of occurence of alpha and number
            num_alpha=lst_alpha_num.count(1)
            num_num=lst_alpha_num.count(0)
              
            #PART A:FIND COUNTRY NAME
            #if country has more than two words
            if num_alpha>0:
                
                last_index_alpha=lst_alpha_num.index(0) #find the last index of the word in the list
                country=" ".join(lst_new_line[1:last_index_alpha+2]) #form the country name
            
            else:
                country=lst_new_line[1] #country has only one word
            
            
            #PART B:SEPERATE VALUES OF YEAR, CO2 AND POPULATION
            #assign year
            first_index_num=lst_alpha_num.index(0)
            year=lst_new_line[2+first_index_num]
            #create list of co2 and population
            co2_pop_lst=lst_new_line[3+first_index_num:]
            if len(co2_pop_lst)==0: #if theres no data for co2 or population
                co2=""
                pop=""
            elif len(co2_pop_lst)==1: # either co2 or population is the value and the other value is empty
                if co2_pop_lst[0]==str(float(co2_pop_lst[0])): #if the first element is a float
                    co2=co2_pop_lst[0]
                    pop=""
                else: #if the first element is not a float, then the value represents the population
                    co2=""
                    pop=co2_pop_lst[0]
            elif len(co2_pop_lst)==2:
                if new_line[-2:]!="\t\n": #if there is no delimiter at the end of the string, then its a
                                            #a co2 and a population
                    co2=co2_pop_lst[0]
                    pop=co2_pop_lst[1]
                else: #if there is a delimiter at the end, then its a co2 with the numbers seperated by a tab
                    co2=co2_pop_lst[0]+"."+co2_pop_lst[1]
                    pop=""

            elif len(co2_pop_lst)==3: #if there is 3 numbers, then is a co2 with the integer and the
                                        #decimal seperated, plus the population

                co2=co2_pop_lst[0]+"."+co2_pop_lst[1] #join with a dot
                pop=co2_pop_lst[2]

            lst_fin.append(country) #assign country
            lst_fin.append(year) #assign year
            lst_fin.append(co2) #assign co2
            lst_fin.append(pop) # assign population
            fobj2.write("\t".join(lst_fin)+"\n") # write the line joining the list with a tab and a
                                                     #newline at the end
            count+=1 #count the number of lines
            
    fobj.close() #close files
    fobj2.close()
    return count #return number of lines

if __name__=="__main__":
    import doctest
    doctest.testmod()