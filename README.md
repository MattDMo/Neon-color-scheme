# Neon Color Scheme

**Neon** is a colorful bright-on-black color scheme for [Sublime Text](https://www.sublimetext.com/) and [TextMate](http://www.macromates.com). In designing it, I've aimed to make as many languages as possible look as good as possible, taking advantage of as many of the available [scopes](https://www.sublimetext.com/docs/scope_naming.html) as I can. **Neon** was originally designed for [Python](http://www.python.org), which has a very detailed language definition, but lots of languages look good with it, like JavaScript, CSS, HTML, Ruby, PHP, shell scripts, XML, Clojure, Fortran, R, LaTeX, Markdown, reStructuredText, and more. It's also great when using [@wuub](https://github.com/wuub)'s fantastic [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL) plugin, which I can't say enough good things about.

Just for clarity's sake: **Neon** is an original work and wasn't based on any other color scheme. If you search [Package Control](https://packagecontrol.io) for [`neon`](https://packagecontrol.io/search/neon) you'll find some other, similarly-named color schemes which are *not* based on this project. Use them if you want -- I particularly like the [Dark Neon Color Scheme](https://packagecontrol.io/packages/Dark%20Neon%20Color%20Scheme), and might borrow some of the colors -- and if you want to fork this project and make your own derivative, go for it! I use the [MIT License](http://opensource.org/licenses/MIT) for a reason.

[![PythonImproved with Neon](https://pigimal.com/img/github/random.png)](https://packagecontrol.io/packages/Python%20Improved)

## Languages/Plugins Supported

Neon's main goal is to make as many languages as possible look as good as possible. That being said, there are some language/markup/framework-specific scopes and sections that you might be interested in:

* [Android Debug Bridge](https://packagecontrol.io/packages/ADBView)/[logcat](https://github.com/leesei/logcat.tmLanguage)
* Bison/YACC
* [BracketHighlighter](https://packagecontrol.io/packages/BracketHighlighter)
* C/C++/[C Improved](https://packagecontrol.io/packages/C%20Improved)
* Clojure/EDN
* CSS/SASS/SCSS - specifically, the [`Syntax Highlighting for SASS`](https://packagecontrol.io/packages/Syntax%20Highlighting%20for%20Sass) package
* diff
* `Find In Files`
* [Fortran](https://packagecontrol.io/packages/Fortran)
* [Git Gutter](https://packagecontrol.io/packages/GitGutter)
* Haskell
* HTML/XML
* Java
* JavaScript/[JavaScriptNext](https://packagecontrol.io/packages/JavaScriptNext%20-%20ES6%20Syntax)/Node.js
* [jQuery](https://packagecontrol.io/packages/jQuery)
* JSON
* JSX/[Babel](https://packagecontrol.io/packages/Babel)
* LaTeX
* Markdown/reStructuredText
* Matlab
* [PackageDev](https://packagecontrol.io/packages/PackageDev) `.sublime-settings`, `.sublime-keymap`, `.sublime-mousemap`, `.sublime-macro`, `.YAML-tmLanguage`, etc.
* PHP
* Python
    * [IPython](http://ipython.org)/[Jupyter](http://jupyter.org) within SublimeREPL
    * Django/[Djaneiro](https://packagecontrol.io/packages/Djaneiro)
    * [Jinja2 templates](https://github.com/mitsuhiko/jinja2-tmbundle)
    * All the customizations in the [`Python Improved`](https://packagecontrol.io/packages/Python%20Improved) syntax definition
    * The new default [`Python.sublime-syntax`](https://github.com/sublimehq/Packages/blob/master/Python/Python.sublime-syntax)
* R/[R-Box](https://packagecontrol.io/packages/R-Box)
* [RAML](https://packagecontrol.io/packages/RAML%20Syntax%20Highlighter)
* Regular Expressions
* Ruby
* Rust
* Scala
* Shell Scripts/[ShellScriptImproved](https://packagecontrol.io/packages/ShellScriptImproved)
* SQL
* [SublimeLinter](https://packagecontrol.io/packages/SublimeLinter)
* [Swift](https://packagecontrol.io/packages/Swift)
* Table of Contents/Task Tags
* Typescript
* YAML

For major changes, I'll test most if not all of the above languages, as well as Makefile, Lua, and Perl, with maybe some others thrown in for fun. When I say "as many languages as possible" I mean it!

If you have a particular language or plugin you'd like Neon to support, just [open an issue](https://github.com/MattDMo/Neon-color-scheme/issues/new) and I'll see what I can do.

There are a bunch of scopes in here that are only found in my [`Python Improved`](https://packagecontrol.io/packages/Python%20Improved) language definition package &mdash; [IPython](https://www.ipython.org) `In`/`Out` statements, [Django](https://djangoproject.org)-specific highlighting (adapted from [`Djaneiro`](https://packagecontrol.io/packages/Djaneiro)), a bunch of improvements from [@facelessuser](https://github.com/facelessuser)'s [`Better Python`](https://github.com/facelessuser/sublime-languages/tree/master/Better%20Python) and [@petervaro](https://github.com/petervaro)'s [Python 3](https://packagecontrol.io/packages/Python%203) package, along with various enhancements, extensions, and bug fixes of my own and contributed by others. If you work with Python, I'd highly recommend getting it.

![Clojure with Neon](https://pigimal.com/img/github/new_clojure.png)

You can find out more about themes in the TextMate [manual](http://manual.macromates.com/en/themes). All the information there applies to Sublime Text as well, which was heavily influenced by TextMate. Both programs can share themes and language definitions pretty much interchangeably, and snippets are usually pretty easy to port from one to the other as well. But, unfortunately for you Win/Lin people, TextMate is only available for macOS.

![Ruby with Neon](https://pigimal.com/img/github/ruby.png)


## What Font is That?

I discovered [`Cousine`](https://www.google.com/fonts/specimen/Cousine) while browsing Google Fonts one day and absolutely love it.

> Cousine was designed by [Steve Matteson](https://profiles.google.com/107777320916704234605/about) as an innovative, refreshing sans serif design that is metrically compatible with Courier New™. Cousine offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to address document portability across platforms.

It's one of the first things I install when setting up a new workstation or VM, and it used to be my go-to monospace font for web design and programming.

More recently, I've been using [`Liberation Mono`](http://www.fontsquirrel.com/fonts/Liberation-Mono), part of the [Liberation](https://fedorahosted.org/liberation-fonts/) font family. It's almost an exact duplicate of Cousine (with a few minor differences), and has the advantage of being available for Fedora (out of the box) and RHEL/CentOS as `liberation-fonts`, and as `ttf-liberation` for Debian and Ubuntu (my current distro of choice).


## Installation for Sublime Text 3

The easiest method is through [Package Control](https://packagecontrol.io/), which you need to [install](https://packagecontrol.io/installation) first as it doesn't come with Sublime Text. (*Note*: It does now!) Open the Command Palette with <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> (Windows/Linux) or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd> (macOS) and type ***`pci`*** to bring up `Package Control: Install`. Click or hit <kbd>Enter</kbd>, type in `neon`, and `Neon Color Scheme` should show up. Select it, then activate the theme by choosing the `Preferences -> Color Scheme -> Neon Color Scheme -> Neon` menu option. Alternatively, paste the following line in `Packages/User/Preferences.sublime-settings` (`Preferences -> Settings - User`):

```js
"color_scheme": "Packages/Neon Color Scheme/Neon.tmTheme"
```

---

If you like to do things the old-fashioned way, in `~/Library/Application Support/Sublime Text 3/Packages/User` (macOS), `%APPDATA%\Sublime Text 3\Packages\User` (Windows), or `~/.config/sublime-text-3/Packages/User` (Linux) (change the `3` to `2` if you're still using the outdated version 2 &mdash; and ***please*** upgrade!):

```bash
git clone https://github.com/MattDMo/Neon-color-scheme.git "Neon Color Scheme"
```

This will create a menu option `Neon` under `Preferences -> Color Scheme -> User -> Neon Color Scheme`. However, unless you `git pull` manually, your installation will never get upgraded with new goodies.


## TextMate Installation:

For right now, manual cloning is the only option. Maybe I'll make a bundle someday for TM1 and TM2. From your home directory (or anywhere, really), enter:

```bash
git clone https://github.com/MattDMo/Neon-color-scheme.git "~/Library/Application Support/TextMate/Themes"
```

Or, you can just download the [`.zip` file](https://github.com/MattDMo/Neon-color-scheme/archive/master.zip) and put it in the proper theme directory yourself.



## Issues

Sometimes the same file looks different in TextMate and Sublime Text. It may be that the scopes are defined somewhat differently, or that the parsers don't work in quite the same way. Hack the `.tmlanguage` definition files if you're interested, it's an exciting combination of XML and regex! To ease the pain somewhat, I definitely recommend installing [`PackageDev`](https://packagecontrol.io/packages/PackageDev) via Package Control. Among many other things, it allows you to convert XML/Plist-based `.tmLanguage` files to YAML syntax, which **Neon** conveniently supports! Everything is much more straightforward to understand and edit, and when you're done you can run a build system from the Command Palette to convert the YAML back to XML.

![YAML-tmLanguage syntax highlighting with Neon](https://www.pigimal.com/img/github/YAML-tmLanguage_new.png)

If you have questions, concerns, or suggested improvements, I'd love to hear from you! Feel free to [open an issue](https://github.com/MattDMo/Neon-sublime-theme/issues/new) or send a [pull request](https://github.com/MattDMo/Neon-sublime-theme/compare/) and I'll get back to you as soon as I can. You can also email me at <mattdmo@mattdmo.com>. Find my blog on Sublime Text and other stuff at [MattDMo.com](https://mattdmo.com).


## License

&copy; 2013-2020 Matt Morrison <mattdmo@mattdmo.com>.

This is free software. It is licensed under the [MIT License](http://opensource.org/licenses/MIT). Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and it would be great if you distribute your work under this or a similar license, but it's not required. A shout-out or a beer would be appreciated.


## Support

[![PayPal donation link](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SJY8KLDDB8DXC)

You can also give on [Gratipay](https://www.gratipay.com/on/github/MattDMo/).

---
