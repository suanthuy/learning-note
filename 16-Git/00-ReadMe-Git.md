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

## Your Identity

The first thing you should do when you install Git is to set your user name and email address. This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

	git config --global user.name "suanthuy"
	git config --global user.email suanthuy12@gmail.com

Again, you need to do only once if you pass the `--global` option, because then Git always use that information for your user on that system.

## Your default branch name

By default, Git will create a branch called `master` when you create a new repository with `git init`.

To set `main` as the default branch name:

	git config --global init.defaultBranch main





