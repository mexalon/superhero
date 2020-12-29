import requests


def get_hero_id(hero_name):
    # если искать не имя героя целиком, метод выдаёт всех, у кого в имени есть искомое сочетание букв
    # в качестве айди остаётся первое вхождение
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero_name}')
    response.raise_for_status()
    if response.json()['response'] == 'success':
        the_hero = response.json()['results'][0]['id']
    else:
        the_hero = 'Unknown Hero'

    return the_hero


def get_hero_name(hero_id):
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/{hero_id}')
    response.raise_for_status()
    if response.json()['response'] == 'success':
        the_hero = response.json()['name']
    else:
        the_hero = "Unknown ID"

    return the_hero


def get_feature(hero_id, comparison_parameter):
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/{hero_id}/powerstats')
    response.raise_for_status()
    if response.json()['response'] == 'success':
        the_feature = response.json()[comparison_parameter]
        if the_feature.isdigit():
            result = int(the_feature)
    else:
        result = 0

    return result


def compare_heroes(comparison_parameter, heroes_list):
    if heroes_list != {}:
        all_heroes = ['spam']
        for hero in heroes_list:
            id_ = get_hero_id(hero)
            all_heroes.append({get_hero_name(id_): get_feature(id_, comparison_parameter)})

        all_heroes.pop(0)
        top_hero = sorted(all_heroes, key=lambda entry: list(entry.values())[0], reverse=True)
        return top_hero[0]


my_heroes_list = {'Thanos', 'Captain America', 'A-Bomb'}
my_comparison_parameter = 'intelligence'
number_one = compare_heroes(my_comparison_parameter, my_heroes_list)
if number_one is not None:
    print(f'{list(number_one.keys())[0]} has best {my_comparison_parameter} in this Gang')
else:
    print('There is no hero in your list')