#  📌 Python Test automation - project

In this project I will challenge myself to create automation tests for the website: https://scouts-test.futbolkolektyw.pl/.
I will be using python and selenium library.

## Table of Contents

- [Getting Started](#-getting-started)
- [About the Project](#-about-project)
- Task 1: [Project configuration](#-project-configuration)
- Subtask 1 [Project Structure](#-project-structure)

## 🚀 Getting Started

Clone the repo and run test in the chosen ide.


## 🧩 About project

 First_automatic_test,_asserts
Why I decided to take part in this challenge?

Because I would like to get better at my QA job and be able to run automated tests as well!

## ☝  Task 1 - Project Configuration

In this task I prepared the environment for running tests.
I prepared the github repo and installed all the software.
I will be using Pycharm as IDE and this special framework: https://github.com/pyslawa/framework_test.

## ☝  Task 2 - Selectors

In this task I learned all about choosing the right selectors.

Now I am aware :

✅ What selectors are,                                                                                                   
✅ Where to look for them,                                                   
✅ How to write Xpath's,                               
✅ How to choose the best ones.

Here, you can see all the selectors I managed to find for the login page of this 
https://scouts-test.futbolkolektyw.pl/
website.

scouts_panel_header_xpath :

//h5
//*[text()="Scouts Panel"]
//h5[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"] 

login_field_xpath :

//*[@id="login"]
//input[@name="login"]
//*[@id="__next"]/form/div/div/div/div/input 

password_field_xpath :              

//*[@id="password"]
//input[@name="password"]
//form/div/div/div[2]/div/input

remind_password_hyperlink_xpath :

//*[@id="__next"]/form/div/div[1]/a
//*[text()="Remind password"]
//child::div/a

language_button_xpath :

//*[@id="__next"]/form/div/div[2]/div/div
//*[text()="English"]]
//*[contains(@class, "MuiSelect-root MuiSelect-select")]

sign_in_button_xpath :

//*[@id="__next"]/form/div/div[2]/button/span[1]
//*[text()="Sign in"]
//*[contains(@class, "MuiButton-l")] 


## ☝  Task 3 - First automated test and assertions

In this task I wrote my first test for logIn Page.

Check Out: 

## ☝  Task 4  - Refactoring, debugging and test cases

Now, there was a time to refactor the code, learn how to work with debugger, write more test cases and automate the whole website.

Check Out: 

## ☝  Task 5  - Robot Framework

In this task, I will gain a knowledge about:                 
✅ Smoke tests,                             
✅ Learn how to configure Suite Test,          
✅ Familiarize with Robot Framework,        
✅ Generate automatic report.

Check Out: 

## ☝  Task 6  - Reporting bugs and Report from tests

In this task I will learn how to catch up bugs and create a repo with them.

Check Out:

selectors
In this project I will challenge myself to create automation tests for the websites.

Subtask 1 - finding Selectors

Testing webiste: https://scouts-test.futbolkolektyw.pl/en/login?redirected=true

Relative Selectors:

//h5[contains(text(),'Scouts Panel')] for the box title

//input[@id='login'] for the login input

//input[@id='password'] for the password Input

//body/div[@id='__next']/form[1]/div[1]/div[1] for the remind password button 
//span[contains(text(),'Sign in')] For the SignIn button

Absolute Selector for the lagugage dropDown:
/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]
In this project I will challenge myself to create automation tests for the websites. 
main
main
