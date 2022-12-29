from pprint import pprint as ppr
import requests as req

res = req.get('https://api.github.com/users/sh1rokovs/repos')


def get_json(def_res):
    j_res = def_res.json()
    l_file = open('list_repos.txt', 'w+')
    for el in range(len(j_res)):
        l_file.write(j_res[el].get('full_name')[10::])
        l_file.write(f'\n')
    l_file.close()
    n_file = open('repos.json', 'w+')
    for el in range(len(j_res)):
        n_file.write(str(j_res[el]))
        n_file.write(f'\n')
    n_file.close()


if 300 <= res.status_code <= 399:
    #    res.headers.get('locations')
    #    res.text для текста
    #    res.content для фото, видео, музыки
    print()

if res.ok:
    get_json(res)
