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