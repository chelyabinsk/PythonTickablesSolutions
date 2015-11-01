import math, csv, random;


print("OOP..");


# Basic class
class Student_step1():
    pass;


# Next student class
class Student_step3():
    courses = ["Biology", "Mathematics", "English"];
    age = 13;
    sex = "Male";


# Quadratic class
class Quadratic_step4():
    a = b = c = 0;
    

# Next-next student class
class Student_step5():
    courses = ["Biology", "Mathematics", "English"];
    age = 13;
    sex = "Male";

    def haveABirthday(self, numberOfBirthdays=1):
        self.age += numberOfBirthdays;
        

# Next-next-next student class
class Student_step6():
    def __init__(self, courses, age, sex):
        self.courses = courses;
        self.age = age;
        self.sex = sex;
    def haveABirthday(self, numberOfBirthdays):
        self.age += numberOfBirthdays;
        

# Quadratic equation
class Quadratic_step7():
    def __init__(self, a, b, c):
        self.a = a;
        self.b = b;
        self.c = c;
    def isReal(self):
        r = (self.b**2) - 4 * self.a * self.c;
        if(r >= 0):
            return True;
        else:
            return False;

# Course class
class School_step8():       
    def __init__(self):
        # Variable that stores number of students in courses
        self.numInCourse = {"Math": 0, "English": 0, "French": 0, "Physics": 0,
                    "PE": 0, "Biology": 0, "History": 0, "Geography": 0, "NONE": 0};

        self.courseDictionary = {0: "NONE",
                                 1: "Math",
                                 2: "English",
                                 3: "French",
                                 4: "Physics",
                                 5: "PE",
                                 6: "Biology",
                                 7: "History",
                                 8: "Geography"};

        self.students = {};
        
        
    def addToCourse(self, name, courses):
        tmp1 = [];
        for i in list(courses):           
            tmp2 = self.courseDictionary[int(i)];
            self.numInCourse[tmp2] += 1;

            tmp1.append(tmp2);

            self.students[name] = tmp1;
            
            
    def displayCourses(self):
        return (self.numInCourse);

    def displayStudents(self):
        return (self.students);


# Random drop class
class Drop_step9():
    def __init__(self, r=1):
        self.x = (0.5 - random.random()) * 2 * r;
        self.y = (0.5 - random.random()) * 2 * r;
        self.inCircle = (self.y) ** 2 + (self.x) ** 2 <= (r) ** 2;

    def isTrue(self):
        return self.inCircle;
    
def step1():
    ''''
    First step, creating a basic class called Student_step1, then creating it's instance, then displaying it's properties.

    Arguments: None.

    Output: Print messages.
    '''

    print("First step, creating a basic class called Student_step1, then creating it's instance.\nThen displaying it's properties.");

    # Creating an instance of the class
    seva = Student_step1();

    # Printing info about the created object
    print(seva);
    

def step2():
    '''
    Second step, converting a to string.

    Arguments: None.

    Output: Print messages.
    '''

    # Define 'a'
    a = 25;

    # Make 'a' a string
    a = str(a);

    print("Defined a, and then used new string class to make it a string");
    

def step3():
    '''
    Created new class Student_step3, and added extra attributes.

    Arguments: None.

    Output: Print messages.
    '''
    print("Creating new class Student_step3, inside of which there are some attributes, which could be changed");

    # Creating an instance of Student_step3 class
    seva = Student_step3();

    print("Default attributes. courses: " + str(seva.courses) + " age: " + str(seva.age) + " sex: " + seva.sex);

    # Change some attributes
    seva.courses.append("Computing");
    seva.age = 18;
    seva.sex = "M";
    
    print("Changed attributes. courses: " + str(seva.courses) + " age: " + str(seva.age) + " sex: " + seva.sex);



def step4():
    '''
    Creating instances of the Quadratic_step4 class with the coefficients from .csv file,
    then put them into a list.

    Arguments: None.

    Output: Print messages.
    '''

    print("Opening 'W05_D01.csv' to read data.\nCreating new instance of the class.\nDisplaying all the 'a' terms from the file.");

    listOfQuadratics = [];

    # Open and read .csv file

    f = open("W05_D01.csv", "r");
    csvrdr = csv.reader(f);
    data = [row for row in csvrdr];
    f.close();

    data = [[eval(k) for k in row] for row in data[1:]];

    for i in data:
        # Create an instance
        q = Quadratic_step4();

        q.a = i[0];
        q.b = i[1];
        q.c = i[2];

        listOfQuadratics.append(q);


    print([q.a for q in listOfQuadratics]);
    

