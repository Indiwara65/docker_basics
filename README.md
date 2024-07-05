# Python Packaging    
## Why
#### Metadata      
* Metadata can be easily logged by packaging the project.   

#### Internal Dependencies      
* If there are any modules that are imported to the main code it might case errors.      
* This due to the fact that python maintains a list of file paths for all the libraries installed. If a internal module is imported python might raise an error 'no module error'.        
* Thses errors will be eliminated by packaging the project.     

#### External Dependencies     
* External dependecies can be easily be installed at the same time the package in installed.       

#### Automation     
* Automating testing will require to import the files which will be problematic if the files arn't packaged.

#### Standardization       
* Python package is will standardized by PEP. (Python Enhancement Proposal) 
* Therefore, a package developed in one device is garanteed to work in another.
### Folder Structure / Source Tree
mypackage/           
├── __init__.py            
├── __main__.py          
├──  module1.py      
└──  module2.py             
* __main__.py will be the entry point when the folder is called __main__.py will be the file that is executed.       
* __init__.py is used by convention to mark the directory as a 

### pyproject.toml
* The pyproject.toml file is written in TOML. Three tables are currently specified, namely **[build-system]**, **[project]** and **[tool]**. Other tables are reserved for future use.         
* Referance - https://packaging.python.org/en/latest/specifications/pyproject-toml/                  
* **source distribution** (s-dist) - contains raw source code and metadata, used for building the project on the target system.         
* **wheel** - a pre-built binary distribution that can be installed quickly without the need for building from source.
* **build-backend** - the tool or library responsible for building the project, specified in the pyproject.toml file.               
#### [build-system]      
* fileds - 
    * requires - required libraries for building the source distribution.                   
    * build-backend - tool used for building the source distribution        

#### [project]           
* **project** this table is used to declare metadata.       
* There are 2 types of metadata -             
    * static - static variables are hard coded in either pyproject.toml, setup.py or setup.cfg file. eg - name, author name, license etc...                   
    * dynamic - dynamic metadata are allocated during the build time.     

* mandotary fileds -             
    * name, version        
* other fileds - 
    * authors, urls, license, description, readme 
              

# Testing            
## Unit Testing   
* Unit testing is focusses a part of a code at a time usually a function or a class at a time.        
* Python has a inbuilt package **unittest** to perform and **pytest** is also a popular package.                   
### PyTest           
* Any file starting with **test_** or ending with **test_** will be identified as a test script by pytest.               
* A function inside the test file starting with **test** will be identified as one test.       
* **Decorators**         
    * **@pytest.fixture** - any code that needs to be run before any test can be put inside a function and by using the above decorator this function will run at the start of any test if specified. Ideal if there are common initializations for more than one test case.      
    * **@pytest.skip** - this decorator can be used before any tests that need to be skipped *eg - @pytest.skip(reason="Not yet implemented")*                  
    * **@pytest.skipif** -  this decorator can be used before any tests that need to be skipped if some condition is True. *eg - @pytest.skipif(sys.platform == "win32", reason="does not run on windows")*   
    * **@pytest.xfail** - this decorator can be used before any test that is known for an error but not fixed up yet. 
* By running *pytest -k testName* we can run an individual test.      
* Common tests -        
    * **assert** - used to test if a return is equal to a specific value.       
    * **pytest.raises** - used to test if the tested unit raises necessary errors where required. All errors in python are given in - https://www.tutorialsteacher.com/python/error-types-in-python          

## Other Tests        
* **flake8**           
    * Uses -      
        * Style Guide Enforcement: Ensures that your code adheres to PEP8, the Python style guide.
        * Code Quality: Identifies common errors in Python code, such as undefined names, unused imports, and other issues that could lead to bugs.    
        * Complexity Checking: Reports on the complexity of your code, helping you identify functions that are too complex and need refactoring.               
        * To run flake8 - **flake8 path/to/file**            
        * To check only a selected number of tests - **flake8 --select E12,E121 path/to/file** (only E12 and E121 will be checked)          
        * To ignore tests - **flake8 --ignore E12,E121 path/to/file** (E12 and E121 will be ignored)                  
        * Run all tests including default ignored tests - **flake8 --select path/to/file**                                        

* **black**       
    * Uses -       
        * Code Formatting: Automatically formats your code to make it consistent. This removes the need for manual formatting and reduces the likelihood of style-related review comments.                    
        * Consistency: Ensures all team members' code looks the same, which makes reading and understanding code easier.          
        * Time-Saving: Saves time during code reviews and reduces the mental load of formatting code manually  .               
        * To run - **black path/to/file**                  
* **mypy**         
    * Uses -     
        * Type Checking: Ensures that your code adheres to specified type hints, catching potential type errors during development rather than at runtime.
        * Documentation: Provides better documentation through type annotations, making it easier to understand what types of arguments a function expects and what it returns.
        * Refactoring Safety: Helps in refactoring code by ensuring that changes do not introduce type inconsistencies.               
        * To run - **mypy path/to/file**               
        