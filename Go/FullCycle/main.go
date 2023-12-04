package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Course struct {
	Name        string
	Description string
	Price       int
}

func (c Course) getFullInfo() string {
	return fmt.Sprintf("Name: %s, Description: %s, Price: %d", c.Name, c.Description, c.Price)
}

func main() {
	http.HandleFunc("/", home)
	http.ListenAndServe(":8080", nil)
}

func home(res http.ResponseWriter, req *http.Request) {
	course := Course{
		Name:        "Golang",
		Description: "Golang Course",
		Price:       100,
	}
	
	json.NewEncoder(res).Encode(course)
}
