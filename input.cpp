/*

Testing input for the programm, for the convenience of checking person in one file, also the length of the code is not long just to make it easier for checking.
However several cases will be checked in this code (IMPORTANT-EVERY TESTS CHECKS ONLY 1 PARTICULAR SCENARIO) how it behaves with different declarations, numbers of usage, places of occurrence and names.
At the end of the file in comments will be expected output that should be written in the output.txt and additional information from prints, like number of occurances, lines of declarations of all variables in the code and
those which are declared more than once.

I am also assuming that input code is working and there are not usage of for example undeclared variables.

Output file was also added to the project, it was done only for easier access, it would generate anyway

*/

#include <iostream>
using namespace std;

class Test
{
    private:
// TEST 1: declaration of multiple variables (3) in the same line, with different types. all of them should be found by the program as variables

        int data1, long data4, float operate;
        
        bool unique = true; //TEST2: Checking if boolean variable will be detected (should be unused)

// TEST 3: The variable data4 will be mentionated in ("//") comments, in this line and one more time in the 59th line and it should still be found by the programm as unused

        int data5; // TEST 4: datat5 will be mentionated in ("") in line 57

        string k; // TEST 5: k will be declared one more time, in line 69, it should be found by the programm as redeclaration and information about warning will be displayed

// TEST 6: Declaring variables in comments (different types), non of them should be found by the programm

// int nonexisting1;

/* double nonexisting2; */

        float data2;
/*

float nonexisting3

*/
        short data3;

    public:
       
       void insertIntegerData(int d) //TEST 7: declaration of a veriable inside parantheses of a method, it should be found as a normal declaration of a variable, used one more time later 
       {                             // also checking that "d" will not be found in longer names like "data1", it should be counted just as a singular d.
          data1 = d;

          cout << "Number:  " << data1; 
        }

       float insertFloatData()
       {
           cout << "\nEnter data5 for  : ";
           cout << " int smth "; //TEST8: declaration in (""), it should not be found 
      //     cin >> data4;
           cin >> data1;
           return data2; 
        }
};

 int main()
 {
      Test o1, o2;
      float secondDataOfObject2;
      long k; // Redeclaration of k, should be detected
      int b = 15; // TEST9: declared variable with assigned value (number), b will be used later
      int p = b; // TEST10: declared variable with assigned value (another variable), p will NOT be used 
      
      char Sign = 'A'; // TEST11: Checking if program will sing char with assigned letter

      cout << "The Sign is:" << Sign; // TEST12: Checking if Sign will be found as used variable in line 70, even if it is after ("") so checking if program cuts all the line or just a part within ("")

      int t;
      cin>>t;

      cin >> k;
        
      count << k * k;

      o1.insertIntegerData(12);
      secondDataOfObject2 = o2.insertFloatData();

      cout << "You entered " << secondDataOfObject2;

    for(int i=0; i<t; i++) // TEST13: Checking if program counts correctly number of variables in code if they are used in the same line, should be 3 of them
    {
       int n;
       int m;
       int s=0;
        
       cin>>n>>m;

       int times[n];
       int tab[n];

        for(int j=0; j<n; j++)
        {
            cin>>times[j];
        }

        for(int l=0; l<n; l++)
        {
            tab[l]=86400/times[l];
            s+=tab[l]; //TEST14: Checking if variable will be counted if it is the first sign from the left (different regex required), s should be counted
        }

       if(s%m==0)
            cout<<s/m<<endl; //TEST15: Checking if variables can be without spaces next to themselves, s and m should be counted
        else
            cout<<s/m+1<<endl;
    } 
      return 0;
 }


/*
THAT'S HOW SHOULD LOOK THE OUTPUT FROM THE output.txt:

Variable operate declared in Line: 22 is never used.
Variable data4 declared in Line: 22 is never used.
Variable unique declared in Line: 24 is never used.
Variable data5 declared in Line: 28 is never used.
Variable data3 declared in Line: 44 is never used.
Variable p declared in Line: 71 is never used.


THAT'S HOW SHOULD LOOK LIKE OUTPUT AFTER COMPILING, IT IS NOT THE CLEARIEST INFORMATION BUT STILL IT IS JUST AN ADDITIONAL OUTPUT FOR BETTER CHECK OF THE PROGRAM:

List of types of variables:
['int', 'float', 'long', 'bool', 'int', 'string', 'float', 'short', 'int', 'float', 'long', 'int', 'int', 'char', 'int', 'int', 'int', 'int', 'int', 'int', 'int']

List of variables:
['data1', 'operate', 'data4', 'unique', 'data5', 'k', 'data2', 'data3', 'd', 'secondDataOfObject2', 'k', 'b', 'p', 'Sign', 't', 'i', 'n', 'm', 's', 'j', 'l']

Counter for each variable:
[4, 1, 1, 1, 1, 5, 2, 1, 2, 3, 5, 2, 1, 2, 3, 3, 6, 5, 5, 4, 6]

Counter for lines, line of declaration of each variable:
[22, 22, 22, 24, 28, 30, 38, 44, 48, 68, 69, 70, 71, 73, 77, 89, 91, 92, 93, 100, 105]

WARNING

Variables declared more than once:
['k', 'k']

Lines of variables declared more than once:
[30, 69]

Types of variables declared more than once:
['string', 'long']

*/