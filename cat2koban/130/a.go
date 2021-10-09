package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var rd = bufio.NewReader(os.Stdin)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  bPrint(a < b, "0", "10")
}

func Scan() string {
	sc.Scan()
	return sc.Text()
}
func rScan() []rune {
	return []rune(Scan())
}
func iScan() int {
	n, _ := strconv.Atoi(Scan())
	return n
}
func fScan() float64 {
	n, _ := strconv.ParseFloat(Scan(), 64)
	return n
}
func SScan(n int) []string {
	a := make([]string, n)
	for i := 0; i < n; i++ {
		a[i] = Scan()
	}
	return a
}
func iSScan(n int) []int {
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = iScan()
	}
	return a
}
// slice := aScan(Scan(), 2)
func aScan(s string, n int) []string {
  a := make([]string, n)
  b := strings.Split(s, " ")
  for i :=0; i < n; i++ {
    a[i] = b[i]
  }
  return a
}
func atoiScan(s string, n int) []int {
	a := make([]int, n)
	b := strings.Split(s, " ")
	for i := 0; i < n; i++ {
		a[i] = atoi(b[i])
	}
	return a
}
func Read() string {
	buf := make([]byte, 0, 1000000)
	for {
		l, p, e := rd.ReadLine()
		if e != nil {
			panic(e)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}
func atoi(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}
func abs(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}
func mod(x, d int) int {
	x %= d
	if x < 0 {
		x += d
	}
	return x
}
func max(a ...int) int {
	x := -P3
	for i := 0; i < len(a); i++ {
		if x < a[i] {
			x = a[i]
		}
	}
	return x
}
func min(a ...int) int {
	x := P3
	for i := 0; i < len(a); i++ {
		if x > a[i] {
			x = a[i]
		}
	}
	return x
}
func sum(a []int) int {
	x := 0
	for _, v := range a {
		x += v
	}
	return x
}
func fSum(a []float64) float64 {
	x := 0.
	for _, v := range a {
		x += v
	}
	return x
}
func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
func modinv(a, m int) int {
	b, u, v := m, 1, 0
	for {
		t := a / b
		a -= t * b
		u -= t * v
		a, b, u, v = b, a, v, u
		if b == 0 {
			break
		}
	}
	u %= m
	if u < 0 {
		u += m
	}
	return u
}
func bPrint(f bool, x string, y string) {
	if f {
		fmt.Println(x)
	} else {
		fmt.Println(y)
	}
}
func iSSPrint(x []int) {
	fmt.Println(strings.Trim(fmt.Sprint(x), "[]"))
}
func sorted(x []int, r bool) []int {
	y := make([]int, len(x))
	copy(y, x)
	if r {
		sort.Sort(sort.Reverse(sort.IntSlice(y)))
		return y
	}
	sort.Ints(y)
	return y
}
func initSlice(n, x int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = x
	}
	return ret
}
func last(a []int) int {
	if len(a) == 0 {
		return 0
	}
	return a[len(a)-1]
}
func factorial(n, m int) ([]int, []int) {
	f := make([]int, n+1)
	inv := make([]int, n+1)
	f[0] = 1
	inv[0] = 1
	for i := 1; i <= n; i++ {
		f[i] = f[i-1] * i % m
		inv[i] = modinv(f[i], m)
	}
	return f, inv
}
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
// slice1 := aScan(Scan(), 2)
// slice2 := []string{"0", "1", "2"}
// array := unique(slice1, slice2)
func unique(ss ...[]string) []string {
    m := map[string]int{}
    for _, s := range ss {
      for _, v := range s {
        m[v]++ // 出現回数をカウント
      }
    }
    res := []string{}
    for k, v := range m {
      if v == 1 {
        // 出現回数が１回のものだけを抽出
        res = append(res, k)
      }
    }
    return res
}
// スライスの中身削除
func removeInts(ints []int, search int) []int {
  result := []int{}
  for _, v := range ints {
    if v != search {
      result = append(result, v)
    }
  }
  return result
}

// スライスの中身削除
func removeStrings(strings []string, search string) []string {
  result := []string{}
  for _, v := range strings {
    if v != search {
      result = append(result, v)
    }
  }
  return result
}

var P1 int = 1000000007
var P2 int = 998244353
var P3 int = 1<<61 - 1
var BINF int = 1 << 60
