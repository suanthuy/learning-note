# Git

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Git is lightning fast and has a huge ecosystem of GUIs, hosting services, and command-line tools.

## GitHub / GitLab

Github and GitLab is a server that allow you to upload and download the source code. Simplely, GitHub and GitLab is a cloud service that store the public or private source code.

## The Three States

Git has three main states that your files can reside in: modified, staged and committed.

    - Modified means that you have changed the file but have not committed it to your database yet.
    - Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
    - Committed means that the data is safely stored in your local database.

The basic Git workflow goes something like this:
1. You modify files in your working tree.
2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area.
3. You do a commit, which takes the files as they are in the staging area and stores the snapshot permanently to your Git directory.

## First-time Git setup

Git comes with a tool called `git config` that lets you get and set configuration variables that control all aspects of how Git looks and operates.

These variables can stored in three different places:
1. `[path]/etc/gitconfig` file: Contain values applied for all users in the system. Because this is a system configuration file, you would need administrative or superuser privilege to make changes to it.
2. `~/.gitconfig` or `~/.config/git/config` file: Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the --global option, and this affects all of the repositories you work with on your system.
3. `config` file in the Git directory (that is, .git/config) of whatever repository you're currently using: Specific to that single repository.

You can view all of your settings and where they are coming from using:

```
git config --list --show-origin
```

### Your Identity

The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

```
git config --global user.name "suanthuy"
git config --global user.email suanthuy12@gmail.com
```

Again, you need to do only once if you pass the `--global` option, because then Git always use that information for your user on that system.

### Your default branch name

By default, Git will create a branch called `master` when you create a new repository with `git init`.

To set `main` as the default branch name:

```
git config --global init.defaultBranch main
```

### Checking your settings

If you want to check your configuration settings, you can use the `git config --list` command to list all the settings Git can find at that point.

## Git Basic

### Initializing a Repository in an Existing Directory

First, you need to go to that project's directory. Then, type `git init`.
This creates a new subdirectory named `.git` that contains all of your necessary repository files - a Git repository skeleton.
### Cloning a Git Repository

If you want to get a copy of an existing Git repository - for example, a project you'd like to contribute to - the command you need is `git clone`. 
If you are familiar with other VCSs such as Subversion, you'll notice that the command is "clone" and not "checkout". This is an important distinction - instead of getting just a working copy, Git receives a full copy of nearly all data that the server has.
Every version of every file for the history of the project is pulled down by default when you run `git clone`.

You clone a repository with `git clone <url>`. For example, if you want to clone the Git linkable library called `libgit2`, you can do this:

```
git clone https://github.com/libgit2/libgit2
```

That creates a directory named `libgit2`, initializes a `.git` directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version.

If you want to clone the repository into a directory named something other than `libgit2`, you can specify the new directory name as an additional argument:

```
git clone https://github.com/libgit2/libgit2 mylibgit
```

That command does the same thing as the previous one, but the target directory is called `mylibgit`.
### Recording Changes to the Repository

Remember that each file in your working directory can be in one of two states: *tracked or untracked*. Tracked files are files that were in the last snapshot, as well as any newly staged files. 

Untracked files are everything else - any files in your working directory that were not in your last snapshot and are not in your staging area. 
When you first clone a repository, all of your files will be *tracked and unmodified* because Git just checked them out and you haven't edited anything.

As you edit files, Git sees them as modified, because you've changed them since your last commit. As you work, you selectively stage these modified files and then commit all those staged changes, and the cycle repeats.

```mermaid

```

### Checking the Status of Your Files

The main tool you use to determine which files are in which state is the `git status` command.

```
git status
```

### Tracking New Files

In order to begin tracking a new file, you use the command `git add`. To begin tracking the `README` file, you can run this:

```
git add README
```

If you run your status command again, you can see that your `README` file is now tracked and staged to be committed.

### Staging Modified Files

If you change a previously tracked file called `CONTRIBUTING.md` and then run your `git status` command again, you will receive the announcement from modified file.

The `CONTRIBUTING.md` file appears under a section named "Changes not staged for commit" - which means that a file that is tracked has been modified in the working directory but not yet staged.

To stage it, you run the `git add` command, `git add` is a multipurpose command - you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved.

Both files are staged and will go into your next commit. At this point, suppose you remember one little change that you want to make in `CONTRIBUTING.md` before you commit it. You open it again and make that change, and you're ready to commit. 

Now `CONTRIBUTTING.md` is listed as both staged and unstaged. It turns out that Git stages a file exactly as it is when you run the `git add` command. If you commit now, the version of `CONTRIBUTTING.md` as it was when you last ran the `git add` command is how it will go into the commit, not the version of the file as it looks in your working directory when you run `git commit`.

If you modify a file after you run `git add`, you have to run `git add` again to stage the latest version of the file.

### Short Status

While the `git status` output is pretty comprehensive, it's also quite wordy. If you run `git status -s` or `git status --short` you get a far more simplified output from the command.

```
git status -s
```

New files that aren't tracked have a `??` next to them, new files that have been added to the staging area have a `A`, modified files have an `M` and so on.

### Ignoring Files

Often, you'll have a class of files that you don't want Git to automatically add or even show you as being untracked.

In such cases, you can create a file listing patterns to match them named `.gitignore`. Here is an example `.gitignore` file:

```
$ cat .gitignore
*.[oa]
*~
```

The first line tells Git to ignore any files ending in ".o" or ".a" - object and archive files that may be the product of building your code. The second line tells Git to ignore all files whose names end with a tilde (~), which is used by many text editors such as Emacs to mark temporary files.

The rules for the patterns you can put in the `.gitignore` file are as follows:

- Blank lines or lines starting with # are ignored.
- Standard glob patterns work, and will be applied recursively throughout the entire working tree.
- You can start patterns with a forward slash (/) to avoid recursivity.
- You can end patterns with a forward slash (/) to specify a directory.
- You can negate a pattern by starting it with an exclamation point (!).

