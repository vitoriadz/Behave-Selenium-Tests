Feature: User registration

  Scenario: Form completed and sent successfully
    Given that the user is on the form page
    When the user fills in the form with valid data
    Then the form is displayed a success message in the terminal

  Scenario: Attempting to submit the form with the name field blank
    Given that the user is on the form page
    When the user fills in the form with the name blank
    Then the form submission fails due to blank name

  Scenario: Attempting to submit the form with a blank last name
    Given that the user is on the form page
    When the user fills out the form with the last name blank
    Then the form submission fails due to blank last name

  Scenario: Attempting to submit the form with an invalid email address
    Given that the user is on the form page
    When the user fills out the form with an invalid email
    Then the form submission fails due to invalid email

  Scenario: Attempting to submit the form with an invalid number
    Given that the user is on the form page
    When the user fills in the form with an invalid number
    Then the form submission fails due to invalid number