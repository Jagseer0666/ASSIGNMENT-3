# ASSIGNMENT-3

Requisition System

Staff requisitions are made using Python which automated functions produce a requisition ID and also do quick total cost calculations along with setting up approval rules. The way software is implemented using key design approaches makes it simple to maintain and structured.

Features

With this system, staff are able to generate requisitions using automated features.

a. Checks if the dates are written properly
b. Makes distinct requisition IDs by increasing a counter with each use
c. Estimates how much customers would pay for the listed merchandise
d. Defines approval based on the total price.
e. Tracks requests based on if they have been: approved, are still pending or are not approved

Design of Software Based on Principle.

KISS (Just make it simple).
Everything in the programming code is laid out in a straightforward manner. A lower function does one thing clearly with minimal extra effort.

Don’t use the same code or logic more than once.
Repeating things like date and approval checks have been largely replaced by putting the code in one central location. We can extend the concept of reusability by providing tracking functions for keeping the working status.

Open/Closed Principle
By using this design, the system can allow extra features to be added without changing the stable functions. It’s possible to introduce new tiers for approvals or export choices, without causing interference for the existing flow.

Following Composition Over Inheritance
Rather than a strict hierarchy, the system depends on well-organized, hierarchical functions. With this method, the emphasis falls on ease of navigation.

Make sure that every method of a class is responsible for only one thing.
There is a function for every single purpose it needs.
Validating a date is done through the get_valid_date() method.
To call the create_requisition() function is to initiate data collection.
Total calculation occurs after running add_products_to_requisition().
* evaluate_requisition() defines the rules for giving the request approval
* print_requisition_summary() shows a detailed summary

Keeping different responsibilities in different parts of a system.
Programming tasks are designed so that input, processing and reporting are done using separate methods to avoid confusion.

You Don’t Have to (YTHT).
Only additional features are added if they are necessary. Experienced developers stick to what is necessary and don’t code more than they need to.

Don’t jump straight to optimizing your code.
Getting a performance correct is not more important than making it clear and accurate. First, the script focuses on being straightforward and then on being fast.

Edit, edit, edit
The system was developed so that upgrades and developments can be made in the future. With modular organization, you can make changes over the years without too much difficulty.

Clean code is better than making your code brilliant or subtle.
The programming uses easy-to-understand names and an understandable sequence. The design is simple enough to be easily understood.

Summary

All things considered, this project demonstrates how well software engineering principles can be put into practice. The script manages to be simple, separate tasks into distinct folders and creates a firm base to start from. Even though the code could use more reuse and validation, it favors environmentally friendly and scalable development.