### Viewing Your Staged and Unstaged Changes

If the `git status` command is too vague for you - you want to know exactly what you changed, not just which files were changed - you can use the `git diff` command.

To see what you've changed but not yet staged, type `git diff` with no other arguments:

```
git diff
```

If you want to see what you've staged that will go into your next commit, you can use `git diff --staged`. This command compares your staged changes to your last commit:

```
git diff --staged
```

It's important to note that `git diff` by itself doesn't show all changes made since your last commit - only changes that are still unstaged. If you've staged all of your changes, `git diff` will give you no output.


### Committing Your Changes

Now that your staging area is set up the way you want it, you can commit your changes.

```
git commit
```

You can see that the default commit message contains the latest output of the `git status` command commented out and one empty line on top.

Alternatively, you can type your commit message inline with the `commit` command by specifying it after a `-m` flag.

### Skipping the Staging Area

Adding the `-a` option to the `git commit` command makes Git automatically stage every file that is already tracked before doing the commit, letting you skip the `git add` part. 

### Removing files

To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and them commit. The `git rm` command does that, and also removes the file from your working directory so you don't see is as an untracked file the next time around.

If you simply remove the file from your working directory, it shows up under the "Changes not staged for commit" (that is *unstaged*).

If you run `git rm`, it stages the file's removal.

Another useful thing you may want to do is keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore.

This is particularly useful if you forgot to add something to your `.gitignore` file and accidentally staged it.

```
git rm --cached README
```

You can pass files, directories, and file-glob patterns to the `git rm` command. That means you can do things such as:

```
git rm log/\*.log
```

Note the backslash (\) in front of the \*. This is necessary because Git does its own filename expansion in addition to your shell's filename expansion. This command removes all files that have the `.log` extension in the `log/` directory. Or, you can do something like this:

```
git rm \*~
```

This command removes all files whose names end with a `~`.

### Moving Files

Unlike many other VCSs, Git doesn't explicitly track file movement.

Git has a `mv` command.

```
git mv file_from file_to
```

In fact, if you run something like this and look at the status, you'll see that Git considers it a renamed file.

However, this is equivalent to running something like this:

```
mv README.md README
git rm README.md
git add README
```

Git figures out that it's a rename implicitly, so it doesn't matter if you rename a file that way or with the `mv` command. The only read different is that `git mv` is one command instead of three - it's a convenience function.

### Viewing the Commit History

You'll probably want to look back to see what has happened. The most basic and powerful tool to do this is the `git log` command.

```
git log
```

By default, with no agruments, `git log` lists the commits made in that repository in reverse chronological order, that is, the most recent commits show up first.

One of the more helpful options is -p or --patch, which shows the difference (the patch output) introduced in each commit. You can also limit the number of log entries displayed, such as using `-2` to show only the last two entries.

```
git log -p -2
```

If you want to see some abbreviated stats for each commit, you can use the `--stat` option.

```
git log --stat
```

As you can see, the `--stat` option prints below each commit entry a list of modified files, how many files were changed, and how many lines in those files were added and removed.

Another really useful option is `--pretty`. This option changes the log output to formats other than default. A few prebuilt option values are available for you to use: `oneline, short, full, fuller`.

```
git log --pretty=oneline
```

The most interesting option value is `format`, which allows you to specify your own log output format.

```
git log --pretty=format:"%h - %an, %ar : %s"
```

The `oneline` and `format` option values are particularly useful with another `log` option called `--graph`. This option adds a nice little ASCII graph showing your branch and merge history.


### Limiting Log Output

In addition to output-formatting options, `git log` takes a number of useful limiting options. You've seen one such option already - the `-2` option, which displays only the last two commits. 

However, the time-limiting options such as `--since` and `--until` are very useful.

```
git log --since=2.weeks
```

### Undoing Things

At any stage, you may want to undo something. Here, we'll review a few basic tools for undoing changes that you've made. Be careful, because you can't always undo some of these undos.

If you want to redo that commit, make the additional changes you forgot, stage them, and commit again using the `--amend` option.

```
git commit --amend
```

This command takes your staging area and uses it for the commit. If you've made no changes since your last commit (for instance, you run this command immediately after your previous commit), then your snapshot will look exactly the same, and all you'll change is your commit message.

### Unstaging a Staged File

The next two sections demonstrate how to work with your staging area and working directory changes.

Right below the "Changes to be committed" text, it says use `git reset HEAD <file>` to unstage.

### Unmodifying a Modified File

What if you realize that you don't want to keep your changes to the `CONTRIBUTTING.md` file? How can you easily unmodify it - revert it back to what it looked like when you last committed?

```
git checkout -- CONTRIBUTTING.md
```

It's important to understand that `git checkout -- <file>` is a dangerous command. Any local changes you made to that file are gone - Git just replaced that file with the last staged or committed version.

Remember, anything that is committed in Git can almost always be recovered. Even commits that were on branches that were deleted or commits that were overwritten with an `--amend` commit can be recovered.

### Undoing things with git restore

Git version 2.23.0 introduced a new command: `git restore`. It's basically an alternative to `git reset` which we just covered.

Let's retrace our step, and undo things with `git restore` instead of `git reset`.

#### Unstaging a Staged File with git restore

Right below the "Changes to be committed" text, it says use `git restore --staged <file>` to unstage. So, let's use that advice to unstage the `CONTRIBUTTING.md` file.

```
git restore --staged CONTRIBUTTING.md
```

#### Unmodifying a Modified File with git restore

How can you easily unmodify it - revert it back to what it looked like when you last committed? Luckily, `git status` tells you how to do that, too.

It tells you pretty explicitly how to discard the changes you've made. Let's do what it says.

```
git restore CONTRIBUTTING.md
```

It's important to understand that `git restore <file>` is a dangerous command. Any local changes you made to that file are gone - Git just replaced that file with the last staged or committed version. Don't ever use this command unless you absolutely know that you don't want those unsaved local changes.

