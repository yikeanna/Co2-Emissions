#Anna Zhang
#260985734
import copy
class Country: #create class Country
    min_year_recorded=10000000 #min_year_recorded will change depending on the output
    max_year_recorded=-100000000 #max_year_recorded will change depending on the output
    
    def __init__(self, iso_code,name,  continents,year, co2_emissions, population):
        
        """
        (Country,str, str, list, dct{int:float}, dct{int:int})
        
        A constructor that takes as input two strings (the iso code and the name of the country respectively),
        a list (the continents to which the country belongs), and integer (indicating the year in which the
        following data has been recorded), a float (indicating the co2 emissions of the country in the specified
        year in millions of tonnes), and a integer (indicating the population of the country in the specified
        year). The constructor uses these input to initialize all the instance attributes accordingly
        
        >>> b = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, -1)
        >>> b.population
        {}
        >>> b.co2_emissions
        {}
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.continents
        ['ASIA', 'EUROPE']
        >>> r.population
        {2007: 14266000}
    
        """
        #change min and max year accordingly
        if year <Country.min_year_recorded:
            Country.min_year_recorded=year
            
        if year>Country.max_year_recorded:
            Country.max_year_recorded=year
        
        if len(iso_code)!=3 and iso_code!='OWID_KOS': #check if its a valid iso
            raise AssertionError('the iso code is invalid')
        
        #initialize instance attributes
        self.iso_code=iso_code
        
        self.name=name
        
        #create a copy of the list
        self.continents=[]
        for continent in continents:
            self.continents.append(continent)
        
        # create a dictionary from year to co2
        self.co2_emissions={}
        if co2_emissions!=-1: #do not put year to co2 in dictionary if co2 is -1
            self.co2_emissions[year]=co2_emissions
        
        
        #create a dictionary from year to population
        self.population={}
        
        if population!=-1: #do not put year to population in dictionary if population is -1
            self.population[year]=population

    def __str__(self):
        
        """
        
        (Country)-> str
        
        str__ method that returns a string representation of a country containing the name, the
        continents (separated by a comma if more than one), and a string representation of both the
        co2_emissions dictionary and the population dictionary. Each piece of information in the string
        should be separated by a tab.
        
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> str(b)
        'Albania\\tEUROPE\\t{2007: 3.924}\\t{2007: 3034000}'
        >>> c = Country("ALB", "Albaadfdfsnia", ["EUROPE,ASIA"], 2020, -1, -1)
        >>> str(c)
        'Albaadfdfsnia\\tEUROPE,ASIA\\t{}\\t{}'
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> str(a)
        'Afghanistan\\tASIA\\t{1949: 0.015}\\t{1949: 7663783}'
        
        """
        continents=""
        #create continents
        for continent in self.continents:
            if continents=="":
                continents+=continent
            else:
                continents+=","+continent
        #return string of continents
        return self.name+"\t"+continents+'\t'+str(self.co2_emissions)+'\t'+str(self.population)

    def add_yearly_data(self,txt):
        
        """
        (Country,str)->Nonetype
        
        This method updates the appropriate attributes of
        the country. Note that if the co2 emission or the population data is an empty column, then no
        changes should be made to the corresponding attribute. Note also that this method should make
        sure to update min_year_recorded and max_year_recorded if need be.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True
        >>> a.population == {1949: 7663783, 2018: 37122000}
        True
        >>> c = Country("ALB", "Albaadfdfsnia", ["EUROPE,ASIA"], 2007, -1, -1)
        >>> c.add_yearly_data("2018\\t9.439\\t37122000")
        >>> c.population
        {2018: 37122000}
        >>> c.co2_emissions
        {2018: 9.439}
        >>> q = Country("QAT", "Qatar", ["ASIA,AFRICA"], 2007, -1, 1218000)
        >>> q.add_yearly_data("1988\\t\\t")
        >>> q.population
        {2007: 1218000}
        >>> q.co2_emissions
        {}
                

        """
    
        #create a list of the text
        lst=txt.split("\t")
        year=int(lst[0]) #assign year
        if lst[1]!='': #if theres a value for co2
            co2_emissions=float(lst[1]) #create a float(not a string)
            self.co2_emissions[year]=co2_emissions
        if lst[2]!='': #if theres a value for population
            population=int(lst[2]) #create an integer
            self.population[year]=population
        
        #update min and max year
        if year <Country.min_year_recorded:
            Country.min_year_recorded=year
            
        if year>Country.max_year_recorded:
            Country.max_year_recorded=year


    def get_co2_emissions_by_year(self, year):
        
        """
        (Country, int)->float
        
        It returns the co2 emission of the country in the specified year if available. It returns 0.0 otherwise.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015
        >>> a.get_co2_emissions_by_year(2000)
        0.0
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.get_co2_emissions_by_year(1949)
        0.0
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_co2_emissions_by_year(2007)
        62.899
        >>> q.co2_emissions
        {2007: 62.899, 1993: 30.985, 1989: 14.292}
        >>> q.get_co2_emissions_by_year(1989)
        14.292
        
        """
        
        #return the co2 of the year
        if year in self.co2_emissions:
            return self.co2_emissions[year]
        #if the co2 does not exist, then return 0.0
        else:
            return 0.0

    def get_co2_per_capita_by_year(self,year):
        
        """
        (Country, int)->float

        It return the co2 emission per capita in tonnes (note that the co2 emissions for a country are recorded in
        millions of tonnes) for the specified year if available. If either the co2 emissions or the population
        of the country are not available for the specified year, the method returns None.
        
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427
        >>> print(a.get_co2_per_capita_by_year(1949))
        None
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.get_co2_per_capita_by_year(2018)
        >>> print(q.get_co2_per_capita_by_year(2018))
        None
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.population
        {2007: 1218000, 1989: 462000}
        >>> q.co2_emissions
        {2007: 62.899, 1989: 14.292}
        >>> q.get_co2_per_capita_by_year(2007)
        51.641215106732346
        
        
        """
        
        # the year appears in the dictionary of co2 and population
        if year in self.co2_emissions and year in self.population:
            
            #formula
            co2_emissions=self.get_co2_emissions_by_year(year)*(10**6)
            population=self.population[year]
            return co2_emissions/population
        #if the year does not exist in at least one of the dictionary
        else:
            return None
        

    def get_historical_co2(self, year):
        """
        (Country, int)->float

        It return the
        historical (total) co2 emission in millions of tonnes that the country has produced for all years up
        to and including the specified year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277
        >>> q.get_historical_co2(2007)
        108.176

        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_historical_co2( 2020)
        9.454
        
        
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.get_historical_co2( 2020)
        0.0
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.22, 7663783)
        >>> a.add_yearly_data("2018\\t\\t37122000")
        >>> a.get_historical_co2( 2020)
        0.22
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t\\t37122000")
        >>> a.get_historical_co2( 2020)
        0.0
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t325.2\\t37122000")
        >>> a.get_historical_co2( 2020)
        325.2
        """
        tot=0.0
        #get the historical, so if the time is smaller or equal to the year
        for time in self.co2_emissions:
            if time<=year:
                tot+=self.co2_emissions[time]
        return tot
        
    @classmethod
    def get_country_from_data(cls,txt):
        """
        (type,str)->Country
        The method should return a new Country object created from the data in the input string.
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{1991: 4.283}\\t{1991: 3280000}'
    
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t\\t453")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{}\\t{1991: 453}'
        
        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE,ASIA\\t1991\\t4234.21\\t")
        >>> a.__str__()
        'Albania\\tEUROPE,ASIA\\t{1991: 4234.21}\\t{}'
        """

        lst=txt.split("\t") #split string into a list by tab
        if len(lst)==5: #if the length of the list is 5
            lst.append("") #add an empty string at the end
        iso_code=lst[0]  #assign iso
        country="".join(lst[1]) #join country name
        lst_continents=[] #assign continent
        lst_continents.append(lst[2])
        continents=lst_continents
        year=int(lst[3]) #assign year
        if lst[4]!="": #if theres a co2 value
            co2_emissions=float(lst[4])
        else:
            co2_emissions=-1
        if lst[5]!="": #if theres a population value
            population=int(lst[5])
        else:
            population=-1
        return cls(iso_code, country, continents, year, co2_emissions, population)

    @staticmethod 
    def get_countries_by_continent(country_id_list):
        
        """
        (lst)->dict
        
        The method returns a dictionary mapping a string representing a continent
        to a list of countries (i.e., objects of type Country) which all belong to that continent. The
        order in which each country appears in the list should match the order in which they appeared in
        the input list.
        
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007,-1,-1)
        >>> c = [q, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['EUROPE'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'
        >>> str(d['EUROPE'][0])
        'Albania\\tEUROPE\\t{}\\t{}'
        
        
        >>> q = Country("QAT", "Qatar", ["ASIA","EUROPE"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t\\t")
        >>> q.add_yearly_data("1888\\t54.54\\t5645646")
        >>> c=[q]
        >>> d = Country.get_countries_by_continent(c)
        >>> len(d)
        2
        >>> str(d['ASIA'][0])
        'Qatar\\tASIA,EUROPE\\t{2007: 62.899, 1888: 54.54}\\t{2007: 1218000, 1888: 5645646}'
        >>> str(d['EUROPE'][0])
        'Qatar\\tASIA,EUROPE\\t{2007: 62.899, 1888: 54.54}\\t{2007: 1218000, 1888: 5645646}'
        
        >>> q = Country("QAT", "Qatar", ["ASIA","EUROPE"], 2007, -1, -1)
        >>> c=[q]
        >>> d = Country.get_countries_by_continent(c)
        >>> len(d)
        2
        >>> str(d['ASIA'][0])
        'Qatar\\tASIA,EUROPE\\t{}\\t{}'
        """

        dct={}
        for country_id in country_id_list: #Go through each country
            
            continents_lst=country_id.continents #assign continent
            if len(continents_lst)==1: #seperate ASIA,EUROPE so it would give ["ASIA","EUROPE"], not ["ASIA,EUROPE"]
               continents_lst= continents_lst[0].split(",")
               
            for continent in continents_lst: #deal with ASIA,EUROPE or add continent to list
                if continent not in dct: #if the continent is not in the dictionary, add continent
                    dct[continent]=[]
                    dct[continent].append(country_id)
                        
                else:
                    dct[continent].append(country_id)
        return dct

    @staticmethod
    def get_total_historical_co2_emissions(country_id_list, year):
        """
        (lst, int)-> float
        
        The method returns a float
        representing the total co2 emissions (in millions of tonnes) produced by all the countries in the
        input list for all years up to and including the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> Country.get_total_historical_co2_emissions(c,2007)
        1721.161
        >>> Country.get_total_historical_co2_emissions(c,2000)
        49.56
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, -1, -1)
        >>> b.add_yearly_data("1991\\t\\t")
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, -1, -1)
        >>> c = [b, r]
        >>> Country.get_total_historical_co2_emissions(c,2007)
        0.0
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> c = [b]
        >>> Country.get_total_historical_co2_emissions(c,1598)
        0.0
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, -1, 54564)
        >>> b.add_yearly_data("2020\\t4.283\\t3280000")
        >>> c = [b]
        >>> Country.get_total_historical_co2_emissions(c,2020)
        4.283
        >>> Country.get_total_historical_co2_emissions(c,2006)
        0.0
        
        """
        
        
        tot=0.0
        for country_id in country_id_list: #checks if the country is int the list
            tot+=country_id.get_historical_co2(year) #add the values
        return tot
    
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(country_id_list,year):
        
        """
        (lst, int)-> float
        A static method called get_total_co2_emissions_per_capita_by_year which takes as input a list of
        countries (i.e., objects of type Country) and an integer representing a year. The method returns
        the co2 emissions per capita in tonnes produced by the countries in the given list in the specified
        year.
        If one of the two data point (co2 or population) is missing for a country in the list, then this
        country should be excluded when computing the value needed. More over, if the total co2 or the
        total population is 0, then the function should return 0.0.
        
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,2007), 5)
        92.98855
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, -1)
        >>> c = [b]
        >>> Country.get_total_co2_emissions_per_capita_by_year(c,2007)
        0.0
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, -1, 4551)
        >>> c = [b]
        >>> Country.get_total_co2_emissions_per_capita_by_year(c,2007)
        0.0
        
        """
        tot_emissions=0.0
        tot_population=0
        
        for country_id in country_id_list: #go through each country
            if year not in country_id.co2_emissions and year not in country_id.population: #go to next country id if year
                                                                                        #does not appear in either co2 or population
                continue
            if country_id.co2_emissions!={} and country_id.population!={} and \
               year in country_id.co2_emissions and year in country_id.population: #check the conditions
                tot_emissions+=float(country_id.co2_emissions[year]) #add co2 emissions to tot
                tot_population+=int(country_id.population[year]) # add population to tot

        if tot_emissions!=0.0 and tot_population!=0: # none of the values can be zero
            tot=tot_emissions*(10**6)/tot_population
        else:
            return 0.0
        
        if tot!=0:
            return tot
        return 0.0 #return a float of zero

    @staticmethod
    def get_co2_emissions_per_capita_by_year(country_id_list,year):
        """

        (lst, int)->dict
        A static method called get_co2_emissions_per_capita_by_year which takes as input a list of countries
        (i.e., objects of type Country) and an integer representing a year. The method returns a
        dictionary mapping objects of type Country to floats representing the co2 emissions per capita in
        tonnes produced by the country in the specified year. Note that it is possible that some of the
        values in the output dictionary might be None. This could occur when the co2 per capita of that
        country for the specified year cannot be computed.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> c = [b, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> len(d1)
        2
        >>> round(d1[r], 5)
        112.4897
        >>> d2 = Country.get_co2_emissions_per_capita_by_year(c, 1991)
        >>> print(d2[r])
        None
        >>> round(d2[b], 5)
        1.30579
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, -1, -1)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, -1,-1)
        >>> c = [b, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> d1[r]
        >>>
        >>> d1[b]
        >>>
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 2.2021, -1)
        >>> c = [b]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> d1[b]
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, -1, 5456)
        >>> c = [b]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> d1[b]
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 2.2021, -1)
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 2.2021, 545611)
        >>> c=[b]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> round(d1[b], 5)
        4.03603
        
        """
        d={}
        for country_id in country_id_list:
                d[country_id]=country_id.get_co2_per_capita_by_year(year) #associate country object to co2 per capita
        return d

    @staticmethod
    def get_historical_co2_emissions(country_id_list, year):
        
        """
        (lst, int)->dict
        A static method called get_historical_co2_emissions which takes as input a list of countries (i.e.,
        objects of type Country) and an integer representing a year. The method returns a dictionary
        mapping objects of type Country to floats representing the total co2 emissions (in millions of
        tonnes) produced by that country for all years up to and including the specified year.
                
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2007)
        >>> len(d1)
        3
        >>> round(d1[q], 5)
        108.176
        >>> d2 = Country.get_historical_co2_emissions(c, 1991)
        >>> print(d2[r])
        0.0
        >>> round(d2[b], 5)
        4.283
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2020, 25.12, 123456)
        >>> b.add_yearly_data("1991\\t\\t3280000")
        >>> b.add_yearly_data("2000\\t45.12\\t")
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2005, 45.1, 1218000)
        >>> c = [b, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2007)
        >>> len(d1)
        2
        >>> d1[b]
        45.12
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2020, -1, -1)
        >>> b.add_yearly_data("1991\\t\\t3280000")
        >>> c = [b]
        >>> d1 = Country.get_historical_co2_emissions(c,2020)
        >>> len(d1)
        1
        >>> d1[b]
        0.0
        
        """
        
     
        d={}
        for country_id in country_id_list:
            d[country_id]=country_id.get_historical_co2(year) #assign country object to historical co2
        return d
    
    @staticmethod
    def get_top_n(d,n):
        
        """
        (dict, int)-> list(of tuples)
        
        • A static method called get_top_n which takes as input a dictionary mapping objects of type Country
        to numbers, and an integer n. The method returns a list of tuples. Each tuple is made up by the
        iso code of a country and the number to which the country is mapped in the input dictionary. Only
        the countries that map to the top n values should appear in the list. The tuples in the list should
        appear sorted on the values in descending order. If there are countries that map to the same values,
        the countries should be compared based on the alphabetical order of their names. Please note that
        this function should NOT modify the input dictionary.

        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t[:5]
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7)]
        >>> t[5:]
        [('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]
        
        >>> z=Country.get_top_n(d, 6)
        >>> z
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7), ('SEN', 6)]
        >>> len(d)
        12
        >>> len(z)
        6
        
        >>> a = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> b = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> c = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> d = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> e = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> f = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3}
        >>> Country.get_top_n(d, 3)
        [('PRY', 10), ('SEN', 5), ('THA', 5)]
        >>> Country.get_top_n(d, 100)
        [('PRY', 10), ('SEN', 5), ('THA', 5), ('AUT', 3), ('IRL', 3)]
                
        """
        dct1=copy.deepcopy(d) #create a copy of the dictionary
        tup_id_num=list(dct1.items()) #turn into tuple
        dct2={}
        for country_id,num in tup_id_num:
            dct2[country_id.name+country_id.iso_code]=num #create a dictionary of nameiso to number
        tup_name_num=list(dct2.items()) #change into tuple
        dct3={}
        for name, num in tup_name_num:
            if num not in dct3: #create anew list
                dct3[num]=[]
                dct3[num].append(name)
            else:
                dct3[num].append(name) #append to list of the number designated
       
        tup_num_countries=list(dct3.items()) #change into tuple
        tup_num_countries.sort() #sort out according to the nuber
        reverse_tup_num_countries=tup_num_countries[::-1] #change order to descending

        d4={}
        
        for num, countries in reverse_tup_num_countries:
            countries.sort() #sort the countries
            for country in countries:
                
                if country[-3:].isupper(): #only put iso to dictionary
                    d4[country[-3:]]=num
                    
                elif country[-8:].isupper(): #for owid_kos
                    d4[country[-8:]]=num
        
        
        tup_d4=list(d4.items()) #create a tuple
        tup_d4_sliced=tup_d4[:n] #slice the tuple
        
        return tup_d4_sliced

