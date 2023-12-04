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

func main() {
	couse := Couse{
		Name:        "Golang",
		Description: "Golang Couse",
		Price:       100,
	}
	http.HandleFunc("/", home)
	http.ListenAndServe(":8080", nil)
}

func home(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello World"))
}
