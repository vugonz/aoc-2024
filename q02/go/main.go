package main

import (
	"bufio"
	"context"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func analyzeArray(start int, arr []int) (bool, []int) {
	ascending := arr[start] < arr[start+1]
	for i := start + 1; i < len(arr); i++ {
		curr := arr[i]
		prev := arr[i-1]
		diff := math.Abs(float64(curr - prev))

		if diff < 1.0 || diff > 3.0 || (ascending && (curr < prev)) || (!ascending && (curr > prev)) {
			return false, []int{i, i - 1, i - 2}
		}
	}
	return true, nil
}

// This is slower
func partTwoParallel() int {
	f, err := os.OpenFile("input.txt", os.O_RDONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanLines)

	safe := 0
	for scan.Scan() {
		arr := make([]int, 0, 16)
		items := strings.Split(scan.Text(), " ")
		for _, x := range items {
			v, _ := strconv.Atoi(x)
			arr = append(arr, v)
		}
		valid, invalidLvlsIdxs := analyzeArray(0, arr)
		if valid {
			safe++
			continue
		}

		ch := make(chan bool)
		ctx, cancel := context.WithCancel(context.Background())
		goro := 0
		for _, lvl := range invalidLvlsIdxs {
			if lvl < 0 {
				continue
			}
			goro++
			go func(lvl int) {
				start := lvl - 2
				if start < 0 {
					start = 0
				}
				aux := make([]int, len(arr))
				_ = copy(aux, arr)
				aux = append(aux[:lvl], aux[lvl+1:]...)
				valid, _ := analyzeArray(start, aux)
				select {
				case <-ctx.Done():
					break
				case ch <- valid:
					break
				}
			}(lvl)
		}
		for range goro {
			if <-ch {
				safe++
				break
			}
		}
		cancel()
	}
	return safe
}

func partTwo() int {
	f, err := os.OpenFile("input.txt", os.O_RDONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanLines)

	safe := 0
	for scan.Scan() {
		arr := make([]int, 0, 16)
		items := strings.Split(scan.Text(), " ")
		for _, x := range items {
			v, _ := strconv.Atoi(x)
			arr = append(arr, v)
		}
		valid, invalidLvlsIdxs := analyzeArray(0, arr)
		if valid {
			safe++
			continue
		}

		for _, lvl := range invalidLvlsIdxs {
			if lvl < 0 {
				continue
			}
			start := lvl - 2
			if start < 0 {
				start = 0
			}
			aux := make([]int, len(arr))
			_ = copy(aux, arr)
			aux = append(aux[:lvl], aux[lvl+1:]...)
			if valid, _ := analyzeArray(start, aux); valid {
				safe++
				break
			}
		}
	}
	return safe
}

func partOne() int {
	f, err := os.OpenFile("input.txt", os.O_RDONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanLines)

	safe := 0
	for scan.Scan() {
		arr := make([]int, 0, 16)
		items := strings.Split(scan.Text(), " ")
		for _, x := range items {
			v, _ := strconv.Atoi(x)
			arr = append(arr, v)
		}
		if valid, _ := analyzeArray(0, arr); valid {
			safe += 1
		}
	}
	return safe
}

func main() {
	fmt.Println(partOne(), partTwo(), partTwoParallel())
}
