****
Flow
****

Understanding how a web page request works its way through Manifesto is essential to being able to troubleshoot problems when they inevitably occur. 

Most important to remember is that Manifesto routes requests based on 3 major variables:

1. $G->req_module: The primary module responsible for handling the request
2. $G->req_function: The function to execute in that module ('display','edit','list','add_to_cart',etc). This may be empty, in which case a default handler is executed
3. $G->req_id: The specific content ID being requested (optional) 

While there are many points in the code for modules to insinuate themselves into the response, the basic flow of execution is as follows:

For the home page
=================

1. Load index.php
	1a. Include site/routes.php to load routes
	1b. Include prep.inc to initialize Manifesto
	1c. Determine which module governs the home page ("Homepage module" in the Site Prefs)
	1d. Load [theme]/page_layouts/home.tmpl.php
2. Depending on the layout of the home page template, load files attached to location events in the template
	2a. Load any files attached to the "page_homepage" event (this is the main home page content)
3. Load footer.tmpl.php
4. Output queued javascript
5. Output debugging, if enabled

For most other pages
====================

1. Load index.php
	1a. Include site/routes.php to load routes
	1b. Include prep.inc to initialize Manifesto
	1c. Determine which module should handle the request
2. Load [module]/module_prep.inc to check permissions and initialize the module
3. If this is an AJAX request (no UI to display), load [module]/controller.php
	3a. One of the handlers in controller.php should respond and exit
4. If not an AJAX request, load [theme]/page_layouts/module.tmpl.php
	4a. Modules are permitted to override this template with [module].tmpl.php, so you may create your own module-specific layouts
5. Depending on the layout of the module template, load files attached to location events in the template
6. Load [module]/controller.inc
	6a. One of the handlers in the controller, based on the $G->req_function being called determines the next include.
	6b. If no function is specific, we execute the default fork of the controller, which usually loads [module]/includes/[module]_home.inc
	
In general, the "Show Included Files" section of the debugging output will show you all of the files being included during page execution. Most of them are simply loading class files, but if you find the first entry that includes a file from "/page_layouts/," you can usually trace the inclusion of files beyond that point to get an idea of where code is being executed.