def step5():
    '''
    Adding methods to classes. Then calling a function to increment age value.

    Arguments: None.

    Output: Print messages.
    '''
    # Create an instance
    seva = Student_step5();

    print("Age: " + str(seva.age));

    seva.haveABirthday();
    print("After haveABirthday function call, Age: " + str(seva.age));

    seva.haveABirthday(10);
    print("Add 10 to current age value, Age: " + str(seva.age));


def step6():
    '''
    Introducing __init__ method.

    Arguments: None.

    Output: Print messages.
    '''
    print("Introducing initialising attributes");

    seva = Student_step6(["Biology", "Maths"],18,"Male");
    print("courses: " + str(seva.courses) + "; age: " + str(seva.age) + "; sex: " + str(seva.sex));


def step7():
    '''
    Counting number of equations in 'W05_D01.csv' file that have real roots using classes.

    Arguments: None.

    Output: Print messages.
    '''

    num = 0;
    
    f = open("W05_D01.csv", "r");
    csvrdr = csv.reader(f);
    data = [row for row in csvrdr];
    f.close();

    data = [[eval(k) for k in row] for row in data[1:]];

    for i in data:
        # Create an instance
        q = Quadratic_step7(i[0], i[1], i[2]);
        if(q.isReal()):
            num += 1;

    print("Number of instances with real roots in 'W05_D01.csv' file: " + str(num));


def step8():
    '''
    Managing data.

    Arguments: None.

    Output: Print messages.
    '''
    print("Obtaining number students on each course, as well as a s dictionary containing\nstudents as keys and lists of enrolled courses as values.");

    student_List = [["Adam", [1, 2, 5]],
                    ["Zoe", [4, 3, 2]],
                    ["Ben", [7]],
                    ["Thomas", []],
                    ["Meryl", [2, 3]],
                    ["James", [6, 7, 2]],
                    ["Leanne", []],
                    ["Angelico", [1]],
                    ["Izabela", [1, 2, 3, 4, 5]],
                    ["Lisa", [1, 8]],
                    ["Penny", [1, 2, 3]]];
    
    # Create an instance
    s = School_step8();
    
    for i in student_List:

        empty = [0];

        # If no subjects have been selected
        if(len(i[1])==0):
            s.addToCourse(i[0], empty);
        else:
            s.addToCourse(i[0], i[1]);
        
        '''
        # Remove characters from the string
        if( len(str(i[1]).translate(None,", []")) == 2):
            print(i[0] + (str(i[1]).translate(None,", []")));
            a = [0];
            s.addToCourse(i[0], a);
        else:
            s.addToCourse(i[0],list(str(i[1]).translate(None,",[] ")));
        '''
    
    print("\nDisplaying List of all students and what subjects they chose:\n" + str(s.displayStudents()));
    print("\nDisplaying number of students in each course:\n" + str(s.displayCourses()));


def step9():
    '''
    Approximation of Pi, using Monte Carlo Simulation, and ranom library.

    Arguments: None.

    Output: Print messages.
    '''
    print("Approximating Pi, using Monte Carlo Simulation and random library.");

    n = 0;

    for i in range(0,1000):
        d = Drop_step9();
        if(d.isTrue()):
            n += 1;
    print("Approx Pi with N of 1000: " + str(float(n*4)/1000));

    N = 1000000;
    n = 0;

    for i in range(0,N):
        d = Drop_step9();
        if(d.isTrue()):
            n += 1;
    
    print("Using N = " + str(N) + " Pi: " + str(float(n*4)/N));

def step10():
    '''
    Inheritance

    Arguments: None.

    Output: None.
    '''
    print("Iheritance");


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
    

def choosingStep():
    '''
    Initial function that allows navigation through the steps that I've done.

    Attributes: None.

    Output: Calling corresponding functions.
    '''
    
    running = True; 

    while running:
        choice = raw_input("\nWhich step do you wanna see? ");

        if(not isInt(choice)):
            print("\nPlease enter natural value");
        else:
            int_choice = abs(int(choice));
            # Escape
            if(int_choice == 199):
                break;
            # 1st step
            elif(int_choice == 1):
                step1();                
            # 2nd step 
            elif(int_choice == 2):
                step2();
            # 3rd step
            elif(int_choice == 3):
                step3();
            # 4th step
            elif(int_choice == 4):
                step4();
            # 5th step
            elif(int_choice == 5):
                step5();
            # 6th step
            elif(int_choice == 6):
                step6();
            # 7th step
            elif(int_choice == 7):
                step7();
            # 8th step
            elif(int_choice == 8):
                step8();
            # 9th step
            elif(int_choice == 9):
                step9();
            # 10th step
            elif(int_choice == 10):
                step10();

# Initiating main loop
choosingStep();
