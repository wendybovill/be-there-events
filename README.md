
# Milestone 3 Project: Back End Development


## Target Audience:

- Members of the public who are looking to advertise events for free.

- Members of the public who are looking for events, whether paid for or free, that are local to them.

- Charities that are looking to promote a charity event.

- Businesses who are looking to promote an event to Advertise their business, or product.


## Purpose: 

- To create a sense of community among members of the public. 
- To make available local recreational events or sponsored events from Charity or Businesses. 
- To enrich the lives of the public who are feeling they are lacking with community connection.
- To give members of the public more options to enjoy supervised recreational activities rather than get
  bored and create problems in their community.
- To encourage a sense of "togetherness" in the communities.

***This site will have:***

1. Home Page with a welcome message and brief outline of what the site is for.

2. Clear Navigation throughout, with a changeable menu depending on logged in or logged out users, and
   a different menu for admin user.

3. Options to view events for logged out users, and logged in users can add Events, add Event Types,
   Update their own Events or Event Types, as well as View and Update their own profiles..

4. Admin user who can view all members, edit all members profiles, and delete members.

5. Admin user who has access to all Events and Event Types to edit or delete if there are safety or
   moderation concerns.

6. A page confirming deleting Events, Event Types or Members before they can be deleted as the final step.

7. An email that gets sent to a user when signing up, to verify their email address. They need to follow
   the emails instructions and click the link that launches the internet browser where they have to input
   their email address and password to log in.

8. The option for a non-member to send an email to the admin. This requires the user to enter their email
   address, name, and message.

9. The option for a member to send an email when logged in, they don't need to enter anything other than
   their message to the admin. Other info is automatically added to the email as its submitted.

10. Page filtering to ensure only logged in users can see certain things, and protection for events,
    event types, and profiles to make sure other users who are not authorised, cannot edit, delete, or
    update things they did not create and does not belong to them.

11. Error handling to cover user data protection, as well as various http errors.

12. A search function that creates a fresh index each time its run. It will have a timer so that if
    a search has ended, and there is no other search performed within 120 seconds, the index is dropped.
    This allows for a users freshly added event to display in the search as soon as its created.
    Otherwise if a user searches for their freshly created event, it would not show in the pre-existing
    index if an index is only created once. Creating and dropping the event when a search is completed
    allows for users new events to show and other users to find the new events as they are added.

13. A log out confirmation before a user is logged out.


## User Stories:

| User ID 	| Type         	| User Story                                                                                                                                                                                                                                                                                                                                                  	| Case Use                                                                                                                                                                                                                                                                                          	|
|---------	|--------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 1       	| Personal     	| **Mandy**<br>A Student App used with friends to<br>test general knowledge on health and anxiety. Is<br>looking for help with managing her anxiety. Finds<br>she did not know as much as she thought and is<br>determined now to find out more about managing her<br>physical health and to help improve her anxiety.                                        	| I would use the Quiz to gain an understanding of<br>much a know about physical<br>health and its effect<br>on my moods.<br><br>Its fun to test my knowledge<br>and its a simple quiz to play when I'm bored also.                                                                                 	|
| 2       	| Personal     	| **Jason**<br>A young adult in university.<br>Battling with insomnia and decided to do some<br>research on how to improve his health to see if it<br>would have an effect on his insomnia. He found the<br>app on the resonate site and decided to give it a go.                                                                                             	| Its made me realise that there are things I<br>can do to improve my mental health, which would<br>help reduce my insomnia. Inspired by the Quiz,<br>I decided to do some more exercise to help<br>regulate my energy levels and moods, as well as<br>to improve my diet, less sugar and caffeine. 	|
| 3       	| Business     	| **Sarah Personal Fitness Trainer**<br> Sarah was<br>referred to the app by her collegues. She discovered<br>its a useful tool to use with her clients, and has<br>helped remind her about the effect diet has on mental<br>health, in addition to exercise.                                                                                                 	| My clients are very greatful for the Quiz App which<br>I get them to complete in our first session.<br><br>It helps them realise that to take care of their body<br>is to take care of them mental health too.                                                                                    	|
| 4       	| Business     	| **Resonate Wellbeing Organisation**<br>Resonates<br>Anxiety website has used the app for their visitors,<br>as a means to engage with them and raise awareness of<br>the importance of tools and other resources in<br>managing mental health.                                                                                                              	| We are delighted with the development of this App<br>and our clients have given great feedback. Our<br>clients have often completed the quiz more than once.                                                                                                                                      	|
| 5       	| Organisation 	| **GP Doctors Surgery**<br>Uses this App for their<br>patients. They are able to download it via a QR code<br>on a poster in their surgery and from their website.<br>It has inspired their patients to do more for<br>themselves and ask for advice in realtion to diet and<br>mental health, rather than just asking for pills to<br>manage mental health. 	| Our practice clients are delighted with this App.<br>It has increased awareness of the importance of diet<br>and exercise in maintaining mental health". Our GP's<br>feel this is helping them manage their patients better.                                                                      	|



