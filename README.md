# Cemetery Database Website
### Flask site developed for a cemetery needing records transferred from an old binder with handwritten entries into a full functioning database with interactivity.

  **This project is for my portfolio and the client is aware I am posting the code and all personal data/link names have been removed for there privacy.** 
  
  Cemetery Database Website is a simple Python-flask site using HTML and a bootsrapped CSS. It utilizes an authentication portal and registration portal with encryption(I am aware
the sign up is only accesible by URL that is intentional).

  ![Login Page](/DudleyCemetary-screenshots/login.png)
  
  ![Registration Page](/DudleyCemetary-screenshots/sign-up.png)

  After logging in the main directory displays every plot in the cemetary with information about the plot.

  ![Home](/DudleyCemetary-screenshots/home.png)

  These plots have UI elements to show availibaility and formatting to make it easier to read the information.

  ![Home-UI](/DudleyCemetary-screenshots/directory.png)

  Each plot has an edit button which will allow you to edit or update existing plots by pulling the info, or lack thereof, from the database.

  ![Edit](/DudleyCemetary-screenshots/edit.png)
  
  ![Update](/DudleyCemetary-screenshots/update.png)

  The search function is very minimal and basic at the clients request future updates will look to expand search capabilities utilizing dynamic drop downs for section and lot. This pulls up another page with the same formatting as the directory with any search that matches the last name typed in.

 ![Search Results](/DudleyCemetary-screenshots/search-results.png)

  Finally the export report allows a user to export the current image of the cemetery's directory from the database into a formatted 
report. This was also at the clients request to be able to keep a physical back up and onboarding new memebr of the cemetery's board.

***If you are interested in using this template I would recomend making an account through the sign-up portal before adding in the database. This is because I deleted the orginal database file from this project and there is no way to add/delete cemetary plots in the application, because they are fixed locations. So you may have issues loading in the database through sql commands before the program actually creates te file you need. (See __init__.py)***
