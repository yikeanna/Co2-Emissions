#Anna Zhang
#260985734
from build_countries import*
import matplotlib.pyplot as plt

def reorder_d(d):
    
    """
    (dict)->dict
    
    sorts the dictionary
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> d=reorder_d(d1)
    >>> len(d)
    4

    """
    country_id_list=[]
    
    for iso in d:
        country_id_list.append(d[iso])#create a new list
    d_cont_to_country_id_list=Country.get_countries_by_continent(country_id_list) #create dictionary
    t=list(d_cont_to_country_id_list.items()) #sort out the tuple
    t.sort()
    sorted_d_cont_to_country_id_list=dict(t)
    new_d={}
    for cont in sorted_d_cont_to_country_id_list:
        if cont=="SOUTH AMERICA":
            new_d["S.AMERICA"]=sorted_d_cont_to_country_id_list[cont] #change name of the continent to shorten it
        elif cont=="NORTH AMERICA":
            new_d["N.AMERICA"]=sorted_d_cont_to_country_id_list[cont]
        else:
            new_d[cont]=sorted_d_cont_to_country_id_list[cont] #map continent to country id
    return new_d

#1
def get_bar_co2_pc_by_continent(d, year):
    
    
    """

    (dict, int)-> list
    
    The function should
    create a bar plot representing the co2 emissions per capita (in tonnes) produced by all the countries
    in each continent. The bars should appear in alphabetical order, and the function should return a
    list of the values being plotted
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2001)
    [0.20320332558992543, 67.01626016260163, 7.6609004739336495, 1.4196063588190764]
    
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d2, 2000)
    >>> len(data)
    6
    >>> data[0] # AFRICA
    1.0975340644568221
    >>> data[3] # N. AMERICA
    14.739682155717826
    >>> round(data[4], 5) # OCEANIA
    12.66302
    
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d2, 1995)
    >>> len(data)
    6
    >>> data[2]
    8.334256467186048
    >>> data[5]
    2.1235314020008627
    
    >>> data = get_bar_co2_pc_by_continent(d2, 2018)
    >>> data
    [1.0993516243804746, 4.62860868275246, 7.42451368347044, 11.473453064132114, 11.48512022073315, 2.62922614131065]

     """
    continents=[]
    lst_values=[]
    new_d=reorder_d(d) #reorder dictionary
    for cont in new_d:
        #get value of total co2 emissions per capita by year
        value_tot_co2_emissions_per_capita_by_year= Country.get_total_co2_emissions_per_capita_by_year(new_d[cont],year) 
        continents.append(cont) #append name of the continent to the list
        lst_values.append(value_tot_co2_emissions_per_capita_by_year) #append the value to the list
    
    
    #graph
    plt.ylabel("co2(in tonnes)")
    plt.bar(continents,lst_values)
    plt.title("CO2 emissions per capita in "+ str(year) +" by anna.zhang@mail.mcgill.ca")
    plt.savefig("co2_pc_by_continent_"+str(year)+".png")
    plt.show()
    return lst_values


#2
def get_bar_historical_co2_by_continent(d,year):
    
    """

    (dict, int)-> lst
    
    The function
    should create a bar plot representing the historical co2 emissions (in millions of tonnes) produced by
    all the countries in each continent. The bars should appear in alphabetical order, and the function
    should return a list of the values being plotted
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2015)
    [4.877, 207.54500000000002, 359.367, 149.34300000000002]


    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 1990)
    >>> len(data)
    6
    >>> round(data[2],4) # EUROPE
    334210.701
    >>> round(data[4],5) # OCEANIA
    8488.463



    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 2018)
    >>> len(data)
    6
    >>> round(data[1], 5) # ASIA
    585465.903
    >>> round(data[4], 5) # OCEANIA
    19845.01
    
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2000)
    [0.0, 0.0, 0.0, 0.0]
    
    
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 2000)
    >>> data
    [23526.186, 280013.2760000001, 404139.4419999999, 338457.92800000013, 11935.638999999997, 22493.824]
    
    
    """
    
    continents=[]
    lst_values=[]
    
    new_d=reorder_d(d)      #order dictionary    
    for cont in new_d:        
        value_historical_co2_by_continent=\
        Country.get_total_historical_co2_emissions(new_d[cont],year) # get total historical co2 emissions
        continents.append(cont) #append country name
        lst_values.append(value_historical_co2_by_continent) #append value
    #graph 
    plt.bar(continents,lst_values)
    plt.ylabel("co2 (in millions of tonnes)")
    plt.title("Historical CO2 emissions up to "+ str(year) +" by anna.zhang@mail.mcgill.ca")
    plt.savefig("hist_co2_by_continent_"+str(year)+".png")
    
    plt.show()
    return lst_values

