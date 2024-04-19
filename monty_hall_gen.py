import random
import tqdm
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--tests', help='number of tests', type=int, default=100000000)
parser.add_argument('-s', '--no_switch', help='flag specifing not to switch doors', action='store_false')
parser.add_argument('-d', '--doors', help='number of doors', type=int, default=3)

args = parser.parse_args()

tests = args.tests
doors = [j for j in range(args.doors)]
switch = args.switch
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
	
	i+=1
	pbar.update(1)

pbar.close()
hits = round(hits/tests, 4)
print(f'{hits*100}%')
