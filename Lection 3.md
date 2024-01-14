# Advanced Python Lection 3

Contents:

1. Topic 1: Recap Class 2
2. Topic 2: GitHub I
3. Topic 3: Bringing Class 1 & 2 to Github

## Topic 1: Recap Class 2

We saw 4 things:

### 1. CLI Parser (Click)

A command-line interface (CLI) is a text-based user interface used to interact with software
and operating systems by typing commands into a console or terminal

Difference between CLI and GUI (Graphical User Interface) is that in CLI you ask your commands via text. In GUI (what we normally used because it's simplicity) is more graphical, but there are some commands that are difficult or impossible to do. 

Example: entering a directory

Via GUI --> you move the mouse to the folder and press two times to open

Via CLI --> cd "Name of the folder"

In CLI we can use scripts, python, sql, javascript ... 

#### Why are they useful?
- User-Friendly Interfaces: Creation of CLIs for Python applications.
- Argument Handling: They manage and interpret command-line arguments and options,
making it easier to control program behavior from the command line.
- Automation Support: Facilitates the automation of tasks via scripts and command-line
tools.
- Error Handling & Help: Offers built-in error handling for invalid arguments and ca
automatically generate help and usage messages.

python program.py -x arg1 -y arg2 (we will make an example of this later)

python fire --> simple way to create CLI

#### Usage examples

Some ideas (All of this from the command line)

- Apply filters from the command line with a flag
- Different splits for train-test in an ML model
- Use different Models
- Apply different ways of cleaning the data

Deep MP

- https://github.com/pepebonet/DeepMP/blob/release/deepmp/DeepMP.py (an example of Pepe creating different commands to use them in his terminal (CLI))

#### What is a CLI Parser?

A Python CLI (Command Line Interface) parser is a tool or library that helps in parsing command-line arguments and options provided to a Python script when it is executed from the command line. Our CLI parser choice will be click (there are more libraries such as argparse). 

#### Building blocks when using Click

- Library: Explains what we do in the script
- click.command: That we will use in the code
- click.options: Where the code will run.
- Pass it to function: Pass to main and use
them in the function

<br><br>

### 2. Debugger (PDB)

Debuggers are tools or utilities that help programmers identify and resolve bugs (errors) in their code
- Error Identification: Pinpointing the exact location of errors
in the code.
- Code Understanding: Understand how a program operates
- Efficiency: Speeds up the process of fixing bugs compared
to manual debugging methods (like print statements).
- Quality Assurance: Improve code quality by facilitating
inspection and testing.
- Learning Tool

#### Debugger work:

Code Working<br>
Code Working<br>
Code Working<br>
Code Working<br>
-Add debugger (stop the code)<br>
-Inspect the problem<br>
-Solve it<br>
Code Not Working —> Code Working<br>
More Code<br>
More code<br>

**Debugger:** Stop the code and maybe
inspect why the code below is giving
problems
- Stops the code at that line and allows you
to access all variables and the state of the
program at that point
- You control it from the command line

There are other options (IDE-specific debuggers) but we will use pdb

### 3. Try & Except

**TRY** and **EXCEPT** are keywords used for
exception handling. This mechanism allows
a program to continue execution even if an
error occurs in a specific block of code.

- *Error Handling:* Allows a program to handle errors gracefully without crashing.
- *User Experience:* Improves the user experience by providing meaningful error messages
instead of cryptic stack traces.
- *Robustness:* Increases the robustness of the application by enabling it to cope with unexpected
situations.
- *Debugging Aid:* Assists in debugging by catching and identifying exceptions.

### 4. Classes

**Classes** are a code template for creating
objects (a particular data structure),
providing initial values for state (member
variables or attributes), and implementations
of behavior (member functions or methods).
Classes encapsulate data for the object and
the methods to interact with that data.

### Why Classes?
- Encapsulation: Classes encapsulate data and
functions, making code more modular and organized.
- Code Reusability: Reducing redundancy and making
maintenance easier.
- Inheritance and Polymorphism: Classes allow the
use of inheritance and polymorphism (same name
different executions), key concepts in object-oriented
programming, enabling flexibility and code reuse (Not
always easy to grasp).

(Data Modelling, GUI & Web Applications, Game Development)

### Main Building Blocks of Classes

- Constructor: Method to start the class and create
objects
- Attributes: Variables that hold the specific objects
- Methods: Functions that define behaviors and can
manipulate attributes.
- Class Calling: Wat to call classes and create
objects

## Topic 2: GitHub 1

#### Code Versioning - GitHub

- Versioning: Allows developers to track changes to
their codebase over time.
- Collaboration: It enables multiple developers to
work on the same project concurrently, managing
code modifications, merging changes, and
resolving conflicts efficiently.
- Backup: Remote code repository, hosting your
project's code and providing a secure backup
- Continuous Integration and Deployment (CI/
CD): Automated build and testing processes.
Ensure code quality, and allows for smooth
deployment to production environments.

        Exercise
        
        Create a new repository to store all your files and the changes you make to them

#### What is .gitignore for?

.gitignore is a file used in all git repositories to
ignore files that you never want to put up in your
remote repository (web / GitHub)

*Examples:*
- Secret information (Passwords etc)
- Large files 

        Exercise
        
        Share the repository with me. Add me as a collaborator

        Add a folder named scripts in the newly created folder and start a new python script

Commit --> Every save you do for any important change you make. A commit can be published in a branch or another. 

Branch --> If you want to do some changes at the same time, you might work in a branch, while your partners are working in another. If you want to upload to the master or main branch, you have to be careful of not having any conflicts with any other part of code another person did.

#### You gotta use GitHub (or similar) 

- If you manage any type of data team or want to in the future 
- If you want to do any data project 
- If you want to properly learn how to work on an ML project 
- If you plan on collaborating with people 
- If you want to create your own product to share on the internet


#### The infrastructure of a problem we are building:

1. Developement (many branches) (Work on development,
Bring together all features
and check that there are no
conflicts)
2. Testing (Test the code to check that
it can go to production. )
3. Launch (Your Production
environment
This is what your users see, you can't have no problems!)

#### Some Comments about commits

- Commit Regularly
- Use Meaningful Commit Messages	 
- Try using branches for different features, bug fixes,
or experiments.
- Merge Changes Carefully
- Push regularly to GitHub for backup

        EXERCISE
        Download dataset FilmGenreStats from the Moodle
        Let’s create a script within our folder that is connected to Github. This script should have:

        - Classes
        - Click
        - Try & Except
        - Maybe some import pdb;pdb.set_trace()
        
        Every meaningful step we take should correspond with a commit


# PRACTICES 

## In class repository: https://github.com/CarlaMarti/Lection3 

## Homework repository: https://github.com/CarlaMarti/homework3