### Working with Remotes

To be able to collaborate on any Git project, you need to know how to manage your remote repositories.

#### Showing Your Remotes

To see which remote servers you have configured, you can run the `git remote` command. It lists the shortnames of each remote handle you've specified. If you've cloned your repository, you should at least see `origin` - that is the default name Git gives to the server you cloned from.

```
git remote
```

You can also specify `-v`, which shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote.

```
git remote -v
```

If you have more than one remote, the command lists them all.

#### Adding Remote Repositories

We've mentioned and given some demonstrations of how the `git clone` command implicitly adds the `origin` remote for you. To add a new remote Git repository as a shortname you can reference easily, run `git remote add <shortname> <url>`.

```
git remote add pd http://github.com/paulboone/ticgit
git remote -v
```

#### Fetching and Pulling from Your Remotes

As you just saw, to get data from your remote projects, you can run:

```
git fetch <remote>
```

The command goes out to that remote project and pulls down all the data from that remote project that you don't have yet. After you do this, you should have references to all the branches from that remote, which you can merge in or inspect at any time.

If you clone a repository, the command automatically adds that remote repository under the name "origin". So, `git fetch origin` fetches any new work that has been pushed to that server since you cloned (or last fetched from) it. 

It's important to note that the `git fetch` command only downloads the data to your local repository - it doesn't automatically merge it with any of your work or modify what you're currently working on. You have to merge it manually into your work when you're ready.

If your current branch is set up to trach a remote branch, you can use the `git pull` command to automatically fetch and then merge that remote branch into your current branch. This may be an easier or more comfortable workflow for you; and by default, the `git clone` command automatically sets up your local `master` branch to track the remote `master` branch on the server you cloned from. Running `git pull` generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.

#### Pushing to Your Remotes

When you have your project at a point that you want to share, you have to push it upstream.

```
git push <remote> <branch>
```


#### Inspecting a Remote

If you want to see more informatNATTYNATTion about a particular remote, you can use the `git remote show <remote>` command. If you run this command with a particular shortname, such as `origin`, you get something like this:

```
git remote shoe origin
```

This command shows which branch is automatically pushed to when you run `git push` while on certain branches.

#### Renaming and Removing Remotes

You can run `git remote rename` to change a remote's shortname. For instance, if you want to rename *pd* to *paul*, you can do so with `git remote rename`:

```
git remote rename pd paul
```

### Tagging

#### Listing Your Tags

Listing the existing tags in Git in straightforward. Just type `git tag` (with optional `-l` or `--list`):

```
git tag
```

You can also search for tags that match a particular pattern. The Git source repo, for instance, contains more than 500 tags. If you're interested only in looking at the 1.8.5 series, you can run this:

```
git tag -l "v1.8.5*"
```

#### Creating Tags

Git supports two types of tags: *lightweight* and *annotated*.

A *lightweight* tag is very much like a branch that doesn't change - it's just a pointer to specific commit.

Annotated tags, however, are stored as full objects in the Git database. They've checksummed; contain the tagger name, email, and date.

It's generally recommended that you create annotated tags so you can have all this information; but if you want a temporary tag or for some reason don't want to keep the other information, lightweight tags are avaiable too.

##### Annotated Tags

Creating an annotated tag in Git is simple. The easiest way is to specify `-a` when you run the `tag` command:

```
git tag -a v1.4 -m "my version 1.4"
git tag
```

The `-m` specifies a tagging message, which is stored with the tag.

You can see the tag data along with the commit that was tagged by using the `git show` command:

```
git show v1.4
```

##### Lightweight Tags

Another way to tag commits is with a lightweight tag. This is basically the commit checksum stored in a file - no other information is kept. To create a lightweight tag, don't supply any of the `-a`, `-s`, or `-m` options, just provide a tag name.

```
git tag v1.4-lw
git tag
```

This time, if you run `git show` on the tag, you don't see the extra tag information. The command just shows the commit.

#### Tagging Later

Now, suppose you forgot to tag the project at v1.2, which was at the "Update rakefile" commit. You can add it after the fact. To tag that commit, you specify the commit checksum at the end of the command:

```
git tag -a v1.2 9fceb02
```


#### Sharing Tags

By default, the `git push` command doesn't transfer tags to remote servers. You will have to explicitly push tags to a shared server after you have created them. 

This process is just like sharing remote braches.

```
git push origin <tagname>
```

If you have a lot of tags that you want to push up at once, you can also use the `--tags` option to the `git push` command.

`git push <remote> --tags` will push both `lightweight` and `annotated` tags. There is currently no option to push only lightweight tags, but if you use `git push <remote> --follow-tags` only annotated tags will be pushed to the remote.

#### Deleting Tags

To delete a tag on your local repository, you can use `git tag -d <tagname>`.

```
git tag -d v1.4-lw
```

The first variation is `git push <remote> :refs/tags/<tagname>`:

The way to interpret the above is to read it as the null value before the colon is being pushed to the remote tag name, effectively deleting it.

The second (and more intuitive) way to delete a remote tag is with:

```
git push origin --delete <tagname>
```

#### Checking out Tags

If you want to view the version of files a tag is pointing to, you can do a `git checkout` of that tag, although this puts your repository in "detached HEAD" state, which has some ill side effects.

```
git checkout v2.0.0
```

In "detached HEAD" state, if you make changes and then create a commit, the tag will stay the same, but your new commit won't belong to any branch and will be unreachable, except by the exact commit hash. Thus, if you need to make changes - say you're fixing a bug on an older version, for instance - you will generally want to create a branch.

```
git checkout -b version2 v2.0.0
```

If you do this and make a commit, your `version2` branch will be slightly different than your `v2.0.0` tag since it will move forward with your new changes, so do be careful.

### Git Aliases

If you don't want to type the entire text of each of the Git commands, you can easily set up an alias for each command using `git config`.

