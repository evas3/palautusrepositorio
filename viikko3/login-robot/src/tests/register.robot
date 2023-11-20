*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  viljo  viljo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
    

Register With Too Short Username And Valid Password
    Input Credentials  k   viljo123
    Output Should Contain  Invalid username or password

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Invalid username or password

Register With Valid Username And Too Short Password
    Input Credentials  simo  k1
    Output Should Contain  Invalid username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sami  kahdeksan
    Output Should Contain  Invalid username or password
