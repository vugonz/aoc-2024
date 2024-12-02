package main

import "testing"

func BenchmarkNormal(b *testing.B) {
	for n := 0; n < b.N; n++ {
		partTwo()
	}
}

func BenchmarkParallel(b *testing.B) {
	for n := 0; n < b.N; n++ {
		partTwoParallel()
	}
}
