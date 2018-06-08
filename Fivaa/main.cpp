#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void helper(int n);

void fivaa(int n) {
    helper(n);
}

void helper(int n) {
    if (n <= 0) return;

    for (int i = 0; i < 2; i++) {
        printf("%d", (n-1));
    }
    for (int i = 0; i < n; i++) {
        printf("%d", (n+1));
    }
    printf("\n");
    helper(n-1);
}

int main()
{
    fivaa(5);
    getchar();
    return 0;
}