```
git config --global alias.so checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

This means that, for example, instead of typing `git commit`, you just need to type `git ci`.

```
git unstage fileA
git reset HEAD -- fileA
```

```
git config --global alias.last 'log -1 HEAD'
```

As you can tell, Git simply replaces the new command with whatever you alias it for. However, maybe you want to run an external command, rather than a Git subcommand. In that case, you start the command with a `!` character. This is useful if you write your own tools that work with a Git repository. We can demonstrate by aliasing `git visual` to run `gitk`:

```
git config --global alias.visual '!gitk'
```

## Git Branching

Unlike many other VCSs, Git encourages workflows that branch and merge often, even multiple times in a day. Understanding and mastering this feature gives you a powerful and unique tool and can entirely change the way that you develop.

### Branches in a Nutshell

To really understand the way Git does branching, we need to take a step back and examine how Git stores its data.

Git doesn't store data as a series of changesets or differences, but instead as a series of *snapshots*.

When you make a commit, Git stores a commit object that contains a pointer to the snapshot of the content you staged. This object also contains the author's name and email address, the message that you typed, and pointers to the commit or commits that directly came before this commit: zero parents for the initial commit, one parent for a normal commit, and multiple parents for a commit that results from a merge of two or more branches.

A branch in Git is simply a lightweight movable pointer to one of these commits. Every time you commit, the `master` branch pointer moves forward automatically.

#### Creating a New Branch

What happens when you create a new branch? Well, doing so creates a new pointer for you to move around.

```
git branch testing
```

This creates a new pointer to the same commit you're currently on.

How does Git know what branch you're currently on? It keeps a special pointer called `HEAD`. Note that this is a lot different than the concept of `HEAD` in other VCSs you may be used to. In Git, this is a pointer to the local branch you're currently on.

You can easily see this by running a simple `git log` command that shows you where the branch pointers are pointing. This option is called `--decorate`.

```
git log --oneline --decorate
```

#### Switching Branches

To switch to an existing branch, you run the `git checkout` command. Let's switch to the new `testing` branch:

```
git checkout testing
```

This moves `HEAD` to point to the `testing` branch.

Now, let's do another commit. This is interesting, because now your `testing` branch has moved forward, but your `master` branch still points to the commit you were on when you ran `git checkout` to switch branch.

Let's switch back to the master branch:

```
git checkout master
```

`git log` doesn't show all the branches all the time.

If you were to run `git log` right now, you might wonder where the "testing" branch you just creaed went, as it would not appear in the output.

To show commit history for the desired branch you have to explicitly specify it; `git log testing`. To show all of the branches, add `--all` to your `git log` command.

That command did two things. It moved the `HEAD` pointer back to point to the `master` branch, and it reverted the files in your working directory back to the snapshot that `master` points to.

It essentially rewinds the work you've done in your `testing` branch so you can go in a different direction.

Now, you make a few changes and commit again. Your project history has diverged. You create and switched to a branch, did some work on it, and then switched back to your branch and did other work. Both of those changes are isolated in separate branches, you can switch back and forth between the branches and merge them together when you've ready.

You can also see this easily with the `git log` command. If you run `git log --oneline --decorate --graph --all`, it will print out the history of your commits, showing where your branch pointers are and how your history has diverged.

```
git log --oneline --decorate --graph --all
```

Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy. Creating a branch is as quick and simple as writing 41 bytes to a file.

*Creating a new branch and switching to it at the same time*

It's typical to create a new branch and want to switch to that new branch at the same time - this can be done in one operation with `git checkout -b <newbranchname>`

You can use `git switch` instead of `git checkout` to:

  - Switch to an existing branch: `git switch testing-branch`
  - Create a new branch and switch to it: `git switch -c new-branch`. The `-c` flag stands for create, you can also use the full flag: `--create`.
  - Return to your previously checked our branch: `git switch -`.

## Basic Branching and Merging

Let's go through a simple example of branching and merging with a workflow that you might use in the real world. You'll follow these steps:

1. Do some work on a website.
2. Create a branch for a new user story you've working on.
3. Do some work in that branch.

At this stage, you'll receive a call that another issue is critical and you need a hotfix. You'll do the following:

1. Switch to your production branch.
2. Create a branch to add the hotfix.
3. After it's tested, merge the hotfix branch, and push to production.
4. Switch back to your original user story and continue working.

### Basic Branching

First, let's say you've working on your project and have a couple of commits already on the `master` branch.

You've decide that you've going to work on issue #53 in whatever issue-tracking system your company uses. To create a new branch and switch to it at the same time, you can run the `git checkout` command with the `-b` switch:

```
git checkout -b iss53
```

Now you get the call that there is an issue with the website, and you need to fix it immediately. With Git, you don't have to deploy your fix along with the `iss53` changes you've made. All you have to do is switch back to your `master` branch.

However, before you do that, note that if your working directory or staging area has uncommitted changes that conflict with the branch you've checking out, Git won't let you switch branches. It's best to have a clean working state when you switch branches. There are ways to get around this that we'll cover later on, in *Stashing and Cleaning*. For now, let's assume you've committed all your changes, so you can switch back to your `master` branch:

```
git checkout master
```

Next, you have a hotfix to make. Let's create a `hotfix` branch on which to work until it's completed:

```
git checkout -b hotfix
git commit -a -m 'Fix broken email address'
```

You can run your tests, make sure the hotfix is what you want, and finally merge the `hotfix` branch back into your `master` branch to deploy to production. You do this with the `git merge` command:

```
git checkout master
git merge hotfix
```

You'll commit the phrase "fast-forward" in that merge. Because the commit `C4` pointed to by the branch `hotfix` you merged in was directly ahead of the commit `C2` you're on, Git simple moves the pointer forward.

To phrase that another way, when you try to merge one commit with a commit that can be reached by following the first commit's history, Git simplifies things by moving the pointer forward.

After your super-important fix is deployed, you've ready to switch back to the work you were doing before you were interrupted. However, first you'll delete the `hotfix` branch, because you no longer need it - the `master` branch points at the same place.

You can delete with the `-d` option to `git branch`.

```
git branch -d hotfix
```

Now you can swith back to your work in process branch on issue #53.

```
git checkout iss53
```

If you need to pull it in, you can merge your `master` branch into your `iss53` branch by running `git merge master`.

### Basic Merging

Suppose you decided that your `iss53` work is complete and ready to be merged into your `master` branch. *All you have to do is check out the branch you wish to merge into and then run the `git merge` command.*

```
git checkout master
git merge iss53
```

Because the commit on the branch you're on isn't a direct ancestor of the branch you're merging in, Git has to do some work.

In this case, Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.

Instead of just moving the branch pointer forward, Git creates a new snapshot that results from this three-way merge and automatically creates a new commit that points to it. This is referred to as a merge commit, and is special in that it has more than one parent.

### Basic Merge Conflicts

Occasionally, this process doesn't go smoothly. If you changed the same part of the same file different in the two branches you've merging, Git won't be able to merge them cleanly. If your fix for issue #53 modified the same part of a file as the `hotfix` branch, you'll get a merge conflix that looks something like this.

Git hasn't automatically created a new merge commit. It has paused the process while you resolve the conflict. If you want to see which files are unmerged at any point after a merge conflict, you can run `git status`.

Anything that has merge conflicts and hasn't been resolved is listed as unmerged. Git adds standard conflict-resolution markers to the files that have conflicts, so you can open them manually and resolve those conflicts.

This means the version in `HEAD` (your `master` branch, because that was what you had checked out when you ran your merge command) is the top part of that block (everything above the *=======* ), while the version in your `iss53` branch looks like everything in the bottom part. In order to resolve the conflict, you have to either choose one side or the other or merge the contents yourself.

This resolution has a little of each section, and the `<<<<<<`, `=========`, and `>>>>>>>>` lines have been completely removed. After you've resolved each of these sections in each conflicted file, run `git add` on each file to mark it as resolved. Staging the file marks it as resolved in Git.

If you want to use a graphical tool to resolve these issues, you can run `git mergetool`, which fires up an appropriate visual merge tool and walks you through the conflict.

If you've happy with that, and you verify that everything that had conflicts has been staged, you can type `git commit` to finalize the merge commit.

### Branch Management

Now that you've created, merged, and deleted some branches, let's look at some branch management tools that will come in handy when you begin using branches all the time.

The `git branch` command does more than just create and delete branches. If you run it with no arguments, you get a simple listing of your current branches.

```
git branch
```

To see the last commit on each branch, you can run:

```
git branch -v
```

The useful `--merged` and `--no-merged` options can filter this list to branches that you have or have not yet merged into the branch you've currently on. To see which branches are already merged into the branch you've on, you can run:

```
git branch --merged
```

Because you already merged in `iss53` earlier, you see it in your list. Branches on this list without the `*` in front of them are generally fine to delete with `git branch -d`; you 've already incorporated their work into another branch, so you're not going to lose anything.

To see all the branches that contain work you haven't yet merged in, you can run:

```
git branch --no-merged
```

This shows your other branch. Because it contains work that isn't merged in yet, trying to delete it with `git branch -d` will fail.

If you really do want to delete the branch and lose that work, you can force it with `-D`.

### Changing a branch name

Suppose you have a branch that is called `bad-branch-name` and you want to change it to `corrected-branch-name`, while keeping all history.

Rename the branch locally with the `git branch --move` command.

```
git branch --move bad-branch-name corrected-branch-name
```

This replaces your `bad-branch-name` with `corrected-branch-name`, but this change is only local for now. To let other see the corrected branch on the remove, push it.

```
git push --set-upstream origin corrected-branch-name
```

You can check the branch again by `git branch`.

```
git branch --all
```

Notice that you're on the branch `corrected-branch-name` and it's avaiable on the remote. However, the branch with the bad name is also still present there but you can delete it by executing the follow command:

```
git push origin --delete bad-branch-name
```

#### Changing the master branch name

Rename your local `master` branch into `main` with the following command.

```
git branch --move master main
```

There is no local `master` branch anymore, because it's renamed to the `main` branch.

To let other see the new `main` branch, you need to push it to the remote. This makes the renamed branch avaiable on the remote.

```
git push --set-upstream origin main
```

Now you have a few more tasks in front of you to complete the transition:

1. Any projects that depend on this one will need to update their code and/or configuration.
1. Update any test-runner configuration files.
1. Adjust build and release scripts.
1. Redirect settings on your repo host for things like the repo's default branch, merge rules, and other things that match branch names.
1. Update references to the old branch in documentation.
1. Close or merge any pull requests that target the old branch.

After you've done all these tasks, and are certain the `main` branch performs just as the `master` branch, you can delete the `master` branch.

```
git push origin --delete master
```

### Branching Workflows

#### Long-Running Branches

Because Git uses a simple three-way merge, merging from one branch into another multiple times over a long period is generally easy to do. This means you can have several branches that are always open and that you use for different stages of your development cycle; you can merge regularly from some of them into others.

Many Git developers have a workflow that embraces this approach, such as having only code that is entirely stable in their `master` branch - possible only code that has been or will be release.

They have another parallel branch named `develop` or `next` that they work from or use to test stability - it isn't necessarily always stable, but whenever it gets to a stable state, it can be merged into `master`.

It's used to pull in topic branches (short-lived branches, like your earlier `iss53` branch) when they're ready, to make sure they pass all the tests and don't introduce bugs.

#### Topic Branches

Topic branches, however, are useful in projects of any size. A topic branch is a short-lived branch that you create and use for a single particular feature or related work. This is something you've likely never done with a VCS before because it's generally too expensive to create and merge branches.

#### Remote Branches

Remote references are references (pointers) in your remote repositories, including branches, tags, and so on. You can get a full list of remote references explicitly with `git ls-remote <remote>`, or `git remote show <remote>`.

Remote-tracking branches are references to the state of remote branches. Git moves them for you whenever you do any network communication, to make sure they accurately represent the state of the remote repositories.

Remote-tracking branch names take the form `<remote>/<branch>`. For instance, if you wanted to see what the `master` branch on your `origin` remote looked like as of the last time you communicated with it, you would check the `origin/master` branch.

If you do some work on your local `master` branch, and, in the meantime, someone else pushes to `git.ourcompany.com` and updates its `master` branch, then your histories move forward differently. Also, as long as you stay out of contact with your `origin` server, your `origin/master` pointer doesn't move.

To synchronize your work with a given remote, you run a `git fetch <remote>` command (in our case, `git fetch origin`). This command looks up which server "origin" is (in this case, it's `git.ourcompany.com`), fetches any data from it that you don't yet have, and updates your local database, moving your `origin/master` pointer to its new, more up-to-date position.

To demonstrate having multiple remote servers and what remote branches for those remote projects look like, let's assume you have another internal Git server that is used only for development by one of your sprint teams. This server is at `git.team1.ourcompany.com`. You can add it as a new remote reference to the project you've currently working on by running the `git remote add` command. Name this remote `teamone`, which will be your shortname for that whole URL.

Now, you can run `git fetch teamone` to fetch everything the remote `teamone` server has that you don't have yet. Because that server has a subset of data your `origin` server has right now, Git fetches no data but sets a remote-tracking branch called `teamone/master` to point to the commit that `teamone` has as its `master` branch.

#### Pushing

When you want to share a branch with the world, you need to push it up to a remote to which you have write access. Your local branchs aren't automatically synchronized to the remotes you write to - you have to explicitly push the branches you want to share. That way, you can use private branches for work you don't want to share, and push up only the topic branches you want to collaborate on.

If you have a branch named `serverfix` that you want work on with others, you can push it up the same way you pushed your first branch. Run `git push <remote> <branch>`.

```
git push origin serverfix
```

This is a bit of a shortcut. Git automatically expands the `serverfix` branchname out to `refs/heads/serverfix:refs/heads/serverfix`, which means, "Take my `serverfix` local branch and push it to update the remote's `serverfix` branch".

If you didn't want it to be called `serverfix` on the remote, you could instead run `git push origin serverfix:awesomebranch` to push your local `serverfix` branch to the `awesomebranch` branch on the remote project.

You can set up a `credential cache`. The simplest is just to keep it in memory for a few minutes, which you can easily set up by running `git config --global credential.helper cache`.

The next time one of your collaborators fetches from the server, they will get a reference to where the server's version of `serverfix` is under the remote branch `origin/serverfix`.

To merge this work into your current working branch, you can run `git merge origin/serverfix`. If you want your own `serverfix` branch that you can work on, you can base it off your remote-tracking branch.

```
git checkout -b serverfix origin/serverfix
```

#### Tracking Branches

Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks it called an "upstream branch").

If you're on a tracking branch and type `git pull`, Git automatically knows which server to fetch from and which branch to merge in.

When you clone a repository, it generally automatically creates a `master` branch that tracks `origin/master`. However, you can set up other tracking branches if you wish. The simple case is the example you just saw, running `git checkout -b <branch> <remote>/<branch>`. This is a common enough operation that Git provides the `--track` shorthand.

```
git checkout --track origin/serverfix
```

In fact, this is so common that there's even a shortcut for that shortcut. If the branch name you're trying to checkout (a) doesn't exist and (b) exactly matches a name on only one remote, Git will create a tracking branch for you.

```
git checkout serverfix
```

To set up a local branch with a different name than the remote branch, you can easily use the first version with a different local branch name.

```
git checkout -b sf origin/serverfix
>>> Branch serverfix set up to track remote branch serverfix from origin.
>>> Switched to a new branch `serverfix`
```

Now, your local branch `sf` wil automatically pull from `origin/serverfix`

If you already have a local branch and want to set it to a remote branch you just pulled down, or want to change the upstream branch you're tracking, you can use the `-u` or `--set-upstream-to` option to `git branch` to explicitly set it at any time.

```
git branch -u origin/serverfix
>>> Branch serverfix set up to track remote branch serverfix from origin.
```

#### Pulling

While the `git fetch` command will fetch all the changes on the server that you don't have yet, it will not modify your working directory at all. It will simply get the data for you and let you merge it yourself.

However, there is a command called `git pull` which is essentially a `git fetch` immediately followed by a `git merge` in most case.

If you have a tracking branch set up as demonstrated in the last section, either by explicitly setting it or by having it created for you by the `clone` or `checkout` commands, `git pull` will look up what server and branch your current branch is tracking, fetch from that server and then try to merge in that remote branch.

#### Deleting Remote Branches

Suppose you're done with a remote branch - say you and your collaborators are finish with a feature and have merged it into your remote's `master` branch (or whatever branch your stable codeline is in).

You can delete a remote branch using the `--delete` option to `git push`. If you want to delete your `serverfix` branch from the server, you can run the following:

```
git push origin --delete serverfix
```

### Rebasing

In Git, there are two main ways to integrate changes from one branch into another: the `merge` and the `rebase`.

#### The Basic Rebase

If you go back to an earlier example from `Basic Merging`, you can see that you diverged your work and made commits on two different branches.

The easiest way to integrate the branches, as we're already covered, is the `merge` command. It performs a three-way merge between the two latest branch snapshots (`C3` and `C4`) and the most recent common ancestor of the two (`C2`), creating a new snapshot (and commit).

However, there is another way: you can take the patch of the change that was introduced in `C4` and reapply it on top of `C3`.In Git, this is called `rebasing`. With the `rebase` command, you can take all the changes that were committed on one branch and replay them on a different branch.

For this example, you would check out the `experiment` branch, and then rebase it onto the `master` branch as follows:

```
git checkout experiment
git rebase master
>>> First, rewinding head to replay your work on top of it ...
>>> Applying: added staged command
```

This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, and finally applying each change in turn.

At this point, you can go back to the `master` branch and do a fast-forward merge.

```
git checkout master
git merge experiment
```

Now, the snapshot pointed to by `C4'` is exactly the same as the one that was pointed to by `C5` in `the merge example`. There is no difference in the end product of the integration, but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history.

