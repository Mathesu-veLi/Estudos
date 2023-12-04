package main

func main() {
	resultado, status := sum(10, 20)
	println(resultado, status)
}

func sum(x int, y int) (int, bool) {
	if x > 10 {
		return x + y, true
	}

	return x + y, false
}
