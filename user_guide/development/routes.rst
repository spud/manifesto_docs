***************
Defining Routes
***************
Manifesto, like many other frameworks, uses a single front controller to route page requests to the appropriate scripts for processing. It uses an .htaccess file to instruct Apache to send all page requests to the default index.php page, and the index page immediately loads the aptly-named "routes.php" file.

In order to process pages, Manifesto requires a minimal amount of information:

#. **Request handler**: This is one of ``restricted``, ``module``, or ``ajax``. The first indicates that the request is for a password-protected area, like the administrative backend. The second, ``module``, is the most common, indicating that the request is a standard URL to be fulfilled by a Manifesto module, and rendered in the browser. The ``ajax`` handler expects to fulfill page requests by returning JSON, XML, or other fragmentary data, without rendering full page views.

#. **Request module**: The module which handles fulfillment of the primary content being requested on the page. Even an aggregate page like the home page is governed by a particular module.

#. **Request function**: The function or method to be performed. The controller uses this information to know how to handle the request. If empty, some default behavior is usually indicated (like "list all entries, paginated").

#. **Request identifier**: This is a unique identifier that allows Manifesto to retrieve a particular content object from the database.

The routes.php file is designed to parse the page URL request into segments, and to assign those segments to the variables described above.

The first segment after the domain name is called the *trigger*. The routes file allows you to specify an array (one per trigger) that indicates how the remaining segments should be mapped to variables. For example, given the URL

http://www.example.org/media/landscapes/display/ocean-view-with-sunset/index.php

The segment "media" is the trigger, and we would create a route map element that looks like this::

	$routes['media'] = array(
		'handler'=>'module',
		'module'=>'media',
		'category'=>seg(0),
		'function'=>seg(1),
		'id'=>seg(2)
	);

And after being processed, we now have ::

	$G->handler = 'module';
	$G->req_module = 'media';
	$G->category->shortname = 'landscapes';
	$G->req_function = 'display';
	$G->req_id = 'ocean-view-with-sunset';

With that, the ``index.php`` page now has the information it needs to route the page to the appropriate module controller.

The index page then loads prep.inc, which handles all the initial site configuration, loading modules, authentication, category setup, theme and stylesheet information, etc.

At this point, Manifesto either loads one of the backend templates (if $handler == 'restricted'), the home page template (if $module == ""), or passes control to one of the modules, whose ``module_prep.inc`` file will determine which template to load.

You'll note that the index.php page contains no HTML markup. No output occurs until we have loaded one of the page_layout templates. In fact, AJAX requests are proceseed without even loading a page_layout template, since they are usually handled by returning a JSON string directly from the controller file, API/REST style.

Creating a custom route
=======================
If you want to create systematic shortcut URLs (rather than one-off custom URLs), you can achieve this with a custom route. For example, imagine that your website has a categorized staff directory, so that filtered views adapt a URL something like ::

   /mod/staff/listing/index.php?category=board-of-directors

You would like a shorter solution that works with any category, so you create a route like::

	$routes['s'] = array(
		'handler'=>'module',
		'module'=>'staff',
		'function'=>'listing',
		'category'=>seg(0)
	);

...and that will allow you to use the much shorter ::

   /s/board-of-directors

to reach the same page. You are basically telling Manifesto that, if the *trigger* is ``s``, then treat the next segment of the URL as the category, and assert that this is for the Staff module(``module=>'staff'``) and that you want to call the ``listing`` handler (``function='listing'``) in the controller.

You may notice that that was a very specific use-case. Because we hard-coded "listing" as the function being requested, that means that we cannot use a URL like ::

   /s/a-different-function/board-of-directors

because we have very specifically redefined the meaning of each segment of the URL, and none of the segments are configured to define the *function*.

If you want to use your custom route for *all* the functionality of a module, you can.

Say you have a Manifesto website with a shopping cart, and the default URL for all shopping cart pages starts with ::

   /mod/shopping_cart/

but you would rather have a cleaner look, like ::

   /store/

You could modify the "URL Path" property of the Module definition, but you would also have to create a custom route that would be able to parse these new URLs. It would look something like this::

	$routes['store'] = array(
		'handler'=>'module',
		'module'=>'shopping_cart',
		'function'=>seg(0),
		'id'=>seg(1),
		'xparam1'=>seg(2),
		'xparam2'=>seg(3),
	);

By using a relatively generic route definition like this, it ensures that all of the functionality that worked with ::

   /mod/shopping_cart/

will now work with ::

   /store/

instead.

The Category
============
For the sake of convenience, because it is frequently used as a content filtering tool, Manifesto is set up to store a single category as the "current" category for the page, so it is easily included in database queries.

If `$G->route['category']` is defined (using a valid category shortname), or if $_REQUEST['category'] is a valid category shortname, Manifesto will lookup the corresponding category and assign it to $G->category. At that point, you can easily add a category-based filer to your database queries by simply calling::

   $oracle->filter_by_category($G->category);

The great advantage here, of course, is that our new query filter understands  category hierarchy, so we filter not only on the current category, but also any of its descendent categories as well.

The default $G->category->shortname is "all," so you may use that to confirm whether or not a non-default category has been set.