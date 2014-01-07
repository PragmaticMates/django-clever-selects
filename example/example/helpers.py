__author__ = 'Erik Telepovsky'


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female')
)


CONTINENT_NORTH_AMERICA = 'north_america'
CONTINENT_SOUTH_AMERICA = 'south_america'
CONTINENT_EUROPE = 'europe'
CONTINENT_ASIA = 'asia'
CONTINENT_AFRICA = 'africa'
CONTINENT_AUSTRALIA = 'australia'
CONTINENT_ANTARCTICA = 'antarctica'
CONTINENTS = (
    (CONTINENT_NORTH_AMERICA, 'North America'),
    (CONTINENT_SOUTH_AMERICA, 'South America'),
    (CONTINENT_EUROPE, 'Europe'),
    (CONTINENT_ASIA, 'Asia'),
    (CONTINENT_AFRICA, 'Africa'),
    (CONTINENT_AUSTRALIA, 'Australia'),
    (CONTINENT_ANTARCTICA, 'Antarctica')
)


# North America
COUNTRY_ALASKA = 'Alaska'
COUNTRY_CANADA = 'Canada'
COUNTRY_USA = 'USA'
COUNTRY_MEXICO = 'Mexico'

# South America
COUNTRY_COLOMBIA = 'Colombia'
COUNTRY_VENEZUELA = 'Venezuela'
COUNTRY_BRAZIL = 'Brazil'
COUNTRY_CHILE = 'Chile'
COUNTRY_URUGUAY = 'Uruguay'
COUNTRY_ARGENTINA = 'Argentina'

# Europe
COUNTRY_SLOVAKIA = 'Slovakia'
COUNTRY_SPAIN = 'Spain'
COUNTRY_BULGARIA = 'Bulgaria'
COUNTRY_PORTUGAL = 'Portugal'
COUNTRY_ITALY = 'Italy'
COUNTRY_UNITED_KINGDOM = 'United Kingdom'

# Asia
COUNTRY_CHINA = 'China'
COUNTRY_RUSSIA = 'Russia'
COUNTRY_JAPAN = 'Japan'
COUNTRY_INDIA = 'India'

# Africa
COUNTRY_ALGERIA = 'Algeria'
COUNTRY_EGYPT = 'Egypt'
COUNTRY_SUDAN = 'Sudan'
COUNTRY_ETHIOPIA = 'Ethiopia'
COUNTRY_SOMALIA = 'Somalia'
COUNTRY_MADAGASCAR = 'Madagascar'

# Australia
COUNTRY_WESTERN_AUSTRALIA = 'Western Australia'
COUNTRY_NORTHERN_TERRITORY = 'Northern Territory'
COUNTRY_SOUTH_AUSTRALIA = 'South Australia'
COUNTRY_QUEENSLAND = 'Queensland'
COUNTRY_NEW_SOUTH_WALES = 'New South Wales'
COUNTRY_VICTORIA = 'Victoria'
COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY = 'Australian Capital Territory'
COUNTRY_TASMANIA = 'Tasmania'

# Antarctica
COUNTRY_SOUTH_ORKNEY_ISLANDS = 'South Orkney Islands'
COUNTRY_GRAHAM_LAND = 'Graham Land'
COUNTRY_MARIE_BYRD_LAND = 'Marie Byrd Land'
COUNTRY_QEEN_MAUD_LAND = 'Queen Maud Land'
COUNTRY_VICTORIA_LAND = 'Victoria Land'
COUNTRY_WILKES_LAND = 'Wilkes Land'

COUNTRIES = {
    CONTINENT_NORTH_AMERICA: [
        COUNTRY_ALASKA, COUNTRY_CANADA, COUNTRY_USA, COUNTRY_MEXICO
    ],
    CONTINENT_SOUTH_AMERICA: [
        COUNTRY_COLOMBIA, COUNTRY_VENEZUELA, COUNTRY_BRAZIL, COUNTRY_CHILE, COUNTRY_URUGUAY, COUNTRY_ARGENTINA
    ],
    CONTINENT_EUROPE: [
        COUNTRY_SLOVAKIA, COUNTRY_SPAIN, COUNTRY_BULGARIA, COUNTRY_PORTUGAL, COUNTRY_ITALY, COUNTRY_UNITED_KINGDOM
    ],
    CONTINENT_ASIA: [
        COUNTRY_CHINA, COUNTRY_RUSSIA, COUNTRY_JAPAN, COUNTRY_INDIA
    ],
    CONTINENT_AFRICA: [
        COUNTRY_ALGERIA, COUNTRY_EGYPT, COUNTRY_SUDAN, COUNTRY_ETHIOPIA, COUNTRY_SOMALIA, COUNTRY_MADAGASCAR
    ],
    CONTINENT_AUSTRALIA: [
        COUNTRY_WESTERN_AUSTRALIA, COUNTRY_NORTHERN_TERRITORY, COUNTRY_SOUTH_AUSTRALIA, COUNTRY_QUEENSLAND,
        COUNTRY_NEW_SOUTH_WALES, COUNTRY_VICTORIA, COUNTRY_TASMANIA, COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY
    ],
    CONTINENT_ANTARCTICA: [
        COUNTRY_SOUTH_ORKNEY_ISLANDS, COUNTRY_GRAHAM_LAND, COUNTRY_MARIE_BYRD_LAND, COUNTRY_QEEN_MAUD_LAND,
        COUNTRY_VICTORIA_LAND, COUNTRY_WILKES_LAND
    ]
}

