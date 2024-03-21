# Restaurant Ekstedt Booking System Testing Documentation

## Summary

This document outlines testing procedures that was used during the development of the project for the Ekstedt Restaurant Website. It includes the manual testing steps, expected outcomes, and references to automated test where applicable.

## Table of Contents

* [Testing](#testing)
    + [1. Base Setup](#base-setup)
    + [2. Stand Alone Pages](#stand-alone-pages)
    + [3. Authentication](#authentication)
    + [4. Contact](#contact)
    + [5. History](#history)
    + [6. Menu]
    + [7. Bookings ]
    + [8. Deployment]
    + [9. Documentation]

---

## Testing
### 1. Base Setup <a name="base-setup"></a>
#### 1.1 Check the layout

**Manual Steps:**

1. Open the website.
2. Navigate through the website's different pages and observe the layout.

**Acceptance Criteria:**

- The base layout should be consistent accross different pages.

**Automated Tests:**

- None

**Outcome:**

- Pass

---

#### 1.2 Static Resources

**Manual Steps:**

1. Open the website.
2. Check the images, CSS, and JavaScript are loading correctly.

**Acceptance Criteria:**

- The resources should load without errors.

**Automated Tests:**

- None

**Outcome:**

- Pass

---

#### 1.3 Navigation Menu

**Manual Steps:**

1. Open the website.
2. Check if navigation is visible on all pages.

**Acceptance Criteria:**

The navigation must be functional and seen on all pages.

**Automated Tests:**

- None

**Outcome:**

- Pass

### 2. Stand Alone Pages <a name="stand-alone-pages"></a>

#### 2.1 Implement a 404 Page.

**Manual Steps:**

1. Open the website.
2. Navigate to a non-existent URL.

**Acceptance criteria:**

- A custom 404 page error should be displayed.

**Automated tests**

- None

**Outcome:**

- Pass

#### 2.2 Implement a 500 Page.

**Manual Steps:**

1. Set DEBUG = False.
2. Create a temporary trigger error function in views.py.
3. Add a trigger-error pattern in urls.py .
4. Visit localhost and /add trigger-error.
5. Revert changes.

**Acceptance criteria:**

- A custom 500 page error should be displayed.

**Automated tests**

- None

**Outcome:**

- Pass

#### 2.3 Implement a 403 Page.

**Manual Steps:**

1. Open the website.
2. Try to access a restricted page without appropriate permissions.

**Acceptance criteria:**

- A custom 403 page error should be displayed.

**Automated tests**

- None

**Outcome:**

- Pass

---

#### 2.4 Implement a Home Page.

**Manual steps:**

1. Open the website.
2. Check if the home is accessible and displays the content.

**Acceptance criteria:**

- Home page should be functional and display relevant information.

**Automated tests:**

- None

**Outcome:**

- Pass

### 3. Authentication <a name="authentication"></a>

#### 3.1 User Account Creation

**Manual Steps:**

1. Open the website, and go to "Register" page.
2. Fill out the form and submit.

**Acceptance Criteria:**

- User should be able to successfully to create an account.

**Automated tests:**

- None

**Outcome:**

- Pass

---

#### 3.2 User Login

**Manual Steps:**

1. Open the website and go to the 'Login' page.
2. Enter the username and password.

**Acceptance Criteria:**

- User should be able to login successfully.

**Automated tests:**

- None

**Outcome:**

- Pass

---

#### 3.3 User Logout

**Manual Steps:**

1. Login to the website.
2. Click the 'Logout' button.

**Acceptance Criteria:**

- User should be logged out successfully.

**Automated tests:**

- None

**Outcome:**

- Pass

### 4. Contact <a name="contact"></a>

#### 4.1 View the contact information

**Manual Steps:**

1. Open the website and go to "Contact" page.
2. Locate the contact information.

**Acceptance Criteria:**

- User should be able to see the contact information.

**Automated tests:**

- None

**Outcome:**

- Pass

#### 4.2 View the location information and opening hours

**Manual Steps:**

1. Open the website and check the footer.
2. Locate the contact information and opening hours.

**Acceptance Criteria:**

- User should be able to see the contact information and opening hours.

**Automated tests:**

- None

**Outcome:**

- Pass

#### 4.3 View the history information

**Manual Steps:**

1. Open the website and the "history" page.
2. View the story of Ekstedt.

**Acceptance Criteria:**

- Should be able to read the history of Ekstedt.

**Automated tests:**

- None

**Outcome:**

- Pass´

#### 4.4 Menu page

**Manual Steps:**

1. Navigate to the "menu" page.
2. Locate the content and see if there is a hyperlink leading to external website.

**Acceptance Criteria:**

- User should be able to see content and hyperlink.

**Automated tests:**

- None

**Outcome:**

- Pass

### 5.Bookings <a name="bookings"></a>

#### 5.1 View list of reservations as regular user

**Manual Steps:**

1. Log in as regular user.
2. Go to "Bookings" page from the nav.
3. Check the displayed table of bookings.

**Acceptance Criteria:**

- User should the list of all their bookings.

**Automated tests:**

- TestBookingList

**Outcome:**

- Pass

#### 5.2 View list of reservations as a staff user

**Manual Steps:**

1. Log in as staff user.
2. Go to "Bookings" page from the nav.
3. Check the displayed table of bookings.

**Acceptance Criteria:**

- User should the list of all todays bookings and future bookings.

**Automated tests:**

- TestBookingList

**Outcome:**

- Pass

#### 5.3 Update a booking

**Manual Steps:**

1. Log in as a user.
2. Go to "Bookings" page from the nav.
3. Select a booking to update.

**Acceptance Criteria:**

- User should be able to update their booking details.

**Automated tests:**

- TestUpdateBooking

**Outcome:**

- Pass

#### 5.4 Delete a booking

**Manual Steps:**

1. Log in as a user.
2. Go to "Bookings" page from the nav.
3. Check the displayed table of bookings.
4. Delete a booking.

**Acceptance Criteria:**

- User should be able to delete on of their bookings.

**Automated tests:**

- TestDeleteBooking

**Outcome:**

- Pass

#### 5.5 Staff is capable of confirming or rejecting a booking

**Manual Steps:**

1. Log in as staff user to the admin interface.
2. Go to "Bookings" page from the list.
3. Confirm or reject a booking.

**Acceptance Criteria:**

- Staff should be able to confirm/reject a booking from admin interface.

**Automated tests:**

- None

**Outcome:**

- Pass

#### 5.6 Select Time and Date for Booking

**Manual Steps:**

1. Log in as a user.
2. Go to "Bookings" page from the nav.
3. Create a new booking.
4. Select date and time.

**Acceptance Criteria:**

- User should be able to choose a date then select a time. While getting the relevant errors shown in case of invalid choices.

**Automated tests:**

- TestBookingList

**Outcome:**

- Pass

### 6.Deployment <a name="deployment"></a>

#### 6.1 Deploy to Heroku

**Manual Steps:**

1. Commit all changes to the repository
2. Push to heroku remote.
3. Open heroku link to confirm the deployment.

**Automated tests:**

- None

**Outcome:**

- Pass

---

### 7. Testing

#### 7.1 Write automated tests and testing documentation

**Manual Steps:**

1. Write automated tests covering key functionalities.
2. Document these tests in `testing.md`.

**Acceptance Criteria:**

- Sufficient automated tests should be written and documented.

**Automated tests:**

- None

**Outcome:**

- Pass

---

### 8. Readme

#### 8.1 Write readme documentation

**Manual Steps:**

1. Write readme documentation.
2. Document the project's setup, features and functionalities in `README.md`.

**Acceptance Criteria:**

- Readme.md should be comprehensive and informative.

**Automated tests:**

- None

**Outcome:**

- Pass

## Browser Testing
The website was tested on different browsers for assuring the features work accordingly.
* Google Chrome
* Microsoft Edge
* Opera

## Code Validation
### HTML