# Neon Theme
###### I renamed the package from `Neon.tmTheme` as the directory name was confusing Sublime (and I assume would TextMate as well), and Github automatically redirects from the old name, so why not? 

### Now available through [Package Control](http://wbond.net/sublime_packages/package_control)!

Neon is a cool bright-on-black theme for [Sublime Text 2](http://www.sublimetext.com/2)/[ST3](http://www.sublimetext.com/3) and [TextMate](http://www.macromates.com) (versions 1 and [2](https://github.com/textmate/textmate)). Used mainly for [Python](http://www.python.org), but lots of languages look good with it, like JavaScript, XML, CSS, shell scripts, Clojure (could use some work), Fortran (really!), PHP, R, Ruby, LaTeX, Markdown/reStructuredText, and more. It's also great when using wuub's fantastic [SublimeREPL](https://github.com/wuub/SublimeREPL) plugin, which I can't say enough good things about. Java looks OK, but I tend to avoid it.

There are a bunch of scopes in here that are only found in my [PythonImproved](https://github.com/MattDMo/PythonImproved) `.tmLanguage` syntax file &mdash; [IPython](http://www.ipython.org) `In`/`Out` statements, [Django](http://djangoproject.org)-specific highlighting (from [Djaniero](https://github.com/squ1b3r/Djaneiro)), and a bunch of improvements from facelessuser's [Better Python](https://github.com/facelessuser/sublime-languages/tree/master/Better%20Python), along with various enhancements, extensions, and bug fixes of my own. If you work with Python, I'd highly recommend getting it.

<img src="http://www.pigimal.com/img/textmate2github.png" alt="Python and CSS with Neon-sublime-theme" />

=======
I'm always tweaking and adding things, so the preview pix may not closely match the actual theme. YMMV.

<img src="http://www.pigimal.com/img/textmate2.png" alt="Python and CSS with Neon-sublime-theme" />


## Installation for Sublime Text 2/3
The easiest method is through [Package Control](http://wbond.net/sublime_packages/package_control). Open the command palette with <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>P</kbd> (Windows/Linux) or <kbd>⌘</kbd><kbd>Shift</kbd><kbd>P</kbd> (OSX) and type `pci` or `packconin` or whatever you like to get `Package Control: Install` showing. Click or hit <kbd>Enter</kbd>, type in `neon`, and `Neon Theme` should show up. Select it, then activate the theme by choosing the `Preferences -> Color Scheme -> Neon Theme -> Neon` menu option.

If you like to do things the old-fashioned way, in `~/Library/Application Support/Sublime Text 2/Packages/User` (OSX), `%APPDATA%\Roaming\Sublime Text 2\Packages\User` (Windows), or `~/.config/sublime-text-2/Packages/User` (Linux):

    git clone git://github.com/MattDMo/Neon-sublime-theme.git 

This will create a menu option `Neon` under `Preferences -> Color Scheme -> User`.


## TextMate Installation:
For right now, manual cloning is the only option. Hopefully a bundle will be available soon for TM1 and TM2.
    
    git clone git://github.com/MattDMo/Neon-sublime-theme.git "~/Library/Application Support/TextMate/Themes"
    
Or, you can just download the [.zip file](https://github.com/MattDMo/Neon-sublime-theme/archive/master.zip) and put it in the proper theme directory yourself.


## Customization

While I really like the level of control I get with Sublime's system of config files, editing themes by hand (in XML) is rough. So, I keep the main copies of my themes in the TextMate folder so I can use its theme editor for tweaks. In `~/Library/Application Support/` I then run `ln -s TextMate/Themes/Neon.tmTheme "Sublime Text 2/Packages/Color Scheme - Default/Neon.tmTheme"` to symlink it to Sublime.

I'd also recommend checking out aziz's [tmTheme-Editor](http://tmtheme-editor.herokuapp.com/#/Neon), but alas it currently only works with [Google Chrome](https://www.google.com/chrome/‎) because of some the HTML5 APIs it uses. Regardless, it's a pretty neat app, and **Neon** is included!


## Issues
Sometimes the same file looks different in TextMate and Sublime Text 2. It may be that the scopes are defined somewhat differently, or that the parsers don't work in quite the same way. Hack the `.tmlanguage` definition files if you're interested.


## License

&copy; 2012-2013 Matt Morrison <mattdmo@pigimal.com>.

This is free software. It is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>. Feel free to use this theme in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0;align:center" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=R97MGGYES6GAJ&lc=US&item_name=Matthew%20D%2e%20Morrison&item_number=neon%2dsublime%2dtheme&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="Donate" alt="PayPal - The safer, easier way to pay online!"></a>
    
