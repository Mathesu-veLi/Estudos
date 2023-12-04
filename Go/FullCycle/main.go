package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type Course struct {
	Name        string
	Description string
	Price       int
}

func (c Course) getFullInfo() string {
	return fmt.Sprintf("Name: %s, Description: %s, Price: %d", c.Name, c.Description, c.Price)
}

func counter() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
		time.Sleep(time.Second)
	}
}

func main() {
	go counter()
	go counter()
	counter()
}

func home(res http.ResponseWriter, req *http.Request) {
	course := Course{
		Name:        "Golang",
		Description: "Golang Course",
		Price:       100,
	}
	
	json.NewEncoder(res).Encode(course)
}
