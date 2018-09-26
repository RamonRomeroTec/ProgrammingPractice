#K=suma de los digitos de N es mayor=
#J es el nuevo

'''
if (k == 1) {
	    cout << 0 << "\n";

	    return 0;
	  }

	  vvull digits(10);
	  ull sum = 0;

	  for (ull i = 0; i < n.size(); ++i) {
	    int digit = n[i] - '0';
	    sum += digit;
	    digits[digit].push_back(i);
	  }

	  ull col = 0, row = 0;
	  ull mnd = 0;

	  while (sum < k) {
	    if (row >= digits[col].size()) {
	      ++col;
	      row = 0;
	    }

	    if (digits[col].size() == 0) {
	      ++col;
	      continue;
	    }

	    int index = digits[col][row];
	    sum -= n[index] - '0';
	    n[index] = '9';
	    sum += 9;
	    ++row;
	    ++mnd;
	  }

	  cout << mnd << "\n";
	  return 0;
'''
if __name__ == '__main__':
    k=int(input())
    l=int(input())
    l=str(l)
    l=list(map(int,l))
    l=sorted(l)
    suma=sum(l)
    d = 0;
    if(suma >= k):
        print(0)
    else:
        for i in range(0, len(l)):
            d += 1;
            suma += 9 - l[i];
            if(suma >= k):
                break

        print(d)
