*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}    http://barru.pythonanywhere.com/daftar
${nama}    Briyan Priyo S
${email}    briyansaputro30@gmail.com
${pass}    admin123

*** Keywords ***
Open page
    Open Browser    ${url}    edge

Register
    Click Element    id=signUp
    Input Text    id=name_register    ${nama}
    Input Text    id=email_register   ${email}
    Input Text    id=password_register    ${pass}
    Click Element    id=signup_register

Login
    Click Element    id=signIn
    Input Text    id=email   ${email}
    Input Text    id=password    ${pass}
    Click Element    id=signin_login

*** Test Cases ***
Register testing
    Open page
    Register
Login
    Login