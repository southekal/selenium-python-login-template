# selenium-python-login-template

### Introduction
* Template to test login page and its elements

### Installation
* git clone https://github.com/southekal/selenium-python-login-template.git
* Go to the directory - "selenium-python-login-template"
* pip install -r requirements.txt (Preferably in virtual env mode or with sudo access)

### Requirements (mentioned in requirements.txt)
* Selenium : WebDriver
* Nose: extension of unittests
* Requests: HTTP library

### Configuration
##### default.cfg
* login page url
* sign up page url
* valid email address
* valid password
* invalid email address
* invalid password
* different screensizes

### Helpers
* driverutil.py - encapsulates webdriver
* locators.py - holds CSS selectors, IDs, names

### Running Tests
* From the home directory "selenium-python-login-template" run
* nosetests --nocapture --nologcapture src/login.py

### Future Enhancements
* Testing against multiple screen sizes.
* More test cases around invalid email/password combination
* Stronger assertion after successful user login.
* Utilizing explicit wait instead of "time.sleep" usage in certain cases.


