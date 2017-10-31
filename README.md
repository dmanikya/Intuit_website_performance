Intuit website performance applicaton

End-to-end flow:
1. Django web application (Development)
2. Deployed in Amazon elastic beanstalk (Prod Deployment)
3. Used Slack's email webhook to integrate with the CloudAlarms in Amazon elasitc beanstalk (Prod Monitoring)


Components of the web application include the performance of:
1. Intuit page load time
2. Server response time
3. DNS lookup time and other DNS related parameters 
- All displayed on intuitive charts (chartjs of Django framework)


Screenshots:
Please check the screenshots in the "Screenshots of web pages in the application" directory


Code is in "src" directory:
1. In the charts directory: urls.py, views.py are the core files.
2. html pages are in "templates" directory
3. ".elasticbeanstalk" directory contains the yml file needed to deploy this code in Amazon's elastic beanstalk (AWS)
4. db.sqlite3 is the database
5. requirements.txt contains all the libraries/packages of Python needed for this application to run.