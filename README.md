## pipelineChecker

### Instructions

- clone `pr`, `pipelineChecker.py` and `properties.py`
- cd into folder they are in
- run `./pr $PR_number`
- checks if pipeline run is completed every n seconds
- notifies via terminal alert the outcome

### Properties required

- github user name
- github password
- URL for repo, i.e. company/repository
- delay (in seconds) of how often to check for an update

### Restrictions

- You need python 3 installed 
- You need any corresponding libraries installed (`pygithub` and `webbot`)
- You need to include your github username and password
- You need to include the URL to the repo to check
- Probably only works on a mac
- Assuming two PR reviewers are mandatory
- Uses Google Chrome and kills all Chrome instances once done