Often, you'll do this to make sure your commits apply cleanly on a remote branch - perhaps in a project to which you're trying contribute but that you don't maintain. In this case, you'd do your work in a branch and then rebase your work onto `origin/master` when you were ready to submit your patches to the main project. That way, the maintainer doesn't have to do any integration work - just a fast-forward or a clean apply.

#### More Interesting Rebases

You can also have your rebase replay on something other than the rebase target branch. You branched a topic branch `server` to add some server-side functionality to your project, and made a commit. Then, you branched off that to make the client-side changes `client` and committed a few times. Finally, you went back to your `server` branch and did a few more commits.

Suppose you decide that you want to merge your client-side changes until it's tested further. You can take the changes on `client` that aren't on `server` (`C8` and `C9`) and replay them on your `master` branch by using the `--onto` option of `git rebase`.

```
git rebase --onto master server client
```

This basically says, "Take the `client` branch, figure out the patches since it diverged from the `server` branch, and replay these patches in the `client` branch as if it was based directly off the `master` branch instead".

Now, you can fast-forward your `master` branch:

```
git checkout master
git merge client
```

Let's say you decide to pull in your `server` branch as well. You can rebase the `server` branch onto the `master` branch without having to check it out first by running `git rebase <basebranch> <topicbranch>` - which checks out the topic branch (in this case, `server`) for you and replays it onto the base branch (`master`).

