# Ekstedt Booking Website

## Overview
This is a project designed and developed to create a complete experience for the clients of Ekstedt Restaurant. The users are given the possibility to create a booking, the admin is capable of approving it and the staff members are meant to manage all the bookings. In order to make a booking, an account registration is needed, while considering that the staff members have special permissions for controlling the data.<br>
The website was created by getting inspiration from a real life exclusive Restaurant Ekstedt, which is based in Stockholm.<br>
**Ekstedt Booking Website** was developed using Python3 (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
<br><br>
The fully deployed project can be accessed at [this link](https://booking-system-ekstedt-80e2fb2174de.herokuapp.com//).<br><br>


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
        - [User Registration and Authentication]
        - [Booking Interface]
        - [Feedback and Confirmation]
        - [Admin Interface]
        - [Database Integration]
        - [Basic Front-End Design]
        - [Testing]
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
The deployed project is available at [this link](https://booking-system-ekstedt-80e2fb2174de.herokuapp.com/).
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

### Structure<hr>

The website's structure is divided into nine different pages with content which is depended on authentication and if the user is client or a staff member.

* **Home:** This is the entry point of the website where users can find excerpts and hyperlinks to history, menu and reservation pages.
* **History:** This page provides users with information about restaurants history and past. Including information about its establishment and the chef's background and culinary philosophy.
* **Menu:** The menu page for Ekstedt restaurant displays the set menu and available pairings. The page also includes a link to the restaurant's wine list on Star Wine List and a reservation button.
* **Reservation:** The page includes information about reservation policy and a button for making a booking.
* **Profile:** The page displays users' reservation history and allows them to manage their bookings.
* **Contact:** Contact page of the restaurant Ekstedt includes info about the address, phone number, and email for reservations and general inquiries.
* **Login:** A page where users need to log in to access and manage their accounts.
* **Manage bookings:** This page is only accessible for staff members and allows them to manage reservations, view bookings, and update the status of tables.
* **Register:** This page allows new users to register and create an account to the website.
* **Profile:** This page allows the users see their past bookings and details.

#### Flowchart

The flowchart for the project was created with using <b>LucidChart</b>.<br><br>

[![N|Solid](static/images/flow_diagram.png)](static/images/flow_diagram.png)<br><br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created by [Balsamiq](https://balsamiq.com/) tool and can be viewed <details>
<summary>Here:</summary>
<img src="static/images/ekstedt_wireframes.png"><br>
</details><br>

**Database**<br>
In the project ElephantSQL was used for PostgreSQL relational database in data storing.
Two diagrams were created to represent the relationships between the tables. The first diagram was created before the website was developed, and it was used to identify the most relevant and useful attributes and tables. The final diagram was created after the website was developed, and it reflects the changes that were made to the attributes and tables.
<br>
<details>
<summary>Initial Model</summary>
<img src="static/images/initial_diagram.png"><br>
</details>

<details>
<p>During the development, it was decided that the admin interface needs a booking confirmation history interface, for better data
analitics. Therefore the diagram changed quite considerably.</p>
<summary>Final Model</summary>
<img src="static/images/latest_diagram.png"><br>
</details><br>

### Surface<hr>
#### Color Scheme and Fonts
* The fonts that were used in this project were taken from [Google Fonts](https://fonts.google.com/):<br>
* h1 - h3 elements: *Playfair Display*
* h4 , p, td, th elements: *Lato*
* font color: #white
* Webpage background image was found [Freepik](https://www.freepik.com/):
<img src="static/images/charcoal_gray_crop.png">

## Agile Methodology
This project was developed using the Agile Methodology.<br>
Epics and user stories were registered using [GitHub](https://github.com/). As User Stories were accomplished they were moved to **ToDo**, **In Progress**, **Done** and **Future Development** lists.
<details>
<summary>Sprint Details</summary>

* **KANBAN BOARD**<br><br>
    <img src="static/images/kanban_board.png" width="60%"><br><br>

* **MVP Epics and Stories:**<br>

* **EPIC 1: Project Setup**<br>
    -#12 Define Clear Project Goals<br>
    -#13 Set Up Git Version Control for Project Management and Collaboration<br>
* **EPIC 2: User Authentication**<br>
    -#15 User Registration for Access to Personalized Features<br>
    -#16 Secure User Login Functionality<br>
* **EPIC 3: Front-End Development**<br>
    -#18 Visually Appealing and User-Friendly Booking Interface<br>
    -#19 User-Centric Design Following UX Principles<br>
* **EPIC 4: Booking System**<br>
    -#21 User-Friendly Booking Form with Date, Time, and Guest Information<br>
    -#22 Real-Time Feedback on Booking Success<br>
    -#23 Confirmation Messages<br>
* **EPIC 5: Admin Interface**<br>
    -#25 Implementation of Basic Admin Dashboard<br>
    -#26 Booking Confirmation and Rejection Functionality in Admin dashboard<br>
* **EPIC 6: Database Integration**<br>
    -#28 Database Setup for Booking Details<br>
    -#29 Basic CRUD Functionality for Booking Management<br>
* **EPIC 7: Testing**<br>
    -#31 Automated Testing for Functionality and Responsiveness<br>
    -#32 Test Results Documentation and Bug Tracking<br>
* **EPIC 8: Documentation**<br>
    -#34 Project README Documentation Creation<br>
    -#35 Data Schema and Deployment Documentation<br>
* **EPIC 10: Deployment**<br>
    -#39 Documentation of Deployment Procedure in README<br>

* **Plausible Future MVP Updates:**<br>

* **EPIC 9: Model Code Efficiency**<br>
    -#37 Implementation of Efficient Model Code for Booking<br>

* **EPIC 10: Deployment**<br>
    -#40 Optimization of Deployment Structure for Improved Accessibility<br>

* **EPIC 11 MVP Review**<br>
    -#42 User Acceptance Testing for MVP Alignment<br>

* **EPIC 12 Iterative Development**<br>
    -#44 Feedback Gathering for Continous Improvement<br>
    -#45 Iterative Feature Development and Refinement<br>
    -#46 Continous Project Iteration for Enhancements<br>
</details><br><br>

## Features

### Existing features and sub-pages<hr>

#### Customer bookings management

Every client that is authenticated can access the "Booking" page where they have an overview over their bookings and from there they can select their booking for it's "Details".
* From "Booking" view they can:
    * View their booking in a table;<br>
    * Create a new booking;<br>
    * Select the booking which leads to the booking details page;<br>
<br><br>

<img src="static/images/bookingslistuser.png"><br><br>

* From "Details" view they can:
    * View the booking details;<br>
    * Select to update their booking;<br>
    * Select to delete their booking;<br>

<img src="static/images/bookingdetails.png"><br><br>

#### Staff bookings management

Staff users that are authenticated can acces the "Booking" page where they have an overview over all of the bookings that will occur today and in the future in table format.
* From "Booking" view they can:
    * View the bookings for today in the first table;<br>
    * View the bookings for future in the second table;<br>
    * Select a booking which leads to the particular booking details page, where it has similar functionalities that were previously mentioned as for the regular user;<br>
    * Create a new booking;<br>
<br><br>

<img src="static/images/staffbookinglist.png"><br><br>

#### Create Bookings

Every user that is authenticated can access the *Booking* page for making a booking. This feature provides a form which the user needs to fill out with booking details. There are different rules for staff and regular users when filling out the form. Information on the form page is provided about the maximum guest number and how long is the minimum length of a booking.
* The form is for selecting the date and time choice of the booking.
    The inputs are validated according to these rules:
    * The date value should be 60 days after the day that the booking is performed, this applies only to a regular user and not the staff. This is that staff can accomodate special occasions when the need arises since they have the overview how the restaurant is running and can make adjustments for the capacity and table placements in the restaurant;<br>
    * Entering the name, number of guests, date and time choice is required;<br>
    * Maximum number of guests for one booking is 6 people;<br>
    * The restaurant does not provide any times for Sunday and Monday;<br>
    * The user cannot make a booking in the past;<br> 
    * The users can choose a time from a list:
        * Tuesday to Friday: "17:30" and "21:15"
        * Saturday: "12:00", "15:30" and "19:00"<br><br>
    * The users are also able to add their email and notes about the booking, which are optional;<br><br>

<img src="static/images/createbooking.png"><br><br>
     
* In case of a successfull booking the user will be redirected to the bookings list page, where also a message will appear.

#### Menu

The "Menu" page provides the users information about the restaurants menu and price. Where they can also click onto a link, which leads them to the wine list on an external site.

<img src="static/images/menupage.png"><br><br>

#### History

The "History" page includes a brief history about the restaurant and the owner, explaining where it all began.

<img src="static/images/historypage.png"><br><br>

#### Contact

The "Contact" page includes information about how to contact the restaurant and where it is located.

<img src="static/images/contactpage.png"><br><br>

#### Profile

The "Profile" page includes information for the user about their past bookings and their user details.

<img src="static/images/profilepage.png"><br><br>

#### Admin Interface

The admin interface includes capabilities for the admin(superuser) to add and remove tables, users and bookings. While also provides the capability for the admin and staff members to confirm and approve bookings. There is also a BookingHistory functionality which provides details about confirmation/rejection of the bookings.

<img src="static/images/admininter.png"><br><br>

#### Potential Future Features

* Email confirmation for users with booking details after the booking has been confirmed by the admin or staff member.
* Password reset feature which can be included hand in hand with email confirmation.
* Possibility for the users to enhance their profile with more information.
* On-site waiting list feature for making it easier to keep track on the upcoming bookings and being on track on customer satisfaction. 

## Responsive Layout and Design

The project has been designed to all types of devices using Bootstrap predefined breakpoints. A custom breakpoint of max-width: 768px was made for devices where the design did not fit.

**Tested Devices:**

- Samsung Galaxy S 23
- Samsung Galaxy S 22
- MSI GL62M 7RDX Laptop

**Devices Through Inspection:**

- Samsung Galaxy S8 +
- IPhone 12 Pro
- IPad Pro

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code for the program.<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project.<br>
[ElephantSQL](https://www.elephantsql.com/) - for PostgreSQL database.<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes.<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the FlowChart and Database relational schema.<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content.<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predefined styled elements and creating responsiveness.<br>
[Google Fonts](https://fonts.google.com/) - for typography.<br>
[Code Institute](https://pep8ci.herokuapp.com/) - used for validating the Python code.<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML.<br>
[CSS - JigSaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS.<br>
[Chrome Dev Tools](https://developer.chrome.com/docs/devtools) - for debugging the project.<br>
[W.A.V.E](https://wave.webaim.org/) - for testing accessibility.<br>
[Cloudinary](https://cloudinary.com/) - for storing static data.<br>
[Chrome Lighthouse Extension] - for testing performance.<br>

### Python Packages

* Django (Framework)
* django-allauth (Library)
* Cloudinary (Library)
* Gunicorn (Web Server)
* psycopg2 (Library)

### Testing

The testing documentation can be found at TESTING.md

## Deployment

### Deploy on Heroku

1. Create a Pipfile
Enter the command `pip3 freeze > requirements.txt`, after this a file with all requirements will be created.

2. Setting up Heroku

* Go to Heroku website (https://www.heroku.com/)
* Login to Heroku and choose *Create App*
* Click *New* and  *Create a New App*
* Choose an application name and location.
* Go to the *Resources* tab 
* From the Resources list select *Heroku Postgres*
* Navigate to the *Deploy* tab
* Click on *Connect to GitHub* and search for your repository
* Navigate to the *Settings* tab
* Reveal Config Vars and add your Cloudinary, DataBase URL (from Heroku-Postgres) and Secret Key.

3. Deployment on Heroku

* Go to the deploy tab.
* Choose the main branch for deploying. It is up to you if you wish to click on automatic deployments. In this app development, this was not done and the application was deployed manually.
* Select the manual Deploy to build the app.

### Forking the repository

In order to create a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [Booking-System-Ekstedt Repository](https://github.com/FlyHighhher/booking-system-ekstedt.git), press <i>Fork</i> in the top right of the page.
- A forked version of the project will appear in your repository.
<br></br>

### Clone the repository

For creating a clone of the repository on your local machine, use <b>Clone:</b>
- On [My Repository Page](https://github.com/FlyHighhher/booking-system-ekstedt.git), click the <i>Code</i> green button, right above the code window.
- You can choose from <i>HTTPS, SSH and GitHub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL.
- Your clone was created.
<hr>

## Credits

### Content

The inspiration was taken from a restaurant that is based in Stockholm. [Ekstedt Restaurant](https://ekstedt.nu/)

### Code

* Help with Bootstrap from their own [Documentation](https://getbootstrap.com/)
* Code from Christian Göran's project [Dome-Restaurant-Repo](https://github.com/christiangoran/dome-restaurant-repo)
* Code from Iasmina Pal's project [Italianissimo-Restaurant-Repo](https://github.com/useriasminna/italianissimo-booking-website)
* A lot of help was Code Institute's walkthrough study materials and projects themselves.

## Acknowledgements

- Code Institute for providing a great course.<br>
- My mentor David Bowers for helping me with questions and providing valuable tips through the project.<br>
- The Ekstedt Restaurant itself for providing great inspiration.<br>
