
import streamlit as st
from flask import Flask, jsonify, request,render_template
# from pymongo import MongoClient
# from bson.objectid import ObjectId
app = Flask(__name__)
html ="""
<body>

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-padding w3-card" style="letter-spacing:4px;">
    <a href="#home" class="w3-bar-item w3-button">Ghadai's Web.........</a>
    <!-- Right-sided navbar links. Hide them on small screens -->
    <div class="w3-right w3-hide-small">
      <a href="#about" class="w3-bar-item w3-button">About</a>
      <a href="#menu" class="w3-bar-item w3-button">Projects</a>
      <a href="#contact" class="w3-bar-item w3-button">Contact</a>
    </div>
  </div>
</div>

<!-- Header -->
<header class="w3-display-container w3-content w3-wide" style="max-width:1600px;min-width:500px" id="home">
  <img class="w3-image" src="https://media.publit.io/file/bag_basudev.jpg" alt="Hamburger Catering" width="1600" height="800">
  <div class="w3-display-bottomleft w3-padding-large w3-opacity">
    <!-- <h1 class="w3-xxlarge">Le Catering</h1> -->
  </div>
</header>

<!-- Page content -->
<div class="w3-content" style="max-width:1100px">

  <!-- About Section -->
  <div class="w3-row w3-padding-64" id="about">
    <div class="w3-col m6 w3-padding-large w3-hide-small">
     <img src="https://media.publit.io/file/ABX/0W8A0250.jpg" class="w3-round w3-image w3-opacity-min" alt="Table Setting" width="600" height="750">
    </div>

    <div class="w3-col m6 w3-padding-large">
      <h1 class="w3-center">About Basudev</h1><br>
      <h5 class="w3-center">Backend developer</h5>
      <p>I am a backend developer with a year of experience in Python and web scraping. My passion for technology and software development began in college, where I pursued a degree in Information Technology. During my studies, I discovered my interest in backend development and honed my skills in Python programming.
      </p>
      <p>
      After graduation, I started my professional career as a backend developer at Confluex marketing Pvt Ltd and As a intern at IBM., where I have gained experience in developing and maintaining the server-side components of web applications. I have worked on several projects using Python's popular web frameworks like Django and Flask, building scalable and maintainable web applications and RESTful APIs.
      </p>
      <p>
      My experience with web scraping libraries like BeautifulSoup and Selenium has allowed me to extract data from web pages, automate web-related tasks, and build data pipelines, ETL processes, and data analysis tools. I have also designed and maintained databases using database management systems like MongoDB and PostgreSQL, creating and managing queries, and implementing database migrations.
      </p>
      <p>
      As a backend developer, I understand the importance of software development best practices, including version control using Git and code review processes. I have experience working collaboratively in a team environment, meeting project deadlines, and using Agile methodologies to ensure efficient, transparent, and collaborative development processes.
      </p>
      <p>
      In summary, I am a dedicated and skilled backend developer with experience in Python and web scraping, who continuously seeks to improve my skills and learn new technologies. I am excited about the possibilities of backend development and look forward to contributing my skills to new and challenging projects.
      </p>
      <!-- <p class="w3-large w3-text-grey w3-hide-medium">Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod temporincididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p> -->
    </div>
  </div>
  
  <hr>
  
  <!-- Menu Section -->
  <div class="w3-row w3-padding-64" id="menu">
    <div class="w3-col l6 w3-padding-large">
      <h1 class="w3-center"><a href="https://github.com/basudevghadai1999">Projects</a></h1><br>
      <h4>Library management system</h4>
      
      <p class="w3-text-grey">The Library Management System is a software application developed in Python that automates the basic processes of a library such as issuing books, returning books, adding new books, deleting books, etc. This project aims to create an efficient and user-friendly system that enables the library staff to manage the library's resources in a simple and organized way.

        The system comprises two modules: a user module and an administrator module. The user module is accessible to all library users, while the administrator module is reserved for library staff who manage the library's resources.
        Technologies and Tools:
        
        Python
        DynamoDb
        Tkinter GUI toolkit for creating the user interface
        Matplotlib for generating reports
        Conclusion:
        The Library Management System project aims to make library management more organized and efficient by automating the basic processes. The system's user module and administrator module are designed to be user-friendly and intuitive. By using this system, the library staff can manage the library's resources more effectively, and the library users can access the books they need more easily.</p><br>
    
      <h4>To Do List</h4>
      <p class="w3-text-grey">The To-Do Application is a Python-based command-line application that allows users to manage their daily tasks. It provides a simple and easy-to-use interface for users to add, delete, and update their tasks. The application also allows users to set due dates for their tasks and prioritize them based on their importance.

        Technology Stack:
        
        The To-Do Application is built using the following technologies:
        
        Python
        Flask
        AWS DynamoDB
        Conclusion:
        
        The To-Do Application is a useful tool for managing daily tasks. With its simple and easy-to-use interface, users can easily add, delete, and update their tasks. The application also allows users to set due dates for their tasks and prioritize them based on their importance. Overall, the To-Do Application provides a convenient way for users to stay organized and on top of their daily tasks.</p><br>
    
      <h4>Book review application</h4>
      <p class="w3-text-grey">The Book Review Application is a Python-based web application that allows users to read and write reviews of books. It provides a platform for book enthusiasts to share their thoughts and opinions on the books they have read. Users can search for books, read book details, and write reviews. The application also includes an admin panel for managing user profiles, books, and reviews.
        Technology Stack:
        
        The Book Review Application is built using the following technologies:
        
        Python
        Flask
        Flask-Login
        Flask-Admin
        DynamoDB
        Google Books API
        Project Deliverables:
      
        The Book Review Application is a great tool for book enthusiasts to share their thoughts and opinions on the books they have read. With its user-friendly interface and robust features, the application provides an engaging platform for users to discover new books and authors, and share their experiences with others.</p>    
        <h4>E vehicle web development</h4>
        <p class="w3-text-grey">This is a web base project developed for providing services to their clienct at diffrent
          places and also in emergency
          Worked as a backend developer for this web development project</p><br>
      
        <h4>Water level detector (static web)</h4>
        <p class="w3-text-grey">This project is used to detect the overhead tank water level ,ECR,UGR etc.
          Data stored from PLC to SQL server.
          I worked as a Backend developer for this static web.
          Technology used: python3,Django,SQL server in backed.</p><br>
      
        
    </div>
    
    <div class="w3-col l6 w3-padding-large">
      <img src="https://media.publit.io/file/bag_basudev.jpg" class="w3-round w3-image w3-opacity-min" alt="Menu" style="width:100%">
    </div>
  </div>

  <hr>

  <!-- Contact Section -->
  <div class="w3-container w3-padding-64" id="contact">
    <h1>Contact</h1><br>
    <!-- <p>We offer full-service catering for any event, large or small. We understand your needs and we will cater the food to satisfy the biggerst criteria of them all, both look and taste. Do not hesitate to contact us.</p> -->
    <p class="w3-text-blue-grey w3-large"><b>Bhubaneswar,Odisha 753010</b></p>
    <p>You can also contact me by phone +91-7008673226 or email ghadaibasudev1234@gmail.com or you can send us a message here:</p>
    <form action="/action_page.php" target="_blank">
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Name" required name="Name"></p>
      <p><input class="w3-input w3-padding-16" type="number" placeholder="How many people" required name="People"></p>
      <p><input class="w3-input w3-padding-16" type="datetime-local" placeholder="Date and time" required name="date" value="2020-11-16T20:00"></p>
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Message \ Special requirements" required name="Message"></p>
      <p><button class="w3-button w3-light-grey w3-section" type="submit">SEND MESSAGE</button></p>
    </form>
  </div>
  
<!-- End page content -->
</div>

<!-- Footer -->
<footer class="w3-center w3-light-grey w3-padding-32">
  <p>Powered by <a href="index.html" class="w3-hover-text-green">Basudev Ghadai</a></p>
</footer>

</body>
"""

@app.route('/')
def index():
    st.write(html, unsafe_allow_html=True)

if __name__ == '__main__':
    app.run()
