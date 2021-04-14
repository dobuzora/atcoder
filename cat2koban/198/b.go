package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s int
	fmt.Scan(&s)
	for s%10 == 0 {
		s /= 10
	}
	str := strconv.Itoa(s)
	isPalindrome(str)
}

func isPalindrome(s string) {
	fmt.Println(s)
}