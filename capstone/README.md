Quizz is a test builder which aims at provoking the user by questions with gradually increasing difficulty depending on the ammount of right choices given by her.

"Quiz" is a simple but efficient web application based mainly on single page app principles which can be used to test specific knowledge in a field and especially grammar in a foreign language. 'Quiz' utilizes Django at backend and JavaScript, HTML, CSS and Bootstrap at the front. 'Quiz' combines the most important concepts presented in the course without unnecessary reppetativeness in their usage. Quiz contains a data base model, db quiries, simple algorithms in python views, Java Script DOM manipulation, Fetch method and timer, API emulation, SPA principles, a strict HTML sceleton and stylish CSS presence.

"Quiz" is a template that could be used for creating different tests and quizes based on multiple choice method. Via the Django Admin the number of questions could be changed as long as they could be divided by 4 withoud reaminder.

I am presenting Quiz as it it is a 'modular component' - still needed to be populated with the required questions according to the field it is going to be used. Randomly one of the fourth buttons acquires the right answer. In the current presentation of Quiz the button is called 'TRUE' and the other ones 'F' comming from 'false'. 

"Quiz" is different from 'E-commerce project', because it is not a catalougue of items.

"Quiz" is different from "Network project ', because it's purpose is to test knowledge and calculate particular input.

Quiz's databes consists of one model. At the beginnig of the project I started with three models but during the process I considered it would be better to reduce the number of quieries and simplify them and thus I created a single one. Instead of __str__ method it includes and method serializing the output data which is then jsonified. 

Quiz is based on several views in the Python code which are mainly simple algorithms to calcualate the client input.

For the implementation of the Single page application principles I used vanilla Java Script.

One of the views is emulating simple API in order to present output data in JSON format. 






