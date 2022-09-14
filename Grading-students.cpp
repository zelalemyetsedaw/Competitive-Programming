vector<int> gradingStudents(vector<int> grades) {
    int n;
    for(int i=0;i<grades.size();i++)
     {    n = grades.at(i);
          if(n<38)
          {
              grades.at(i) = n;
          }
          else if{
            (n%5 >= 3) grades.at(i) += (5-(n%5));
          }
          else {
          grades.at(i) = n;
          }
           }
     return grades;
}
