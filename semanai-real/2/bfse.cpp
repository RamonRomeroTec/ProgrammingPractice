#include <iostream>
using namespace std;

  int l[100001],aux[100001],aux2[100001],p[100001];
int main() {
  int n = 0, m= 0, i = 0, j, c = 0;
  cin >> n >> m;
  for (i=0;i<n;i++){
    cin >> l[i];
  }
    for (i = n-1; i >= 0; i--)
    {
     if (aux[l[i]] == 0)
        { aux2[i] = aux2[i + 1] + 1;
        }
        else
        { aux2[i] = aux2[i + 1];
        }
        aux[l[i]] = 1;
    }

    for (i = 0; i<m; i++)
    {
        cin>>c;
        p[i]=aux2[c-1];

    }

    for (i = 0; i<m; i++){
        cout<<p[i]<<endl;
    }

}
