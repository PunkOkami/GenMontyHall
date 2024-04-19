import random
import tqdm

tests = 100000000
doors = [j for j in range(3)]
switch = True
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
