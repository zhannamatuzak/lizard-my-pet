# Lizard Is My Pet - Testing Documentation

## Manual Testing

### Testing User Stories

- Each completed user story on the [sprint backlog](https://github.com/users/zhannamatuzak/projects/1) was tested against the acceptance criteria, see the corresponding screenshots as evidence.
- This included reviewing each feature to check the usability, visual design and performance.


| Milestone | [Create the full Backend](https://github.com/zhannamatuzak/lizard-my-pet/milestone/1) |
------------|---------------------------------------------------------------------------------------|

| Epic    | [Full User Managment](https://github.com/zhannamatuzak/lizard-my-pet/issues/3)  |
----------|--------------------------------------------------------------------------------|

| Title | Number | Definition | Completed? | Label |
|-------|--------|------------|------------|-------|
| USER STORY: Log in | [#2](https://github.com/zhannamatuzak/lizard-my-pet/issues/2) | As a **USER** I would like to log in with the registration credentials. | [x] | Must Have |
| USER STORY: Registration  | [#1](https://github.com/zhannamatuzak/lizard-my-pet/issues/1) | As a **USER**, I would like to have a registration form with no need of email authentication, so I can start writing experiences right away. | [x] | Must Have |
| USER STORY: Log out | [#4](https://github.com/zhannamatuzak/lizard-my-pet/issues/4) | As a **USER**, I would like to be able to log out. | [x] | Must Have |
| USER STORY: USER STORY - Authorization | [#4](4) | As an **ADMIN**, I would like that the user must be authorized in order to write his/her experiences (comments) under the posts. | [x] | Must Have |

| Epic    | [Manage posts]()  |
----------|-------------------|

| Title | Number | Definition | Completed? | Label |
|-------|--------|------------|------------|-------|
| USER STORY: Log in | [#2]() | | [x] | Must Have |
| USER STORY: Registration  | [#1]() |  | [x] | Must Have |
| USER STORY: Log out | [#4]() |  | [x] | Must Have |


## Validation Testing

### [HTML W3C Validator](https://validator.w3.org/) 
As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Jinja templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.

| Page | Result |
| :--- | :--- |
| [Home Page](documentation/) | Pass |
| [Lizard Detail](documentation/) | Pass |
| [Edit Comment](documentation/) | Pass |
| [Sign up](documentation/)| Pass |
| [Login](documentation/) | Pass |
| [Logout](documentation/) | Pass |
| [Error 404](documentation/) | Pass |

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

| File | Result |
| :--- | :--- |
| **STEAMAND LEAF** |
| [stemandleaf/urls.py](documentation/) | Pass |  
| **BLOG** |
| [blog/views.py](documentation/) | Pass | 
| [blog/models.py](documentation/) | Pass | 
| [blog/forms.py](documentation/) | Pass |
| [blog/urls.py](documentation/) | Pass | 
| [blog/admin.py](documentation/) | Pass | 


## Visual (UI) Testing: Cross Browser and Cross Device Testing

- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers. Priority was given to mobile devices and tablets. 

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** | Passed 
|-----------------------------|------------------|---------|------------------|---------
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |
| dev tools: Samsung S8+      | Chrome           | android | 360 x 740 px     |
| real phone: Pixel 6         | Chrome           | android | 393 x 851 px     |
| real phone: iPhone 14 Pro   | safari           | iOs     | 390 x 844 px     |
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |
| real tablet: Pixel Tablet   | Chrome           | android | 834 x 1075 px    |
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |
| browserstack                | Edge 113         | windows | 1440 x 672 px    |

## Lighthouse

For the performance, accessibility, best practices and SEO of the site for mobile and desktop, [Page Speed](https://pagespeed.web.dev/) and the major pages were passed through the validation. 

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![image]() |
| Lizard Detail | ![image]() |
| Edit Experience | ![image]() |
| Delete Experience | ![image]() |
| Sign up |![image]() |
| Sign in | ![image]() |

- Desktop performed well on all major pages of the site with minimal improvements needed.

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![image]() |
| Plant Detail | ![image]() |
| Edit Comment | ![image]() |
| Delete Comment | ![image]() |
| Sign up | ![image]() |
| Login | ![image]() |

## Outstanding Defects
- There are no outstanding defects.


