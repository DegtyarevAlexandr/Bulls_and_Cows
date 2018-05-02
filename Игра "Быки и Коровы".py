#!/usr/bin/env python3
# На этом файле я эксперементирую с его запуском
# Игра "Быки и Коровы" Версия: 0.5.2

import random


def unique_random_number():
	random_unique_number = random.sample(range(10), 4)
	str_urn = [str(i) for i in (random_unique_number)]
	return str_urn


def player_number():
	tmp_input = ''

	while True:
		tmp_input = input('''Введите число из четырёх неповторяющихся цифр. Например: 0123\n''')
		if tmp_input.isdigit() and len(tmp_input) == 4 and len(set(tmp_input)) == 4:
			break
		elif tmp_input == 'eeee':
			print('Кулхацкер? Это ты? =)')
		else:
			print('Так не пойдёт. Соблюдайте правила.')

	return list(tmp_input)


# как ещё можно реализовать подобную проверку?
def compare_numbers(real_numbers, try_numbers):
	bulls, cows = 0, 0

	for i, try_number in enumerate(try_numbers):
		if try_number in real_numbers:
			if try_numbers[i] == real_numbers[i]:
				bulls += 1
			else:
				cows += 1

	print('Быков:', bulls, '  Коров:', cows)
	return bulls, cows


print('\n---------------', 'Игра "Быки и Коровы"', '---------------\n')
print('          Я загадал четырёхзначное число!')
print('           В нём нет повторяющихся цифр.')
print('             Попробуйте угадать его. \n')

secret_number = unique_random_number()

print('             ', secret_number, '\n')  # строка для отладки
print('Чтобы начать игру:')

while True:
	try_player_number = player_number()
	bulls, cows = compare_numbers(secret_number, try_player_number)

	if bulls == 4:
		print('\n---------------', 'Поздравляю! Вы угадали. Это было число:', '---------------')
		print('                        ', secret_number)
		break
