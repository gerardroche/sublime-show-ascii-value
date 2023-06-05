# ShowAsciiValue

A Sublime Text plugin to show the [ASCII](https://en.wikipedia.org/wiki/ASCII) value of the character under the cursor in decimal, hexadecimal and octal, on the status bar.

## Installation

Close Sublime Text, then download or clone this repository to a directory named **ShowAsciiValue** in the Sublime Text Packages directory for your platform:

**Linux**

`git clone https://github.com/gerardroche/sublime-show-ascii-value.git ~/.config/sublime-text-3/Packages/ShowAsciiValue`

**OSX**

`git clone https://github.com/gerardroche/sublime-show-ascii-value.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/ShowAsciiValue`

**Windows**

`git clone https://github.com/gerardroche/sublime-show-ascii-value.git %APPDATA%\Sublime/ Text/ 3/Packages/ShowAsciiValue`

## Usage

The ASCII value of the character under the cursor is shown on the status bar in decimal, hexadecimal and octal.

For example, when the cursor is on a 'R':

```
<R>  82,  Hex 52,  Octal 122
```

The following special characters are shown as notation:

Character | Notation
:-------- | :-------
`\0` | <kbd>&lt;Nul&gt;</kbd>
`" "` | <kbd>&lt;Space&gt;</kbd>
`\t` | <kbd>&lt;Tab&gt;</kbd>
`\n` | <kbd>&lt;NL&gt;</kbd>

## License

Released under the [GPL-3.0-or-later License](LICENSE).