## Technology Requirements:

Html
Css
MaterializeCss (included in script and style links)
Gitpod
VS Code
Git Repository
JS Query
Favicons (as pngs and linked in styles in html head section)
FontAwesome
Python
Various Python Modules:
    blinker==1.6.2
    click==8.1.3
    dnspython==2.3.0
    Flask==2.3.2
    Flask-Ext==0.1
    Flask-Mail==0.9.1
    Flask-PyMongo==2.3.0
    ipywidgets==8.0.6
    itsdangerous==2.1.2
    jupyter==1.0.0
    jupyter-console==6.6.3
    jupyterlab-widgets==3.0.7
    pymongo==4.3.3
    qtconsole==5.4.3
    QtPy==2.3.1
    Werkzeug==2.3.4
    widgetsnbextension==4.0.7
Jinja Template
Mongo Database
Heroku
Adobe Illustrator to create the Favicon image
Pexels.com for the free image used on the site
Balsamiq for Wireframes
Lucid Charts for the Site Blueprint (Flowchart Diagram)
Microsoft Excel to create the usercases that are then uploaded as CSS to convert to MD Tables
MD Table converter
Favicon Converter
Chrome, Firefox, Safari
Ipad, Iphone, Macbook for testing
Windows, Android phone for testing
Selenium Extension in Browser and installed in VS Code with NPM to translate .side files


## Development Process:  

*Development Method:*

After receiving technical specification and design requirements, wireframe was created in Balsamiq.
The Html and CSS were created for the templates to, the base template was created using Jinja template.
Each html page was created as the python functions and routes were created requiring that view.
CSS was modified on an ongoing basis in accordance with relevant view being developed.
CSS was designed with Mobile First approach, allowing for larger screens responsiveness as a last
modification requirement. Text across the site is scaled in accordance to the size of the viewing device.

Javascript was adjusted only within the queries. The functions for styles were taken from the
MaterializeCSS requirements and modified as required in the instructions.
Research was done on StackFlow, and WC3 and many other sites, as well as using some code inspired
from the CI modules. Function planning and route planning took place before routes were developed.
These were planned on paper (I prefer working on paper for planning). Database Schema was also
planned on paper. Please see attached document: Plans.

The basic variables were setup based on my rough sketches and page flows. forms were planned and
implemented in accordance with the required routes, where necessary also passing the variables
required into the routes (such as username, error code, user id, type id, etc). 

Emails sending functions and templates were created in the App file after the other basic site functions.
The search parameter was created after the emails and required further research in flask documentation
and Mongo Database Documentation to ensure I did it correctly. I also looked into Python documentation
to support my functions being correct, ensure the syntax was correct, as well as understand how the
timer function works which I then implemented in my timer function within the search index creation 
and search index dropping.

I tested right throughout using the problems raised within the Gitpod Visual Code workspace terminals, as
well as using debug with Werkzeug indicating the errors and the error causes. This allowed me to 
correct code as I was writing throughout, I was testing on the live server. This was up until
the emails were needing to be tested. I could not do this within the Gitpod environment, it kept 
timing out. So I then had to deploy to Heroku to test the email sending correctly. I used my own
host company called "Wideworldwebhosting.co.uk" to create an email address and email routes.
I used the configuration from this in creating the requirements in the settings in the app for
sending emails. I also added these to Heroku in order to test the email sending. These gave no issues.
Sending emails and clients (as well as the admin) receive emails.

Emails are sent to the client with the information they have sent to the admin.
Emails confirming Sign up are sent to the client, as well as emails asking the user to verify their
email address are sent to the client and received by the client. 

After this I continued to work in the gitpod environment testing and debugging when sending to the 
live server that comes with Gitpod. However, whenever an email required to be sent I had to re-deploy
the code to Heroku to use the updated code and test on Heroku. Testing was performed manually.

At the end of the Development, before final testing the code for CSS and html was again put through
the respective validators at W3 Validator and Jigsaw. Errors were identifed and fixed where necessary. Notes were
created of the errors and added to the debugging md file. There were numerous errors with MaterializeCSS third
party extension, however these I have left as they are not within my remit. They are not causing any
site errors or errors within my code. 

Throughout the development process, handwritten notes were made, serving as a 'To Do List' of what
needs to be done and then ticked off when completed. These are available as photographs in notes.md

