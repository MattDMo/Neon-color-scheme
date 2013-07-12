# Neon-sublime-theme
I renamed the package from `Neon.tmTheme` as the directory name was confusing Sublime (and I assume would TextMate as well), and Github automatically redirects from the old name, so why not? This will also make it easier for when I submit to [Package Control](http://wbond.net/sublime_packages/package_control).

A cool bright-on-black theme I made for [TextMate](http://www.macromates.com) and [Sublime Text 2](http://www.sublimetext.com/2) ([ST3](http://www.sublimetext.com/3) also works with it). Used mainly for [Python](http://www.python.org), but lots of languages look good with it, like JavaScript, XML, CSS, shell scripts, Clojure (could use some work), Fortran (really!), PHP, R, Tcl, and more. It's also great when using wuub's fantastic [SublimeREPL](https://github.com/wuub/SublimeREPL) plugin, which I can't say enough good things about. Java and Ruby look OK, but I tend to avoid them.

There are a bunch of scopes in here that are only found in my [PythonImproved](https://github.com/MattDMo/PythonImproved) `.tmLanguage` syntax file &mdash; [IPython](http://www.ipython.org) `In`/`Out` statements, [Django](http://djangoproject.org)-specific highlighting (from [Djaniero](https://github.com/squ1b3r/Djaneiro)), and a bunch of improvements from facelessuser's [Better Python](https://github.com/facelessuser/sublime-languages/tree/master/Better%20Python), along with various enhancements, extensions, and bug fixes of my own. If you work with Python, I'd highly recommend getting it.

<img src="http://www.pigimal.com/img/textmate2github.png" alt="Python and CSS with Neon.tmTheme" />

=======
I'm always tweaking and adding things, so the preview pix may not closely match the actual theme. YMMV.

<img src="http://www.pigimal.com/img/textmate2.png" alt="Python and CSS with Neon.tmTheme" />

## Installation
In `~/Library/Application Support/` or the equivalent for your platform:

* TextMate:
    `git clone git://github.com/MattDMo/Neon.tmTheme.git TextMate/Themes`
* Sublime: `git clone git://github.com/MattDMo/Neon.tmTheme.git "Sublime Text 2/Packages/Color Scheme - Default"`
* Or, you can just download the [.zip file](https://github.com/MattDMo/Neon.tmTheme/archive/master.zip) and put it in the proper theme directory yourself.

## Customization

While I really like the level of control I get with Sublime's system of config files, editing themes by hand (in XML) is rough. So, I keep the main copies of my themes in the TextMate folder so I can use its theme editor for tweaks. In `~/Library/Application Support/` I then run `ln -s TextMate/Themes/Neon.tmTheme "Sublime Text 2/Packages/Color Scheme - Default/Neon.tmTheme"` to symlink it to Sublime.

I'd also recommend checking out aziz's [tmTheme-Editor](http://tmtheme-editor.herokuapp.com/), but alas it currently only works with [Google Chrome](https://www.google.com/chrome/‎) at the moment because of some the HTML5 APIs it uses. Regardless, it's a pretty neat app, and **Neon.tmTheme** should be listed on there soon!

## Issues
Sometimes the same file looks different in TextMate and Sublime Text 2. It may be that the scopes are defined somewhat differently, or that the parsers don't work in quite the same way. Hack the `.tmlanguage` definition files if you're interested.

## License

&copy; 2012-2013 Matt Morrison <mattdmo@pigimal.com>.

This is free software. It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. Feel free to use this theme in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0;align:center" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>

    
