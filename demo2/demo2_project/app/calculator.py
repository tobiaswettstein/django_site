from django.shortcuts import render, HttpResponse
import requests
import json

def one_one():

    import random
    d = 20
    g = 20
    log = []
    

    while d > 0 and g > 0:
    
        attack_roll_d = random.randint(1, 20)
        log.append('Dwarf rolls: ' + str(attack_roll_d) + '')
    
        if attack_roll_d + 1 >= 14 and attack_roll_d < 20:
            axe_damage = random.randint(1, 10)
            g = g - axe_damage
            log.append('Goblin takes ' + str(axe_damage) + ' points from the dwarven axe.')

        elif attack_roll_d == 20:
            log.append('Critical Hit!')
            axe_damage_crit = 3 * (random.randint(1, 10))
            g = g - axe_damage_crit
            log.append('Goblin takes ' + str(axe_damage_crit) + ' points from the dwarven axe.')
    
        else:
            log.append('Dwarf missed!')


        if g < 1:
            break
  
        attack_roll_g = random.randint(1, 20)
        log.append('Goblin rolls: ' + str(attack_roll_g))

        if attack_roll_g + 1 >= 15 and attack_roll_g < 20:
            spear_damage = random.randint(1, 8)
            d = d - spear_damage
            log.append('Dwarf takes ' + str(spear_damage) + ' points from the goblin spear.')

        elif attack_roll_g == 20:
            log.append('Critical Hit!')
            spear_damage_crit = 3 * (random.randint(1, 8))
            d = d - spear_damage_crit
            log.append('Dwarf takes ' + str(spear_damage_crit) + ' points from the goblin spear.')

        else:
            log.append('Goblin missed!')


    if d < 1:
        log.append('Goblin wins!')

    if g < 1:
        log.append('Dwarf wins!')

    return log


    # #this numbers rounds!!:

    # r = dict(list(enumerate(log)))
    # r_json = []
    # r_json.append(r)
    # return r_json

    # # or this:
    # dicts = {}
    # l = len(log)
    # k = range(l)
    # for i in k:
    #     dicts[i] = log[i]
    # return dicts

