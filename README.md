# game
![Python application](https://github.com/jmarthernandez/game/workflows/Python%20application/badge.svg?branch=master)

## Contributing to game

### Create a branch
All of your work needs to happen on a separate branch from master.  We don't want to commit directly to master before someone reviews the changes to code.

To create a branch navigate to github.com/jmarthernandez/game and create a new branch by typing desired branch name into the branch selector.

If you want to make your branch have multiple words use `-`'s between the words.  For example, `my-branch` not my `my branch`.

![Create Branch Example](/images/create-branch.png)

Congrats! Now your branch has all the latest code that your fellow engineers have contributed to game.  You will notice that your branch is on github but you can't find it on Pycharm.

### Checkout your new branch on Pycharm
We need to fetch the branch created on github and check it out on our own computer.
- Open Pycharm
- Open Terminal(In bottom left corner)
- run `git fetch` in terminal
- run `git checkout my-branch-name`

It should look something like this
![Fetch and Checkout](/images/fetch-branch.png)

If you get an error saying `error: pathspec 'testbranch' did not match any file(s) known to git.` this means that you forget to run `git fetch` or that you did not create the branch on github yet.

That error look like this
![Fetch and Checkout](/images/forget-fetch.png)

If you have changes that you have not yet committed they will be carried over to the new branch.  They will not be deleted.

### Make code changes and commit
Make your changes to the code and make sure everything is formatted correctly.

Run `git status` in the terminal to see what files you have changed.  If there are any you didn't mean to change go in and revert your changes.

The files in red will not be added to your commit.  All of them should be red at this point because we haven't added any files to the commit.

After you have verified you only changed the files you want, run `git add game.py`(or whatever file you changed) in the terminal.

Now when running `git status` you'll notice that the files are now green.  This means when you make a commit the green files will be included.

Now you will run `git commit -m 'Added thing to code'` followed by `git push`.  Now your code should be on github and ready to be added to a pull request.

Create a pull request https://guides.github.com/activities/hello-world/#pr

TLDR steps
- `git status` to make sure we are only changing what we want
- `git add ourfile.py` to include file in commit
- `git commit -m 'My useful commit message`
- `git push`
- create pull request