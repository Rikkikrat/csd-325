# Rikki Kratochvil
# Assignment: 7.2 Test Cases
#Date: 05/01/2026

def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    

print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 13960000))
print(city_country("paris", "france", 2148000, "french"))
