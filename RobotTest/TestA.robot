*** Settings ***
Library     SeleniumLibrary
Test Teardown    CloseApp
Test Setup    LaunchMyBrowser



*** Variables ***



*** Test Cases ***
Validate_Client_Says_Text

       TRY
               validate_Client_Says_False
       EXCEPT  Unable to find CLIENT SAYS Title
               validate_Client_Says_True
       END

       Log to console   Execution is ###########




*** Keywords ***

validate_Client_Says_False

    Click Element    //h2[text()='CLIENT SAYSMMM']

validate_Client_Says_True

    Log to console   Execution is @@@@@@@@@@

LaunchMyBrowser

        Open Browser    https://www.fleekitsolutions.com/      chrome
        Maximize Browser Window
        Sleep   2


CloseApp
        [Teardown]
        Close All Browsers
















