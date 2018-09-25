#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <math.h>
#include <set>

using namespace std;
typedef long long ll;
const ll MAX=1e9+9;
ll fastPower(ll a,ll b){
  ll p=1;
  while(b){
    if(b&1)p=p*a%MAX;
    b>>=1,a=a*a%MAX;
  }
  return p;
}

int main(){
  ll n,a,b,k;
  cin>>n>>a>>b>>k;
  string s;
  cin>>s;
  ll cur=0;
  for(int i=0;i<k;i++){
      if(s[i]=='+'){
        cur=(cur+fastPower(a,n-i)*fastPower(b,i)%MAX)%MAX;
      }
      else{
        cur=(cur-fastPower(a,n-i)*fastPower(b,i)%MAX+MAX)%MAX;
      }
  }
  ll t=fastPower(a,k*(MAX-2)%(MAX-1))*fastPower(b,k)%MAX;
  if(t==1){
    cout<<cur*((n+1)/k)%MAX;
  }else{
    cout<<cur*fastPower(t-1,MAX-2)%MAX*(fastPower(t,(n+1)/k)-1)%MAX;
  }
  return 0;
}
