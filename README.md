# Neon Color Scheme

Neon is a colorful bright-on-black color scheme for [Sublime Text 2](http://www.sublimetext.com/2)/[ST3](http://www.sublimetext.com/3) and [TextMate](http://www.macromates.com) (versions 1 and [2](https://github.com/textmate/textmate)). In designing it, I've aimed to make as many languages as possible look as good as possible, taking advantage of as many of the available [scopes](http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html#scopes) as I can. Neon was originally designed for [Python](http://www.python.org), which has a very detailed language definition, but lots of languages look good with it, like JavaScript, CSS, HTML, Ruby, PHP, shell scripts, XML, Clojure, Fortran (really!), R, LaTeX, Markdown, reStructuredText, and more. It's also great when using @wuub's fantastic [SublimeREPL](https://github.com/wuub/SublimeREPL) plugin, which I can't say enough good things about. 

![PythonImproved with Neon](http://pigimal.com/img/github/python.png)

## Languages/Plugins Supported

Neon's main goal is to make as many languages as possible look as good as possible. That being said, there are some language/markup/framework-specific scopes and sections that you might be interested in:

* Python
    * IPython
    * Django
    * [Jinja2 templates](https://github.com/mitsuhiko/jinja2-tmbundle)
* Clojure
* Ruby
* jQuery
* JSON
* C/C++
* diff
* HTML/XML
* Markdown/reStructuredText
* PHP
* CSS
* SASS - specifically, the [Syntax Highlighting for SASS](https://sublime.wbond.net/packages/Syntax%20Highlighting%20for%20Sass) package
* [Git Gutter](https://sublime.wbond.net/packages/GitGutter)
* `Find In Files`
* [AAAPackageDev](https://sublime.wbond.net/packages/AAAPackageDev) `.sublime-settings`
* [SublimeLinter](https://sublime.wbond.net/packages/SublimeLinter)

For major changes, I'll test most if not all of the above languages, as well as JavaScript (use [JavaScriptNext](https://sublime.wbond.net/packages/JavaScriptNext%20-%20ES6%20Syntax), it's awesome!), R, Makefile, Lua, Java, Perl, Fortran (my excuse &mdash; I work with [NumPy](http://www.numpy.org)), LaTeX, and `bash` shell scripts, with maybe some others thrown in for fun. When I say "as many languages as possible" I mean it!

If you have a particular language or plugin you'd like Neon to support, just [open an issue](https://github.com/MattDMo/Neon-color-scheme/issues/new) and I'll see what I can do.

There are a bunch of scopes in here that are only found in my [Python Improved](https://sublime.wbond.net/packages/Python%20Improved) language definition package &mdash; [IPython](http://www.ipython.org) `In`/`Out` statements, [Django](http://djangoproject.org)-specific highlighting (adapted from [Djaniero](https://github.com/squ1b3r/Djaneiro)), and a bunch of improvements from @facelessuser's [Better Python](https://github.com/facelessuser/sublime-languages/tree/master/Better%20Python), along with various enhancements, extensions, and bug fixes of my own. If you work with Python, I'd highly recommend getting it.

![Clojure with Neon](http://pigimal.com/img/github/clojure.png)

You can find out more about themes in the TextMate [manual](http://manual.macromates.com/en/themes). All the information there applies to Sublime Text as well, which was heavily influenced by TextMate. Both programs can share themes and language definitions pretty much interchangeably, and snippets are usually pretty easy to port from one to the other as well. But, unfortunately for you Win/Lin people, TextMate is only available for OSX.

[![R with Neon](http://pigimal.com/img/github/R.png)](https://github.com/randy3k/Enhanced-R)

## What Font is That?
I discovered [Cousine](http://www.google.com/fonts/specimen/Cousine) while browsing Google Fonts one day and absolutely love it. 

> Cousine was designed by [Steve Matteson](https://profiles.google.com/107777320916704234605/about) as an innovative, refreshing sans serif design that is metrically compatible with Courier New™. Cousine offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to address document portability across platforms.

It's one of the first things I install when setting up a new workstation or VM, and it's my go-to monospace font for web design.

## Installation for Sublime Text 2/3
The easiest method is through [Package Control](https://sublime.wbond.net/), which you need to [install](https://sublime.wbond.net/installation) first as it doesn't come with Sublime Text. Open the command palette with <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> (Windows/Linux) or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd> (OSX) and type `pci` or `packconin` or whatever you like to get `Package Control: Install` showing. Click or hit <kbd>Enter</kbd>, type in `neon`, and `Neon Color Scheme` should show up. Select it, then activate the theme by choosing the `Preferences -> Color Scheme -> Neon Color Scheme -> Neon` menu option. Alternatively, paste the following line in `Packages/User/Preferences.sublime-settings` (`Preferences -> Settings - User`):

```js
"color_scheme": "Packages/Neon Color Scheme/Neon.tmTheme"
```

If you like to do things the old-fashioned way, in `~/Library/Application Support/Sublime Text 2/Packages/User` (OSX), `%APPDATA%\Sublime Text 2\Packages\User` (Windows), or `~/.config/sublime-text-2/Packages/User` (Linux) (change the `2` to `3` for ST3...):

```bash
git clone git://github.com/MattDMo/Neon-color-scheme.git "Neon Color Scheme"
```

This will create a menu option `Neon` under `Preferences -> Color Scheme -> User -> Neon Color Scheme`.


## TextMate Installation:
For right now, manual cloning is the only option. Hopefully a bundle will be available soon for TM1 and TM2. From your home directory (or anywhere, really), enter:

```bash    
git clone git://github.com/MattDMo/Neon-color-scheme.git "~/Library/Application Support/TextMate/Themes"
```

Or, you can just download the [.zip file](https://github.com/MattDMo/Neon-color-scheme/archive/master.zip) and put it in the proper theme directory yourself.


## Customization

While I really like the level of control I get with Sublime's system of config files, editing themes by hand (in XML) is rough. So, I keep the main copies of my themes in the TextMate folder so I can use its theme editor for tweaks. In `~/Library/Application Support/` I then run `ln -s TextMate/Themes/Neon.tmTheme "Sublime Text 2/Packages/Color Scheme - Default/Neon.tmTheme"` to symlink it to Sublime.

I'd also recommend checking out aziz's [tmTheme-Editor](http://tmtheme-editor.herokuapp.com/#/Neon), but be warned that it currently only works with [Google Chrome](https://www.google.com/chrome/) because of some the HTML5 APIs it uses. Regardless, it's a pretty neat app, and **Neon** is included!

So, the above two options are nice if you're on a Mac, or have Chrome, or otherwise are just making a few minor tweaks, but I've recently just discovered a game-changer. @facelessuser has written [`ColorSchemeEditor`](https://github.com/facelessuser/ColorSchemeEditor), a cross-platform GUI tool (written in Python) for creating and editing `.tmTheme` color schemes, and it has very quickly become one of my favorite apps. Be aware that it's still under active development, but that also means if you have any feature requests or assistance to offer you'll be gladly welcomed. If the forum is working, check out [this post](www.sublimetext.com/forum/viewtopic.php?f=5&t=11819) in the Sublime Text forum announcing the plugin and app. The documentation is minimal, it's not available through Package Control, and you currently need to download the platform-specific compiled binaries via links from the forum post (hint, google the page's URL and view the cached version to get the links if the forum is still down) and put them in your `Packages/User` directory in order for the plugin to work, but it's so worth it if you need to tweak or completely refactor a color scheme. If you want to try and build the binary yourself, read through [this issue](https://github.com/facelessuser/ColorSchemeEditor/issues/11). The directions are for Windows, but they also work on OS X, and should work for Linux as well.

Keep your eyes out, Neon Light should be coming soon!


## Issues
Sometimes the same file looks different in TextMate and Sublime Text. It may be that the scopes are defined somewhat differently, or that the parsers don't work in quite the same way. Hack the `.tmlanguage` definition files if you're interested, it's an exciting combination of XML and regex!

If you have questions, concerns, or suggested improvements, I'd love to hear from you! Feel free to [open an issue](https://github.com/MattDMo/Neon-sublime-theme/issues/new) or send a [pull request](https://github.com/MattDMo/Neon-sublime-theme/compare/) and I'll get back to you as soon as I can. You can also email me at <mattdmo@pigimal.com>. Find my blog on Sublime Text and other stuff at [MattDMo.com](http://mattdmo.com).


## License

&copy; 2012-2014 Matt Morrison <mattdmo@pigimal.com>.

This is free software. It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. Feel free to use this theme in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be greatly appreciated.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0;align:center" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=R97MGGYES6GAJ&lc=US&item_name=Matthew%20D%2e%20Morrison&item_number=neon%2dsublime%2dtheme&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="Donate" alt="PayPal - The safer, easier way to pay online!"></a>
<p>
You can also [give on Gittip](https://www.gittip.com/on/github/MattDMo/).
    
