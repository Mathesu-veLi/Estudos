package main

import (
	"fmt"
	"net/http"
)

type Couse struct {
	Name        string
	Description string
	Price       int
}

func (c Couse) GetFullInfo() string {
	return fmt.Sprintf("Name: %s, Description: %s, Price: %d", c.Name, c.Description, c.Price)
}

func main() {
	couse := Couse{
		Name:        "Golang",
		Description: "Golang Couse",
		Price:       100,
	}

	fmt.Println(couse.GetFullInfo())

	http.HandleFunc("/", home)
	http.ListenAndServe(":8080", nil)
}

func home(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello World"))
}
