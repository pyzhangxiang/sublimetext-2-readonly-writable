#Set file readonly or writable in Sublime Text 2

[Sublime Text 2][1] plugin to set file readonly or writable based on 
"Toggle Read-Only" (https://github.com/reflog/toggle-readonly)

Deferent to "Toggle Read-Only", this plugin has two commands in the context menu of tab, side bar and buffer area:

Set Readonly (enabled if the file is writable)

Set Writable (enabled if the file is readonly)

##Install

If you are using the [Sublime Package Manger][2] hold down Ctrl+shift+p and type
`Package Control: Install Package`. Then search for `ReadonlyWritable` and hit return.

If you are not using the package manager then `cd` into your Sublime packages directory (open SublimeText, menu: Preferences -> Browse Packages).  Then run

`git clone https://github.com/pyzhangxiang/sublimetext-2-readonly-writable.git ReadonlyWritable`

Or you can download the package as a [compressed file][3], then uncompress it into your Sublime packages directory.

##Usage

To use the command right click on the file in the tab or side bar or in the buffer area.


  [1]: http://www.sublimetext.com
  [2]: http://wbond.net/sublime_packages/package_control
  [3]: https://github.com/pyzhangxiang/readonly-writable/downloads
