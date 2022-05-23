
import requests
import pytest
import json


def test_1():
    url = 'http://dataservice.accuweather.com/locations/v1/regions'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert len(res) == 10


def test_2():
    url = 'http://dataservice.accuweather.com/locations/v1/regions'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'ID': 'ASI', 'LocalizedName': 'Asia', 'EnglishName': 'Asia'} in res


def test_3():
    url = 'http://dataservice.accuweather.com/locations/v1/regions'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'ID': 'MEA', 'LocalizedName': 'Middle East',
            'EnglishName': 'Middle East'} in res


def test_4():
    url = 'http://dataservice.accuweather.com/locations/v1/topcities/50'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert len(res) == 50


def test_5():
    url = 'http://dataservice.accuweather.com/locations/v1/topcities/50'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'Version': 1, 'Key': '28143', 'Type': 'City', 'Rank': 10, 'LocalizedName': 'Dhaka', 'EnglishName': 'Dhaka', 'PrimaryPostalCode': '', 'Region': {'ID': 'ASI', 'LocalizedName': 'Asia', 'EnglishName': 'Asia'}, 'Country': {'ID': 'BD', 'LocalizedName': 'Bangladesh', 'EnglishName': 'Bangladesh'}, 'AdministrativeArea': {'ID': 'C', 'LocalizedName': 'Dhaka', 'EnglishName': 'Dhaka', 'Level': 1, 'LocalizedType': 'Division', 'EnglishType': 'Division', 'CountryID': 'BD'},
            'TimeZone': {'Code': 'BDT', 'Name': 'Asia/Dhaka', 'GmtOffset': 6.0, 'IsDaylightSaving': False, 'NextOffsetChange': None}, 'GeoPosition': {'Latitude': 23.71, 'Longitude': 90.407, 'Elevation': {'Metric': {'Value': 5.0, 'Unit': 'm', 'UnitType': 5}, 'Imperial': {'Value': 16.0, 'Unit': 'ft', 'UnitType': 0}}}, 'IsAlias': False, 'SupplementalAdminAreas': [], 'DataSets': ['AirQualityCurrentConditions', 'AirQualityForecasts', 'FutureRadar', 'MinuteCast']} in res


def test_6():
    url = 'http://dataservice.accuweather.com/locations/v1/topcities/50'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'Version': 1, 'Key': '113487', 'Type': 'City', 'Rank': 10, 'LocalizedName': 'Kinshasa', 'EnglishName': 'Kinshasa', 'PrimaryPostalCode': '', 'Region': {'ID': 'AFR', 'LocalizedName': 'Africa', 'EnglishName': 'Africa'}, 'Country': {'ID': 'CD', 'LocalizedName': 'Democratic Republic of the Congo', 'EnglishName': 'Democratic Republic of the Congo'}, 'AdministrativeArea': {'ID': 'KN', 'LocalizedName': 'Kinshasa', 'EnglishName': 'Kinshasa', 'Level': 1, 'LocalizedType': 'City',
                                                                                                                                                                                                                                                                                                                                                                                             'EnglishType': 'City', 'CountryID': 'CD'}, 'TimeZone': {'Code': 'WAT', 'Name': 'Africa/Kinshasa', 'GmtOffset': 1.0, 'IsDaylightSaving': False, 'NextOffsetChange': None}, 'GeoPosition': {'Latitude': -4.316, 'Longitude': 15.298, 'Elevation': {'Metric': {'Value': 180.0, 'Unit': 'm', 'UnitType': 5}, 'Imperial': {'Value': 590.0, 'Unit': 'ft', 'UnitType': 0}}}, 'IsAlias': False, 'SupplementalAdminAreas': [], 'DataSets': ['AirQualityCurrentConditions', 'AirQualityForecasts', 'MinuteCast']} in res


def test_7():
    url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'q': '18612',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert len(res) == 2


