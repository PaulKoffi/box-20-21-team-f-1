Feature: Launch a rocket

    Scenario: launching a rocket
        Given we will to launch a rocket at a site
            When Richard starts the poll of the rocket PGP-6000 at Paris
            Then Elon sends the order to launch the rocket PGP-6000 at Paris
            Then after 60 seconds , the satellite was successfully delivered by PGP-6000

    Scenario: launching a rocket
        Given we will to launch a rocket at a site
            When Richard starts the poll of the rocket Columbia-176 at Paris
            Then Elon sends the order to launch the rocket Columbia-176 at Paris and after 30 seconds richard destroy it
            Then the satellite was not successfully delivered by Columbia-176