#3
def get_bar_co2_pc_top_ten(d,year):
    
    """
    (dict, int)->list
    
    The function should
    create a bar plot representing the co2 emissions per capita (in tonnes) produced by the top 10
    producing countries in the dictionary (if the dictionary contains less than 10 countries, then you
    should graph all of them). The bars should appear in order of co2 produced, and the function
    should return a list of the values being plotted
        
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2001)
    >>> len(data)
    5
    >>> data[0]
    67.01626016260163
    >>> data[4]
    0.20320332558992543

    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 2000)
    >>> len(data)
    10
    >>> data[0] # QAT
    58.388513513513516
    >>> data[4] # USA
    21.288834407209247
    >>> data[9] # SAU
    14.341511807975223
    
    >>> data=get_bar_co2_pc_top_ten(d2, 2011)
    >>> data==[39.11984282907662, 35.03517964071856, 27.22948232323232, 24.225888324873097,\
    22.407668231611893, 21.41233140655106, 18.90857270593495, 17.936995296832016, 17.88469561980076, 17.60503042309325]
    True
    
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 1800)
    >>> data[0]
    2.1605413472647177
    
    """
    isos=[]
    lst_values=[]
    
    d_id_to_co2={}
    for iso in d:
        country_id=d[iso] #get country object
        co2_per_capita_by_year=country_id.get_co2_per_capita_by_year(year) #calculate co2 per capita
        d_id_to_co2[country_id]=co2_per_capita_by_year #map country object to value
    d_no_none={} #dictionary that removes none value
    for country_id in d_id_to_co2:
        if d_id_to_co2[country_id]!=None: #remove none for country object that return none
            d_no_none[country_id]=d_id_to_co2[country_id]
    t=Country.get_top_n(d_no_none, 10) #change into a tuple to reorder the dictionary
    
    for name, co2 in t:
        isos.append(name) #add iso to list
        lst_values.append(co2) #add values to list
    
    #graph
    plt.bar(isos,lst_values)
    plt.ylabel("co2 (in tonnes)")
    plt.title("Top 10 countries for CO2 emissions pc in "+ str(year) +" by anna.zhang@mail.mcgill.ca")
    plt.savefig("top_10_co2_pc_"+str(year)+".png")
    plt.show()
    
    return lst_values

#4
def get_bar_top_ten_historical_co2(d,year):
    
    """
    (dict,int)->list
    
    The function should
    create a bar plot representing the historical co2 emissions (in millions of tonnes) produced by the
    top 10 producing countries in the dictionary (if the dictionary contains less than 10 countries, then
    you should graph all of them). The bars should appear in order of co2 produced, and the function
    should return a list with the values being plotted.

    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_top_ten_historical_co2(d1, 2015)
    [306.696, 166.33, 149.34300000000002, 48.923, 41.215, 3.748, 3.324, 1.553, 0.0]
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 2018)
    >>> len(data)
    10
    >>> round(data[0],5) # USA
    404769.397
    >>> data[1] # CHN
    210201.179
    >>> round(data[8],5) # CAN
    32517.775

    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data=get_bar_top_ten_historical_co2(d2,2000)
    >>> data==[301943.7180000001, 76220.11699999997, \
    72805.80799999999, 71940.95700000002, 68459.44400000003, 41015.341, 31048.06799999999, 22219.773000000023, 21392.696000000007, 20727.115]
    True
        
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data= get_bar_top_ten_historical_co2(d2,2020)
    >>> data== [404769.39699999994, 210201.179, 100720.35800000001, \
    91300.31399999997, 77448.89600000001, 63517.21400000001, 51196.387000000024, 37952.874, 32517.775000000034, 27232.40300000002]
    True
    """
    isos=[]
    lst_values=[]
    
    d_id_to_co2={}
    for iso in d:
        country_id=d[iso]  #find country_id
        country_historical_co2=country_id.get_historical_co2(year) #vvalue for historical co2 until the year
        d_id_to_co2[country_id]=country_historical_co2 #create dictionary that maps from country object to value
    t=Country.get_top_n(d_id_to_co2, 10) #slice the tuple
    
    for name, co2 in t:
        isos.append(name) #add iso
        lst_values.append(co2) #add value
    
    #graph
    plt.bar(isos,lst_values)
    plt.ylabel("co2 (in millions of tonnes)")
    plt.title("Top 10 countries for historical CO2 up to "+ str(year) +" by anna.zhang@mail.mcgill.ca")
    plt.savefig("top_10_hist_co2_"+str(year)+".png")
    plt.show()
    
    return lst_values

