# EmailSender.py
A python script to e-mail someone 

To be successful in sending an email through G-Mail with SMTP, follow the steps below

1. Create a new email account with g-mail or use a pre-existing g-mail account.
2. Ensure 2 Factor Authentication is active or if it isn't, activate it.
3. Generate a password with Google app password  
  a. to do this, go to google account settings   
  b. click on security   
  c. scroll down to 'Signing in to Google'   
  d. click on app password and choose custom   
  e. copy password for later   
  
  ----------------------------------------------
  
  To run the code, open up terminal or command prompt
  
  1. cd into the folder that has the code   
  2. type this into the terminal or command prompt   
    a. python3 name_of_python_file.py -t <email_you_want_to_send_to> -l <email_you_are_sending_from_that_you_created_app_password> -p <app_password_you_created_earlier>      
              **WITHOUT THE <> AND REPLACE IT WITH CORRESPONDING INFO**    
  3. If it successful, it will say email sent.   
