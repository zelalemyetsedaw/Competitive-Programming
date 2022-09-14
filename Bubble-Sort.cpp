void countSwaps(vector<int> a) {
    int numswaps =0;
    int n = a.size();
    for(int i=0;i<(n-1);i++)
    {
        for(int j=0;j<(n-i-1);j++)
        if(a.at(j) > a.at(j+1))
        {
            int temp = a.at(j);
            a.at(j) = a.at(j+1);
            a.at(j+1) = temp;
            numswaps += 1;
        }
    }
    cout << "Array is sorted in "<<numswaps<<" swaps." << endl;
    cout << "First Element: " << a.at(0) << endl;
    cout << "Last Element: " << a.at(n-1) << endl;

}
