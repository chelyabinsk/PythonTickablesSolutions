from __future__ import division;
from decimal import *;
import math,random;

# Variable that allows while loop to repeat
running = True;

# Example of bad phone book (have to search from begening to the end 
badPhoneBook = [["Vince",3],
                ["Zoe",2],
                ["Julien",6],
                ["Thomas",10],
                ["Mike",1],
                ["Matt",4]];


def isInt(i):
    '''
    This function checks that 'i' can be converted to integer, by using try/except method,
        if value of 'i' can be converted to integer then True is returned, if not False is returned.

    Arguments: Function accepts any type of variable, in any format.

    Output: Function returns True/False, if conversion to integer has been sucessful/unsucessful.
    '''
    try:
        int(i);
        return True;
    except ValueError:
        return False;


def printHello():
    '''
    First function that when is called printes "Hello" into the output shell.

    Arguments: No arguments in this function.

    Output: Only output of this function is message "Hello" into the shell.
    '''
    print("Hello");


def myDiv(a,b):
    '''
    This is a function that performs division, but ensures that no division by 0 is done.
        If b =/= 0 then value a/b is returned.

    Arguments: Function takes 2 arguments "a" and "b"; both could be either integers or floats or anyt other type of number (but no text/string).

    Output: If "b" does not equal zero, then the result of a/b is returned as output.
    '''
    if(b==0):
        print("can't divide by 0");
    else:
        return a/b;
    

def divSumKB(k,b):
    '''
    This function takes 2 variables "k" and "b", then goes through the loop to find the sum of all numbers <= "k"
        which are not divisible by "b".

    Arguments: "k" and "b" should be integers.

    Output: Function will return the sum.
    '''
    tmpSum = 0;
    for i in range(1,k+1):
        # Check that i is not divisible by b without remainder
        if( i%b != 0):
            tmpSum += i;
    return tmpSum;


def doSquare(n,i=100,highPrecision = False):
        '''
        Function to calculate square root of any number using previously shown algorithm.
            Number of itterations could be changed for higher accuracy.

        This function allows 2 ways of getting an answer:
        1) If function is used like this "doSquare(10)",
            then answer will be shown to max float number of decimal places.
        2) If function is used like this "doSquare(10,10,True),
            then answer will be done to 10'000 decimal places, by using 10 itterations.

        Arguments: n - number to find square root of. (any digit. no text)
                   i - number of itterations through the formula. (integer)
                   highPrecision - should answer be displayed to 10'000 digits. (boolean)
        '''
        steps = i;        

        kTmp = n;
        xTmp = 1;

        # If high precision has been chosen
        if(highPrecision):
            # Precision to 10'000 digits
            getcontext().prec = 10000;

            # Itteration
            for i in range(1, steps+1):

                xTmp = Decimal(0.5) * ( Decimal(xTmp) + Decimal(kTmp)/Decimal(xTmp) );
                
            return Decimal(kTmp/xTmp);
            
        else:
            # Algorithm
            for i in range(1, steps+1):
                xTmp = 0.5 * ( xTmp + (kTmp)/xTmp );
                #Print what is going on with every value on each itteration
                #Print("K = " + str(kTmp/xTmp) + ", sqrt(K) = "+ str(math.sqrt(n)) + "; itteration: " + str(i));
            return kTmp/xTmp;
        

# Comparing math.sqrt(x) function, to suggested algorithm
def compareRoots(upTo,itter):
    '''
    Function that compares the math.sqrt(x) value, to the itteration formula answer.
    Function goes through all the integers between 1 and higher limit, which was passed with
        argument upTo.
    Difference between methods is printed into shell.

    Arguments: upTo - up to what number should the methods be checked. (integer)
               itter - number of itterations used by formula for square root. (integer)

    Output: Only output of this function, is the which square root of 'i' is currently being compared
        what is the math.sqrt(x) value, and what is the difference between answers given by different
        methods.
    '''
    for i in range(1,upTo+1):
        #print("i: " + str(i)
        #        +"\nRoot by algorithm with 100 itterations: " + str(doSquare(i))
        #        +"\nRoot using math.sqrt(x): " + str(math.sqrt(i)) );
        print("For i: " + str(i) + " Difference is = " + str(math.sqrt(i) - doSquare(i,itter) ));


