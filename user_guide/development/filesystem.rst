*********************************
The Manifesto Directory Structure
*********************************

This guide merely provides an overview of the files and directories to be found in Manifesto website installation.

At the root level, there are only 4 significant PHP files::

   _media_browser.php
      The popup window for media selection used by the editor
   _link_browser.php
      The popup window for link creation used by the editor
   cronmaster.php
      The default script used by cron to trigger scheduled tasks
   index.php
      The default script page

The first two provide popup windows for Manifesto's WYSIWYG editor. The **index.php** page receives and parses all page requests, and includes the appropriate templates needed to respond to the request. It contains no actual HTML markup, all of which belongs in the page_layout and other templates.

Additional files::

   .htaccess
      The default .htacces file, similar to the one used by WordPress, etc.
   prep.inc
      This is the initialization script the prepares the environment, parses the request URL, etc.
   robots.txt
      The standard robots.txt text, specify which files robots may access

Directories::

   cronjobs
      Directory containing default scripts to be run on a schedule
   docs
      The junk drawer directory, containing notes, license, documenation, etc
   images
   	  Storage for site-wide, core image elements (deprecated)
   locale
   	  Storage for locale-specific translation files (deprecated)
   mods
   	  Core and Base modules live in here. Described in more detail below.
   site
	  All implementation-specific files go in here. The /site/ directory may contain its own /mods/ directory, containing modules specific to this site, and may have one or more alternate *Themes*, allowing limitless overrides of any of the templates available on the site.

In theory, you should never modify any files outside of the /site/ directory, because all of those files belong to the core Manifesto package, and may be overwritten the next time the software is upgraded.

Each module is a directory containing one or more sub-directories that house all the classes, templates, and addtional files to provide the module's functionality.

Module Directory::

   module_prep.inc
      This file handles additonal preparation specific to the module, which occurs before any modular templates have been loaded
   controller.inc
      This acts like a module-specific controller file, routing page requests based on function to the appropriate templates and scripts
   admin_includes/
      Scripts used for functionality in the Site Management interface
   classes/
      Directory containing Class definition files
   cronjobs/
      Contains any moudle-specific scripts run on a schedule
   editor_includes/
      Scripts used for functionality in the Editorial interface
   includes/
   	  All related templates and random function files
   styles/
   	  Module-specific CSS files
