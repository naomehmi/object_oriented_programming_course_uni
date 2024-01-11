# object_oriented_programming_course_uni

This repository contains my code for my Object Oriented Programming (OOP) course in uni. (in progress)

notes
- `class_k` = contains every class that is used for each meeting (labeled as _#M[x]_ in the file to separate classes used per meeting)
- `m[x]_task[y]` = _m[x]_ is the xth meeting of the course, and _task[y]_ is the yth task of the meeting
- prompts and some variable names are in Indonesian
- some class names are pretty random because of the instructions given by each assignment :v

## topics for each meeting

### week 1 (m01)

- introduction to oop (class creations, instantiating objects, properties, methods)
- task 1 = attendance list of lecturers (dosen) and students (mahasiswa)
- task 2 = simple stock report of an e-commerce website
- task 3 = creating a student ID card for a private course

### week 2 (m02)

- inheritance and polymorphism (super classes and subclasses)
- task 1 = making a parent class containing name, ID, and other general info; where the 2 child classes then inehrit those properties
- task 2 = making a parent class for a product (produk), then create classes for specific products, such as hand sanitizers, car wheels, bottles, etc that inherit properties and methods from the parent class

### week 3 (m03)

- abstract classes (abc library, abstract properties, and abstract methods)
- task 1 = creating 2 different child classes that inherit properties and methods from a parent class and an abstract class. The child classes both have a method with the same name but different outputs.
- task 2 = making an abstract class that has 3 abstract properties and 1 abstract method, and a parent class containing 3 properties (name, phone number, fee); Then, 3 child classes are created to inherit all those properties and methods. After that, adding a unique property to each child class (for example, in the `MuridSD` class, the gender (`jenisKelamin`) property is added to it; in the `MuridSMP` class, the age (`umur`) property is added to it)

### week 4 (m04)

- try and exception (ValueError, AttributeError, etc)
- both tasks require users to input data (such as names, phone numbers, genders, etc), then the program prevents inputs that don't meet the conditions (e.g. a person's name containing number and symbols)

### week 5 (m05)

- iterator pattern (using for in array, iter(), and next())
- task 1 = making a simple program to input and find the data of students using `for`
- task 2 = making a simple program to input and find the remaining stock of an item in a warehouse system, notifying the user if the stock of the item is low using `iter()` and `next()`

### week 6 (m06)

- lists, sets, dictionaries
- comprehension
- task 1 = storing dictionaries containing the student ID, name, and phone number of students into a list. There are methods for validating data before appending them into the list, sorting the list based on student ID, printing/showing all the data, and searching for a specific student
- task 2 = storing dictionaries containing the product code, name, and stock of products into a list. There are methods for validating data before appending them into the list, sorting the list based on product code, printing/showing all the data, and showing the products that are almost out of stock (less than 10)

### week 7 (m07)

- yield, generators
- using `.send()`, `next()` to send user input to the object.
- storing input data into a list of dictionaries
- task 1 = making a simple program to store data of college students (student ID number, name, and phone number), printing all of them, and a search feature based on their student ID number
- task 2 = making a simple program to store data of products, printing all of them, checking products with low stocks

### week 8 (m08)

- midterms week, skipped

### week 9 (m09)

- design patterns (decorator pattern, observer pattern, strategy pattern)
- recording the attendance of college students and lecturers in a university event. i used the decorator pattern to differentiate the college students (MahasiswaM9 class) and lecturers (DosenM9 class), then i used an observer pattern to append attendees into 2 lists based on whether they are college students (mahasiswa) or lecturers (dosen).

### week 10 (m10)

- design patterns pt. 2 (template pattern, singleton pattern)
- same objective as week 9, but this time i used singleton pattern (i followed how the module did it, but idk i'm hesitant whether it's correct or not)
- this time i validated the data before inputting it into the `self._Absensi` dictionary, which contains the attendees of the event

### week 11 (m11)

- design patterns pt. 3 (adapter pattern, facade pattern, command pattern)
- um, the task for this week was basically just printing out the class's name, room, and subject. so i think i implemented the facade pattern(?) by making three different classes containing their name, room, and subject then combined them into another class called `Receptionist`. pls it's way too simple im hesitating to consider it as an implementation of the facade design pattern

### week 12 (m12)

- design patterns pt. 4 (abstract factory pattern, composite pattern)
- the task for this week was so also really simple. the lecturer wanted us to total the enrollment fee of a new university student by using object oriented programming. i made a class that has an attribute that is a list of all the fees, then the total would be calculated with a function called `returnPrice()`. based on the module, i implemented the composite design pattern, but then again im also hesitant about it because it's wayyyy too simple

### week 13 (m13)

- testing (unittest, pytest)
- the task for this week was to simply test any program from the previous meetings (using unittest or pytest) and check whether the results are correct or not. i chose week 9 and checked whether the total amount of attendees are correct or not

### week 14 (m14)

- solid pt. 1 (SRP - Single Responsibility Principle, OCP - Open Closed Principle)
- the task for this week was to redo m1's code so it applies to SRP and OCP

### week 15 (m15)

- coming soon...

### week 16

- final exams week, skipped