def fibonacci(n):
    '''
    Function that generates a fibonacci sequence of numbers. Then returns an array of n fibonacci numbers.
        0,1,1..... etc

    Arguments: n - how many fibonaci numbers to be generated. (integer)

    Output: Array of fibonacci numbers, of length n.
    '''    
    a, b = 0, 1;
    c = 0;
    ansArray = [0];
    for i in range(1,n):
        c = a + b;
        b = a;
        a = c;
        # Add new number to the array
        ansArray.append(c);
    return ansArray;


def listComprehension(n):
    '''
    Function that cubes n, if n is odd, n^2 + 1 if n is divisible by 4, n - 1 otherwise.

    Arguments: n - n could be any value <= 100. (integer)

    Output: List of numbers satisfied the conditions, unless n > 100 then False is returned
    '''

    # Check that n is not more than 100
    if(n<=100):
        # Generate list from 1 to n
        generatedList = [x for x in range(1,n+1)];
        # Filter the generatedList to satisfy the conditions of the function and store it in outputList
        outputList = [x**3 if x%2 == 1 else x**2 + 1 if x%4 == 0 else x - 1 for x in generatedList];

        return outputList;
    else:
        return False;


'''
Main Loop
'''
while running:
    choice = raw_input("\nWhich tickable do you wanna see? ");

    if(not isInt(choice)):
        print("Please enter natural value");
    else:
        int_choice = abs(int(choice));
        # Escape
        if(int_choice == 199):
            break;
        # 1st step tickable
        elif(int_choice == 1):
            print("\nCreated a simple printHello function. Calling it now..");
            printHello();
        # 2nd step tickable
        elif(int_choice == 2):
            print("\nCreated a function myDiv which takes to parameters, a/b. Calling it now with a = 5, b = 4\n"
                  + str( myDiv(5,4) ) );
        # 3rd step
        elif(int_choice == 3):
            print("\nChecking that no division by 0 is attempted. myDiv a = 1, b = 0");
            myDiv(1,0);
        # 4th step
        elif(int_choice == 4):
            print("\nFunction that returns the sum of of first K integers not divisible by B."
                  +"\nK = 10'000 and B = 3");
            print("Sum is = " + str(divSumKB(10000,3) ));
        # 5th step
        elif(int_choice == 5):
            print("\nI wasn't sure if I was suppost to compare previous algorithm with first 10'000 numbers,\nor"
                  +" to calucalte one square root to 10'000 digits.\nSo I did both...");
            print("Choose '1' to compare algorithm approach to math.sqrt(x) function for first 10'000 numbers");
            print("Or choose '2' to get 10'000 digits of ANY number using algorithm and math.sqrt(x) function");
            choice = int(input("I choose (1 or 2): "));

            if(choice==1):
                print("Calculate square root using previously suggested algorithm. Roots of first 10000 digits");
                itter = int(input("Number of itterations: "));
                compareRoots(10000,itter);
            elif(choice==2):
                # Getting value for the number from the user
                num = int(input("Find square root of: "));
                # Getting number of itterations from the user
                itter = int(input("Number of itterations for algorithm: "));

                print("Using math.sqrt("+str(num)+") to 10'000 digits is: ");
                # Set precision
                getcontext().prec = 10000;

                # Assign value to mathSquareValue using standart sqrt function
                mathSquareValue = Decimal(num).sqrt()
                print(mathSquareValue);

                print("\n\n\nUsing Algorithm with "+str(itter)+" itterations ans to 10'000 digits"
                      "\nof square root of " + str(num) + " is:\nCould take some time..");

                # Call a function to calculate difference between methods using high precision
                formulaSquareValue = doSquare(num,itter,True);
                print(formulaSquareValue);

                # Calculate the difference between methods
                differenceBetweenMethods = mathSquareValue - formulaSquareValue;

                print("\n\n\nDifference between methods = " + str(differenceBetweenMethods));

        # 6th step
        elif(int_choice == 6):
            print("\nCalculate fibonacci numbers up to n");
            n = input("n = ");
            print(fibonacci(n));
        # 7th step
        elif(int_choice == 7):
            print("\n7th step is not a tickable. Using single line comments.");
        # 8th step
        elif(int_choice == 8):
            print("\n8th step is not a tickable. Using multiline comments.");
        # 9th step
        elif(int_choice == 9):
            print("\nUsing common coding convention through out my work.");
        # 10th step
        elif(int_choice == 10):
            print("\nLists");

            alist = [1,2,3,4,5,6,7,8,9,10];
            blist = [30,40,50,60];
            clist = alist + blist;

            print("clist = " + str(clist));
            print("Length of clist = " + str(len(clist)));
            print("0th entry in clist = " +str(clist[0]));
            print("-1th entry of clist = " + str(clist[-1]));
            print("clist[3:12] = " + str(clist[3:12]));

            index = clist.index(40);
            print("index of '40' in clist = " + str(index));
            print("print '40' using clist[start:stop] = " + str(clist[index:index + 2]));
        # 11th step
        elif(int_choice == 11):
            print("\nUsing append function with lists.");
            myList = [];

            for i in range(11):
                if i%2 == 0:
                    myList.append(i);
            print("Even number below 11 as an array = " + str(myList));
        # 12th step
        elif(int_choice == 12):
            print("\nList of first 1300 integers divisible by 3.");

            numList = [];
            i = 1;
            loop = True;
            while(loop):
                if(i%3==0):
                    numList.append(i);
                    if(len(numList)==1300):
                        break;
                i += 1;
            print("List = " + str(numList));
            print("Largest number = " + str(numList[len(numList)-1]));
        # 13th step
        elif(int_choice == 13):
            print("\nComprehensions");

            squares = [e**2 for e in range(1,11) if e % 2 == 1];
            print("squares = " + str(squares));
        
        # 14th step
        elif(int_choice == 14):
            print("\nFunction(n) with some rules, satisfying rules. Using list comprehensions");
            n = int(input("Please enter n <= 100: "));
            print(listComprehension(n));
        # 15th step
        elif(int_choice == 15):
            alist = [1,74,2,100,-123];
            print("\nalist = " + str(alist));
            print("Max value in alist = " + str(max(alist)));
            print("Min value in alist = " + str(min(alist)));
            print("Length of alist = " + str(len(alist)));
        # 16th step
        elif(int_choice == 16):
            print("\nDictionaries");

            def searchPB(target):
                '''
                Function to demonstrate how to search through a bad dictionary.

                Arguments: target - value to search for in the dictionary. (string)

                Output - Either value assigned to that target in the array, or message saying that
                    target hasn't been found.
                '''
                for e in badPhoneBook:
                    print("Checking %s" %e);
                    if e[0] == target:
                        return e[1];
                return "%s not in phonebook" % target;

            print(searchPB("Zoe"));

            # Example of a good phone book, using dictionaries
            goodPhoneBook = {"Vince": 3,
                            "Zoe":2,
                            "Julien":6,
                            "Thomas":10,
                            "Mike":1,
                            "Matt":4};

            print("Get Thomas's value : " + str(goodPhoneBook.get("Thomas")));
            print("Get Brayden's value : " + str(goodPhoneBook.get("Brayden")));
            print("Get Brayden's value; changed false : " + str(goodPhoneBook.get("Brayden", 'Not in book')));
            print("Get Thoma's value; changed false : " + str(goodPhoneBook.get("Thomas", 'Not in book')));

            # Modifying elements of the dictionary
            print("Value of Vince in dictionary = " + str(goodPhoneBook["Vince"]));
            # Change value
            goodPhoneBook["Vince"] = 8;
            print("Vince's new value = " + str(goodPhoneBook["Vince"]));
        # 17th step
        elif(int_choice == 17):
            print("\nItterating over the list badPhoneBook");

            pb = {};

            # Loop to go through the bad dictionary and hash it into good one
            for i in badPhoneBook:
                pb[i[0]] = i[1];

            print("pb = " + str(pb));
        # 18th step
        elif(int_choice == 18):
            print("\nI think I used concepets from step 18 to solve step 17.");
                
