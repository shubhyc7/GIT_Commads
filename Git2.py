


  ----------------------Git Commands 2 ------------------------

  # change directory to codebase

  cd / Users/computer-name/Documents/website

  ----------------------------------------------------------

  # git init (make directory a git repository)

  git init

  ----------------------------------------------------------

  # git add

  git add .
  git add index.html
  git add css

  ----------------------------------------------------------

  # git commit

  git commit - m "My first commit message"

  ----------------------------------------------------------

  # git status

  git status

  ----------------------------------------------------------

  # git config

  # Running git config globally
  git config - -global user.email "my@emailaddress.com"
  git config - -global user.name "Brian Kerr"

  # Running git config on the current repository settings
  git config user.email "my@emailaddress.com"
  git config user.name "Brian Kerr"

  ----------------------------------------------------------

  # git branch

  # Create a new branch
  git branch new_feature

  # List all remote or local branches
  git branch - a

  # Delete a branch
  git branch - d new_feature

  # Checkout an existing branch / Switching to branch 'new_feature'
  git checkout new_feature

  # Checkout and create a new branch with that name / Creating and switching to branch 'staging'
  git checkout - b staging

  ----------------------------------------------------------

  # git merge

  # Merge changes into current branch
  git merge new_feature

  # When you've completed development in your branch and everything works fine, the final step 
  # is merging the branch with the parent branch(dev or master). This is done with the git 
  # merge command.

  # First you should switch to the dev branch:

  git checkout dev

  # Before merging, you should update your local dev branch:

  git fetch

  # Finally, you can merge your feature branch into dev:

  git merge < branch-name >

  # Git Merge

  # Once you’re done with development inside your feature branch and tested your code, you 
  # can merge your branch with the parent branch. This could be either a develop branch or 
  # a master branch depending on the git workflow you follow.

  # When running a git merge command, you first need to be on the specific branch that you 
  # want to merge with your feature branch.

  # Let’s see how to use the git merge command with an example.

  # Using Git Merge Command

  # Imagine you’re currently in your feature branch called feature1 and you’re ready to 
  # merge it to the develop branch.

  # We must first switch to the develop branch using the checkout command.

  git checkout develop

  # Before merging, you must make sure that you update your local develop branch. 
  # This is important because your teammates might’ve merged into the develop branch 
  # while you were working on your feature. We do this by running the pull command.

  git pull
  # If there are no conflicts while pulling the updates, you can finally merge your 
  # feature1 branch into the develop branch.

  # We do this by using the git merge command followed by the branch name that we want 
  # to merge into our current branch.

  git merge feature1

  ----------------------------------------------------------

  # git remote

  # Add remote repository
  git remote add origin git @ account_name.git.beanstalkapp.com: / acccount_name/repository_name.git
  
  # List named remote repositories
  git remote - v

  ----------------------------------------------------------

  # git clone

  # To create a local working copy of an existing remote repository
  git clone git @account_name.git.beanstalkapp.com: / acccount_name/repository_name.git

  ----------------------------------------------------------

  # git pull
  # To get the latest version of a repository run git pull. This pulls the changes from 
  # the remote repository to the local computer.
  git pull origin staging

  ----------------------------------------------------------

  # git push

  # Sends local commits to the remote repository.
  git push origin staging

  # Push all local branches to remote repository
  git push - -all

  ----------------------------------------------------------

  # git stash

  # To save changes made when they’re not in a state to commit them to a repository. 
  # Store current work with untracked files
  git stash - u

  # Git Stash temporarily shelves your work, so you can switch to another branch, work on something 
  # else, and then come back to this at a later time.
  # It’s perfect if you need to work on something else and you’re midway through a code change, but 
  # aren’t ready to commit the code.

  # Using Git Stash Save Command
  git stash save “< stash-message >”

  # This will stash your changes with the message you entered. This can be helpful when you want to 
  # come back and restore your stash, especially when you have several stashes.

  # However, this will only stash your tracked files that you added using git add. If you want to 
  # include the untracked files as well, run
  git stash save - u


  # Using Git Stash List Command

  # When you want to view all the stashed code, you can view them using this command. Once you stash
  #  your code, git will assign a stash id, so you can restore a specific stashed code later.

  # For example:

  git stash list


  # This might show the following

  # stash@{0}: On master: Stashed with message1
  # stash@{1}: On master: Stashed with message2

  # Using Git Stash Apply Command
  # This will automatically restore and apply the topmost stash in the stack.
  git stash apply

  # If you want to restore a specific stash that you want to apply, using the above example, you can 
  # simply run git stash apply stash@{1}.
  # Note: When you use git stash apply, the stashed version will be applied to your current 
  # working branch.However, it will not delete the stash from the stack.

  # Using Git Stash Pop Command

  # To automatically also delete the stash from the stack, the git stash pop command is used.

  # If you want to do it for a specific stash in the stack, run git stash pop stash@{0}.

  # Bring stashed work back to the working directory
  git stash pop

  ----------------------------------------------------------

  # git log 

  # To show the chronological commit history for a repository.
  # Show entire git log
  git log

  git log - -summary

  # List of all commit with commit id and commit message)	git log - -oneline

  # Show git log with date pameters
  git log - -before = "Oct 20"

  # Show git log based on commit author
  git log - -author = "Brian Kerr"

  ----------------------------------------------------------

  # git rm

  # Remove files or directories from the working index(staging area).
  # To remove a file from the working index:
  git rm - -cached css/style.css

  # To delete a file (force):
  git rm - f css/style.css

  # To remove an entire directory from the working index (cached):
  git rm - r - -cached css/

  # To delete an entire directory (force):
  git rm - r - f css/

  ----------------------------------------------------------
  # Git revert

  # Sometimes we need to undo the changes that we've made.
  git log - - oneline

  # Then we just need to specify the hash code next to our commit that we would like to undo:
  git revert 3321844

  ----------------------------------------------------------

  # Git Diff

  # Git Diff is my go-to command when I want to quickly see the difference between my current branch 
  # and another branch(usually the branch I’m merging into).
  # This will show you any uncommitted changes in your local repo.
  git diff  

  # To compare two branches
  # This will show all the file differences between the two branches.   
  git diff branch1 branch2 ./path/to/file.txt

  # This command will show a comparison of the changes made to file file.txt across the 
  # branches branch1 and branch2.

  ----------------------------------------------------------

  # Remove a file ( or folder)	

  git rm - r < file-name.txt >

  ----------------------------------------------------------

  # Return to previous commit	
      
  git checkout < commit id >

  ----------------------------------------------------------    
    
  # Revert commit(undo one particular commit)	
      
  git revert < commit id >
      
  ----------------------------------------------------------

  # Reset to previous commit(remove history of all commit after)	
      
  git reset < commit id >

  ----------------------------------------------------------

  # Rename a local branch	
      
  git branch - m < old branch name > <new branch name >

  ----------------------------------------------------------

  # Delete a remote branch	

  git push origin --delete <branch name>

  ----------------------------------------------------------

  # Preview changes before merging	

  git diff < source branch > <target branch >

  # Merge a branch into the active branch	
      
  git merge < branch name >

  ----------------------------------------------------------


