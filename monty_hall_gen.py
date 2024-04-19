import random
import tqdm
import argparse


def simulation(switch: bool, tests: int, doors: list[int]):
	i = 0
	hits = 0
	pbar = tqdm.tqdm(total=tests)
	
	while i < tests:
		doors_copy = doors.copy()
		chosen_door = random.choice(doors_copy)
		correct_door = random.choice(doors_copy)
		
		doors_copy.remove(chosen_door)
		temp = False
		if correct_door in doors_copy:
			doors_copy.remove(correct_door)
			temp = True
		
		doors_copy.remove(random.choice(doors_copy))
		if temp:
			doors_copy.append(correct_door)
		
		if switch:
			chosen_door = random.choice(doors_copy)
		
		if correct_door == chosen_door:
			hits += 1
		
		i += 1
		pbar.update(1)
	
	pbar.close()
	hits = round(hits / tests, 4)
	print(f'Percentage of games won: {hits * 100}%')


parser = argparse.ArgumentParser()

parser.add_argument('-t', '--tests', help='number of tests', type=int, default=100000000)
parser.add_argument('-d', '--doors', help='number of doors', type=int, default=3)

args = parser.parse_args()

tests = args.tests
doors = [j for j in range(args.doors)]

print(f'Probability of winning with {len(doors)} doors when switching: ', end='')
prob = 1/(args.doors - 2)
prob = 1 + prob
prob = prob/args.doors
prob = round(prob, 4) * 100
print(f'{prob}%\n')

print(f'Simulating games with {len(doors)} doors and switching...')
simulation(switch=True, tests=tests, doors=doors)
print()

print(f'Probability of winning with {len(doors)} doors but no switching: ', end='')
prob = 1/args.doors
prob = round(prob, 4) * 100
print(f'{prob}%\n')

print(f'Simulating games with {len(doors)} doors but no switching...')
simulation(switch=False, tests=tests, doors=doors)

