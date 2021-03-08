#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i=0; i < (n); ++i)
int main() {
  int n, x;
  cin >> n >> x;
  x *= 100;
  int total = 0;
  rep(i, n) {
    int v, p;
    cin >> v >> p;
    int a = v*p;
    total += a;
    if (total > x) {
      cout << i+1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
  return 0;
}