
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

| USER 	| TYPE 	| CASE 	|
|---	|---	|---	|
| Janet 	| Student 	| "My friends and I are often saying we don't know what to do. It is great to have a website that lists everything that’s on. We can search for free events too which is what we need since we are students. We would recommend this to our friends<br>as its something we all need to have so we don't end up bored with nothing to do."  	|
| Max 	| Student 	| This is such a good idea. We are often bored in the holidays and all our friends could be anywhere else in the country due to living away from home at Uni. I find we are sometimes at a loose end. We don't want to just hang out at a pub all the time. Its good knowing whats on and when and where.  	|
| John T 	| Business 	| I'm so glad we have finally got somewhere we can advertise to promote our business events in for free. We sometimes have events for promotions and as a business we've been struggling since Covid19 shut everything down. We are all really feeling the pinch from Cost Of Living. So something like this gives us a free platform to promote our business and give back to the community at the same time.  	|
| Sandra 	| Charity 	| "We run the local charity shop for Cancer awareness. We are so happy we can advertise our events locally to draw people in who can either get involved in sponsored runs and marathons or who can donate to the cause. This website is exactly whats needed to boost our communities since Covid19. Facebook used to be able to do that but now they charge for everything. So being able to have a central free place to look is what we've needed."  	|
| Pete 	| Organisation/Club 	| As an organisation its been hard to get younger members recruited. Now we can advertise our events for free in the community and get more young people and families involved. People often don’t know what fly fishing is. We've been asked all sorts of thing when its mentioned. Now we can promote our sport and our club and hopefully get some new members to join up soon.  	|



## Technology Requirements:

Html<br>
Css<br>
MaterializeCss (included in script and style links)<br>
Gitpod<br>
VS Code<br>
Git Repository<br>
JS Query<br>
Favicons (as pngs and linked in styles in html head section)<br>
FontAwesome<br>
Jinja Template<br>
Mongo Database<br>
Heroku<br>
Adobe Illustrator to create the Favicon image<br>
Pexels.com for the free image used on the site<br>
Balsamiq for Wireframes<br>
Lucid Charts for the Site Blueprint (Flowchart Diagram)<br>
Microsoft Excel to create the usercases that are then uploaded as CSS to convert to MD Tables<br>
MD Table converter<br>
Favicon Converter<br>
Chrome, Firefox, Safari<br>
Ipad, Iphone, Macbook for testing<br>
Windows, Android phone for testing<br>
Python<br>
Various Python Modules:<br>
-   blinker==1.6.2<br>
-   click==8.1.3<br>
-   dnspython==2.3.0<br>
-   Flask==2.3.2<br>
-   Flask-Ext==0.1<br>
-   Flask-Mail==0.9.1<br>
-   Flask-PyMongo==2.3.0<br>
-   ipywidgets==8.0.6<br>
-   itsdangerous==2.1.2<br>
-   jupyter==1.0.0<br>
-   jupyter-console==6.6.3<br>
-   jupyterlab-widgets==3.0.7<br>
-   pymongo==4.3.3<br>
-   qtconsole==5.4.3<br>
-   QtPy==2.3.1<br>
-   Werkzeug==2.3.4<br>
-   widgetsnbextension==4.0.7<br>


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

*Database Schema:*

The database schema was designed after deciding what the site functionality should be like.
Once the views were identified, it was decided what each users would need for the views to operate correctly, portraying the correct information to each user, and this helped decide what routes were needed and therefore the functions to call and operate the routes and views by the user requirements.
This is a non-relational database using Mongo DB. The Schema fit into 3 main tables, being: Users, Events and Event Types. A search index gets created in the Events Table to search for Events using keywords gathered from Event title field, Event type field, Is_paid_for field to search for Free or paid, Event_location_town, and Event_location_postcode. Each time a search is performed, a datbase is created, it is dropped 2 minutes (120 seconds) after the last search is performed. This allows the user to get the newest events that have been created, within the results of the search they ran.
Users are only allowed to edit their own events and event types, and as a result we have an 'added_by' field in the Event Types tables and in the Event tables.

