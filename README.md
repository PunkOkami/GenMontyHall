# GenMontyHall
Generalisation of Monty Hall problem to any natural number of doors

## Used packages:
- [tqdm](https://github.com/tqdm/tqdm)

## Usage
Script has default option values that will make it into classic Monty Hall problem with contestant always switching when given choice
```shell
python monty_hall_gen.py
```
Output:
```shell
100%|██████████| 100000000/100000000 [02:38<00:00, 632281.07it/s]
66.66%
```

### Options
```shell
python monty_hall_gen.py -h
```
- -t/--tests - number of tests for each simulation
- -d/--doors - number of doors
- -s/--no_switch - flag specifying not to switch doors

## Note
All code and math functions used in this repo were created without stealing other people's idea, so they may be a bit shit.
You have been warned.

Repo still WIP, will be expanded (maybe) this week (hopefully).