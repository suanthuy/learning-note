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

	git config --list --show-origin

### Your Identity

The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

	git config --global user.name "suanthuy"
	git config --global user.email suanthuy12@gmail.com

Again, you need to do only once if you pass the `--global` option, because then Git always use that information for your user on that system.

### Your default branch name

By default, Git will create a branch called `master` when you create a new repository with `git init`.

To set `main` as the default branch name:

	git config --global init.defaultBranch main

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

	git clone https://github.com/libgit2/libgit2

That creates a directory named `libgit2`, initializes a `.git` directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version.

If you want to clone the repository into a directory named something other than `libgit2`, you can specify the new directory name as an additional argument:

	git clone https://github.com/libgit2/libgit2 mylibgit

That command does the same thing as the previous one, but the target directory is called `mylibgit`.
### Recording Changes to the Repository







