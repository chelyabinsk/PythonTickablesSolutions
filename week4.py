import math,random,time;

running = True;

# Function to check if string can be converted to integer
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


def isPrime(n):
    '''
    Function to check if 'n' is prime.

    Works by creating array of numbers that divide n without remainder. (thus making n not prime)
        if number is prime then array will have an entry of 0. (because there's goign to be no remainder)
    If array's min number isn't 0 then there're a divisors of n, so n is composite,
        else n is prime.

    Arguments: n - number that is goign to be checked for primality (integer)

    Output: True if the smallest value of remainder in array isn't 0, then number is prime, else if smallest
        value in array is 0, then there's a number that divides n without a remainder, so number isn't prime
        and output is False.
    '''
    return min([n % e for e in range(2,n)]) != 0;


def iterX(n):
    '''Itterative approach to calculate 2^(n - 1).

    Arguments: n - any natural number. (integer, no text)

    Output: Result of 2^(n - 1).
    '''

    r = 1;

    for i in range(n-1):
        r *= 2;

    return r;


def recX(n):
    '''
    Recursive example of calculating 2^(n - 1)

    Arguments: n - any natural number (integer, no text)

    Output: Result of 2^(n - 1)
    '''

    if n == 1:
        return 1;

    return 2 * recX(n - 1);
    

def factorialIter(n):
    '''
    Itterative way to calculate n!

    Arguments: n - number to calculate factorial of. (integer)

    Output: Final factorial. Integer
    '''

    ans = 1;
    
    for i in range(n,1,-1):
        ans *= i;
    return ans;


def factorialRec(n):
    '''
    Recursive way to calculate n!

    Arguments: n - number to calculate factorial of. (integer)

    Output: Final factorial. Integer
    '''
    if(n==0):
        return 1;
    return n * factorialRec(n - 1);


def fibonacciRec(n):
    '''
    Function to calculate nth fibonacci number.

    Arguments: n - number of numbers from the sequence. (integer)

    Output: nth fibonacci number.
    '''
    if( (n==0) or (n==1) ):
        return 1;    
    return fibonacciRec(n - 1) + fibonacciRec(n - 2);


def jumbledList(maximumNumber, sizeOfList):
    '''
    Function that mixes list

    Arguments: maximumNumber - max number of shuffles. (integer)
               sizeOfList - number of entirs in the list. (integer)

    Output: Returns randomly shuffles list
    '''

    return random.sample(range(1, maximumNumber+1), sizeOfList);


def insertionSort(data):
    '''
    Insertion sort algorithm

    Arguments: data - list to be sorted. (list)

    Output: returns sorted list. 
    '''
    firstUnsorted = 0;  # Set the starting position in the unsorted list

    while( firstUnsorted < (len(data) - 1) ):  # Go through every entry in the old data list
        indexOfSmallest = firstUnsorted;  # Assume that first entry in the old list is the smallest
        index = firstUnsorted + 1;  # Move up to the next position

        # Loop to find any number smaller than the index, if found then make the new index have position of the
        # smaller number
        while( index <= (len(data) - 1) ):  # Go through all the entries from the index to the end of list
            if( data[index] < data[indexOfSmallest] ):  # If there a number smaller than current known smallest
                indexOfSmallest = index;  # Make the index of the smaller number be the position of the smallest one

            index += 1;  # Move the index up. continue through the list

        data[firstUnsorted], data[indexOfSmallest] = data[indexOfSmallest], data[firstUnsorted];  # Swap first unsorted with earlier unsorted item
        firstUnsorted += 1;  # Move up one in the list.

    return data;  # Return the result


def bubbleSort(data):
    '''
    Bubble sort algorithm

    Arguments: data - unsorted list. (list)

    Output: returns sorted list.
    '''
    firstUnsorted = 0;
    swap = True;

    while( (firstUnsorted < (len(data) - 1)) and (swap == True) ):
        swap = False;

        # Bubble up
        index = len(data) - 1;
        while(index > firstUnsorted):
            if( data[index] < data[index - 1] ):
                # Swapping index and index - 1
                tmp = data[index-1];
                data[index - 1] = data[index];
                data[index] = tmp;                
                swap = True;

            index -= 1;

        firstUnsorted += 1;

    return data;


def timing(string):
    '''
    Function to determine time taken to execute a function

    Arguments: name of the function. (string)

    Output: time taken to comple function as a float.
    '''
    sumTime = 0;
    for i in range(0, 10):
        startTime = time.time();
        eval(string);
        sumTime += time.time() - startTime;
    return sumTime / 10;

