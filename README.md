# Ekstedt Booking Website

## Overview



## Table Of Contents

    * [Overview](#overview)
    * [UX](#ux)
        + [Strategy](#strategy)
        + [Scope](#scope-hr-)
        + [Structure](#structure-hr-)
        + [Skeleton](#skeleton-hr-)
        + [Surface](#surface-hr-)
            -[Color Scheme & Fonts](#color-scheme-and-fonts)
            -[Visual Effects](#visual-effects)
    * [Agile Methodology](#agile-methodology)
    * [Features](#features)
        + [Existing Features](#existing-features)
            - []
            - []
            - []
            - []
            - []
        + [Future feature considerations](#future-feature-considerations)
    * [Responsive Layout And Design](#responsive-layout-and-design)
    * [Tools Used](#tools-used)
        + [Python Packages](#python-packages)
    * [Testing](#testing)
    * [Deployment](#deployment)
        + [Deploy On Heroku](#deploy-on-heroku)
        + [FORK THE REPOSITORY](#fork-the-repository)
        + [CLONE THE REPOSITORY](#clone-the-repository)
    * [Credits](#credits)
        + [Content](#content)
        + [Media](#media)
        + [Code](#code)
    * [Acknowledgements](#acknowledgements)

## Overview

The Ekstedt Restaurant Booking System is a project designed to facilitate online reservations for users while offering efficient booking management for the site owner. Key features include user registration and authentication, a user-friendly booking interface, immediate confirmation and feedback, an admin interface for booking oversight, and secure database integration. The project prioritizes UX design principles, security measures and thorough documentation. It aims to meet the goals for both the external users, seeking a seamless booking experience, and the site owner, aiming for effective online booking management.

<br><br>
The deployed project is available at [this link](project link).
<br><br>

## UX

The site was created with respecting The Five Planes of Website Design:<br>

### Strategy<hr>

**User Stories:** <br>

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**Project Setup**                         |  ||
|                                       |1A| As a project manager, I want to clearly define project goals so that I have a clear understanding of what needs to be achieved.|             
|                                       |1B| As a developer, I want to set up version control using Git so that the project can be effectively managed.|
|**User Authentication**                  |  ||
|                                       |2A| As a user, I want to be able to register for an account so that I can access personalized features.|
|                                       |2B| As a user, I want to be able to log in to my account securely.|
|**Front-End Development**                     |  ||
|                                       |3A| As a user, I want to see a visually appealing and user-friendly booking interface.|
|                                       |3B| As a user, I want the design to follow UX principles to ensure a positive and intuitive experience.|
|**Booking System**                            |  ||
|                                       |4A| As a user, I want to fill out a booking form with the date, time, and number of guests.|
|                                       |4B| As a user, I want immediate feedback on the success of my booking.|
|                                       |4C| As a user, I want to receive confirmation emails or messages for successful bookings.|
|**Admin Interface**                               |  ||
|                                       |5A| As a site owner, I want to access a basic admin dashboard to view and manage bookings.|
|                                       |5B| As a site owner, I want the ability to confirm or reject bookings from the admin dashboard.|
|**Database Integration**                           |  ||
|                                       |6A| As a developer, I want to set up a database to store booking details.|
|                                       |6B| As a site owner, I want to have basic CRUD functionality for managing bookings.|
|**Testing**                         |  ||
|                                       |7A| As a developer, I want to develop automated tests to assess the functionality and responsiveness of the booking system.|
|                                       |7B| As a developer, I want to document test results, including identified bugs and fixes.|
|**Documentation**                      |  ||
|                                       |8A| As a developer, I want to create a README documentation that articulates the project's purpose, target audience, and security features.|
|                                       |8B| As a developer, I want to document the data schema and deployment procedure for future reference.|
|**Model Code Efficiency**                      |  ||
|                                       |8A| As a developer, I want to implement efficient model code to handle booking-related operations.|
|**Deployment**                      |  ||
|                                       |8A| As a developer, I want to document the deployment procedure in the README.|
|                                       |8B| As a developer, I want to ensure the deployment is well-structured and easy to follow.|
|**MVP Review**                      |  ||
|                                       |8A| As a project manager, I want to conduct user acceptance testing to ensure the MVP meets the goals of external users and the site owner.|

**Project goal:**<br>
The general goal of the project is to create a website for restaurant Ekstedt, which enables an efficient and user-friendly online restaurant booking system that allows users to easily book meals for themselves and others, specifying the desired time and date. Simultaneuosly, the system aims to empower the site owner by providing a robust admin interface for efficient management of online bookings at their eatery.

### Scope<hr>

**Simple and Intuitive User Experience:**<br>
* Design a user interface that is easy to navigate, consistent with the graphical profile and theme of the restaurant.
* Create a header, footer and a visible navbar throughout the website for seamless navigation.
* Implement an intuitive booking form with clear fields for date, time and the number of guests.
* Ensure visual notifications for all user actions and maintain user orientation during website navigation.
* Prioritize accessibility guidelines for an inclusive and user-friendly experience.

**Relevant Content:**
* Display essential information about the restaurant, including its name, location, phone number and email.
* Present the menu sets and wines which are available to order for the clients.

**Features for an Upgraded Experience:**
* Develop a reservation section allowing users to view all available tables for a specific date and time.
* Implement a profile page for users to manage upcoming bookings.
* Introduce a staff-member account with access to a management interface for handling all user bookings.
* Provide quick booking confirmation with immediate feedback.
* Incorporate notifications or reminders for upcoming reservations to enhance user engagement.

**Different Client and Staff-Member Accounts:**
* Establish distinct account types for clients (users making reservations) and staff members (site owner and administrators).
* Allow clients to register, log in and manage their accounts.
* Enable staff members to access an admin interface for efficient booking management, confirmation, and rejection.
* Implement filters visible only to staff members for finding specific reservations.

**Responsiveness:**
* Develop a responsive website that works seamslessly across various devices, including desktops, tablets and mobile devices.
* Optimize the user interface for different screen sizes, ensuring a consistent and enjoyable experience.