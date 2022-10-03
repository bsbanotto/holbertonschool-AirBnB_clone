# AirBnB_clone

# About
This project is the first step towards building our first full web application, the AirBnB clone. What we accomplish in this first step will be built on in following projects.


## Each task is linked and will help:

 - Put in place a parent class called ``BaseModel`` to handle initialization, serialization and deserialization of future instances
 -  Create all classes used for AirBnB ``User, State, City, Place...`` that inherit from BaseModel
 - Create an abstracted storage engine: File storage.
 - Unittesting will be required to validate classes and storage engine


# Console
A command line interpreter will be able to manage the objects of our project in the following ways:

 - Create a new object(i.e. User or Place)
 - Retrieve an object from a file
 - Do operations on objects that have been retrieved
 - Update attributes of an object
 - Destroy an object

# Command Interpreter: Interactive Mode

First launch the console:

```
/AirBnb_clone$ ./console.py
```

Once launced you will be presented with an ``(hbnb) `` prompt ready to accept and execute individually typed commands.

Example: Create a new User<br>
`` (hbnb) create User``

Example: Create a new BaseModel<br>
`` (hbnb) create BaseModel``


# Command Interpreter: Non-Interacive Mode

To use in non-interactive mode echo the commands and pipe it to console.py

Example: Create a new User<br>
``AirBnb_clone$ echo "create User" | ./console.py``

Example: Create a new BaseModel<br>
``AirBnb_clone$ echo "create BaseModel" | ./console.py``

# Commands

## help -- shows help
### Usage:
For a list of built-in commands:<br>
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

For specific help on a command:<br>
```
(hbnb) help <command>
```
Example: Help for the create command<br>
```
(hbnb) help create

Creates a new instance of a class
Saves new instance to JSON file
Prints the id of the new instance
If the class name is missing, prints:
	** class name missing **

If the class name doesn't exist, prints:
	** class doesn't exist **
```


## create: Creates a new instance of an allowed class
### Usage:
> create 'class name'<br>

Example to create new BaseModel:<br>
```
(hbnb) create BaseModel
11d611e5-02b7-4586-a9b7-1180d7a7be96
```
If class name is missing, prints: ``** class name missing **``<br>
if class name doesn't exist, prints: ``** class doesn't exist **``<br>

## show: Prints the string representation of an instance based on the class name and id
### Usage:
> show 'class name' 'id'<br>

Example:<br>
```
(hbnb) show BaseModel 11d611e5-02b7-4586-a9b7-1180d7a7be96
[BaseModel] (11d611e5-02b7-4586-a9b7-1180d7a7be96) {'id': '11d611e5-02b7-4586-a9b7-1180d7a7be96', 'created_at': datetime.datetime(2022, 10, 2, 16, 7, 17, 241925), 'updated_at': datetime.datetime(2022, 10, 2, 16, 7, 17, 241961)}
```
If the class name is missing, prints:  ``** class name missing **``<br>
If the class name doesn't exist, prints: ``** class doesn't exist **``<br>
If the id is missing, prints: ``** instance id missing **``<br>
If the instance of the class name doesn't exist, print ``** no instance found **``<br>

## destroy: Deletes a specific instance of a class
### Usage:
> destroy 'class name' 'ID'<br>

Example:<br>
```
(hbnb) destroy BaseModel 11d611e5-02b7-4586-a9b7-1180d7a7be96
```
If the class name is missing, prints:  ``** class name missing **``<br>
If the class name doesn't exist, prints: ``** class doesn't exist **``<br>
If the id is missing, prints: ``** instance id missing **``<br>
If the instance of the class name doesn't exist, print ``** no instance found **``<br>

## all: Prints a string representation of all objects or all objects of a specific class(if no class is specified)
### Usage:
To show all objects:<br>
> all

To show objects of a specific class<br>
> all 'class name'

