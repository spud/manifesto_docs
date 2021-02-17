**********************
The template hierarchy
**********************

Bear in mind that every file in the default theme acts as a fallback for any file in your custom theme. If you have not customized a particular template, it will use the default template.

This applies to page layout templates, view templates, CSS files, and javascript files. You only override the files you want to change.

At the same time, you can override virtually any file and customize it to your needs. This is true of all the files in the default theme, but also applies to files in the Core and Base suites of modules.

You may use the Admin/Themes interface to copy over, edit, or delete files in your theme (and get a visual indication of which files are default, overridden, and new). But you may also simply copy files over manually in the filesystem to override them.

When debugging is enabled, the ``Includes files`` listing can be critical in identifying which files are being loaded into the construction of your page.
