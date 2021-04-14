package main

import (
	"fmt"
)

func checkEven(nums []int) bool {

}

func main() {
	var n int
	fmt.Scan(&n)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&nums[i])
	}
	fmt.Println(nums)
}