Example:<br>
```
(hbnb) all BaseModel
["[BaseModel] (78c7997c-dc97-40b5-a0df-fb26c051293a) {'id': '78c7997c-dc97-40b5-a0df-fb26c051293a', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 40, 846612), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 40, 848329)}"]
["[BaseModel] (35f7a7b1-3c8e-49b3-b306-74bb149241e7) {'id': '35f7a7b1-3c8e-49b3-b306-74bb149241e7', 'created_at': datetime.datetime(2022, 10, 2, 16, 18, 0, 948788), 'updated_at': datetime.datetime(2022, 10, 2, 16, 18, 0, 948801)}"]
```
Example:<br>
```
(hbnb) all User
["[User] (f381523d-d565-4b11-b97e-e572a8bb997e) {'id': 'f381523d-d565-4b11-b97e-e572a8bb997e', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842053), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842068)}"]
```
Example:<br>
```
(hbnb) all
["[BaseModel] (78c7997c-dc97-40b5-a0df-fb26c051293a) {'id': '78c7997c-dc97-40b5-a0df-fb26c051293a', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 40, 846612), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 40, 848329)}"]
["[User] (f381523d-d565-4b11-b97e-e572a8bb997e) {'id': 'f381523d-d565-4b11-b97e-e572a8bb997e', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842053), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842068)}"]
["[BaseModel] (35f7a7b1-3c8e-49b3-b306-74bb149241e7) {'id': '35f7a7b1-3c8e-49b3-b306-74bb149241e7', 'created_at': datetime.datetime(2022, 10, 2, 16, 18, 0, 948788), 'updated_at': datetime.datetime(2022, 10, 2, 16, 18, 0, 948801)}"]
```
If the class name doesn't exist, prints: ``** class doesn't exist **``<br>

## update: Update an instance
### Usage:
> update 'class name' 'ID' 'attribute' '"attribute value"'

Example:<br>
```
(hbnb) show User f381523d-d565-4b11-b97e-e572a8bb997e
[User] (f381523d-d565-4b11-b97e-e572a8bb997e) {'id': 'f381523d-d565-4b11-b97e-e572a8bb997e', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842053), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842068)}
(hbnb) update User f381523d-d565-4b11-b97e-e572a8bb997e first_name "Joseph"
show User f381523d-d565-4b11-b97e-e572a8bb997e
[User] (f381523d-d565-4b11-b97e-e572a8bb997e) {'id': 'f381523d-d565-4b11-b97e-e572a8bb997e', 'created_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842053), 'updated_at': datetime.datetime(2022, 10, 2, 16, 17, 42, 842068), 'first_name': 'Joseph'}
```
Only one attribute can be updated at a time<br>
Each argument is to be separated by a space<br>
A string argument with a space must be wrapped with double quotes<br>
If the class name is missing, prints:  ``** class name missing **``<br>
If the class name doesn't exist, prints: ``** class doesn't exist **``<br>
If the id is missing, prints: ``** instance id missing **``<br>
If the instance of the class name doesn't exist, prints:  ``** no instance found **``<br>
If the attribute name is missing, prints:  ``** attribute name missing **``<br>
If the value for the attribute name doesn't exist, prints: ``**value missing **``<br>

## quit: Quit the console by raising the SystemExit exception
### Usage:
> quit
Example:<br>
```
(hbnb) quit
```

## EOF: Quit the console by stopping the process
### Usage:
Press Ctrl + Z on keyboard<br>
```
(hbnb) 
[3]+  Stopped                 ./console.py
```

# Classes
## List of allowed classes and their attributes
```
User
 - email
 - password
 - first_name
 - last_name
```
``` 
State
 - name
```
```
City
 - state_id
 - name
```
```
Amenity
 - name
```
```
Place
 - city_id
 - user_id
 - name
 - description
 - number_rooms
 - number_bathrooms
 - max_guest
 - prict_by_night
 - latitude
 - longitude
 - amenity_ids
```
```
Review
 - place_id
 - user_id
 - text
```

##  Authors:

> Zach Wilsterman: [Github](https://github.com/wilstermanz)

> Ben Sbanotto: [GitHub](https://github.com/bsbanotto)