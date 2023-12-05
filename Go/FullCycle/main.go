package main

import (
	"fmt"
	"time"
)

func worker(workerID int, data chan int) {
	for x := range data {
		fmt.Printf("Worker %d received %d\n", workerID, x)
		time.Sleep(time.Second)
	}
}

func main() {
	channel := make(chan int)
	for i := 0; i < 3; i++ {
		go worker(i, channel)
	}

	for i := 0; i < 10; i++ {
		channel <- i
	}
}
