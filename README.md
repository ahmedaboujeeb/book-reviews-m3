# Book Reviews

[Link to live website.](https://book-reviews-m3.herokuapp.com/)

Book Reviews is a website where users share thier reviews and what they think about books they've read. 

## UX


### User Story

#### As a user

- Share you reviews on books you've read with other users.
- Read other users' reviews.
- Search for book reviews by genre, book name, author or review. 
- Create a private account.
- Log in and log out of your account.
- Add reviews by adding the book name, the name of the author, a link to the book cover image and your review.
- Edit or delete your reviews.


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

- HTML, CSS: used for the main website structure and styling.
- JavaScript: Jquery for collapsable navbar.
- Visual Studio Code: this whole project is done using VS Code.
- Font Awesome: social media icons were taken from fontawesome.com.
- GitHub: used to deploy and host this project.
- Heroku: used to deploy and host this project.
- Flask: 
- Materialize: the website theme is taken from materializecss.com as well as other features.


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

- Click on 'Read Review' button directs to the review page

### Signup page

- If First name field left empty it will be underlined in red
- If Last name field left empty it will be underlined in red
- If User name field left empty it will be underlined in red
- If Password field left empty it will be underlined in red
- Click submit with First name field empty, will show message "Please fill out this filed" with no action
- Click submit with Last name field empty, will show message "Please fill out this filed" with no action
- Click submit with User name field empty, will show message "Please fill out this filed" with no action
- Click submit with Pssword field empty, will show message "Please fill out this filed" with no action
- Fill out all fields and click submit redirects you to 'Account' page, message will show "You are signed up!" and data will be stored in data base

### Account page

- Click on 'Add Review' directs you to 'Add Review' page
- Click on 'Go to Reviews' directs you to 'Reviews' page

### Login page

- If  User Name field left empty it will be underlined in red
- If Password field left empty it will be underlined in red
- Click Log in with User Name field empty, will show message "Please fill out this filed" with no action
- Click Log In with Password field empty, will show message "Please fill out this filed" with no action
- Fill out all fields and click Log In redirects you to 'Account' page, message will show "Logged In!" and you will be able to add reviews

### Add review 

- If Genre field left empty it will be underlined in red
- If Book name field left empty it will be underlined in red
- If Author field left empty it will be underlined in red
- If Link to book cover field left empty it will be underlined in red
- If Review field left empty it will be underlined in red
- Click Add with Genre or/and Book name or/and Author or/and Link to book cover or/and Review field empty, will show message "Please fill out this filed" and no action
- Fill out all fields and click Add button will add review 


### Edit review form

- If Genre field left empty it will be underlined in red
- If Book name field left empty it will be underlined in red
- If Author field left empty it will be underlined in red
- If Link to book cover field left empty it will be underlined in red
- If Review field left empty it will be underlined in red
- Click Add with Genre or/and Book name or/and Author or/and Link to book cover or/and Review field empty, will show message "Please fill out this filed" and no action
- Fill out all fields and click Add button will add review 

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


### Bugs



## Deployment

### Deployed version

1. On GitHub, go to repository's main page [link](https://github.com/ahmedaboujeeb/book-reviews-m3)
2. Above the list of files, click Code
3. Clone using https and copy URL
4. Open terminal
5. Type "git clone" and then paste the URL https://github.com/ahmedaboujeeb/book-reviews-m3.git
6. Press Enter to create your local clone

### Developmment version



## Credits

