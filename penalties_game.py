import random
import time

name_gamer = input("Напиши си името : \n")
print(f"Здравей, {name_gamer},")
print('Добре дошъл в играта "Дузпи"\n')
print('Избери си отбор, с който ще играеш като напишеш цифрата срещу съответния отбор\n')
print("1 - Манчестър Юнайтед")
print("2 - Реал Мадрид\n")
gamer_team_number = input("Очаквам твоя избор:")
gamer_team = ''
gamer_goalkeeper = ''
gamer_player1 = ''
gamer_player2 = ''
gamer_player3 = ''
gamer_player4 = ''
gamer_player5 = ''
if gamer_team_number == '1':
    gamer_team = "Манчестър Юнайтед"
    gamer_goalkeeper = 'Давид Де Хеа'
    gamer_player1 = 'Кристиан Ериксен'
    gamer_player2 = 'Маркъс Рашфорд'
    gamer_player3 = 'Джендън Санчо'
    gamer_player4 = 'Каземиро'
    gamer_player5 = 'Бруно Фернандеш'
    print("Ти избра Манчестър Юнайтед\n")
    print(f"За твоя отбор на вратата застава {gamer_goalkeeper}")
    print(f"Твоите изпълнители на дузпи ще бъдат {gamer_player1}, {gamer_player2}, {gamer_player3}, {gamer_player4},"
          f" {gamer_player5}.\n")
elif gamer_team_number == '2':
    gamer_team = "Реал Мадрид"
    gamer_goalkeeper = 'Кибо Куртоа'
    gamer_player1 = 'Ферико Валверде'
    gamer_player2 = 'Тони Крос'
    gamer_player3 = 'Лука Модрич'
    gamer_player4 = 'Винисиус'
    gamer_player5 = 'Карим Бензема'
    print("Ти избра Реал Мадрид\n")
    print(f"За твоя отбор на вратата застава {gamer_goalkeeper}")
    print(f"Твоите изпълнители на дузпи ще бъдат {gamer_player1}, {gamer_player2}, {gamer_player3}, {gamer_player4},"
          f" {gamer_player5}")

oponent_goalkeeper = ''
oponent_player1 = ''
oponent_player2 = ''
oponent_player3 = ''
oponent_player4 = ''
oponent_player5 = ''
time.sleep(2)
print('Избери отбор, срещу който ще играеш като напишеш цифрата срещу съответния отбор\n')
print("1 - Манчестър Юнайтед")
print("2 - Реал Мадрид\n")
oponent_team_number = input("Очаквам твоя избор:")
oponent_team = ''
if oponent_team_number == '1':
    oponent_team = "Манчестър Юнайтед"
    oponent_goalkeeper = 'Давид Де Хеа'
    oponent_player1 = 'Кристиан Ериксен'
    oponent_player2 = 'Каземиро'
    oponent_player3 = 'Джендън Санчо'
    oponent_player4 = 'Маркъс Рашфорд'
    oponent_player5 = 'Бруно Фернандеш'
    print("Ти избра да играеш срещу Манчестър Юнайтед\n")
    print(f"За техния отбор на вратата застава {oponent_goalkeeper}")
    print(f"Техните изпълнители на дузпи ще бъдат {oponent_player1}, {oponent_player2}, {oponent_player3},"
          f" {oponent_player4},{oponent_player5}.\n")
elif oponent_team_number == '2':
    oponent_team = "Реал Мадрид"
    oponent_goalkeeper = 'Кибо Куртоа'
    oponent_player1 = 'Ферико Валверде'
    oponent_player2 = 'Тони Крос'
    oponent_player3 = 'Лука Модрич'
    oponent_player4 = 'Винисиус'
    oponent_player5 = 'Карим Бензема'
    print("Ти избра да играеш срещу Реал Мадрид\n")
    print(f"За техния отбор на вратата застава {oponent_goalkeeper}")
    print(f"Техните изпълнители на дузпи ще бъдат {oponent_player1}, {oponent_player2}, {oponent_player3}, "
          f"{oponent_player4},{oponent_player5}.\n")

oponent_reaction_list_pressure = ['1', '2', '3']
oponent_reaction_list = ['1', '2', '3', '4', '5']

