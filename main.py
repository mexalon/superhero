import requests


def get_hero(hero_name):
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero_name}')
    response.raise_for_status()
    return response.json()


def get_feature(hero_name, comparison_parameter):
    the_hero = get_hero(hero_name)
    the_feature = the_hero['results'][0]['powerstats'][comparison_parameter]
    if the_feature.isdigit():
        result = int(the_feature)
    else:
        result = False

    return result


def compare_heroes(comparison_parameter, *heroes_list):
    if heroes_list != ():
        all_heroes = ['spam']
        for hero in heroes_list:
            all_heroes.append({hero: get_feature(hero, comparison_parameter)})

        all_heroes.pop(0)
        top_hero = sorted(all_heroes, key=lambda entry: list(entry.values())[0], reverse=True)
        return top_hero[0]


my_heroes_list = ('Hulk', 'Captain America', 'spider-man', 'Niki Sanders', 'Thanos')
my_comparison_parameter = 'intelligence'
number_one = compare_heroes(my_comparison_parameter, *my_heroes_list)
print(f'{list(number_one.keys())[0]} has best {my_comparison_parameter} in this Gang')
