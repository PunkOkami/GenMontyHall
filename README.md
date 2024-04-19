# GenMontyHall
Generalisation of Monty Hall problem to any natural number of doors

Script calculates probability of winning with number of doors chosen when switching doors and when not switching doors as well it then simulates chosen number of tests

## Used packages:
- [tqdm](https://github.com/tqdm/tqdm)

## Usage
Script has default option values that will make it into classic Monty Hall problem with contestant always switching when given choice
```shell
python monty_hall_gen.py
```
Output:
```shell
Probability of winning with 3 doors when switching: 66.67%

Simulating games with 3 doors and switching...
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100000000/100000000 [02:10<00:00, 766275.21it/s]
Percentage of games won: 66.67%

Probability of winning with 3 doors but no switching: 33.33%

Simulating games with 3 doors but no switching...
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100000000/100000000 [01:44<00:00, 958563.34it/s]
Percentage of games won: 33.33%
```

### Options
```shell
python monty_hall_gen.py -h
```
- -t/--tests - number of tests for each simulation
- -d/--doors - number of doors

## Note
All code and math functions used in this repo were created without stealing other people's idea, so they may be a bit shit.
You have been warned.

Repo still WIP, will be expanded (maybe) this week (hopefully).