gamer_score = 0
oponent_score = 0
penalty_count = 0
result = str(gamer_score) + str(oponent_score)
for i in range(1, 6):
    penalty_count += 1
    if penalty_count == 1:
        oponent_reaction_taker = random.choice(oponent_reaction_list)
        oponent_reaction_keeper = random.choice(oponent_reaction_list)
        time.sleep(2)
        print(f'Първа дузпа за отбора на {gamer_team}.')
        print(f'Зад топката застава {gamer_player1}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3- Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще изпълниш дузпата:')
        if gamer_reaction != oponent_reaction_keeper:
            print(f'{gamer_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            gamer_score += 1
        else:
            print(f'{gamer_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{oponent_goalkeeper} хвана твоята дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')
        time.sleep(1)
        print(f'Първа дузпа за отбора на {oponent_team}.')
        print(f'Зад топката застава {oponent_player1}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3- Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще се хвърли твоят вратар:')
        if gamer_reaction != oponent_reaction_taker:
            print(f'{oponent_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            oponent_score += 1
        else:
            print(f'{oponent_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{gamer_goalkeeper} хвана противниковата дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')




    elif penalty_count == 2:
        oponent_reaction_taker = random.choice(oponent_reaction_list)
        oponent_reaction_keeper = random.choice(oponent_reaction_list)
        time.sleep(1)
        print(f'Втора дузпа за отбора на {gamer_team}.')
        print(f'Зад топката застава {gamer_player2}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3- Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще изпълниш дузпата:')
        if gamer_reaction != oponent_reaction_keeper:
            print(f'{gamer_player2} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            gamer_score += 1
        else:
            print(f'{gamer_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{oponent_goalkeeper} хвана твоята дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')
        time.sleep(1)
        print(f'Втора дузпа за отбора на {oponent_team}.')
        print(f'Зад топката застава {oponent_player2}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3- Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще се хвърли твоят вратар:')
        if gamer_reaction != oponent_reaction_taker:
            print(f'{oponent_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            oponent_score += 1
        else:
            print(f'{oponent_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{gamer_goalkeeper} хвана противниковата дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')




    elif penalty_count == 3:
        oponent_reaction_taker = random.choice(oponent_reaction_list)
        oponent_reaction_keeper = random.choice(oponent_reaction_list)
        time.sleep(1)
        print(f'Трета дузпа за отбора на {gamer_team}.')
        print(f'Зад топката застава {gamer_player3}.')
        print("Напрежението върху футболистите се покачва и вече имаш само 3 избора:")
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3 - Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще изпълниш дузпата:')
        if gamer_reaction != oponent_reaction_keeper:
            print(f'{gamer_player3} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            gamer_score += 1
        else:
            print(f'{gamer_player3} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{oponent_goalkeeper} хвана твоята дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')
        time.sleep(1)
        print(f'Трета дузпа за отбора на {oponent_team}.')
        print(f'Зад топката застава {oponent_player3}.')
        print("Напрежението върху футболистите се покачва и вече имаш само 3 избора:")
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Долен ляв ъгъл\n"
              "2 - Горен ляв ъгъл\n"
              "3 - Средата на вратата\n"
              "4 - Долен десен ъгъл\n"
              "5 - Горен десен ъгъл\n")
        gamer_reaction = input('Избери къде ще се хвърли твоя вратар:')
        if gamer_reaction != oponent_reaction_taker:
            print(f'{oponent_player3} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            oponent_score += 1
        else:
            print(f'{oponent_player3} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{gamer_goalkeeper} хвана противниковата дузпа')
        if gamer_score == 0 and oponent_score == 3:
            break
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')





    elif penalty_count == 4:
        oponent_reaction_taker = random.choice(oponent_reaction_list_pressure)
        oponent_reaction_keeper = random.choice(oponent_reaction_list_pressure)
        time.sleep(1)
        print(f'Четвърта дузпа за отбора на {gamer_team}.')
        print(f'Зад топката застава {gamer_player4}.')
        print("Напрежението върху футболистите се покачва и вече имаш само 3 избора:")
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Ляв ъгъл\n"
              "2 - Средата на вратата\n"
              "3 - Десен ъгъл\n")
        gamer_reaction = input('Избери къде ще изпълниш дузпата:')
        if gamer_reaction != oponent_reaction_keeper:
            print(f'{gamer_player4} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            gamer_score += 1
        else:
            print(f'{gamer_player4} се засилва.')
            time.sleep(1)
            print('Стреля')
            time.sleep(1)
            print('И пропуска!')
            print(f'{oponent_goalkeeper} хвана твоята дузпа')
            if gamer_score == 0 and oponent_score == 3:
                break
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')
        time.sleep(1)
        print(f'Четвърта дузпа за отбора на {oponent_team}.')
        print(f'Зад топката застава {oponent_player4}.')
        print("Напрежението върху футболистите се покачва и вече имаш само 3 избора:")
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Ляв ъгъл\n"
              "2 - Средата на вратата\n"
              "3 - Десен ъгъл\n")
        gamer_reaction = input('Избери къде ще се хвърли твоя вратар:')
        if gamer_reaction != oponent_reaction_taker:
            print(f'{oponent_player4} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И бележи!')
            oponent_score += 1
        else:
            print(f'{oponent_player1} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(1)
            print('И пропуска!')
            print(f'{gamer_goalkeeper} хвана противниковата дузпа')
            if (gamer_score == 2 and oponent_score == 4) or (gamer_score == 1 and oponent_score == 3) or \
                    (gamer_score == 0 and oponent_score == 2) or (gamer_score == 4 and oponent_score == 2)\
                    or (gamer_score == 3 and oponent_score == 1):
                break
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')






    elif penalty_count == 5:
        oponent_reaction_taker = random.choice(oponent_reaction_list_pressure)
        oponent_reaction_keeper = random.choice(oponent_reaction_list_pressure)
        time.sleep(1)
        print(f'Пета дузпа за отбора на {gamer_team}.')
        print(f'Зад топката застава {gamer_player5}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Ляв ъгъл\n"
              "2 - Средата на вратата\n"
              "3 - Десен ъгъл\n")
        gamer_reaction = input('Избери къде ще изпълниш дузпата:')
        if gamer_reaction != oponent_reaction_keeper:
            print(f'{gamer_player5} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(2)
            print('И бележи!')
            gamer_score += 1
            gamer_score += 1
        else:
            print(f'{gamer_player5} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(2)
            print('И пропуска!')
            print(f'{oponent_goalkeeper} хвана твоята дузпа')
            if (gamer_score == 3 and oponent_score == 3) or (gamer_score == 4 and oponent_score == 2) or\
                    (gamer_score == 3 and oponent_score == 1):
                break
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')
        time.sleep(1)
        print(f'Пета дузпа за отбора на {oponent_team}.')
        print(f'Зад топката застава {oponent_player5}.')
        print("Всяка посока съответства номера посочен срещу нея :\n"
              "1 - Ляв ъгъл\n"
              "2 - Средата на вратата\n"
              "3 - Десен ъгъл\n")
        gamer_reaction = input('Избери къде ще се хвърли твоя вратар:')
        if gamer_reaction != oponent_reaction_taker:
            print(f'{oponent_player5} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(2)
            print('И бележи!')
            oponent_score += 1
        else:
            print(f'{oponent_player5} се засилва.')
            time.sleep(1)
            print('Стреля.')
            time.sleep(2)
            print('И пропуска!')
            print(f'{gamer_goalkeeper} хвана противниковата дузпа')
        print(f'Резултатът е {gamer_score}:{oponent_score}\n')

man_utd_reserves = ['Давид Де Хеа', 'Алехандро Гарначо''Фред','Рафаел Варан','Лисандро Мартинез']
real_madrid_reserves = ['Едер Милитао', 'Даниел Карвахал''Антионио Рюдигер','Камавинга','Родриго']
penalty_taker = ''

if gamer_score > oponent_score:
    print(f'Честито, {name_gamer}!')
    print(f'Ти победи {oponent_team} с резултат {gamer_score}:{oponent_score}')
elif gamer_score < oponent_score:
    print(f'Съжалявам, {name_gamer}')
    print(f'Ти загуби от {oponent_team} с резултат {gamer_score}:{oponent_score}.')
elif gamer_score == oponent_score:
    while True:
        if gamer_score > oponent_score:
            print(f'Честито, {name_gamer}!')
            print(f'Ти победи {oponent_team} с резултат {gamer_score}:{oponent_score}')
        elif gamer_score < oponent_score:
            print(f'Съжалявам, {name_gamer}')
            print(f'Ти загуби от {oponent_team} с резултат {gamer_score}:{oponent_score}.')
        else:
            penalty_count += 1
            penalty_taker = random.choice(man_utd_reserves)
            oponent_reaction_taker = random.choice(oponent_reaction_list_pressure)
            oponent_reaction_keeper = random.choice(oponent_reaction_list_pressure)
            time.sleep(1)
            print(f'{penalty_count}-та дузпа за отбора на {gamer_team}.')
            print(f'Зад топката застава {penalty_taker}.')
            print("Всяка посока съответства номера посочен срещу нея :\n"
                  "1 - Ляв ъгъл\n"
                  "2 - Средата на вратата\n"
                  "3 - Десен ъгъл\n")
            gamer_reaction = input('Избери къде ще изпълниш дузпата:')
            if gamer_reaction != oponent_reaction_keeper:
                print(f'{penalty_taker} се засилва.')
                time.sleep(1)
                print('Стреля.')
                time.sleep(2)
                print('И бележи!')
                gamer_score += 1
                gamer_score += 1
            else:
                print(f'{penalty_taker} се засилва.')
                time.sleep(1)
                print('Стреля.')
                time.sleep(2)
                print('И пропуска!')
                print(f'{oponent_goalkeeper} хвана твоята дузпа')
            print(f'Резултатът е {gamer_score}:{oponent_score}\n')
            time.sleep(1)
            penalty_taker = random.choice(real_madrid_reserves)
            print(f'{penalty_count}-та дузпа за отбора на {oponent_team}.')
            print(f'Зад топката застава {penalty_taker}.')
            print("Всяка посока съответства номера посочен срещу нея :\n"
                  "1 - Ляв ъгъл\n"
                  "2 - Средата на вратата\n"
                  "3 - Десен ъгъл\n")
            gamer_reaction = input('Избери къде ще се хвърли твоя вратар:')
            if gamer_reaction != oponent_reaction_taker:
                print(f'{penalty_taker} се засилва.')
                time.sleep(1)
                print('Стреля.')
                time.sleep(2)
                print('И бележи!')
                oponent_score += 1
            else:
                print(f'{penalty_taker} се засилва.')
                time.sleep(1)
                print('Стреля.')
                time.sleep(2)
                print('И пропуска!')
                print(f'{gamer_goalkeeper} хвана противниковата дузпа')
            print(f'Резултатът е {gamer_score}:{oponent_score}\n')




