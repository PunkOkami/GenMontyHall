package main

import (
	"fmt"
	"github.com/peterbourgon/ff/v4"
	"github.com/peterbourgon/ff/v4/ffhelp"
	"github.com/schollz/progressbar/v3"
	"math/rand"
	"os"
)

func monty_hall_calc(doors int, switching bool) float32 {

	var switching_val float32 = 0
	if switching {
		switching_val = 1.0
	}

	prob := switching_val
	prob = prob / (float32(doors - 2))
	prob++
	prob = prob / float32(doors)
	return prob
}

func monty_hall_sim(test int, doors int, switching bool) (float32, error) {
	var hits int = 0

	var prog_bar = progressbar.Default(int64(test), "Simulating")

	for i := 0; i < test; i++ {
		var doors_arr []int

		for j := 0; j < doors; j++ {
			doors_arr = append(doors_arr, j)
		}

		var correct_door = doors_arr[rand.Intn(len(doors_arr))]
		var chosen_door = doors_arr[rand.Intn(len(doors_arr))]

		var doors_copy = append(doors_arr[:chosen_door], doors_arr[chosen_door+1:]...)

		var openned_door_ind = rand.Intn(len(doors_copy))
		var oppened_door = doors_copy[openned_door_ind]
		if oppened_door == correct_door {
			if oppened_door == doors_copy[len(doors_copy)-1] {
				openned_door_ind--
			} else {
				openned_door_ind++
			}
		}

		doors_copy = append(doors_copy[:openned_door_ind], doors_copy[openned_door_ind+1:]...)

		if switching {
			chosen_door = doors_copy[rand.Intn(len(doors_copy))]
		}

		if chosen_door == correct_door {
			hits++
		}

		err := prog_bar.Add(1)
		if err != nil {
			return 0, err
		}
	}

	err := prog_bar.Close()
	if err != nil {
		return 0, nil
	}

	return float32(hits), nil
}

func main() {
	flag_set := ff.NewFlagSet("GenMontyHall_go")
	var (
		doors = flag_set.Int('d', "doors", 3, "number of doors")
		tests = flag_set.Int('t', "tests", 10000000, "number of tests")
		help  = flag_set.Bool('h', "help", "help")
	)

	err := ff.Parse(flag_set, os.Args[1:])
	if err != nil {
		fmt.Println("Paring arguments failed: ", err)
	}

	if *help {
		fmt.Printf("%s\n", ffhelp.Flags(flag_set))
		os.Exit(0)
	}

	var switch_prob = monty_hall_calc(*doors, true) * 100
	fmt.Printf("Probability of winning when switching %.2f%%\n", switch_prob)

	switch_sim, err := monty_hall_sim(*tests, *doors, true)
	if err != nil {
		fmt.Printf("Error happened with progress bar, poor you %v\n", err)
		os.Exit(1)
	}
	switch_sim = switch_sim / float32(*tests) * 100
	fmt.Printf("Percentage of wins when switching %.2f\n", switch_sim)

	var non_switch_prob = monty_hall_calc(*doors, false) * 100
	fmt.Printf("Probability of winning when not switching %.2f%%\n", non_switch_prob)

	non_switch_sim, err := monty_hall_sim(*tests, *doors, false)
	if err != nil {
		fmt.Printf("Error happened with progress bar, poor you %v\n", err)
		os.Exit(1)
	}

	non_switch_sim = non_switch_sim / float32(*tests) * 100
	fmt.Printf("Percentage of wins when switching %.2f", non_switch_sim)
}
