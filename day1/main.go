package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func insertSorted(arr []int, item int) []int {
	i := sort.SearchInts(arr, item)
	arr = append(arr, 0) // resize the slice to accommodate the new element
	copy(arr[i+1:], arr[i:])
	arr[i] = item
	return arr
}

func first() int {
	f, err := os.OpenFile("input.txt", os.O_RDONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	first := make([]int, 0)
	second := make([]int, 0)

	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanLines)
	for scan.Scan() {
		items := strings.Split(scan.Text(), "   ")
		f, _ := strconv.Atoi(items[0])
		s, _ := strconv.Atoi(items[1])
		first = insertSorted(first, f)
		second = insertSorted(second, s)
	}

	r := 0.0
	for i, v := range first {
		r += math.Abs(float64(second[i] - v))
	}

	if err := scan.Err(); err != nil {
		panic(err)
	}

	return int(r)
}

func second() int {
	f, err := os.OpenFile("input.txt", os.O_RDONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	left := make([]int, 0)
	right := make([]int, 0)
	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanLines)
	for scan.Scan() {
		items := strings.Split(scan.Text(), "   ")
		f, _ := strconv.Atoi(items[0])
		s, _ := strconv.Atoi(items[1])
		left = insertSorted(left, f)
		right = insertSorted(right, s)
	}

	occurs := make(map[int]int)
	for _, v := range right {
		occurs[v]++
	}

	fmt.Println(occurs)
	r := 0
	for _, v := range left {
		if occurs, exists := occurs[v]; exists {
			r += v * occurs
		}
	}

	if err := scan.Err(); err != nil {
		panic(err)
	}

	return int(r)
}

func main() {
	fmt.Println(first(), second())
}
