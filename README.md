This is a fitness app made in 2-3 days as a final project for my bootcamp. It's to demonstrate the use of Python, APIs and a bit of Flask. It's finished for the purpose for the assessment, but WIP in terms of user-friendliness. It still needs a lot of work on the front end—I'm hoping to at least set up a form or some buttons as a way to get input, and format the output so it looks nicer.

It is supposed to be a web application that does two things: 
1. Exercise planner: Gives you a random list of exercises according to given parameters like number of exercises and equipment, so you don't have to choose on your own.
2. Calorie counter: Allows you to makea list of a couple recipes and get the total calories for them.

**Installing and Running the Project:** I don't have a server for it. You can download it and run it on debug mode, then use your localhost to take a look at the front end. But you still need to type in the path you want to go (/exerciseplanner or /caloriecounter), then add your input in the terminal... I learned the hard way that I probably should've worked on both frontend and backend at the same time, rather than backend then frontend.

For the exercise planner, it'll give you the .JSON on your browser. The database I used is https://github.com/yuhonas/free-exercise-db. Thank you for sharing!

Unfortunately for the calorie counter, I removed the API key for security reasons, but you can sign up at https://spoonacular.com/food-api for free and you can get your own API key that way. It'll give you the list of recipes, the calories, and the total calories.
