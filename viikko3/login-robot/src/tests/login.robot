*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Test Cases ***
Login With Incorrect Password
    Input  kalle
    Input  kalllllll234
    Run Application
    Output Should Contain  Invalid username or password


Login With Nonexistent Username
    Input  kosma
    Input  kalle1234
    Run Application
    Output Should Contain  Invalid username or password