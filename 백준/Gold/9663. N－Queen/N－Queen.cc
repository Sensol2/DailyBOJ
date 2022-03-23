#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <list>
#include <cstdlib>

using namespace std;

int cnt = 0;

bool promising(int x, int y, int* col)
{
	for (int i = 1; i < y; i++)
	{
		if (x == col[i]) //만약 같은 열에 존재하면
		{
			return false;
		}
		int deltaX = std::abs(col[i] - x);
		int deltaY = std::abs(i - y);
		if (deltaX == deltaY) //만약 대각선 상에 존재하면
		{
			return false;
		}
	}
	return true;
}

void queen(int x, int y, int* col, int num)
{
	if (!promising(x,y,col))
	{
		return;
	}
	else
	{
		if (y == num)
		{
			cnt++;
			return;
		}
		col[y] = x;
		for (int i = 1; i <= num; i++)
		{
			queen(i, y + 1, col, num);
		}
	}
}

int main()
{
	int num;
	cin >> num;

	int** board = new int* [num];
	for (int i = 0; i < num; ++i)
		board[i] = new int[num];

	int* col = new int[num];
	queen(0, 0, col, num);
	printf("%d", cnt);
	return 0;
}