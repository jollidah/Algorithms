#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	int numCases, idx = 1, tmp;
	scanf_s("%d", &numCases);
	numCases = pow(2, numCases);
	int *arr = new int[numCases];
	for (int i = 0; i < numCases; i++)	// 배열 0으로 초기화
	{
		arr[i] = 0;
	}
	for (int i = 0; i < numCases - 1; i++)	// 입력 갯수만큼만 반복
	{
		while (true)
		{
			if (idx * 2 < numCases && arr[idx * 2] == 0)	// 왼쪽 탐색
			{
				idx *= 2;
				continue;
			}
			else if (arr[idx] == 0)		// 가운데 탐색
			{
				scanf_s("%d", &tmp);
				arr[idx] = tmp;
				break;
			}
			else if (idx * 2 + 1 < numCases && arr[idx * 2 + 1] == 0)	// 오른쪽 탐색
			{
				idx = idx * 2 + 1;
				continue;
			}
			else
			{
				idx /= 2;		// 모두 아니면 부모 노드로 이동
			}
		}
	}
	tmp = 1;		// tmp 변수 재활용
	for (int i = 1; i < numCases; i++)
	{
		printf("%d ", arr[i]);
		if (i == tmp)
		{
			printf("\n");
			tmp = (tmp + 1) * 2 - 1;		// 다음 뛰어쓸 위치를 찾기 위한 수식
		}
	}
}
