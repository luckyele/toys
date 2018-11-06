#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int x,y,z;
	int d[3] = {1, 2, 3};
	do {
		x = d[0];
		y = d[1];
		z = d[2];
		cout << x << y << z << endl;
	} while (next_permutation(d, d+3));
	return 0;
}

