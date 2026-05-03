# Nvim cheat sheet

## Motion master

Command + Count + Motion. Command likes d, c, y, v.

Using `h, j, k, l` to move left, down, up, right.

```
    w   jump by start of words (punctuation considered words)
    W   jump by words (spaces separate words)
    e   jump to end of words (punctuation considered words)
    E   jump to end of words (no punctuation)
```

Using `i` for inserting, the insert mode will apply before the cursor.

Using `I` for inserting, the insert mode will apply beginning of the line.

Using `a` for append, the insert mode will apply after the cursor.

Using `A` for append, the insert mode will apply after line.

Using `w` for jumping forward to the next word, move to the beginning of the word.

Using `b` for jumping backward to the last word, move to the beginning of the word.

Using `e` for jumping forward to the next word, move to the end of the word.

Using `0` for jumping to the beginning of the line.

Using `$` for jumping to the end of the line.

Using `^` or `_` for jumping to the first character of the line.

Using `f` for finding the character and moving the the character. Using `t` for finding the character and moving to the before character. Using `;` to repeat find forward. Using `,` to repeat find backward.

Using `F` for finding the backward character. Using `T` for finding the backward character and move to the next to position.

Using `df` + <character> or `dt` + <character> to delete all the text to or reach the target.

Using `d` + <number> + `f` + <character> or `d` + <number> + `t` + <character> to delete all the text to or reach the target.

Using `yf` + <character> or `yt` + <character> to yank all the text to or reach the target.

You can use number with `f` to move to the character.

```
    4ft --> move to the fouth t character.
```

Using `==` for auto format the code.

Using `gg` for moving to the beginning of the file.

Using `shift + g` for moving to the end of the file.

Using `dw` to delete a word.

Using `dd` to delete a line.

Using `u` to undo.

Using `shift + r` to replace until you want.

Using `yw` to yank a word.

Using `yy` to yank a line.

Using `yap` to yank a paragraph.

Using `p` to paste after the cursor.

Using `shift + p` to paste before the cursor.

Using `ctrl + r` to redo.

Using `shift + [` for moving forward to the next empty line. Using `shift + ]` for moving backward to the last empty line.

Using `%` for moving to the connected pair like (), [], {}.

Using `command + motion + range` for advantage motion.

```
    diw --> delete in word --> delete a word
    di` --> delete in `` --> delete everything in ``
    di( --> delete in () --> delete everything in ()
    da` --> delete around `` --> delete everything in `` and around that word
    yip --> yank in paragraph --> delete everything in `` and ``
    ci( --> change in ()
```

Using `.` for repeat the last action.

Using `o` for creating new line below.

Using `shift + v` for entering linewise visual mode, which is used to select and manipulate entire lines of text. To choose all the line.

Using `/` for searching forwards. Text `/` then is text what you want to find. Using `n` to next and `shift + n` to scroll backward.

Using `?` for searching backwards.

Replace in nvim. First, using visual mode to choose the paragraph. Then, type `:` and `s/<target>/<replaced text>/g`. The /g to make sure the result is globally fixed on all occurrences on all the selected lines.

Replace in nvim in other way. First, entering the command mode. Then, type `%s/<target>/<replaced text>/g`

`ctrl + v` is the visual block mode.

Using `zz` to move the window to center.

`shift + h`

`shift + m`

Using `Ctrl w v` to split window horizontal.

Using `Ctrl d` to page down and `Ctrl u` to page up.

Using `gg` to move to the beginning of file.

Using `Shift g` to move to the end of file.

Using `:` + <number> to move to the number line.

Using `y` to yank anything. Then, press `*` for searching and using `n` or `N` for moving forward and backward.

Using `vi{` for choose all the text inside {} or `va{` for choose everything and around {}, `viw` for choose only the word, `viW` for choosing all the big word until hit space. You can use y for yanking.

`Vy` and `yy` have the same function but `Vy` the cursor will move to the beginning of the line.

Using `v%` to highlight all the 

Using `va{` to highlight all the text and around {}. Then, using `Shift V` to hightlight all the lines. You can use `o` in visual mode to move backward and forward, go to the first line and last line.

Using `yap` for yanking the paragraph and all the empty lines around. You can use `dap` for delete the paragraph and all the empty lines around.

Using `>` + <number> + `j` or `k` for shift all the lines to the left.

You can using `ctrl` + `v` for entering V-block mode. Then, press `I` for entering insert mode. After, you text anything in the first line, all the other lines will apply the same structure.

Highlight by visual mode and text `:` to entering replace function. Then, text `s/$/";` to add "; to the end of all the highlight lines.After that, using `g ctrl a` to increase all the index. The other way to do the same thing is that using `vip` to highlight the paragraph.Then, using `:` to entering replace mode and text like this for replacing `:'<,'>s/\(\w.*\)/data[0] = "\1";`

You can use `ctrl a` to increasing the first element number in the line, better when using with visual mode.

`ctrl o`