def get_countries_from_file(filename):
    
    """

    (str)-> dict
    
    Finally, add to this module (but outside the class Country) a function called get_countries_from_file.
    This function takes as input a string representing a filename which has exactly the same format as
    the output file generated by the function add_continents_to_data. The function creates and return a
    dictionary mapping ISO country codes (strings) to objects of type Country based on the data in the file.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    >>> str(d1['ALB'])
    'Albania\\tEUROPE\\t{2002: 3.748}\\t{2002: 3126000}'


    >>> d2= get_countries_from_file("Anna_large_co2_data.tsv")
    >>> len(d2)
    193
    """
    
    
    fobj=open(filename, 'r', encoding="utf-8") #open file
    d={}
    
    
    for line in fobj:
        if line=="\n": #if its the last line
            break
        
        line=line.strip("\n") #remove \n
        splited_line=line.split("\t") #split the line into \t
        iso_code=splited_line[0] #assign iso code
        
        if iso_code not in d: #add a new iso code to the dictionary that maps to country id
            country_id = Country.get_country_from_data(line)
            d[iso_code]=country_id

        else:
            a=d[iso_code] 
            year_co2_pop_lst=splited_line[3:] #get list with year, co2 and population
            while len(year_co2_pop_lst)<3: #if theres a value missing, then add "" until the lenght
                                            #of the list is 3
                year_co2_pop_lst.append("")
            year_co2_pop_txt="\t".join(year_co2_pop_lst) #join the list
            a.add_yearly_data(year_co2_pop_txt) #add any additional information
           
    return d

if __name__=="__main__":
    import doctest
    doctest.testmod()
