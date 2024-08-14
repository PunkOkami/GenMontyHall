import random
import tqdm
import argparse


def monty_hall_calc(doors: int, switch: bool) -> float:
	switch_val = int(switch)

	prob = switch_val/ (doors - 2)
	prob += 1
	prob /= doors
	return prob


def monty_hall_sim(switch: bool, tests: int, doors: int) -> float:
	i = 0
	hits = 0
	pbar = tqdm.tqdm(total=tests)

	
	while i < tests:
		doors_arr = [j for j in range(doors)]
		chosen_door = random.choice(doors_arr)
		correct_door = random.choice(doors_arr)

		doors_arr.remove(chosen_door)

		oppened_door_ind = random.randint(0, len(doors_arr)-1)
		oppened_door = doors_arr[oppened_door_ind]
		if correct_door == oppened_door:
			if oppened_door == doors_arr[-1]:
				oppened_door_ind -= 1
			else:
				oppened_door_ind += 1
			oppened_door = doors_arr[oppened_door_ind]
		doors_arr.remove(oppened_door)
		
		if switch:
			chosen_door = random.choice(doors_arr)
		
		if correct_door == chosen_door:
			hits += 1
		
		i += 1
		pbar.update(1)
	
	pbar.close()
	hits = round(hits / tests, 4)
	return hits


parser = argparse.ArgumentParser(prog='GenMontyHall_py', description='Monty hall simulator - Python version')

parser.add_argument('-t', '--tests', help='number of tests', type=int, default=100000000)
parser.add_argument('-d', '--doors', help='number of doors', type=int, default=3)

args = parser.parse_args()

tests = args.tests
doors = args.doors

print(f'Probability of winning with {doors} doors when switching: ', end='')
print(f'{monty_hall_calc(doors=doors, switch=True) * 100}%\n')

print(f'Simulating games with {doors} doors and switching...')
hits = monty_hall_sim(switch=True, tests=tests, doors=doors)
print(f'Percentage of games won: {hits * 100}%')

print(f'Probability of winning with {doors} doors but no switching: ', end='')
print(f'{monty_hall_calc(doors=doors, switch=False) * 100}%\n')

print(f'Simulating games with {doors} doors but no switching...')
hits = monty_hall_sim(switch=False, tests=tests, doors=doors)
print(f'Percentage of games won: {hits * 100}%')
