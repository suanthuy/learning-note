## Fzf cheat sheet

Alternatively, you can use "git clone" the fzf repository to any directory and run install script.

```
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    ~/.fzf/install
```

Fuzzy find through your *command history*

```
    ctrl + r
```

Fuzzy find through the current directory. To choose multiple files, using TAB and then hit enter to complete the command.

```
    ctrl + t
```

Using $ sign to find all the file in the folder.

```
    ctrl + t
    .css$
    # Fuzzy will appear all the options.
```

Autocomplete, using ** and TAB. Fuzzy find will appear.

```
    cd **
```