def insertionBubbleDifference(numOfElements):
    '''
    Function to compare speed of insertion and bubble sort.

    Arguments: numOfElements - How many elements to be sorted in the list.

    Output: print message for time taken by bubble sort, and insertion, and difference.
    '''

    l = range(1,int(numOfElements));
    l = jumbledList(int(numOfElements),int(numOfElements));


    # Time taken by bubble search
    bubbleTime = timing("bubbleSort(" + str(l) + ")");
    # Time taken by insertion algorithm
    insertionTime = timing("insertionSort(" + str(l)+")");
    print("Bubble: " + str(bubbleTime) + ", Insertion: " + str(insertionTime) + "; Difference = " + str(abs(insertionTime - bubbleTime)));

def testFunction():
    '''
    Basic test function, that performs addition from 0 to 10^6.

    Arguments: None

    Output: None
    '''
    k = 0;

    while k < (10**6):
        k += 1;


def sequencialSearch(unsortedList, searchingEntry):
    '''
    Sequencial search algorithm, sorts array, then returns index of required entry

    Arguments: unsortedList - unsorted list to search in. (list)

               searchingEntry - which entry in file should look for. (integer,float,string)

    Output: integer value of the index in the unsortedList.    
    '''

    # Sort the list
    sortedList = insertionSort(unsortedList);

    #print("Sorted = " + str(sortedList));

    # Set index to 0
    index = 0;

    # Set found to false
    found = False;

    while( (index < len(sortedList)) and (not found) ):
        if sortedList[index] == searchingEntry:
            found = True;
        elif(sortedList[index] > searchingEntry):
            index = len(sortedList);
        else:
            index += 1;
    if found:
        return index;
    else:
        return False;


def binarySearch(unsortedList, searchingEntry):
    '''
    Binary search algorithm, sorts array, then returns index of required entry

    Arguments: unsortedList - unsorted list to search in. (list)

               searchingEntry - which entry in file should look for. (integer,float,string)

    Output: integer value of the index in the unsortedList.    
    '''
    # Sort the list
    sortedList = insertionSort(unsortedList);

    # Set index to 0
    index = 0;

    # Set first = 0
    first = 0;

    # Set last to (length of list) - 1
    last = len(sortedList) - 1;

    # Set found to false
    found = False;

    # While not found, and first is less or equal to last
    while( (first <= last) and (not found) ):
        # Make middle to (first + last) / 2
        middle = int( (first + last) / 2 );
        # If found in the middle
        if(sortedList[middle] == searchingEntry):
            found = True;
        else:
            # If Data[Middle] > Item
            if(sortedList[middle] > searchingEntry):
                last = (middle - 1);
            else:
                first = (middle + 1);

    return middle;

# Copied example of recursive binary search from Wikipedia
def recursiveBinarySearch(array, target, imin, imax):
    '''
    Recursive binary search.

    Arguments:

    Output:
    '''
    # Test if array is empty
    if(imax < imin):
        return False;
    else:
        # Calculate midpoint to cut set in half
        imid = int( ((imax - imin) / 2) + imin );

        # Three-way comparison
        if(array[imid] > target):
            # Key is in lower subset
            return recursiveBinarySearch(array, target, imin, imid-1);
        elif(array[imid] < target):
            # Key is in upper subset
            return recursiveBinarySearch(array, target, imid + 1, imax);
        else:
            return imid;

