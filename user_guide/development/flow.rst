****
Flow
****

Understanding how a web page request works its way through Manifesto is essential to being able to troubleshoot problems when they inevitably occur. 

Most important to remember is that Manifesto routes requests based on 3 major variables:

* $G->req_module: The primary module responsible for handling the request
* $G->req_function: The function to execute in that module ('display','edit','list','add_to_cart',etc). This may be empty, in which case a default handler is executed
* $G->req_id: The specific content ID being requested (optional) 

While there are many points in the code for modules to insinuate themselves into the response, the basic flow of execution is as follows:

For the home page
=================

#. Load index.php

   #. Include site/routes.php to load routes
   #. Include prep.inc to initialize Manifesto
   #. Determine which module governs the home page ("Homepage module" in the Site Prefs)
   #. Load [theme]/page_layouts/home.tmpl.php
	
#. Depending on the layout of the home page template, load files attached to location events in the template

   #. Load any files attached to the "page_homepage" event (this is the main home page content)
	
#. Load footer.tmpl.php
#. Output queued javascript
#. Output debugging, if enabled

For most other pages
====================

#. Load index.php

   #. Include site/routes.php to load routes
   #. Include prep.inc to initialize Manifesto
   #. Determine which module should handle the request
	
#. Load [module]/module_prep.inc to check permissions and initialize the module
#. If this is an AJAX request (no UI to display), load [module]/controller.php

   #. One of the handlers in controller.php should respond and exit
	
#. If not an AJAX request, load [theme]/page_layouts/module.tmpl.php

   #. Modules are permitted to override this template with [module].tmpl.php, so you may create your own module-specific layouts
	
#. Depending on the layout of the module template, load files attached to location events in the template
#. Load [module]/controller.inc

   #. One of the handlers in the controller, based on the $G->req_function being called determines the next include.
   #. If no function is specific, we execute the default fork of the controller, which usually loads [module]/includes/[module]_home.inc
	
In general, the "Show Included Files" section of the debugging output will show you all of the files being included during page execution. Most of them are simply loading class files, but if you find the first entry that includes a file from "/page_layouts/," you can usually trace the inclusion of files beyond that point to get an idea of where code is being executed.