```
git rebase master server
```

This replays your `server` work on top of your `master` work.

Then, you can fast-forward the base branch (`master`).

```
git checkout master
git merge server
```

You can remove the `client` and `server` branches because all the work is integrated and you don't need them anymore, leaving your history for this entire process looking like `Final commit history`.

```
git branch -d client
git branch -d server
```

#### The Perils of Rebasing

    Do not rebase commits that exist outside your repository and that people may have based work on.

If you follow that guideline, you'll be fine. If you don't, people will hate you, and you'll be scorned by friends and family.

When you rebase stuff, you're abandoning existing commits and creating new ones that are similar but different. If you push commits somewhere and others pull them down and base work on them, and then you rewrite those commits with `git rebase` and push them up again, your collaborators will have to re-merge their work and things will get messy when you try to pull their work back into yours.

Let's look at an example of how rebasing work that you've made public can cause problems. Suppose you clone from a central server and then do some work off that.

Now, someone else does more work that includes a merge, and pushes that work to the central server. You fetch it and merge the new remote branch into your work.

Next, the person who pushed the merged work decides to go back and rebase their work instead; they do a `git push --force` to overwrite the history on the server. You then fetch from that server, bringing down the new commits.

Now you're both in a pickle. If you do a `git pull`, you'll create a merge commit which includes both lines of history, and your repository will be very crazy.

