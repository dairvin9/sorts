#include <iostream>

using namespace std;

void my_q_sort(int arr[], int begin, int end)
{
	int left = begin;
	int right = end;
	int temp;
	int pivot = (begin + end) / 2;
	
	while (left <= right)
	{
			while (arr[left] < arr[pivot])
				left++;
			while (arr[right] > arr[pivot])
				right--;
			if (left <= right)
			{
				temp = arr[left];
				arr[left] = arr[right];
				arr[right] = temp;
				
				left++;
				right--;
			}	
		
	}	
	


	if (begin < right)
		my_q_sort(arr, begin, right);
	if (end > left)
		my_q_sort(arr, left, end);
	
}
/*void quickSort(int arr[], int left, int right)
 {
  int i = left, j = right;
  int tmp;
  int pivot = arr[(left + right) / 2];

 /
  while (i <= j) {
        while (arr[i] < pivot)
              i++;
        while (arr[j] > pivot)
              j--;
        if (i <= j) {
              tmp = arr[i];
              arr[i] = arr[j];
              arr[j] = tmp;
              i++;
              j--;
    }
}

if (left < j)
    quickSort(arr, left, j);
if (i < right)
        quickSort(arr, i, right);
}*/

int main()
{
	int taco[5]= {4,6,2,8,1};
	my_q_sort(taco, 0,4);
	//quickSort(taco,0,4);
	for (int i = 0; i < 5; i++)
		cout << taco[i];
	return 0;
}