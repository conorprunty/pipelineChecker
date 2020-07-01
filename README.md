# pipelineChecker

-clone 'pr' and 'pipelineChecker.py'
-cd into folder they are in
-run ./pr $PR_number
-checks if pipeline run is completed every 60 seconds
-notifies via terminal alert the outcome

Notes:

You need python 3 installed 
You need any corresponding libraries installed (pygithub and webbot)
You need to include your github username and password
You need to include the URL to the repo to check
Probably only works on a mac
Assuming two PR reviewers are mandatory
Uses Google Chrome and kills all Chrome instances once done