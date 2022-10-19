int countingValleys(int steps, string path) {
    int altitude=0;
    int noofvalleys=0;
    for(int i=0;i<steps;i++)
    {
        if(path[i] == 'U')
        {
            if(altitude==-1)
            {
                noofvalleys++;
            }
            altitude++;
        }
        else if (path[i] == 'D') {
             altitude--;
        }
    }
    return noofvalleys;

}
