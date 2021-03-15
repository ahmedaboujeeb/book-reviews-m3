# Book Reviews

[Link to live website.](https://book-reviews-m3.herokuapp.com/)

Book Reviews is a website where users share thier reviews and what they think about books they've read. 

![Book reviews homepage](https://github.com/ahmedaboujeeb/book-reviews-m3/blob/main/screenshots/web/Screen%20Shot%202021-03-02%20at%2016.21.23.png)

## UX

[Link to screenshots](https://github.com/ahmedaboujeeb/book-reviews-m3/tree/main/screenshots)

### User Story

#### As a user

- Share you reviews on books you've read with other users
- Read other users' reviews
- Search for book reviews by genre, book name, author or review.
- Create a private account
- Log in and log out of your account
- Add reviews by adding the book name, the name of the author, a link to the book cover image and your review
- Edit or delete your reviews

![Reviews page](https://github.com/ahmedaboujeeb/book-reviews-m3/blob/main/screenshots/web/Screen%20Shot%202021-03-08%20at%2010.45.22.png)

## Features

- Navbar
- Sign up form
- Login form
- Search bar
- Read review
- Log out
- Add review form
- Edit review
- Delete review


## Technologies Used

- Programming languages: HTML, CSS, JavaScript, Python
- Frameworks: Flask, Jquery
- Database: MongoDB
- Code editor: Visual Studio Code
- Version control: GitHub, Heroku

## Testing

### Home page

- Click on 'Login' directs to login page
- Click on 'Sign Up' directs to Signup page

### Review page

#### Search functionality

- Click on search field
- Type in text and/or numbers in search field
- Click enter shows results
- Click enter with empty search field shows message "Please fill out this field" with no action
- Click on search button also shows search results
- Click on search button with empty search field will show message "Please fill out this field" with no action
- Click on search button with less than 3 characters shows message "Please lenghten this tex to 3 characters or more (you are currently using less than 2 character)" with no action
- Click on back to reviews button at any time directs you back to 'Reviews' page

#### Review card

- Click on 'Read Review' button redirects to the review page

### Signup page

- All fields are required, if one or more fields left empty it will be underlined in red
- Click submit with one or more fields empty, warning message shows "please fill our this field"
- If one or more fields have the wrong format or has less characters than required warning message will show
- Fill out all fields and click submit redirects you to 'Account' page, message will show "You are signed up!" and data will be stored in data base

![Sign up page](https://github.com/ahmedaboujeeb/book-reviews-m3/blob/main/screenshots/web/Screen%20Shot%202021-03-02%20at%2016.06.17.png)

### Account page

- Click on 'Add Review' redirects you to 'Add Review' page
- Click on 'Go to Reviews' redirects you to 'Reviews' page

### Login page

- If  User Name field left empty it will be underlined in red
- If Password field left empty it will be underlined in red
- Click Log in with User Name field empty, warning message shows "Please fill out this filed" 
- Click Log In with Password field empty, warning message "Please fill out this filed" 
- If one or more fields have the wrong format or has less characters than required warning message will show
- If username or password or both are incorrect or not registred "sigend up" error messgage shows "Username/Password incorrect"
- Fill out all fields and click Log In redirects you to 'Account' page, message will show "Logged In!" and you will be able to add reviews

### Add review 

- All fields are required, if one or more fields left empty it will be underlined in red
- Click Add with one or more fields empty, warning message shows "please fill out this field"
- If one or more fields have the wrong format or has less characters than required warning message will show
- Fill out all fields and click Add button will add review 

![Add review](https://github.com/ahmedaboujeeb/book-reviews-m3/blob/main/screenshots/web/Screen%20Shot%202021-03-02%20at%2016.05.47.png)

### Edit review 

- All fields are required, if one or more fields left empty it will be underlined in red
- Click Update with one or more fields empty, warning message shows "please fill out this field"
- If one or more fields have the wrong format or has less characters than required warning message will show
- Fill out all fields and click Update button will add review 
- Click on Back "Cancel" button redirects to review page

### Review page

- Click on back to reviews redirects you to reviews page
- Click on edit button redirects you to edit page
- Click on delete button, confirmation message pops up. Click "Ok" delets review, click "Cancel" cancels request

### Responsiveness

The website was tested using Google Chrome developer tools, and is responsive on the following devices:

 - Moto G4
 - Galaxy S5
 - Pixel 2
 - Pixel 2 XL
 - iPhone 5/SE
 - iPhone 6/7/8
 - iPhone 6/7/8 Plus
 - iPhone X
 - iPad
 - iPad Pro
 - Surface Dou

 The webiste was tested on the following browsers:
 - Google Chrome
 - Safari

### Navbar

- Click on 'Home' directs you to home page
- Click 'Reviews' directs to the reviews page
- Click on 'Login' directs to login page
- Click on 'Signup' directs you to signup page
- When Logged in click on 'Account' directs to account page
- When Logged in click on 'Add Review' directs to add review page
- When Logged in click on 'Log Out' logs you out and directs to 'Login' page

### Programming languages validation

- validator.w3.org
- CSS passed jigsaw.w3.org validator with no errors
- Python code is consistent in style and conforms to the PEP8 style guide.

## Deployment

### Local deployment

1. On GitHub, go to repository's main page [link](https://github.com/ahmedaboujeeb/book-reviews-m3)
2. Above the list of files, click Code
3. Clone using https and copy URL
4. Open terminal
5. Type "git clone" and then paste the URL https://github.com/ahmedaboujeeb/book-reviews-m3.git
6. Press Enter to create your local clone

### Heroku deployment

1. Log in to your Heroku account
2. Create a new app
3. In Setting go to Reveal config vars
4. Set the following variables:
  - IP = 0.0.0.0
  - MONGO_DBNAME = {Your MongoDB name}
  - MONGO_URI = {Your MongoDB URI}
  - SECRET_KEY = {Your secret key}
  - PORT = 5000
5. On your code editor create requirements.txt 
6. Creat a Procfile
7. Push changes to Git
8. Log in to Heroku from your terminal 
9. Add existing repsitories to Heroku 
10. Push changes to Heroku

## Credits

This project was inspired by Code Institute 

### Media

- Hero image was taken from pexels.com
- Social media Icons were taken from fontawesome.com and materializecss.com
- Theme was taken from materializecss.com
- Fonts taken from fonts.google.com

