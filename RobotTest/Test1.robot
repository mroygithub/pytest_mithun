*** Settings ***
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***

Verify Google Application

    Open Browser    https://www.docker.com      Chrome
    Maximize Browser Window
    Mouse Over  (//a[text()='Developers'])
    sleep   2
    Click Element   (//a[text()='Getting Started'])
    sleep   3
    #Log To Console      Get location
    ${currURL}=     Get Location
    Log To Console  ${currURL}
    Should Be True  """${currURL}""" == """${exURL}"""
    Close All Browsers