def get_plot_co2_emissions(d,iso_codes, min_year, max_year):
    
    
    """
    (dict, list, int, int)->list
    
    The function should plot the co2 emissions of the selected countries (those whose
    ISO code appears in the input list) from min_year to max_year. You should use a different style
    for each line plotted (it’s up to you to choose the style), and you should plot a maximum of 10-11
    data points (to keep the plot readable). To do that, plot the data of the years from min_year to
    max_year using a step obtained by taking the number of total years and dividing it by 10. The
    function should return a 2D list. Each sublist should contain the co2 emission of a selected country
    from min_year to max_year. The position of the sublists should match the position of the ISO code
    in the input list
    (dict,list,int, int)->list
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1990, 2000)
    >>> len(data)
    5
    >>> len(data[1]) # CHN
    11
    >>> data[0][:5] # USA
    [5121.179, 5071.564, 5174.671, 5281.387, 5375.034]
    >>> d2 = get_countries_from_file("Anna_large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> len(data[0]) # USA
    201
    >>> data[2][4] # RUS
    0.0
    >>> data[4][190] # GBR
    600.773
    >>> data[3][200] # DEU
    900.376
    
    >>> data=get_plot_co2_emissions(d2, ["TZA", "NLD", "PER"], 1903, 2000)
    >>> data[0][14]
    0.0
    
    >>> data[2][15]
    1.946
    
    >>> data=get_plot_co2_emissions(d2, ["VNM", "IRN", "GBR","AUT","MEX"], 1955, 2015)
    >>> len(data[0])
    61
    """
    
    
    leap=round((max_year-min_year)/10) #leap between values(total of 10-11)
    country_id_list=[]
    style=["v:c",".-r",",--y","v-.g","<:b",".-c",",--k","v-.m",\
           "<:m",".--b",",-k"] #style for lines on graph
    lst=[]
    countries_co2_lst=[]
    i=0
    for iso in iso_codes:
        
        if iso in d:
            country_id_list.append(d[iso])#add country object
    
    for country_id in country_id_list:
        d_year_to_co2=country_id.co2_emissions #dictionary of year to co2
        x_coord=[]
        y_coord=[]
        top=min_year
        #useful if top(year) is not in the dictionary)
        year_up=top+1
        year_down=top-1
        
        while top<=max_year: #loop until top is bigger than max_year
            if top in d_year_to_co2: 
                x_coord.append(top)
                y_coord.append(d_year_to_co2[top])
                top+=leap
            
            else: #if year is not in the dictionary
                
                if year_up in d_year_to_co2 and not year_up>max_year: #checks that year_up is bigger than min_year and if its in dictionary
                    #add year and value
                    x_coord.append(year_up)
                    y_coord.append(d_year_to_co2[year_up])
                    top+=leap #go to the next jump
                elif year_down in d_year_to_co2 and not year_down<min_year:
                    x_coord.append(year_up)
                    y_coord.append(d_year_to_co2[year_down])
                    top+=leap
                else:
                    year_up+=1 #look for next year
                    year_down-=1 #look for year before
        
        lst.append(y_coord) #add year
        plt.plot(x_coord,y_coord,style[i]) #plot data of the country
        i+=1

        country_co2_lst=[]
        time=min_year
        while time<=max_year: # loop  must stop when time is max_year
            if time in country_id.co2_emissions: #if time is in the dictionary
                country_co2_lst.append(country_id.co2_emissions[time])
            else: #if the time is not present in the dictionary, add 0.0
                country_co2_lst.append(0.0)
            time+=1
        countries_co2_lst.append(country_co2_lst) 
      
    #graph
    plt.ylabel("co2 (in millions of tonnes)")
    plt.title("CO2 emissions between "+ str(min_year)+" and "+ str(max_year) +" by anna.zhang@mail.mcgill.ca")
    plt.legend(iso_codes)
    plt.savefig("co2_emissions_"+str(min_year)+"_"+str(max_year)+".png")
    plt.show()

    return countries_co2_lst

if __name__=="__main__":
    import doctest
    doctest.testmod()