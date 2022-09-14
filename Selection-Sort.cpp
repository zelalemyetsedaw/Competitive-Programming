int select(int arr[], int i)
{
    
    int maximum = arr[0], index = 0;
        for (int j=1; j<=i; j++)
        {
            if (arr[j] > maximum)
            {
               index = j;
               maximum = arr[j];
            }
        }
        return index;// code here such that selecionSort() sorts arr[]
}


void selectionSort(int arr[], int n)
{
  int i, j;
       for (i = n-1; i >=0; i--)      
       {
            int j = select(arr, i);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
       }
  
  
  
}
