import requests

def the_smartest_hero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    res = requests.get(url) # делаем запрос GET на указаный URL
    file = res.json() # присваемаем переменую к оесурсу в формате json
    name_hero = ['Hulk', 'Captain America',  'Thanos']
    int = 0
    for x in file:
        if x['name'] in name_hero:
            power = x["powerstats"]
            smart_hero = power["intelligence"]
            if smart_hero > int:
                int = smart_hero
                name = x['name']
    return name

if __name__ == "__main__":
    print(the_smartest_hero())












