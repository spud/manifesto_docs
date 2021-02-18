*******************************
Important Concepts in Manifesto
*******************************

In order to have a better understanding of Manifesto's architectural design principles and infrastructure, there are a few points worth emphasizing.

Content
=======

It is important to remember that, above all, Manifesto is designed for serving *content* more so than just *pages.* In this sense, Manifesto fundamentally acts like an API, capable of managing, listing, and displaying structured data of any sort.

It happens to have an excellent module for serving HTML-pages-as-content (you could host an entire site using only the **TemplatePages** module), but it also works well for mailing list archives, or CD collections, or concert events, where each of those content types is a **first-class citizen** of Manifesto, with its own database structure, access methods, and view templates.

The PageController
==================

Manifesto takes advantage of an supervisory object called the PageController (instantiated as the object ``$G``).

The PageController acts as a storage repository for site preferences, current language, loaded modules, current user and other information that is convenient to have readily stored for use in business logic and page rendering. Consequently, you will frequently see::

global $G;

at the start of many of the built-in rendering functions like ``edit`` or ``display`` that will need to access related modules and preferences that Manifesto needs to help with interoperability.

Routing
=======================

At a fundamental level, URLs in Manifesto identify unique views by specifying the following information:

* A module that provides the content (stored as ``$G->req_module``)
* A specific ID for the content (stored as ``$G->req_id``)
* A specific action to take (edit, display, delete, update, etc, stored as ``$G->req_function``)
* A specific content type (more common on the backend, stored as ``$G->req_class``)

Routes -- the mapping between URL structure and handling the page request -- are configured in ``sites/routes.php``. They function, basically, by converting segments of the URL to those pieces of information. Custom URLs work by assigning default values to some of those variables.

For example, the default URL structure::

/mod/dated_posts/display/12/index.php

provides the module, function, and ID (the content type, "Dated Post" is the only one available for that module, so it is implied). You could create a custom route in routes.php that makes::

/news/12/index.php

pull up the same content, by specifying that any URL starting with "news" automatically assigns "dated_posts" as the module, "Dated Posts" as the class, and "display" as the function. It still uses the "12" segment of the URL to identify the ID.

To continue the example, since the Dated Posts module supports the "shortname" property, you may also use the structure::

/news/my-news-title

to represent the content, where "my-news-title" is the shortname property for Dated Post #12. Properly designed modules understand that if a *numeric* ID is represented in a URL segment, it should be looked up in the database by comparing it to the "objectid" column in the database, but if a *text* string is used in the URL, it should be compared against the "shortname" column in the database.

Controllers
===========

Every module provides its own controller script, named "controller.inc." Manifesto, however, includes a unique step *between* the route and the controller in the form of a script called ``module_prep.inc``. Some interesting things happen in module_prep.inc:

* Manifesto checks to confirm that the current user has "read" access to the current module
* Any request for a unique piece of content will require looking up the content in the database, so Manifesto attempts to retrieve the content and stores the result in ``$G->contentobj``. This saves developers the trouble of having to repeat the process of retrieving the content for every method handled by the controller.
* If the request is an AJAX request, module_prep.inc next loads the controller, which is expected to output a standard JSON reponse and exit.
* If the request is a standard page request, Manifesto next loads the page layout template (which itself is expected to load the controller file). The idea here is that many or all of the handlers in the controller are going to be rendered within the structure of that template, so we might as well start now.

The nice thing about Manifesto, though, is that all of this behavior is plainly visible in the code, so creating your own module that deviates from this pattern is easily achieved if necessary.

Loading javascript
==================

Manifesto buffers its javascript output before rendering it to the screen, and this allows it to load and order elements like javascript at any point during the execution of the request. If you use::

$G->add_script('my-custom-javascript', G_URL.'site/themes/my-theme/custom.js');

from anywhere in your script prior to loading the page layout template, your script will be output when the ``PageController::output_scripts()`` call is made in the template, usually at the bottom of the page_layout templates.

