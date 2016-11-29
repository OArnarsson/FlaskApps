# Basic Flask app
### About
This is the most basic level of a flask app, It contains:
1. app.py - The Flask application.
2. requirements.txt - Everything you need to create the flask app.
3. Procfile - To tell heroku what commands should be run.  

The Application on [heroku](https://basic-flask-aba.herokuapp.com/)

### instruction
1. [Fork](https://github.com//login?return_to=%2Fandriandresson%2FFlaskApps) or [clone](https://github.com/andriandresson/FlaskApps/) the repository.  
2. Navigate to <code>$ cd /flaskApps/First_FlaskApp/ </code>  
3. Install requriements: <code>$ pip install requirements.txt </code>
4. Create new app on [heroku](https://dashboard.heroku.com/new?org=personal-apps)
5. login to heroku <code>heroku login</code>  
6. Make sure you are in the root of your project <code>$ cd flaskApps/First_FlaskApp/</code>  
7. Initialize project <code>$ git init</code>  
8. Add git repo to heroku remote <code>$ heroku git:remote -a newHerokuAppName</code>
9. Stage your project<code>$ git add .</code>
10. Commit your changes <code>$ git commit -m "My first commit"</code>
11. Push to heroku master <code>$ git push heroku master</code>  

Your flask app should now be running on heroku!