def test_8():
    url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'q': '18612',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'Version': 1, 'Key': '7579_PC', 'Type': 'PostalCode', 'Rank': 85, 'LocalizedName': 'Dallas', 'EnglishName': 'Dallas', 'PrimaryPostalCode': '18612', 'Region': {'ID': 'NAM', 'LocalizedName': 'North America', 'EnglishName': 'North America'}, 'Country': {'ID': 'US', 'LocalizedName': 'United States', 'EnglishName': 'United States'}, 'AdministrativeArea': {'ID': 'PA', 'LocalizedName': 'Pennsylvania', 'EnglishName': 'Pennsylvania', 'Level': 1, 'LocalizedType': 'State', 'EnglishType': 'State', 'CountryID': 'US'}, 'TimeZone': {'Code': 'EDT', 'Name': 'America/New_York', 'GmtOffset': -4.0, 'IsDaylightSaving': True,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'NextOffsetChange': '2022-11-06T06:00:00Z'}, 'GeoPosition': {'Latitude': 41.336, 'Longitude': -75.962, 'Elevation': {'Metric': {'Value': 364.0, 'Unit': 'm', 'UnitType': 5}, 'Imperial': {'Value': 1193.0, 'Unit': 'ft', 'UnitType': 0}}}, 'IsAlias': False, 'ParentCity': {'Key': '335406', 'LocalizedName': 'Dallas', 'EnglishName': 'Dallas'}, 'SupplementalAdminAreas': [{'Level': 2, 'LocalizedName': 'Luzerne', 'EnglishName': 'Luzerne'}], 'DataSets': ['AirQualityCurrentConditions', 'AirQualityForecasts', 'Alerts', 'DailyAirQualityForecast', 'DailyPollenForecast', 'ForecastConfidence', 'FutureRadar', 'MinuteCast', 'Radar']} in res


def test_9():
    url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'q': '474015',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert len(res) == 3


def test_10():
    url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'
    query = {
        'apikey': 'AtxCnIgM1Y1ROLsvOTOUJ2JYw6WJ8R3N',
        'q': '474015',
        'language': 'en-us',
        'details': 'false',
    }
    req = requests.get(url, params=query)
    res = json.loads(req.text)
    assert {'Version': 1, 'Key': '532254_PC', 'Type': 'PostalCode', 'Rank': 0, 'LocalizedName': '474015', 'EnglishName': '474015', 'PrimaryPostalCode': '474015', 'Region': {'ID': 'ASI', 'LocalizedName': 'Asia', 'EnglishName': 'Asia'}, 'Country': {'ID': 'IN', 'LocalizedName': 'India', 'EnglishName': 'India'}, 'AdministrativeArea': {'ID': 'MP', 'LocalizedName': 'Madhya Pradesh', 'EnglishName': 'Madhya Pradesh', 'Level': 1, 'LocalizedType': 'State', 'EnglishType': 'State', 'CountryID': 'IN'}, 'TimeZone': {'Code': 'IST', 'Name': 'Asia/Kolkata', 'GmtOffset': 5.5,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'IsDaylightSaving': False, 'NextOffsetChange': None}, 'GeoPosition': {'Latitude': 26.25, 'Longitude': 78.172, 'Elevation': {'Metric': {'Value': 195.0, 'Unit': 'm', 'UnitType': 5}, 'Imperial': {'Value': 639.0, 'Unit': 'ft', 'UnitType': 0}}}, 'IsAlias': False, 'SupplementalAdminAreas': [{'Level': 2, 'LocalizedName': 'Gwalior', 'EnglishName': 'Gwalior'}, {'Level': 3, 'LocalizedName': 'Gwalior', 'EnglishName': 'Gwalior'}], 'DataSets': ['AirQualityCurrentConditions', 'AirQualityForecasts', 'Alerts', 'ForecastConfidence', 'FutureRadar', 'MinuteCast', 'PremiumAirQuality']} in res
