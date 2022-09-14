vector<int> countingSort(vector<int> arr) {
   vector<int> count_arr(100);
   
    for(int i=0;i<100;i++)
    {
        count_arr.at(i) = 0;
    }
    for(int i=0;i<arr.size();i++)
    {
        ++count_arr.at(arr[i]);
    }
    
    
    return count_arr;

}