# Main Loop
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
            print("\nOpen a text file myTextFile.txt");

            textFile = open('myTextFile.txt','w');

            for i in range(1,11):
                textFile.write("%s\n"%i);

            textFile.close();
        # 2nd step
        if(int_choice == 2):
            print("\nReading from the text file myTextFile.txt");

            textFile = open('myTextFile.txt', 'r');
            string = textFile.read();
            print("Contents of the text file as a string: " + string);

            # Change string into list
            data = string.split('\n');

            # Convert all entries to integer
            data = [ int(e) for e in data[:-1] ];

            print("Split the string into list: " + str(data));
        # 3rd step
        if(int_choice == 3):
            print("\nChecking if number is prime in the list of numbers via the provided function");

            # Open text file
            textFile = open("W03_D01.txt",'r');

            # Get the data from the file as a string
            string = textFile.read();

            # Change string into list
            data = string.split('\n');

            # Convert entries to integer
            data = [ int(e) for e in data[:-1] ];

            listOfPrime = {};

            textFile.close();

            for i in range(0,len(data)):
                if(isPrime(data[i])):
                    listOfPrime[data[i]] = "is prime";

            print(listOfPrime);
            print("Number of primes = " + str(len(listOfPrime)) );
        # 4th step
        if(int_choice == 4):
            print("\nExperimenting with csv libriary");
            import csv;
        # 5th step
        if(int_choice == 5):
            print("\nRecursion.");
            print("Itterative approach to calculate 2^(n - 1), n=10: " + str(recX(10)));
            print("Recursive approach to calculate 2^(n - 1), n=10: " + str(iterX(10)));
        # 6th step
        if(int_choice == 6):
            print("\nCalculating factorial using recursion");
            print("Factorial of n=10, ittterative way: " + str(factorialIter(10)));
            print("Factorial of n=10, recursive way: " + str(factorialIter(10)));
        # 7th step
        if(int_choice == 7):
            print("\n15th number in Fibonacci sequence using recursion: " + str(fibonacciRec(15)));
        # 8th step
        if(int_choice == 8):
            print("\nShuffling");

            l = range(1, 31);
            l = jumbledList(30, 20);
            print("l: " + str(l));
        # 9th step
        if(int_choice == 9):
            print("\nSorting shuffled list use .sort() function");
            
            # Jumble l list
            l = range(1,31);
            l = jumbledList(30,20);
            print("Shuffled list = " + str(l));
            l.sort();
            print("Sorted list = " + str(l) + " length: " + str(len(l)));

            l = jumbledList(30,20);
            print("\nNew jumbled l = " + str(l));

            l = insertionSort(l);            
            print("Sorted list using insertion algorithm = " + str(l));
        # 10th step
        if(int_choice == 10):
            print("\nUsing bubble sort algorithm.");

            l = range(1,31);
            l = jumbledList(30,20);
            print("Shuffled list = " + str(l));
            l = bubbleSort(l);
            print("Sorted using bubble sort = " + str(l));
        # 11th step
        if(int_choice == 11):
            print("\nTime module");
            print("Current time of the computer (in seconds) is: " + str(time.time()));
            print("Time taken to add 1 from 0 to 10^6 (Average from 10 tries): " + str(timing("testFunction()")));
            print("Difference between bubble and insertion sort (Average from 10 tries).");
            num = raw_input("How many elements? ");
            insertionBubbleDifference(num);
        # 12th step
        if(int_choice == 12):
            print("\nSearching for index 4558 by hand, and then using index method in file W04_D01.txt.");

            textFile = open("W04_D01.txt","r");
            string = textFile.read();
            # Change string into list
            data = string.split('\n');

            # Convert all entries to integer
            data = [ int(e) for e in data[:-1] ];
            textFile.close();
            print("Index o f 4558 is " + str(data.index(4558)));

            # If you know the total number of entries, then one could go from the begining, other from the end
        # 13th step
        if(int_choice == 13):
            print("\nSequential search");
            
            #Open file and get the data
            textFile = open("W04_D01.txt",'r');
            string = textFile.read();
            # Change string into list
            data = string.split('\n');

            # Convert all entries to integer
            data = [ int(e) for e in data[:-1] ];

            #print("Length = " + str(len(data)));


            searchingFor = 19;
            
            index = sequencialSearch(data, searchingFor);

            print("Index of " + str(searchingFor) + " is " + str(index));

            searchingFor = 592;
            
            index = sequencialSearch(data, searchingFor);

            print("Index of " + str(searchingFor) + " is " + str(index));

            searchingFor = 9507;
            
            index = sequencialSearch(data, searchingFor);

            print("Index of " + str(searchingFor) + " is " + str(index));

            searchingFor = 4221;
            
            index = sequencialSearch(data, searchingFor);

            print("Index of " + str(searchingFor) + " is " + str(index));
        # 14th step
        if(int_choice == 14):
            print("\nBinary search.");

            #Open file and get the data
            textFile = open("W04_D01.txt",'r');
            string = textFile.read();
            # Change string into list
            data = string.split('\n');

            # Convert all entries to integer
            data = [ int(e) for e in data[:-1] ];
            
            searchingFor = 4221;
            ans = binarySearch(data, searchingFor);

            print(str(searchingFor) + " is at " + str(ans));
        # 15th step
        if(int_choice == 15):
            print("\nComparing binary search to sequencial. (10 times, and take the average)");
            print("I will use already sorted list.");
            num = int(raw_input("How many entries in the list? "));

            l = [];

            for i in range(0, num):
                l.append(random.randint(0, num));

            l = insertionSort(l);
            #l = jumbledList(num,num);

            # sequential time
            seqTime = timing("sequencialSearch(" + str(l) + ",99)");

            # binary time
            binTime = timing("binarySearch(" + str(l) + ",99)");

            print("Sequencial search: " + str(seqTime) + " Binary search: " + str(binTime) );
        # 16th step
        if(int_choice == 16):
            print("\nRewriting binary search as a recursive algorithm.");
            print("I will use already sorted list. I used example from Wikipedia to understand recursive version\nof algorithm.");
            num = int(raw_input("How many entries in the list? "));

            l = [];

            for i in range(0, num):
                l.append(random.randint(0, num));

            l = insertionSort(l);

            # Recursive time
            rTime = timing("recursiveBinarySearch(" + str(l) + ", 99, " + str(min(l)) + "," + str(max(l)) + ")");

            # Itterative time
            bTime = timing("binarySearch(" + str(l) + ",99)");
            print("Recursive time: " + str(rTime) + "; Itterative time: " + str(bTime));
            

            
        

