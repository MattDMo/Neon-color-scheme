# Neon.tmTheme

A cool bright-on-black theme I made for [TextMate](http://www.macromates.com) and [Sublime Text 2](http://www.sublimetext.com/2). Used mainly for [Python](http://www.python.org), but lots of languages look good with it, like JavaScript, XML, CSS, shell scripts, Clojure (could use some work), Fortran (really!), PHP, R, Tcl, and more. It's also great when using wuub's fantastic [SublimeREPL](https://github.com/wuub/SublimeREPL) plugin, which I can't say enough good things about. Java and Ruby look OK, but I tend to avoid them.

<<<<<<< HEAD
<img src="http://www.pigimal.com/img/textmate2github.png" alt="Python and CSS with Neon.tmTheme" />
=======
I'm always tweaking and adding things, so the preview pix may not closely match the actual theme. YMMV.

<img src="http://www.pigimal.com/img/textmate2.png" alt="Python and CSS with Neon.tmTheme" />
>>>>>>> a few tweaks here and there

## Installation
In `~/Library/Application Support/` or the equivalent for your platform:

* TextMate:
    `git clone git://github.com/MattDMo/Neon.tmTheme.git TextMate/Themes`
* Sublime: `git clone git://github.com/MattDMo/Neon.tmTheme.git "Sublime Text 2/Packages/Color Scheme - Default"`
* Or, you can just download the [.zip file](https://github.com/MattDMo/Neon.tmTheme/archive/master.zip) and put it in the proper theme directory yourself.

## Customization

While I really like the level of control I get with Sublime's system of config files, editing themes by hand (in XML) is rough. So, I keep the main copies of my themes in the TextMate folder so I can use its theme editor for tweaks. In `~/Library/Application Support/` I then run `ln -s TextMate/Themes/Neon.tmTheme "Sublime Text 2/Packages/Color Scheme - Default/Neon.tmTheme"` to symlink it to Sublime.

## Issues
Sometimes the same file looks different in TextMate and Sublime Text 2. It may be that the scopes are defined somewhat differently, or that the parsers don't work in quite the same way. Hack the .tmlanguage definition files if you're interested.

## License

&copy; 2012-2013 Matt Morrison <mattdmo@pigimal.com>.

This is free software. It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. Feel free to use this theme in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0;align:center" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>

    
