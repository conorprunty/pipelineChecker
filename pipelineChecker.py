# -*- coding: utf-8 -*-
import time
from datetime import datetime
from github import Github
from webbot import Browser
import sys
import os


def notify(message):
    os.system("killall -9 'Google Chrome'")
    os.system("osascript -e 'Tell application \"System Events\" to display dialog \"" + message + "\"'")


user = "<github_username>"
password = "<github_password>"

if len(sys.argv) < 2:
    notify(message='No PR number passed as argument')
    sys.exit(0)

prNum = sys.argv[1]

g = Github(user, password)
repo = g.get_repo("<path_to_repo>")
prTitle = repo.get_pull(int(prNum))

web = Browser()
#web.driver.set_window_position(-10000, 0)
web.go_to('https://github.com')
web.click('Sign in')
web.type(user, into='Username or email address')
web.click('NEXT', tag='span')
web.type(password, into='Password')
web.click('Sign in', tag='span')
print(prNum)
web.go_to('https://github.com/<path_to_repo>/pull/' + prNum)
a = web.get_page_source()
b = str(a)

if b.find("Subscribe to our newsletter") != -1:
    # this means it's a 404
    # theoretically this could change I guess
    notify(message='PR %s does not exist' % prNum)
    sys.exit(0)

while True:
    web.go_to('https://github.com/<path_to_repo>/pull/' + prNum)
    a = web.get_page_source()
    b = str(a)
    web.driver.minimize_window()

    if b.find("Some checks haven’t completed yet") != -1:
        # still waiting on run to finish
        print("run still going at {0}".format(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))

    elif b.find("1 errored and 1 successful") != -1:
        # looks like it failed, best alert the user!
        notify(message='darn, the pipeline for PR %s failed' % prNum)
        sys.exit(0)

    elif b.find("2 successful checks") != -1:
        # may have finished successfully but let's
        # check if it needs a rebuild...
        if b.find("conflicts that must be resolved") != -1 or b.find("branch is out-of-date") != -1:
            notify(message='build %s successful but may need to be rebuilt' % prNum)
            sys.exit(0)

        elif b.find("At least 2 approving reviews are required") != -1:
            notify(message='build %s successful but may need another sign off' % prNum)
            sys.exit(0)

        else:
            notify(message='build %s successful, merge merge merge' % prNum)
            sys.exit(0)

    else:
        notify(message='build %s may be completed or deleted, please check' % prNum)
        sys.exit(0)

    time.sleep(60)
    continue
