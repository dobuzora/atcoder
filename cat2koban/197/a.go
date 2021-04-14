package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scan(&s)
	a := strings.Split(s, "")
	fmt.Print(a[1])
	fmt.Print(a[2])
	fmt.Print(a[0])
}