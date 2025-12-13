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