If you run a `git log` when your history looks like this, you'll see two commits that have the same author, date, and message, which will be confusing. Furthermore, if you push this history back up to the server, you'll reintroduce all those rebased commits to the central server, which can further confuse people. It's pretty safe to assume that the other developer doesn't want `C4` and `C6` to be in the history; that's why they rebased in the first place.

#### Rebase When You Rebase

If you **do** find yourself in a situation like this, Git has some further magic that might help you out. If someone on your team force pushes changes that overwrite work that you've based work on, your challenge is to figure out what is yours and what they've rewritten.

It turns out that in addition to the commit SHA-1 checksum, Git also calculates a checksum that is based just on the patch introduced with the commit. This is called a `patch-id`.

If you pull down work that was rewritten and rebase it on top of the new commits from your partner, Git can often successfully figure out what is uniquely yours and apply them back on top of the new branch.

For instance, in the previous scenario, if instead of doing a merge when we're at `Someone pushes rebased commits, abandoning commits you've based your work on` we run `git rebase teamone/master`, Git will:

- Determine what work is unique to our branch (`C2, C3, C4, C6, C7`).
- Determine which are not merge commits (`C2, C3, C4`).
- Determine which have not been rewritten into the target branch (just `C2` and `C3`, since `C4` is the same patch as `C4'`)
- Apply those commits to the top of `teamone/master`.

So instead of the result we see in `You merge in the same work again into a new merge commit`, we would end up with something more like `Rebase on top of force-pushed rebase work`.

This only works if `C4` and `C4'` that your partner made are almost exactly the same patch.

You can also simplify this by running a `git pull --rebase` instead of a normal `git pull`. Or you could do it manually with a `git fetch` followed by a `git rebase teamone/master` in this case.

#### Rebase vs Merge

Now that you've seen rebasing and merging in action, you may be wondering which one is better. Before we can answer this, let's step back a bit and talk about what history means.

One point of view on this is that your repository's commit history is a `record of what actually happened`. It's a historical document, valuable in its own right, and shouldn't be tampered with. From this angle, changing the commit history is almost blashphemous; you're lying about what actually transpired. So what if there was a messy series of merge commits?

The opposing point of view is that the commit history is the `story of how your project was made`. You wouldn't publish the first draft of a book, so why show your messy work? When you're working on a project, you may need a record of all your missteps and dead-end paths, but when it's time to show your work to the world, you may want to tell a more coherent story of how to get from A to B.

People in this camp use tools like `rebase` and `filter-branch` to rewrite their commits before they're merged into the mainline branch. They use tools like `rebase` and `filter-branch`, to tell the story in the way that's best for future readers.

