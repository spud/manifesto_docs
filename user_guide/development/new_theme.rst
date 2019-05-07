*************************
Setting up a custom theme
*************************

Almost immediately after installation, you will want to override the default theme. There is currently no mechanism to "import" a theme, and there is no current ecosystem for themes, so you will most likely be cloning the default theme for your site.

Log into the Administrative interface for your site, and click "Themes" in the left-hand navigation. A new subsection will slide down, with "Manage..." as the first item. Click it.

The subsequent page will display some basic information about the default theme, and at the bottom you will see a button: Create a clone of this theme.

Click the button, and fill out the form, giving your theme a new name, and indicating which files and directories you wish to copy over to the new theme.

You do not **have** to copy anything by default, but in general you probably want to copy

   layout_templates
      The outer HTML structure of all of your pages
   global page_head include file
      The main file that loads CSS and javascript into the page head
   global pagebanner include file
      The template included as the page header (logo, site title, etc)
   global footer include file
      The footer included on every default page template

The `_site_settings.scss` and `site.scss` SASS files are automatically copied to the new theme, but you can indicate if you want the (empty to begin with) site.css file to be copied over as well.

The manifesto.css and administration.css files should only be modified by an experienced Manifesto developer, as you could severely affect the backend interface.

If you want to immediately have the new theme applied to your site, check the box to Activate.

After submitting the form, you will be shown a confirmation page with a few more pieces of information. Submit that form, and you're all set with your new theme.

The template hierarchy
======================

Bear in mind that every file in the default theme acts as a fallback for any file in your custom theme. If you have not customized a particular template, it will use the default template.

This applies to page layout templates, view templates, CSS files, and javascript files. You only override the files you want to change.

At the same time, you can override virtually any file and customize it to your needs. This is true of all the files in the default theme, but also applies to files in the Core and Base suites of modules.

You may use the Admin/Themes interface to copy over, edit, or delete files in your theme (and get a visual indication of which files are default, overridden, and new). But you may also simply copy files over manually in the filesystem to override them.

When debugging is enabled, the "Includes files" listing can be critical in identifying which files are being loaded into the construction of your page.
