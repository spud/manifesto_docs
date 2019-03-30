*****************
Quick start guide
*****************

#. Download Manifeto, and expand the archive. The resulting folder will be the root of your website.
#. You will need to have an empty database and database user account set up, or administrative permission to create a new database.
#. In a web browser, navigate to http://[www.your-site.com]/install.php
#. Complete the form to configure your site and the administrator user account
#. Submit, paying attention to any error messages that may appear.
#. The following page should contain detailed information about the establishment of your site.

Once installed, you should be able to immediately use and manage the site, using the editorial administration interface to generate content.

Top-level things to know:

- You should never need to edit or modify any files outside of the /site/ directory. The site folder contains any modules you load specifically for your site, the composer.json file for loading third-party libraries, and the /themes/ directory where your customizations will live.
- The URLs /admin/ and /editor/ are for managing the site configuration and content management respectively
- Your first course of action is likely to be either installing additional required modules, or cloning the default theme to begin customization
- There are default, canonical routes for publicly accessing any module content, which follows this pattern::

http://example.org/mod/[module_shortname]/[function]/[identifier]/index.php

and this structure is parsed into segments that help route the request to the proper module and controller. Most content types, however, will allow you to construct completely custom URLs for any content, allowing URLs like

http://example.org/my-custom-content

but of course these requests must simply be looked up in the database, rather than being programatically determined by the URL structure. 
