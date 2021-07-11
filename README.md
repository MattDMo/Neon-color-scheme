[![Package Control](https://packagecontrol.herokuapp.com/downloads/Neon%20Color%20Scheme.svg)](https://packagecontrol.io/packages/Neon%20Color%20Scheme)
[![GitHub release](https://img.shields.io/github/release/mattdmo/neon-color-scheme.svg)](https://github.com/MattDMo/Neon-color-scheme/releases/latest)
[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-3fabd1?logo=paypal)](https://paypal.me/MattMorrison966)

# Neon Color Scheme

**Neon** is a colorful bright-on-black color scheme for [Sublime Text](https://www.sublimetext.com/). In designing it, I've aimed to make as many languages as possible look as good as possible, taking advantage of as many of the available [scopes](https://www.sublimetext.com/docs/scope_naming.html) as I can. **Neon** was originally designed for [Python](http://www.python.org), which has a very detailed language definition, but lots of languages look good with it, like JavaScript, CSS, HTML, Ruby, PHP, shell scripts, XML, Clojure, Fortran, R, LaTeX, Markdown, reStructuredText, and more. It's also great when using [@wuub](https://github.com/wuub)'s fantastic [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL) plugin, which I can't say enough good things about. Unfortunately it is no longer being maintained.

Just for clarity's sake: **Neon** is an original work and wasn't based on any other color scheme. If you search [Package Control](https://packagecontrol.io) for [`neon`](https://packagecontrol.io/search/neon) you'll find some other, similarly-named color schemes which are *not* based on this project. Use them if you want -- I particularly like the [Dark Neon Color Scheme](https://packagecontrol.io/packages/Dark%20Neon%20Color%20Scheme), and might borrow some of the colors -- and if you want to fork this project and make your own derivative, go for it! I use the [MIT License](http://opensource.org/licenses/MIT) for a reason.


![Python with Neon Color Scheme](https://mattdmo.com/img/Python_win.png)

![Ruby with Neon Color Scheme](https://mattdmo.com/img/Ruby_macOS.png)

## Languages/Plugins Supported

Neon's main goal is to make as many languages as possible look as good as possible. That being said, there are some language/markup/framework-specific scopes and sections that you might be interested in:

* [Android Debug Bridge](https://packagecontrol.io/packages/ADBView)/[logcat](https://github.com/leesei/logcat.tmLanguage)
* Bison/YACC
* [BracketHighlighter](https://packagecontrol.io/packages/BracketHighlighter)
* C/C++/[C Improved](https://packagecontrol.io/packages/C%20Improved)
* Clojure/EDN
* Coffeescript
* CSS/SASS/SCSS - specifically, the [`Syntax Highlighting for SASS`](https://packagecontrol.io/packages/Syntax%20Highlighting%20for%20Sass) package
* diff
* [Dockerfiles](https://packagecontrol.io/packages/Dockerfile%20Syntax%20Highlighting)
* `Find In Files`
* [Fortran](https://packagecontrol.io/packages/Fortran)
* [Git Gutter](https://packagecontrol.io/packages/GitGutter)
* Haskell
* HTML/XML
* Java
* JavaScript/[JavaScriptNext](https://packagecontrol.io/packages/JavaScriptNext%20-%20ES6%20Syntax)/Node.js
* [jQuery](https://packagecontrol.io/packages/jQuery)
* JSON
* JSX/[Babel/React](https://packagecontrol.io/packages/Babel)
* LaTeX
* Markdown/reStructuredText
* Matlab
* [Mediawiker](https://packagecontrol.io/packages/Mediawiker) wiki markup
* [PackageDev](https://packagecontrol.io/packages/PackageDev) `.sublime-settings`, `.sublime-keymap`, `.sublime-mousemap`, `.sublime-macro`, `.YAML-tmLanguage`, etc.
* PHP/[Laravel Blade](https://packagecontrol.io/packages/Laravel%20Blade%20Highlighter)
* Python
    - [IPython](http://ipython.org)/[Jupyter](http://jupyter.org) within [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL)
    - Django/[Djaneiro](https://packagecontrol.io/packages/Djaneiro)
    - [Jinja2 templates](https://github.com/mitsuhiko/jinja2-tmbundle)
    - All the customizations in the [`Python Improved`](https://packagecontrol.io/packages/Python%20Improved) syntax definition
    - The new default [`Python.sublime-syntax`](https://github.com/sublimehq/Packages/blob/master/Python/Python.sublime-syntax)
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
* [TOML](https://packagecontrol.io/packages/TOML)
* [Typescript](https://packagecontrol.io/packages/TypeScript%20Syntax)
* [Vue](https://packagecontrol.io/packages/Vue%20Syntax%20Highlight)
* YAML

For major changes, I'll test most if not all of the above languages, as well as Makefile, Lua, and Perl, with maybe some others thrown in for fun. When I say "as many languages as possible" I mean it!

![Regex Find/Replace with Neon Color Scheme](https://mattdmo.com/img/regex_widget_win.png)

If you have a particular language or plugin you'd like Neon to support, just [open an issue](https://github.com/MattDMo/Neon-color-scheme/issues/new) and I'll see what I can do.

There are a bunch of scopes in here that are only found in my [`Python Improved`](https://packagecontrol.io/packages/Python%20Improved) language definition package &mdash; [IPython](https://www.ipython.org) `In`/`Out` statements, [Django](https://djangoproject.org)-specific highlighting (adapted from [`Djaneiro`](https://packagecontrol.io/packages/Djaneiro)), a bunch of improvements from [@facelessuser](https://github.com/facelessuser)'s [`Better Python`](https://github.com/facelessuser/sublime-languages/tree/master/Better%20Python) and [@petervaro](https://github.com/petervaro)'s [Python 3](https://packagecontrol.io/packages/Python%203) package, along with various enhancements, extensions, and bug fixes of my own and contributed by others. If you work with Python, I'd highly recommend getting it.

![Clojure with Neon Color Scheme](https://mattdmo.com/img/Clojure_linux.png)

![LaTeX with Neon Color Scheme](https://mattdmo.com/img/LaTeX_win.png)


## What Font is That?

I discovered [`Cousine`](https://www.google.com/fonts/specimen/Cousine) while browsing Google Fonts one day and absolutely love it.

> Cousine was designed by [Steve Matteson](https://profiles.google.com/107777320916704234605/about) as an innovative, refreshing sans serif design that is metrically compatible with Courier New™. Cousine offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to address document portability across platforms.

It's one of the first things I install when setting up a new workstation or VM, and it used to be my go-to monospace font for web design and programming.

For a while now, I've been using [`Liberation Mono`](http://www.fontsquirrel.com/fonts/Liberation-Mono), part of the [Liberation](https://fedorahosted.org/liberation-fonts/) font family. It's almost an exact duplicate of Cousine (with a few minor differences), and has the advantage of being available for Fedora (out of the box) and RHEL/CentOS as `liberation-fonts`, and as `ttf-liberation` for Debian and Ubuntu (my current distro of choice).

![Rust with Neon Color Scheme](https://mattdmo.com/img/Rust_linux.png)

![XML with Neon Color Scheme](https://mattdmo.com/img/XML_macOS.png)


## Installation for Sublime Text

The easiest method is through [Package Control](https://packagecontrol.io/), which now comes with Sublime Text. Open the Command Palette with <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> (Windows/Linux) or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd> (macOS) and type ***`pci`*** to bring up `Package Control: Install`. Hit <kbd>Enter</kbd>, type in `neon`, and `Neon Color Scheme` should show up. Select it, then activate the theme by choosing the `Preferences -> Select Color Scheme… -> Neon` menu option. Alternatively, paste the following line in `Packages/User/Preferences.sublime-settings` (`Preferences -> Settings`, right-side pane):

```js
"color_scheme": "Packages/Neon Color Scheme/Neon.sublime-color-scheme"
```

If you were using the old pre-3.0 version of **Neon**, the file name was `Neon.tmTheme`. I switched to the `.sublime-color-scheme` format both because JSON is far easier to work with than XML, and there are some cool new features in Sublime Text 4 that don't work with `.tmTheme` files.

## TextMate Installation:

Due to the switch to the `.sublime-color-scheme` format, TextMate is no longer supported.

![Javascript with Neon Color Scheme](https://mattdmo.com/img/JavaScript_linux.png)

![C with Neon Color Scheme](https://mattdmo.com/img/C_macOS.png)

## Issues

If you have questions, concerns, or suggested improvements, I'd love to hear from you! Feel free to [open an issue](https://github.com/MattDMo/Neon-sublime-theme/issues/new) or send a [pull request](https://github.com/MattDMo/Neon-sublime-theme/compare/) and I'll get back to you as soon as I can. You can also ping me on the Twitters [@MattDMo](https://twitter.com/MattDMo), or catch me on the [Sublime Discord server](https://discord.com/channels/280102180189634562/280102180189634562).

![JSON with Neon Color Scheme](https://mattdmo.com/img/JSON_macOS.png)

## License

&copy; 2013-2021 Matt Morrison <mattdmo@mattdmo.com>.

This is free software. It is licensed under the [MIT License](http://opensource.org/licenses/MIT). Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and it would be great if you distribute your work under this or a similar license, but it's not required. A shout-out or a beer would be appreciated.


## Support

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=R97MGGYES6GAJ&lc=US&item_name=Matthew%20D%2e%20Morrison&item_number=Neon%20Color%20Scheme&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="Donate" alt="PayPal - The safer, easier way to pay online!"></a>
