# Worldmap

Worldmap is a brane package for creating maps of the world using Geopandas. Each country can be given a value representing a color in the red, yellow and green range.

## Installation

If on Linux or MacOS first run:

``` chmod +x run.py ```

Otherwise/then:

```console
brane build container.yml
brane push world map 1.0.0
```

## Usage

```brane
import worldmap;

let countries := ["Canada", "United States of America"];

let values := [100.0, -50];

create_map(values, countries, "Legend name", "/data/wordcloud.png");
```

## Notes
Countries and values are matched using their index where blank countries receive a value of 0. Lowest value in the array is represented using the color red and highest value is represented by green. These values can be positive, negative, floats or integers.

Countries should be provided with names according to this list:

['Fiji', 'Tanzania', 'W. Sahara', 'Canada', 'United States of America', 'Kazakhstan', 'Uzbekistan', 'Papua New Guinea', 'Indonesia', 'Argentina', 'Chile', 'Dem. Rep. Congo', 'Somalia', 'Kenya', 'Sudan', 'Chad', 'Haiti', 'Dominican Rep.', 'Russia', 'Bahamas', 'Falkland Is.', 'Norway', 'Greenland', 'Fr. S. Antarctic Lands', 'Timor-Leste', 'South Africa', 'Lesotho', 'Mexico', 'Uruguay', 'Brazil', 'Bolivia', 'Peru', 'Colombia', 'Panama', 'Costa Rica', 'Nicaragua', 'Honduras', 'El Salvador', 'Guatemala', 'Belize', 'Venezuela', 'Guyana', 'Suriname', 'France', 'Ecuador', 'Puerto Rico', 'Jamaica', 'Cuba', 'Zimbabwe', 'Botswana', 'Namibia', 'Senegal', 'Mali', 'Mauritania', 'Benin', 'Niger', 'Nigeria', 'Cameroon', 'Togo', 'Ghana', "Côte d'Ivoire", 'Guinea', 'Guinea-Bissau', 'Liberia', 'Sierra Leone', 'Burkina Faso', 'Central African Rep.', 'Congo', 'Gabon', 'Eq. Guinea', 'Zambia', 'Malawi', 'Mozambique', 'eSwatini', 'Angola', 'Burundi', 'Israel', 'Lebanon', 'Madagascar', 'Palestine', 'Gambia', 'Tunisia', 'Algeria', 'Jordan', 'United Arab Emirates', 'Qatar', 'Kuwait', 'Iraq', 'Oman', 'Vanuatu', 'Cambodia', 'Thailand', 'Laos', 'Myanmar', 'Vietnam', 'North Korea', 'South Korea', 'Mongolia', 'India', 'Bangladesh', 'Bhutan', 'Nepal', 'Pakistan', 'Afghanistan', 'Tajikistan', 'Kyrgyzstan', 'Turkmenistan', 'Iran', 'Syria', 'Armenia', 'Sweden', 'Belarus', 'Ukraine', 'Poland', 'Austria', 'Hungary', 'Moldova', 'Romania', 'Lithuania', 'Latvia', 'Estonia', 'Germany', 'Bulgaria', 'Greece', 'Turkey', 'Albania', 'Croatia', 'Switzerland', 'Luxembourg', 'Belgium', 'Netherlands', 'Portugal', 'Spain', 'Ireland', 'New Caledonia', 'Solomon Is.', 'New Zealand', 'Australia', 'Sri Lanka', 'China', 'Taiwan', 'Italy', 'Denmark', 'United Kingdom', 'Iceland', 'Azerbaijan', 'Georgia', 'Philippines', 'Malaysia', 'Brunei', 'Slovenia', 'Finland', 'Slovakia', 'Czechia', 'Eritrea', 'Japan', 'Paraguay', 'Yemen', 'Saudi Arabia', 'Antarctica', 'N. Cyprus', 'Cyprus', 'Morocco', 'Egypt', 'Libya', 'Ethiopia', 'Djibouti', 'Somaliland', 'Uganda', 'Rwanda', 'Bosnia and Herz.', 'Macedonia', 'Serbia', 'Montenegro', 'Kosovo', 'Trinidad and Tobago', 'S. Sudan']
