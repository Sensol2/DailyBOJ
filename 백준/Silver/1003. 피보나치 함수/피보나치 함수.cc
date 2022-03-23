#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int count;
	int a;
	int arr[100] = { 1, 1, };
	int cnt[2][100]; //0은 0 횟수, 1은 1횟수

	cnt[0][0] = 1;
	cnt[0][1] = 0;
	cnt[1][0] = 0;
	cnt[1][1] = 1;


	for (int i = 2; i < 100; i++)
	{
		arr[i] = arr[i - 2] + arr[i - 1];
		cnt[0][i] = cnt[0][i - 2] + cnt[0][i - 1];
		cnt[1][i] = cnt[1][i - 2] + cnt[1][i - 1];
	}

	//for (int i = 0; i < 40; i++)
	//{
	//	printf("%d\n", arr[i]);
	//}

	int inputs[100]; 
	scanf("%d", &count);
	for (int i = 0; i < count; i++)
	{
		scanf("%d", &inputs[i]);
	}
	for (int i = 0; i < count; i++)
	{
		printf("%d %d\n", cnt[0][inputs[i]], cnt[1][inputs[i]]);
	}
	return 0;
}