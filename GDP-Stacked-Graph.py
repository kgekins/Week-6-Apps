import requests as rq
import bs4
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
page = rq.get(url)

bs4page = bs4.BeautifulSoup(page.text, 'html.parser')
tables = bs4page.find_all('table',{'class':"wikitable"})

from io import StringIO
import streamlit as st

GDP = pd.read_html(StringIO(str(tables[0])))[0].replace(r'\[.*?\]', '', regex=True)
GDP.columns = ['Country/Territory', 'IMF Forecast', 'IMF Year', 'World Bank Estimate', 'World Bank Year', 'UN Estimate', 'UN Year']
GDP = GDP[GDP['Country/Territory'] != 'World']
GDP['IMF Forecast'] = pd.to_numeric(GDP['IMF Forecast'], errors='coerce')


# Group countries by continent
continent_mapping = {
    'United States': 'North America', 'China': 'Asia', 'Germany': 'Europe', 'Japan': 'Asia', 'India': 'Asia',
    'United Kingdom': 'Europe', 'France': 'Europe', 'Brazil': 'South America', 'Italy': 'Europe', 'Canada': 'North America',
    'Russia': 'Europe', 'Mexico': 'North America', 'Australia': 'Oceania', 'South Korea': 'Asia', 'Spain': 'Europe',
    'Indonesia': 'Asia', 'Netherlands': 'Europe', 'Turkey': 'Asia', 'Saudi Arabia': 'Asia', 'Switzerland': 'Europe',
    'Poland': 'Europe', 'Taiwan': 'Asia', 'Belgium': 'Europe', 'Sweden': 'Europe', 'Argentina': 'South America',
    'Ireland': 'Europe', 'Thailand': 'Asia', 'Austria': 'Europe', 'Israel': 'Asia', 'United Arab Emirates': 'Asia',
    'Norway': 'Europe', 'Singapore': 'Asia', 'Philippines': 'Asia', 'Malaysia': 'Asia', 'South Africa': 'Africa',
    'Egypt': 'Africa', 'Chile': 'South America', 'Finland': 'Europe', 'Vietnam': 'Asia', 'Pakistan': 'Asia',
    'Bangladesh': 'Asia', 'Czech Republic': 'Europe', 'Romania': 'Europe', 'Portugal': 'Europe', 'New Zealand': 'Oceania',
    'Greece': 'Europe', 'Iraq': 'Asia', 'Algeria': 'Africa', 'Qatar': 'Asia', 'Kazakhstan': 'Asia', 'Hungary': 'Europe',
    'Kuwait': 'Asia', 'Ukraine': 'Europe', 'Morocco': 'Africa', 'Slovakia': 'Europe', 'Ecuador': 'South America',
    'Sri Lanka': 'Asia', 'Kenya': 'Africa', 'Ethiopia': 'Africa', 'Uzbekistan': 'Asia', 'Angola': 'Africa',
    'Dominican Republic': 'North America', 'Myanmar': 'Asia', 'Oman': 'Asia', 'Luxembourg': 'Europe', 'Panama': 'North America',
    'Ghana': 'Africa', 'Bulgaria': 'Europe', 'Costa Rica': 'North America', 'Uruguay': 'South America', 'Croatia': 'Europe',
    'Belarus': 'Europe', 'Lebanon': 'Asia', 'Tanzania': 'Africa', 'Slovenia': 'Europe', 'Lithuania': 'Europe',
    'Serbia': 'Europe', 'Azerbaijan': 'Asia', 'Jordan': 'Asia', 'Tunisia': 'Africa', 'Paraguay': 'South America',
    'Libya': 'Africa', 'Turkmenistan': 'Asia', 'Congo, Democratic Republic of the': 'Africa', 'Bolivia': 'South America',
    'Bahrain': 'Asia', 'Cameroon': 'Africa', 'Yemen': 'Asia', 'Latvia': 'Europe', 'Estonia': 'Europe', 'Uganda': 'Africa',
    'Zambia': 'Africa', 'Nepal': 'Asia', 'El Salvador': 'North America', 'Iceland': 'Europe', 'Honduras': 'North America',
    'Cambodia': 'Asia', 'Trinidad and Tobago': 'North America', 'Cyprus': 'Europe', 'Zimbabwe': 'Africa', 'Senegal': 'Africa',
    'Papua New Guinea': 'Oceania', 'Bosnia and Herzegovina': 'Europe', 'Botswana': 'Africa', 'Mali': 'Africa',
    'Madagascar': 'Africa', 'Malta': 'Europe', 'Mauritius': 'Africa', 'Namibia': 'Africa', 'Mozambique': 'Africa',
    'Macedonia': 'Europe', 'Mongolia': 'Asia', 'Armenia': 'Asia', 'Albania': 'Europe', 'Jamaica': 'North America',
    'Niger': 'Africa', 'Burkina Faso': 'Africa', 'Guinea': 'Africa', 'Malawi': 'Africa', 'Moldova': 'Europe',
    'Chad': 'Africa', 'Tajikistan': 'Asia', 'Benin': 'Africa', 'Rwanda': 'Africa', 'Haiti': 'North America',
    'Kyrgyzstan': 'Asia', 'Somalia': 'Africa', 'Montenegro': 'Europe', 'Maldives': 'Asia', 'Togo': 'Africa',
    'Mauritania': 'Africa', 'Eswatini': 'Africa', 'Guyana': 'South America', 'Burundi': 'Africa', 'Lesotho': 'Africa',
    'Suriname': 'South America', 'Central African Republic': 'Africa', 'Bhutan': 'Asia', 'Cape Verde': 'Africa',
    'San Marino': 'Europe', 'Comoros': 'Africa', 'Solomon Islands': 'Oceania', 'Gambia': 'Africa', 'Vanuatu': 'Oceania',
    'Samoa': 'Oceania', 'Saint Lucia': 'North America', 'Kiribati': 'Oceania', 'Palau': 'Oceania', 'Marshall Islands': 'Oceania',
    'Nauru': 'Oceania', 'Tuvalu': 'Oceania'
}


GDP['Continent'] = GDP['Country/Territory'].map(continent_mapping)

import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app
st.title('GDP Stacked Bar Plot by Continent')

# User selection for GDP source
gdp_source = st.selectbox('Select GDP Source', ['IMF Forecast', 'World Bank Estimate', 'UN Estimate'])

# Filter out rows with NaN values in the selected GDP source
GDP_filtered = GDP.dropna(subset=[gdp_source])

# Group by continent and sum the GDPs
continent_gdp = GDP_filtered.groupby('Continent')[gdp_source].sum().sort_values(ascending=False)

# Plotting
fig, ax = plt.subplots()
continent_gdp.plot(kind='bar', stacked=True, ax=ax)
ax.set_ylabel('GDP in USD')
ax.set_title(f'GDP by Continent ({gdp_source})')

