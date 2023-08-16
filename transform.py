import pandas as pd
from extract import extract_data 

def transform_data(data):
    langues_codes = {
        'English': 'EN',
        'French': 'FR',
        'Chinese': 'ZH',
        'Hindi': 'HI',
        'Portuguese': 'PT',
        'Spanish': 'ES',
        'German': 'DE',
        'Italian': 'IT',
        'Norwegian': 'NO',
        'Russian': 'RU',
        'Dutch': 'NL',
        'Swedish': 'SV',
        'Japanese': 'JA',
        'Czech': 'CS',
        'Yiddish': 'YI',
        'Gujarati': 'GU'
    }

    data['Language code'] = data['Original language'].map(langues_codes)

    return data

if _name_ == "_main_":
    extracted_data = extract_data()  
    transformed_data = transform_data(extracted_data) 
    print("Données transformées:")
    print(transformed_data.head())