Now, to the question of whether merging or rebasing is better: hopefully you'll see that it's not that simple. Git is a powerful tool, and allows you to do many things to and with your history, but every team and every project is different. Now that you know how both of these things work, it's up to you to decide which one is the best for your particular situation.

You can get the best of both worlds: rebase local changes before pushing to clean up your work, but never rebase anything that you've pushed somewhere.

## Git on the Server

### The Protocols

Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git. Here we'll discuss what they are and in what basic circumstances you would want (or not want) to use them.

#### Local Protocol

The most basic is the *Local protocol*, in which the remote repository is in another directory on the same host. This is often used if everyone on your team has access to a shared filesystem such as an `NFS` mount, or in the less likely case that everyone logs in to the same computer. The latter wouldn't be ideal, because all your code repository instances would reside on the same computer, making a catastrophic loss much more likely.

If you have a shared mounted filesystem, then you can clone, push to, and pull from a local file-based repository. To clone a repository like this, or to add one as a remote to a existing project, use the path to the repository as the URL. For example, to clone a local repository, you can run something like this:

```
git clone /srv/git/project.git
git clone file:///srv/git/project.git
```

Git operates slightly differently if you explicitly specify `file://` at the beginning of the URL. If you just specify the path, Git tries to use hardlinks or directly copy the files it needs.

The main reason to specify the `file://` prefix is if you want a clean copy of the repository with extraneous references or objects left out - generally after an import from another VCS or something similar.

To add a local repository to an existing Git project, you can run something like this:

```
git remote add local_proj /srv/git/project.git
```

##### The Pros

The pros of file-based repositories are that they're simple and they use existing file permissions and network access. If you already have a shared filesystime to which your whole team has access, setting up a repository is very easy. You stick the base repository copy somewhere everyone has shared access to and set the read/write permissions as you would for any other shared directory.

This is also a nice option for quickly grabbing work from someone else's working repository. If you and a co-worker are working on the same project and they want you to check something out, running a command like `git pull /home/john/project` is often easier than them pushing to a remote server and you subsequently fetching from it.

##### The Cons

The cons of this method are that shared access is generally more difficult to set up and reach from multiple locations than basic network access. If you want to push from your laptop when you're at home, you have to mount the remote disk, which can be difficult and slow compared to network based access.

It's important to mention that this isn't necessarily the fastest option if you're using a shared mount of some kind. A local repository is fast only if you have fast access to the data. A repository on `NFS` is often slower than the repository over `SSH` on the same server, allowing Git to run off local disks on each system.

Finally, this protocol does not protect the repository against accidental damage. Every user has full shell access to the `remote` directory, and there is nothing preventing them from changing or removing internal Git files and corrupting the repository.

#### The HTTP Protocols

Git can communicate over HTTP using two different modes. Prior to `Git 1.6.6`, there was only one way it could do this which was very simple and generally read-only. In `version 1.6.6`, a new, smarter protocol was introduced that involved Git being able to intelligently negotiate data transfer in a manner similar to how it does over SSH. In the last few years, this new `HTTP protocol` has become very popular since it's simpler for the user and smarter about how it communicates. The newest version is often referred to as the `Smart HTTP protocol` and the older way as `Dumb HTTP`. We'll cover the newest `Smart HTTP` protocol first.

##### Smart HTTP

`Smart HTTP` operates very similarly to the SSH or Git protocols but runs over standard `HTTPS ports` and can use various `HTTP authentication mechanism`, meaning it's often easier on the user than something like SSH, since you can use things like username/password authentication rather than having to set up SSH keys.

##### Dumb HTTP

If the server does not respond with a Git HTTP smart service, the Git client will try to fall back to the simpler `Dumb HTTP protocol`. The `Dumb protocol` expects the bare Git repository to be served like normal files from the web server. The beauty of `Dumb HTTP` is the simplicity of setting it up.

##### The Pros

The simplicity of having a single URL for all types of access and having the server prompt only when authentication is needed makes things very easy for the end user. Being able to authenticate with a username and password is also a big advantage over SSH, since users don't have to generate SSH keys locally and upload their public key to server before being able to interact with it.

##### The Cons

Git over `HTTPS` can be a little more tricky to set up compared to SSH on some servers. Other than that, there is very little advantage that other protocols have one `Smart HTTP` for serving Git content.

If you are using `HTTP` for authenticated pushing, providing your credentials is sometimes more complicated than using keys over SSH. However, several credential caching tools you can use. Read Credential Storage.

#### The SSH Protocol

A common transport protocol for Git when self-hosting is over SSH. This is because SSH access to servers is already set up in most places. SSH is also an authenticated network protocol and because it's ubiquitous, it's generally easy to set up and use.

To clone a Git repository over SSH, you can specify an `ssh://` URL like this:

```
git clone ssh://[user@]server/project.git
git clone [user@]server/project.git
```

##### The Pros

The pros of using SSH are many. First, SSH is relatively easy to set up. Next, access over SSH is secure - all data transfer is encrypted and authenticated. Last, like the `HTTPS`, `Git` and `Local protocols`, SSH is efficient, making the data as compact as possible before transferring it.

##### The Cons

The negative aspect of SSH is that it doesn't support anonymous access to your Git repository. If you're using SSH, people `must` have SSH access to your machine, even in a read-only capacity.

#### The Git Protocol

##### The Pros

The Git protocol is often the fastest network transfer protocol avaiable. If you're serving a lot of traffic for a public project or serving a very large project that doesn't require user authentication for read access, it's likely that you'll want to set up a Git daemon to serve your project.

##### The Cons

Due to the lack of TLS or other cryptography, cloning over `git://` might lead to an arbitrary code execution vulnerability, and should therefore be avoided unless you know what you doing.

If you run `git clone git://example.com/project.git`, an attacker who controls e.g your router can modify the repo you just cloned, inserting malicious code into it. Running `git clone http://example.com/project.git` should be avoided for the same reason.






