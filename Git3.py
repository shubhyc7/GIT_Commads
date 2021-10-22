



  --------------------------Git Commands 3 -----------------------------
  ____________________________________________________________________

  p.s. git config can be changed in file .gitconfig or in console:

  CONFIGURE GIT(optional)
  1. Set your name
  $ git config - -global user.name < YOUR NAME >

  2. Set your email
  $ git config - -global user.email < YOUR EMAIL ADDRESS >

  ____________________________________________________________________

  HTTPS(recommended, optional)
  1. Cache credentials for Windows
  $ git config - -global credential.helper wincred

  2. Same for Linux(works with Windows too)
  $ git config - -global credential.helper cache

  ____________________________________________________________________

  SSH key(optional)
  Use gitlab\github to generate the key or:

  1. Check existing ssh keys(e.g. id_dsa.pub)
  $ ls - al ~/.ssh

  2. Generate new key
  $ ssh-keygen - t rsa - C < your_email@example.com >
  ... then add place to save generated key
  ... then enter your passphrase to be encrypted

  3. Add generated key to the ssh-agent
  $ eval "$(ssh-agent -s)"
  $ ssh-add ~/.ssh/id_rsa

  4. Test it
  $ ssh - T < git@github.com >

  ____________________________________________________________________

  START A REPO
  1. Clone
  $ git clone < copy here https or ssh link to the repo >

  2. Initialize the repo locally
  $ git init

  ____________________________________________________________________

  CONFIGURE REMOTES
  1. Watch remotes
  $ git remote - v

  2. Add remote(origin, your fork, fetch sources)
  $ git remote add < remoteName > <git@bitbucket.org... >

  3. Delete remote
  $ git remote remove < remoteName >

  4. Rename remote
  $ git remote rename < oldName > <newName >
  ____________________________________________________________________

  USE A FORK(optional)
  Create a fork in github/gitlab
  1. Add new remote, writing in link of your fork
  $ git remote add < myfork > <git@bitbucket.org... >

  2. Fetch it
  $ git fetch < myfork >

  3. Merge or rebase it
  $ git checkout master
  $ git rebase < myfork > /master

  4. Push a commit
  $ git push myfork < localBranch > <remoteBranch >
  Then create a pull request from your fork in github/gitlab

  ____________________________________________________________________

  CONFIGURE ALIASES(optional)
  These are used as shorthands:
  $ git config - -global alias.co checkout
  $ git config - -global alias.ci commit
  $ git config - -global alias.st status
  $ git config - -global alias.br branch
  $ git config - -global alias.hist 'log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short'
  $ git config - -global alias.type 'cat-file -t'
  $ git config - -global alias.dump 'cat-file -p'
  Do rebase istead of merge always when pull:
  $ git config - -global branch.autosetuprebase always

  /********************** LOCAL CHANGES ** *******************/

  CHECK STATE OF CODE & HISTORY
  1. Watch status of your code
  $ git status

  2. Find differences between current and other branch
  $ git diff < branch >

  3. Watch history of changes
  $ git log

  4. Watch graphic history
  $ gitk

  ____________________________________________________________________

  STASH CODE(temporarily saves the code if you need to checkout but don't want to commit)
  1. Save your changes
  $ git stash

  2. Watch a list of stacks in stash
  $ git stash list

  3. Apply your changes after work in other branch or pull/fetch
  $ git stash apply

  4. Delete stashed changes
  $ git stash drop

  ____________________________________________________________________

  COMMIT YOUR CHANGES
  1. Watch the last commit
  $ git last

  2. Add changes to commit
  $ git add .
  $ git add . -A(adds all changes with imgs and deleted files)

  3. Revert local commit(it creates new commit and leaves current in history - safe)
  $ git revert HEAD~ < 1 >
  See more: https: // www.atlassian.com/git/tutorials/undoing-changes/git-revert

  4. Reset commit(undo changes from the last commit to < 1 > and clean logs - unsafe!)
  $ git reset HEAD ^ <1 >
  $ git reset - -hard HEAD ^ <1 >

  3. Post commit
  $ git commit - m '<Your message with changes here>'

  4. Add changes and commit in one command
  $ git commit - a - m '<Your message with changes here>'

  5. Checkout to another commit of current branch, without loss of changes
  $ git checkout < 38d1209 >

  6. Checkout to a specific file in the chosen commit
  $ git checkout < 12d3910 > <index.html >

  ____________________________________________________________________

  WORK with BRANCHES
  1. Watch existing branches(current is marked with *)
  $ git branch
  or to see current branch
  $ git status

  2. Watch last commits of every branch
  $ git branch - v

  3. Change branch
  $ git checkout < branch2 >

  4. Create new branch
  $ git - b branchName

  5. Create branch from the current one and checkout
  $ git checkout - b branchName

  6. Delete a branch
  $ git branch - d < branchName >

  ____________________________________________________________________

  /************************ SYNCHRONIZE CHANGES ** *******************/
  FETCH = take changes from origin
  $ git fetch ( < origin > )

  PULL = fetch + merge
  Choose the needed branch!
  $ git pull ( < origin > )
  or if special branch needed:
  $ git pull origin < branch >
  or fetch + rebase instead of merge:
  $ git pull - -rebase origin

  MERGE = take changes from origin or other branch and merge them into the current one,
  branchy complex history
  $ git merge < branch >
  See more: https: // www.atlassian.com/git/tutorials/using-branches/git-merge

  REBASE = take commit and move it to the right place between commits from origin, linear 
  neat history Never use on public branches!
  $ git rebase < origin > / < branch >
  See more: https: // www.atlassian.com/git/tutorials/merging-vs-rebasing

  PUSH = take commited changes and send it to the origin or fork repo
  $ git push ( < origin > ) ( < branch > )
  Avoid using forced pushing to the repo!

  ____________________________________________________________________

  /************************ USEFUL DOCS & TUTORIALS ** ***************/
  ENG
  https: // training.github.com/kit/downloads/github-git-cheat-sheet.pdf
  https: // www.atlassian.com/git/tutorials/

  RUS
  http: // githowto.com/ru
  http: // git-scm.com/book/ru/v1

  ____________________________________________________________________  

  