Handwritten notes forming part of development and testing:
[https://github.com/wendybovill/quiz-project/blob/cf7fefcbdea1a41fa06a9813784a2cf11f4629cb/documentation/handwritten_notes.md](https://github.com/wendybovill/quiz-project/blob/cf7fefcbdea1a41fa06a9813784a2cf11f4629cb/documentation/handwritten_notes.md)
	

## Site Design Process

1. Content:

Identified a user need within the community to provide an event list facility online for users to engage
with and add to or utilize to determine which events are available that they can attend or for others to
attend. The site was designed with a target audience who is looking for excitement and to create a mystery
and a sense of excitement "Deep Purple" colourscheme was chosen. The image used was from the Pexels.com 
website and free to use. It is chosen for the excited, party, vibrant and fun atmosphere it conveys.
The rest of the site, for example forms are plain and do not distract from the events or buttons which 
are coloured to match their functions. Red is caution about deleting something. A confirmation dialog is
made available to prevent accidental deletion. The content is based on user input. Example events and
test events have been created, as has example event types and test event types. Users can search for
events by name, type, town, postcode and if its free.


2. Design: 

**Site Specification and Website Flow:** Documentation for Website Planning. 




**Wireframe with Balsamiq:**

| Desktop Mockup | Iphone Mockup |
|----------------|---------------|
| ![Balsamiq Wireframe]()     |  ![Balsamiq Wireframe 2]()     |

	

	*Logo:* Formito.com Free Favicon Maker

	*Colours:* Purple, Teal, and Navy, with white and grey as a base. 
	(Colour symbolism: Purple: Mystery, Teal: Excitement and freshness, Navy: As a blue tone conveys serenity).


3. 	Documentation including readme file, spec sheet. Estimated time 1 week.

4. 	Development strategy: Develop the base page and styles, that then will be used as a template for the
	rest of the site pages. View plans are create, then the Route plan to match the Views. 
    The code for the Routes are determined by the Views required. The Database Schema is created based on the
    functionality plan and routes required.


## Design Variation:
The site has extra features added which are not in the original mockups/wireframes, which were a simple design
of the layout of the site. The Site Blueprint (Flowchart) determines the Views required and the site flow for
tiered authenticated access.


## Future Development:

1. Add an email update function and view to require the user to re-verify their newly updated email.

2. Add a password reset function and view so if a user forgets their password they get sent an email
   to reset their password.

3. Add a username forgotten function and view so if a user forgets their username they get sent an email
   for them to be reminded what their username is.

4. Change the login form and (functions and routes) to enable members to login with either username or email.

5. Add route, view and functions to enable a user to upload an image to their event.

6. Add a route, view and functions to enable a user to upload a profile picture if they wish.

7. Set the front page to display the next event in a section and also to display a section showing the latest
   event added.
	

# Acknowledgements

- Stackflow for help with Javascript and CSS where required,where information was read and then
  interpreted and applied to the requirements of the site and functions required for the actions
  necessary:<br>
	  - To plan out what functions to use and streamline them rather than bulky functions.<br>
	  - Further information on shortening functions and syntax used.<br>
	  - Information on how to write to the local storage.<br>
	  - Information on editing the api to create one for the questions and answer content.<br>
	  - Information in adding and removing classes.<br>
	  - Information in switching question and answers and indicating which ones are correct or not.<br>

- Markdown table generator used: https://www.tablesgenerator.com/markdown_tables

- CSS various sites used to assist in getting information on using a gradient as the background, using
  using unconventional positioning and resizing, which the validator complains of, but it works rather 
  than not working without these parameters.


# Debugging & Test Results:

**TEST CASES:**

Test Cases:
[https://github.com/wendybovill/test_cases.md](https://github.com/wendybovill/test_cases.md)

WC3 Validation and CSS Jigsaw:
https://github.com/wendybovill/.pdf

https://github.com/wendybovill/.pdf



**SCREENSHOTS of Debugging, error fixing and troubleshooting:**

Pdf showing testing screenshots:
https://github.com/wendybovill/Testing_screenshots.pdf


*Debugging:* 

Document of validation and errors can be viewed by clicking on the link below:
[https://github.com/wendybovill/Validator_tests.md](https://github.com/wendybovill/Validator_tests.md)


Handwritten notes forming part of development and testing:
[https://github.com/wendybovill/handwritten_notes.md](https://github.com/wendybovill/handwritten_notes.md)


*References used to assist debugging:*

- W3 schools html validator: http://validator.w3.org

- W3 schools jigsaw css validator: http://jigsaw.w3.org

- Werkzeug showing errors in debugging process

- Regular commits were made throughout the process to github as deployed early to use gitpod for testing
  (problems detected in the terminal were then corrected)

- Python documentation, Flash documentation


## Screenshots of Index page from finished site - Desktop View

| Screenshot showing first part of Index Page Finished Site |
|-----------------------------------------------------------------------|
| ![Finished Site Desktop Index Page](https://github.com/wendybovill/.png)|
| Screenshot showing second part of Index Page Finished Site Desktop View  |
| Finished Site Screenshots MD file [https://github.com/wendybovill/Finished_Site_Screenshots.md](https://github.com/wendybovill/Finished_Site_Screenshots.md)|


