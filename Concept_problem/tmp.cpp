algorithm quicksort(A, low, high)
 if low >= high then
 return;
 p := partition_Hoare(A, low, high)
 quicksort(A, low, p)
 quicksort(A, p+1, high)
function partition_Hoare(A, low, high)
 pivot := A[low]
 i := low - 1
 j := high + 1
 while true do
do i := i + 1 while (A[i] < pivot) // 비교(comparison) 연산자 ‘<’
 do j := j – 1 while (A[j] > pivot) // 비교(comparison) 연산자 ‘<’
 if i < j then
 swap A[i] with A[j] // swap 연산
 else
 return j
 
 
 algorithm quicksort(A, low, high)
 if low >= high then
 return;
 p := partition_Hoare(A, low, high)
 quicksort(A, low, p-1)
 quicksort(A, p+1, high)
function partition_Lomuto(A, low, high)
 pivot := A[low]
 j := low
 for i := low+1 to high do
 if A[i] < pivot then // 비교(comparison) 연산자 ‘<’
 j := j + 1
 swap A[i] with A[j] // swap 연산
 pivot_pos := j
 swap A[pivot_pos] with A[low] // swap 연산
 return pivot_pos
 
 