Handwritten notes forming part of development and testing:
|
| Code Function Prep 	| Database Schema Plan 	|
|---	|---	|
| ![Code Prep](https://github.com/wendybovill/milestone-project-3/blob/7d03ced489b6a8c47be530662bf45bbe167a2cea/documentation/IMG_6266.png) 	| ![Database Schema](https://github.com/wendybovill/milestone-project-3/blob/791bc2d59c3df3ae01b7da2dbb14a9cbfe9cf304/documentation/IMG_6267.png)  	|


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


**Wireframe with Balsamiq:**

| Mockups |
|----------------|
| ![Balsamiq Wireframe](https://github.com/wendybovill/milestone-project-3/blob/05c8f408e4f5559092d70e072df660f56bf10867/documentation/screenshots/P3-wireframe.png)     |

	*Logo:* Bee in Purple and White Stripes (Creative Licence) used Illustrator to design and Formito.com Free Favicon Maker to convert to favicon

	*Colours:* Purple, Teal, and Navy, with white and grey as a base. 
	(Colour symbolism: Purple: Mystery, Teal: Excitement and freshness, Navy: As a blue tone conveys serenity).


3. 	Documentation including readme file, spec sheet. Estimated time 1 week.

4. 	Development strategy: Develop the base page and styles, that then will be used as a template for the
	rest of the site pages. View plans are create, then the Route plan to match the Views.

5.	The code for the Routes are determined by the Views required. The Database Schema is created based on the
	functionality plan and routes required.

6. Blueprint


   **Blueprint and Website Flow:** Documentation for Website Planning. 
![Site Flow Chart Blueprint](https://github.com/wendybovill/milestone-project-3/blob/b4af1a3ed763165c7f955c41618f19f32c66113a/documentation/screenshots/Project_3_Blueprint.png)


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


# Deployment Process / Re-Deployment Process

|  	| DEPLOYMENT PROCESS / REDEPLOYMENT PROCESS 	|
|---	|---	|
| 1 	| As part of the development process varioius dependencies were installed. The first step is to ensure these are added to "requirements.txt".<br>In the terminal in your work environment, run this command: "pip3 freeze > requirements.txt" 	|
| 2 	| If you don't already have a Procfile, then you need to create one in the root directory, create a new file called Procfile (with no extension on the<br> end). Inside this file type echo web: python run.py 	|
| 3 	| Ensure that in the .gitignore file env is listed to be ignored. 	|
| 4 	| In workspace, in app.py ensure debug is set to false 	|
| 5 	| Go to Heroku and login using creditentials supplied in separate file, otherwise if not already setup for Heroku you will need to register and follow<br> that process. Once signed in, you need to go to either create a new app or go to the corresponding app created. Go to "Deploy" tab, <br>and add in your respository url from github repository.  Then go to the tab "Settings". In settings go to Vars and add in the information that <br>needs to be hidden from public view such as the following: Secret_Key, Database url and database password, Database name and port, <br>Email host IP, Email username, Email Passwords, Email port used, SSL/Tls etc. All the variables that would be required for the database and <br>any other email or other host systems to connect to the App. 	|
| 6 	| Ensure the vars you have entered match up with what has been required in the env file that is being ignored by .gitignore file, once you have<br> verified you have all of these set up. In the terminal do Git add . (to add all files, include the fullstop), git commit -m "commit message here" and <br>then finally do git push. Once the final changes are pushed to github, go to heroku, and in the tab "Deploy" select the branch to be deployed <br>(from githup) and select Deploy Branch. Then in Heroku, top right corner, under "more" select view logs, and ensure there are no errors in <br>the logs. If there are, then go to your workspace and fix them. Recommit them to github and redeploy branch, check logs, and next to the <br>"more" on top right you can view app. Test out the app that it works correctly. If not repeat process of fixing and redeploying. 	|
| 7 	| The database that has been used for this app is mongodb. Credentials supplied in separate document not publically available. There should be <br>no need to redploy this if the url is correctly added to the heroku vars configs. Login information is supplied in a separate file, not part of the <br>public domain. If you need to create a new user you can do this once logged in, under the database access tab, create a user defining what <br>access level they have. You can create a password and username, make sure you write this down somewhere. Go to the network access <br>section and add the ip address of the client that needs to connect to the database. Then go to Databases and select "connect" to complete <br>the process. 	|
| 8 	| The url for the database includes the database name and login credentials, so this needs to be added to the heroku and env configs vars <br>and kept secret. 	|


# Acknowledgements

- Stackflow was referenced but the solutions I needed were not in there instead language documentation was used eg. python, flash, mongo, and jinja<br>
- I used notes I made during the module lessons, and the documentation for python, flash, mongo, and jinja.<br>
- Pep8 Standards were followed and pylint in visual studio code was used
- MaterializeCSS for use of their css
- Markdown table generator used: https://www.tablesgenerator.com/markdown_tables
- Lucid Chart for the Blueprints
- Favicon for its converter from png to favicons
- Adobe Illustrator to make the Bee Logo
- Balsamiq to make the wireframes
- Gitpod for the Workspace environment
- Github for commits and keeping track
- Heroku for deployment
- Mongo DB for a database


# Debugging & Test Results:

**TEST CASES:**

Test Cases and Debugging:

| Test Cases: |
|---|
| ID 1 |
| Title Testing in Safari Browser with Gitpod |
| Owner wendybovill |
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True |
| Steps  |
| Opened Site. Loaded Signup page. Filled in Form but on submission KeyError displayed. FAIL<br>ERROR : signup email was not defined. The username variable had not been passed through<br>to the sign_up email function. See screenshot 1a<br>Fix: Included variables required passed through to the format method within the sign_up_email<br>from the route/view on lines 166 of the app.py as per screenshot 1b<br>Opened Site. Loaded Signup page. Filled in Form. on submission sign up occurred and redirected as<br>per route defined on call back. PASS |
| ![Screenshot 1a](https://github.com/wendybovill/milestone-project-3/blob/b9f4261d80572a48189c680d306353fc499ee997/documentation/screenshots/1a.png) |
| 1a |
| ![Screenshot 1b](https://github.com/wendybovill/milestone-project-3/blob/f36b960fd4df2a844f03b513eaa623bab0f08144/documentation/screenshots/1b.png) |
| 1b |
| Priority Medium |
| Status Completed |
| Estimate 30 minutes |
| Type Acceptance |
| Automation Manual |
| ID 2 |
| Title Testing in Safari Browser with Gitpod |
| Owner wendybovill |
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True |
| Also required: Email account and client |
| Steps  |
| Checked email recevied after Sign up. PASS<br>Clicked link within email to verify users email address. Browser responded to load page. PASS<br>Page loading failed. Name Error see screenshot 2a. FAIL<br>Fix: Line 248 in app.py user_verfied was incorrect syntax. Dot notation required. Changed to<br>user.verfied using dot notation.<br>Clicked link within email to verify users email address. Browser responded to load page. PASS<br>View opened correctly to form which then was filled in and submitted verifying the user and<br>redirected to profile page as per callback route. PASS |
| ![Screenshot 2a](https://github.com/wendybovill/milestone-project-3/blob/ded804d24f93a2b791e547e192c36ca4da5628f0/documentation/screenshots/2a.png) |
| 2a |
| Priority Medium |
| Status Completed |
| Estimate 25 minutes |
| Type Acceptance |
| Automation Manual |
| ID 3 |
| Title Testing in Safari Browser with Gitpod and Heroku |
| Owner wendybovill |
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True |
| Steps  |
| On Events page: Filled in search form with term. Submitted Search. FAIL<br>Heroku showed an IndentationError in line 470 of app.py  See screenshot 3a<br>Fix: Indented line as was under-indented after if statement on line 469 of app.py<br>Returned to Events page in browser after re-committing to Github.<br>Performed Search term submission. <br>Form Submission suceeded. Events loaded as per search term. PASS |
| ![Screenshot 3a](https://github.com/wendybovill/milestone-project-3/blob/285472c55f18d270604427a220f93a6e08b3124e/documentation/screenshots/3a.png) |
| 3a |
| Priority Medium |
| Status Completed |
| Estimate 20 minutes |
| Type Acceptance |
| Automation Manual |
| ID 4 |
| Title Testing in Safari Browser |
| **Owner ** wendybovill |
| Precondition Required: Sarari Browser. Heroku. Gitpod/Visual S Code Terminal. Debugging ON/True |
| Steps  |
| In browser url address field. changed endpoint to a non-existent view to test http error response. Loaded http response page called. PASS<br>Page showed flash message as defensive programming defined for error status code 404. PASS<br>Further error statuses defined and tested. Each error code gives different feedback messages to user. PASS |
| Screenshots 4a. 4b. 4c |
| ![Screenshot 4a](https://github.com/wendybovill/milestone-project-3/blob/4f9d6a3cb90791799f7415ff642620b8dc8fd7df/documentation/screenshots/4a.png) |
| 4a |
| ![Screenshot 4b](https://github.com/wendybovill/milestone-project-3/blob/3cdbafc37e4292cfd4fa90faba07067ea94697e6/documentation/screenshots/4b.png) |
| 4b |
| ![Screenshot 4c](https://github.com/wendybovill/milestone-project-3/blob/26edae38724b5b0e3900354715d0bf032d7efa95/documentation/screenshots/4c.png) |
| 4c |
| Priority Medium |
| Status Completed |
| Estimate 1 hour |
| Type Acceptance |
| Automation Manual |
| ID 5 |
| Title Testing in Safari Browser |
| Owner wendybovill |
| Precondition Required: Sarari Browser. W3C Schools css validators |
| Steps  |
| Using Validation service on w3c for css. entered url for automated testing. FAIL  see screenshot 5a<br>Response indicated lines 619. 862. 1019 in Styles.css had the same error - display: flexbox. No such property for display. Required 'flex' instead.<br>Edited those lines in styles.css file to 'display: flex;' <br>Saved file and re-committed to github.<br>Re-ran the validator.<br>No errors displayed in site css. PASS<br>Validation errors detected in Materializecss third party stylesheets. ACCEPTED.<br>No fix available to third party stylesheets as too numerous and not within scope. |
| ![Screenshot 5a](https://github.com/wendybovill/milestone-project-3/blob/086fe134138d980d0502306f9e5347ec04b03f34/documentation/screenshots/5a.png) |
| 5a |
| Priority Medium |
| Status Completed |
| Estimate 10 minutes |
| Type Acceptance |
| Automation Automated |
| ID 6 |
| Title Testing in Safari Browser |
| Owner wendybovill |
| Precondition Required: Sarari Browser. W3C Schools html validators |
| Steps  |
| Using Validation service on w3c for css. entered url for automated testing. FAIL  see screenshot 5a<br>Response indicated lines 619. 862. 1019 in Styles.css had the same error - display: flexbox. No such property for display. Required 'flex' instead.<br>Edited those lines in styles.css file to 'display: flex;' <br>Saved file and re-committed to github.<br>Re-ran the validator.<br>No errors displayed in site css. PASS<br>Validation errors detected in Materializecss third party stylesheets. ACCEPTED.<br>No fix available to third party stylesheets as too numerous and not within scope. |
| ![Screenshot 6a](https://github.com/wendybovill/milestone-project-3/blob/229b7106f79e26362ba1e4fc040772dd33174a70/documentation/screenshots/6a.png) |
| 6a |
| ![Screenshot 6b](https://github.com/wendybovill/milestone-project-3/blob/e317cbf9c8617f03c0a732ce1780c9597e914297/documentation/screenshots/6b.png)|
| 6b |
| Priority Medium |
| Status Completed |
| Estimate 10 minutes |
| Type Acceptance |
| Automation Automated |
| ID 7 |
| Title Testing for Responsiveness |
| Owner wendybovill |
| Precondition Required: Testing in Safari Browser. Chrome Browser. Firefox Browser. Internet Explorer and mobile devices: |
| Mobiles Apple Iphone XS. Iphone 8 Plus and Android Hero. 11 and 12 Inch Ipads |
| Steps  |
| Loaded each device. checked each page: Events. Contact Us. Sign Up. Verify and Login as a logged out user <br>Each device loaded and displayed page content as expected with correct responsiveness. PASS<br>Then repeated steps as logged in user. including Profile page. Search. Edit Profile. Edit Event Types. Edit Event. Add Event. Add Event Types<br>Contact us as logged in user. Delete own Event and Event Types. PASS. <br>Next Tested View All Members. Edit Members. as admin user. PASS |
| Priority Medium |
| Status Completed |
| Estimate 1 hour  |
| Type Acceptance |
| Automation Manual |


*User Testing:*

Manual Testing various possible user attempts to work around the site security was undertaken to ensure a user could not:
- edit, update or delete other users Events or Event Types
- see or edit or update other users profiles
- use url changing as logged in or logged out users to view other users content, either profiles, or edit events or edit event types
- view, edit, update or delete member profiles as an admin user
- urls cannot be changed to gain access to restricted areas, users are redirected either through http error status responses to the index page with a relevant message or on the same pages with flash messages instructing them they are not authorized and need to log in (where appropriate)

  

*References used to assist debugging:*

- W3 schools html validator: http://validator.w3.org

- W3 schools jigsaw css validator: http://jigsaw.w3.org

- Werkzeug showing errors in debugging process

- Regular commits were made throughout the process to github as deployed early to use gitpod for testing
  (problems detected in the terminal were then corrected)

- Python documentation, Flash documentation


## Screenshots of Finished Site

| Screenshot Desktop Index Page |
|-----------------------------------------------------------------------|
| ![Finished Site Desktop Index Page](https://github.com/wendybovill/milestone-project-3/blob/43f702c830ea4035ead9ffff36f81610628a9149/documentation/screenshots/laptop.png)|

| Screenshot Ipad Index Page |
|-----------------------------------------------------------------------|
| ![Finished Site Ipad Index Page](https://github.com/wendybovill/milestone-project-3/blob/5df605d3f7c8bf6e2c985f2d33b0908a51b0ab55/documentation/screenshots/Ipad_index.PNG)|

| Screenshot Iphone Index Page |
|-----------------------------------------------------------------------|
| ![Finished Site Iphone Index Page](https://github.com/wendybovill/milestone-project-3/blob/200db3944839cdde5c523a451f6fd3ddd5c7bf78/documentation/screenshots/iphone.PNG)|


