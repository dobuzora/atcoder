package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var sc = bufio.NewScanner(os.Stdin)
	sc.Scan()
	s := sc.Text()
	a := strings.Split(s, "")
	if a[0] == a[1] && a[0] == a[2] {
		fmt.Println("Won")
	} else {
		fmt.Println("Lost")
	}
}