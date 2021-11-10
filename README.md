
## SPM-Learning Management System
LMS is an online learning platform that helps businesses enhance their Training & Development programme for their employee as it allow users to attend a course from the comfort of their own home and gain the necessary knowledge that is needed for their job.

### Getting started
You need to have certain tools and packages installed in order to run the application.

Following the steps below from the prerequisites till the end of the installation guide is necessary in order for the application to run smoothly.

### Prerequisites
Python 3.9 or later (https://www.python.org/downloads/)
Node.js (https://nodejs.org/en/download/)
WampServer (https://www.wampserver.com/en/)
Visual Studio Code (https://code.visualstudio.com/download)

### Setting up

Setting up the local database
1. Start up WampServer
2. Launch your browser, type localhost/phpmyadmin in the address bar.
3. Enter the username: root, leave the password field blank and login.
4. Click on "Import" located on the top navigation bar, choose file and locate the lms.sql file. Click "Go" to execute the SQL statement.

Installing the necessary packages
1. Open Visual Studio Code
2. Click on "File" > "Open Folder" and locate the LMS folder, and open it.
3. Click on Terminal > New Terminal. In the Terminal, ensure you are in the same folder as the requirements.txt, type: "pip install -r requirements.txt"

### How to run the application
Running the application locally
1. Start up WampServer
2. Open Visual Studio Code, then open the LMS folder.
3. Open a new terminal (Terminal > New Terminal) within VS code.
4. Within the terminal, navigate to server/app folder (cd server/app), then type python app.py to start the backend server.
5. Now navigate to the spm-app folder in the terminal, then type "npm start" to start the Node.js server which will host your frontend.
6. If you have problem starting up the Node.js server. Type "npm install" in the terminal and try again. Make sure you are in the spm-app folder

### Tools used to build the app
1. Flask is a backend web framework written in Python. It provides us the ability to create various endpoints for the frontend to make API calls to perform different operations.
2. ReactJS is frontend JavaScript library used to build our frontend page. It allows us to build reusable UI components that allows us to drastically reduce the lines of codes and reduces the need to reload an entire page when there is a change of state/data.
3. MySQL is a relational database management system used to store our data.


### Functionalities

#### Learner
View Course Catalogue - Learners have the ability to browse the course catalogue to view the various course offerings the learning management system provides.

View Prerequisite Courses - Certain courses have prerequisite course(s) that learners need to complete before enrolling. Learners are able to view the prerequisite courses for a specific course in the course catalogue.

Self Enrolment - Learners are able to enroll themselves to a class to take their desired course.

Search course - Learners can utilize the search function to filter   specific courses based on course title. This provides a more pleasant experience for the users when browsing for courses.

View Enrolled Class - Learners who are enrolled to a class can view information about the class. Specifically the course being taught, and what are the learning objectives of the said course.

View Curriculum - Learners who are enrolled to a class can view the curriculum for a particular class. Information includes the lessons, the course material(s) for each lesson, their progression status and quiz score for each lesson, as well as their final exam score.

Mark Lesson As Complete - Learners can mark a lesson as complete in the curriculum page so that they are able to progress to the next lesson.

Take Quiz - Learners can take a quiz for each lesson, and a final quiz for the course. They will be given a limited time to complete the quiz. The quiz questions can come in the form of MCQ or True/False.

#### Admin
View list of available courses - The admin can view an exhaustive list of courses, with each course showing the different classes, and each class showing information such as the start date, end date, start time, end time, trainer name and the class size.

Search course - The admin can search for a course based on the course title to filter courses that they want to see. 

View classlist - The admin can view the list of students for a specific class. Information of each student includes the name, role, department, and designation.

Remove trainer from a class - The admin can remove an assigned trainer from a class.

View list of trainers - The admin can view a list of trainers. Information of each trainer includes the name, role, department and desgination. 

Assign trainer to a class - From the list of trainers, the admin can select a trainer and assign that trainer to a class.

View list of eligible learners - For a specific class, the trainer can view a list of learners who are eligible to enroll for that class.

Enroll learner to a class - From the list of eligible trainers for a class, the admin can select a learner and enroll that learner to the class.

View list of classes without trainer - The admin can view a list of classes that do not have an assigned trainer.

Set self-enrol date for classes - The admin can set the self-enrol start date and end date for a class. 

View list of enrolment application - The admin can see a list of learners and the course and class they applied to enroll to, with the option to approve or reject their enrollment application.

Approve/Reject Enrollment - From the list of enrolment applications, the admin can approve or reject them.

#### Trainer
View list of assigned classes - The trainer can view a list of classes he is assigned to teach. Information about each class includes the course name, start and end date of the class, the timing of the class and total capacity. 

View classlist - The trainer can view the list of students for a specific class. Information of each student includes the name, role, department, and designation.

View assigned class - Trainers who are assigned to a class can view information about the class. Specifically the course being taught, and what are the learning objectives of the said course.

View class result - Trainer can view a list of students for a specific class, and for each student, the trainer can see a breakdown of their quiz scores across different lessons, as well as the course final quiz score

View uploaded quiz - Trainer can view a quiz that they have created and uploaded, in edit mode. 

Set Quiz Duration - Within the quiz creation or existing quiz view, he/she can set the time limit of the quiz.

Assign Quiz to Lesson - Within the quiz creation or existing quiz view, he/she can assign the quiz to a specific lesson of a class.

Assign Quiz as a Final Quiz of a Course - Within the quiz creation or existing quiz view, he/she can assign the quiz to be a final quiz of a course.

Set Quiz Name - Within the quiz creation or existing quiz view, he/she can set the title of the quiz.

Add a Question - Within the quiz creation or existing quiz view, the trainer can add a Multiple Choice or True/False question for that quiz.

Remove Question - Within the quiz creation or existing quiz view, the trainer can remove an existing question from the quiz.

Edit Question - Within the quiz creation or existing quiz view, the trainer can edit an existing question and save it.

Add Quiz Option - Within each quiz question, the trainer can add an option with a value and indicate whether that option is a correct answer, and save it.


### Authors
- Lee Shun Hui 
- Chua Zihui Trisha
- Ong Chuen Kai
- Yeo Yao Cong 
- Darren Ho Shu Hao