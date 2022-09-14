void insertionSort1(int n, vector<int> arr) {
   int key = arr[n-1];
   int j= n-1;
   while(arr[j-1]>key && j>0)
   {
       arr[j] = arr[j-1];
       for(int i=0;i<n;i++)
        {cout<< arr[i] << " ";}
        j--;
       cout << endl;
   }
   arr[j] = key;
   for(int i=0;i<n;i++)
   cout << arr[i] << " ";

}
