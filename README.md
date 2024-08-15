# GenMontyHall
Generalisation of Monty Hall problem to any natural number of doors

Script calculates probability of winning with number of doors chosen when switching doors and when not switching doors as well it then simulates chosen number of tests. Coded in both Python and Go.
Showcase code


## Used packages:
### Python:
- [tqdm](https://github.com/tqdm/tqdm)
### Go:
- [progressbar](https://github.com/schollz/progressbar)
- [ff](https://github.com/peterbourgon/ff)

## Installation
Clone code repo...
```zsh
git clone https://github.com/PunkOkami/GenMontyHall.git
```
...and build the binary of Go code
```zsh
go build -o monty_hall_go monty_hall_gen.go
```

## Usage
Script has default option values that will make it into classic Monty Hall problem
### Python
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
### Go
```shell
./monty_hall_go 
```
Output:
```shell
Probability of winning when switching 66.67%
Simulating 100% |█████████████████████████████████████████████████████████████████████████████████| (10000000/10000000, 5329730 it/s)        
Percentage of wins when switching 66.66                                                                                                      
Probability of winning when not switching 33.33%
Simulating 100% |█████████████████████████████████████████████████████████████████████████████████| (10000000/10000000, 5685147 it/s)        
Percentage of wins when switching 33.35   
```

## Options
### Python
```shell
python monty_hall_gen.py -h
```
- -t/--tests - number of tests for each simulation
- -d/--doors - number of doors
### Go
```shell
 ./monty_hall_go -h
```
- -d, --doors INT   number of doors (default: 3)
- -t, --tests INT   number of tests (default: 10000000)

## Note
All code and math functions used in this repo were created without stealing other people's idea, so they may be a bit shit.
You have been warned.