CITIES = {
    # North America
    COUNTRY_ALASKA: [
        'Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan', 'Wasilla', 'Kenai'
    ],
    COUNTRY_CANADA: [
        'Ottawa', 'Edmonton', 'Victoria', 'Winnipeg', 'Halifax', 'Toronto', 'Charlottetown', 'Quebec City'
    ],
    COUNTRY_USA: [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego'
    ],
    COUNTRY_MEXICO: [
        'Mexico City', 'Ecatepec', 'Guadalajara', 'Puebla', 'Leon', 'Juarez', 'Tijuana'
    ],

    # South America
    COUNTRY_COLOMBIA: [
        'Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena'
    ],
    COUNTRY_VENEZUELA: [
        'Isla Raton', 'La Esmeralda', 'Maroa', 'Puerto Ayacucho', 'San Carlos de Rio Negro',
    ],
    COUNTRY_BRAZIL: [
        'Sao Paulo', 'Rio de Janeiro', 'Salvador', 'Fortaleza', 'Belo Horizonte'
    ],
    COUNTRY_CHILE: [
        'Puente Alto', 'Maipu', 'La Florida', 'Las Condes', 'San Bernardo'
    ],
    COUNTRY_URUGUAY: [
        'Montevideo', 'Salto', 'Ciudad de la Costa', 'Paysandu', 'Las Piedras', 'Rivera', 'Maldonado'
    ],
    COUNTRY_ARGENTINA: [
        'Buenos Aires', 'Cordoba', 'Rosario', 'Mendoza', 'La Plata'
    ],

    # Europe
    COUNTRY_SLOVAKIA: [
        'Bratislava', 'Kosice', 'Trebisov', 'Poprad', 'Zilina', 'Puchov', 'Banska Bystrica', 'Presov'
    ],
    COUNTRY_SPAIN: [
        'Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Malaga', 'Murcia'
    ],
    COUNTRY_BULGARIA: [
        'Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven'
    ],
    COUNTRY_PORTUGAL: [
        'Lisbon', 'Porto', 'Vila Nova de Gaia', 'Amadora', 'Braga', 'Agualva-Cacem', 'Funchal'
    ],
    COUNTRY_ITALY: [
        'Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice'
    ],
    COUNTRY_UNITED_KINGDOM: [
        'London', 'Wells', 'Ripon', 'Truro', 'Ely', 'Chichester', 'Worcester', 'Oxford'
    ],

    # Asia
    COUNTRY_CHINA: [
        'Beijing', 'Shanghai', 'Hong Kong', 'Jinjiang', 'Xiamen', 'Sihui'
    ],
    COUNTRY_RUSSIA: [
        'Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Nizhny Novgorod', 'Samara', 'Omsk', 'Kazan'
    ],
    COUNTRY_JAPAN: [
        'Tokyo', 'Aichi', 'Akita', 'Chiba', 'Fukui', 'Fukushima', 'Hokkaido', 'Ishikawa', 'Kyoto', 'Osaka'
    ],
    COUNTRY_INDIA: [
        'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Jaipur'
    ],

    # Africa
    COUNTRY_ALGERIA: [
        'Alger', 'Oran', 'Constantine', 'Annaba', 'Blida', 'Batna', 'Djelfa'
    ],
    COUNTRY_EGYPT: [
        'Cairo', 'Alexandria', 'Giza', 'Shubra El-Kheima', 'Port Said', 'Suez', 'Luxor'
    ],
    COUNTRY_SUDAN: [
        'Omdurman', 'Khartoum', 'Khartoum Bahri', 'Nyala', 'Port Sudan', 'Kassala', 'Ubayyid', 'Kosti', 'Wad Madani'
    ],
    COUNTRY_ETHIOPIA: [
        'Addis Ababa', 'Dire Dawa', 'Mek\'ele', 'Adama', 'Gondar', 'Awasa', 'Bahir Dar', 'Jimma', 'Dessie'
    ],
    COUNTRY_SOMALIA: [
        'Mogadishu', 'Hargeisa', 'Bosaso', 'Galkayo', 'Berbera', 'Merca'
    ],
    COUNTRY_MADAGASCAR: [
        'Antananarivo', 'Toamasina', 'Antsirabe', 'Fianarantsoa', 'Mahajanga', 'Toliara', 'Antsiranana'
    ],

    # Australia
    COUNTRY_WESTERN_AUSTRALIA: [
        'Perth', 'Bunbury'
    ],
    COUNTRY_NORTHERN_TERRITORY: [
        'Darwin', 'Toowoomba'
    ],
    COUNTRY_SOUTH_AUSTRALIA: [
        'Adelaide'
    ],
    COUNTRY_QUEENSLAND: [
        'Brisbane', 'Gold Coast-Tweed', 'Sunshine Coast', 'Townsville', 'Cairns'
    ],
    COUNTRY_NEW_SOUTH_WALES: [
        'Sydney', 'Newcastle-Maitland', 'Wollongong', 'Albury-Wodonga'
    ],
    COUNTRY_VICTORIA: [
        'Melbourne', 'Geelong', 'Ballarat', 'Bendigo', 'Shepparton-Mooroopna'
    ],
    COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY: [
        'Canberra-Queanbeyan',
    ],
    COUNTRY_TASMANIA: [
        'Hobart', 'Launceston'
    ],

    # Antarctica
    COUNTRY_SOUTH_ORKNEY_ISLANDS: [

    ],
    COUNTRY_GRAHAM_LAND: [

    ],
    COUNTRY_MARIE_BYRD_LAND: [

    ],
    COUNTRY_QEEN_MAUD_LAND: [

    ],
    COUNTRY_VICTORIA_LAND: [

    ],
    COUNTRY_WILKES_LAND: [

    ],
}
