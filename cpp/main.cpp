#include <iostream>
#include <cmath>

using namespace std; 


//a working if and loop
int max(int my_list[])
{
    int max = my_list[0]; 
    for (int i=1; i<5; i++)
        if (my_list[i] > max)
            max = my_list[i]; 
    return max;
}

//a working function
int pSquare(int value)
{
    return value*value;
}

//program results
int main()
{
    //base project
    string x = "Hello World!";
    cout << x << endl;

    //run if and loop
    int a, b, c, d, e, f;
    int my_list[] = {a=9, b=2, c=7, d=15, e=4, f=14};
    cout << "The largest number in the list is " << max(my_list) << endl;

    //run functions 
    cout << pSquare(5) << endl;
    cout << pSquare(7) << endl;
    return 0;
}
