# AirBnB clone - The console

![Just a hotel (courtesy Holberton & Koome Mwiti)](https://github.com/Rmolimock/AirBnB_clone/blob/master/Readme_images/Screen%20Shot%202019-07-04%20at%205.24.23%20PM.png)

### Description
This is the first step towards building your first full web application: the AirBnB clone. For the end-user to be able to interact with a fully functioning AirBnB clone we must be able to finalize the backend and the front end which will involve building;

The image below demonstrates what this entire project will entail.

![AirBnB Clone process (courtesy Holberton)](https://github.com/Rmolimock/AirBnB_clone/blob/master/Readme_images/AirBnB%20Clone%20process.png)

* The console
* The Storage Engines e.g. JSON, MySQL
* Flask RESTful api - Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with your existing ORM/libraries. Flask-RESTful encourages best practices with minimal setup. 
* Flask - Flask is a micro web framework written in Python. It is classified as a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
* JSON (Java Script Object Notation) - Lightweight format for storing and transporting data. Often used when data is sent from a server to a web page
* Front-end (Client facing) e.g Javascript, HTML 


## What you should learn from this initial AirBnB clone project:

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the cmd module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage datetime</li>
<li>What is an UUID</li>
<li>What is args and how to use it</li>
<li>What is kwargs and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>




## [0. README](./README.md)

* A README file that describes the AirBnB clone project

## [0. AUTHORS Acknowledgement](./AUTHORS)

* This file details contacts of the authors of this shell project and contributors as per the git commits

## [1. Be PEP8 compliant!](./AirBnB_clone/)

* A beautiful code that passes the pep8 formatting compliance checks.

## [2. Unittests](./AirBnB_clone/tests/test_models/)

* A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together. In this project we utilized several tests for the different python class methods that we utilized in our functions to check for any edge cases that would break or check for possible improvements.

## Unittests repository set-up

**Repo set-up**

- AirBnB -> Models -> engine -> file_storage.py

* And thus the structure for our tests_cases …

- AirBnB -> Tests-> test_models -> test_engine -> test_file_storage.py

- AirBnB -> Tests-> test_models -> test_base_model.py


For example in testing for unit tests for our BaseModel Class we used the following edge cases

![BaseModel Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/Readme_images/unittest_image.png) BaseModel Unittests

<ul>
<li> What other unittests did we develop to test our project? </li>
<ul>
<li> ![Amenity Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/tests/test_models/test_amenity.py) test_amenity.py - Unittests for amenity class </li>
<li> ![City Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/tests/test_models/test_city.py) test_city.py - Unittests for city class </li>
<li> ![Review Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/tests/test_models/test_review.py) test_review.py. </li>
<li> ![User Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/tests/test_models/test_user.py) </li>
<li> ![Place Class Unittests](https://github.com/Rmolimock/AirBnB_clone/blob/master/tests/test_models/test_place.py) </li>
</ul>
</ul>

### [3. BaseModel ](./AirBnB_clone)

    **BaseModel Class Methods**

- Defines all common attributes/methods for other classes

- ![Base class](https://github.com/Rmolimock/AirBnB_clone/blob/master/models/base_model.py)

## What does it contain for it to run?

    **__init__.py file**
	
	- The __init__.py files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string , unintentionally hiding valid modules that occur later on the module search path

![Base Class __init__ file](https://github.com/Rmolimock/AirBnB_clone/blob/master/Readme_images/__init__%20example.png)

   **class methods str, save, to_dict**

![BaseModel class](https://github.com/Rmolimock/AirBnB_clone/blob/master/Readme_images/str%20save%20dict%20classes.png) - Public instance class methods

	- def __str__() returns string representation of an instance
	- def save() saves an instance and calls the storage instance to save to file
	- def to_dict returns a dictionary containing instance attributes

---


## Shout outs!
<ol>
<li>[](https://github.com/abmcbride5)</li>
<li>[](https://github.com/renefibonacci660)</li>
</ol>
=======

## Authors
* **Koome Mwiti** - [komerela](https://github.com/komerela)
* **LinkedIn** - [koomemwiti](www.linkedin.com/in/koomemwiti)

=======
* **Russell Mullimock** - [Rmolimock](https://github.com/Rmolimock)
* **LinkedIn** - [rmolimock](www.linkedin.com/in/russellmolimock)
