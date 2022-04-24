import requests
import json
import unittest
import pprint

def get_gdp(country_code, date):
    """
    This function takes a country code (e.g USA, BRA) and a date in years (e.g. 2017).
    Call the World Bank API to get gdp data searched by country and years.
    It returns the value as an integer.
    """
    format = 'JSON'
    indicator = 'NY.GDP.MKTP.CD'
    url = f'http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={date}&format={format}'
    data = requests.get(url)
    data_decoded = json.loads(data.text)
    pprint.pprint(data_decoded)
    return data_decoded[1][0]['value']




def get_data(country_code, first_year, second_year):
    """
    This function takes a country code (e.g. USA, BRA) and two consecutive years (e.g. 2004 and 2005).
    Call the World Bank API to get gdp data searched by country and years.
    Return the data from API after converting to a python list
    that has gdp related information.
    Once you receive data from the API, paste the data to 
    JSON Online Editor and look at the contents.
    """
    format = 'JSON'
    indicator = 'NY.GDP.MKTP.CD'
    date = f'{first_year}:{second_year}'
    url = f'http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={date}&format={format}'
    data = requests.get(url)
    data_decoded = json.loads(data.text)
    pprint.pprint(data_decoded)
    return data_decoded

def gdp_growth(country_code, first_year, second_year):
    """
    This function receives three parameters: one is the country code and the other two
    are the two consecutive years that you want to find the gdp growth for.
    Call get_data and analyze the returned list.
    This function returns the gdp growths of the two years of the country in a tuple.
    """
    
    data = get_data(country_code, first_year, second_year)
    gdp_2020 = data[1][0]['value']
    gdp_2019 = data[1][1]['value']
    return gdp_2019, gdp_2020

class TestDiscussion10(unittest.TestCase):
    def test_get_gdp(self):
        data = get_gdp("USA", 2020)
        self.assertEqual(type(data), int)
        self.assertEqual(data, 20953030000000)

    def test_check_data(self):
        data1 = get_data('BRA', 2019, 2020)
        self.assertEqual(type(data1), list)
        self.assertEqual(data1[1][0]['countryiso3code'], "BRA")

    def test_gdp_growth(self):
        self.assertEqual(type(gdp_growth('BRA', 2019, 2020)), tuple)
        self.assertEqual(gdp_growth('BRA', 2019, 2020), (1877824273720.78, 1444733258971.65))

def main():
    print("-----GDP-----")
    year = 2020
    country = 'USA'
    gdp = get_gdp(country, year)
    print(f"The total GDP in {country} is {gdp} in the year {year}")
    print("-----GDP Growth-----")
    country = "BRA"
    first_year = 2020
    second_year = 2019
    value1, value2 = gdp_growth(country, first_year, second_year)
    print(f"The GDP growth in {country} is {value1} in {first_year} and {value2} in {second_year}")
    
    print("-----Unittest-------")
    unittest.main(verbosity=2)
    print("------------")

if __name__ == "__main__":
    main()
