**************
Page Templates
**************

Manifesto renders HTML pages by employing a consistent series of templates, each of which may be overridden by the developer.

Like many CMS frameworks, the index.php is used strictly for receiving and routing requests, and contains no HTML markup.

The **page layout** templates contain the outermost structure of a rendered page, consisting of the ``html``, ``head``, and ``body`` tags (both open and closed), as well as any column-based structure interior to the page.

Within that template, event calls are executed in various places to acquire the content that will fill in the page. Most of those event calls result in more specific view templates becoming embedded in the page template, e.g. within the <head> section, the ``page_head`` event is called to include scripts, css, and other ``head`` elements, while the ``module_prep.inc`` file belonging to the current module is included to further process the request. See the Workflow_ document for more information on the sequence of includes that is typically executed during a page request.

.. _Workflow:

A default installation of Manifesto includes the following templates:

admin.tmpl.php
	The default template for /admin/ pages. Typically not user-modified, as it includes a fair amount of routing logic.

disabled.tmpl.php
	The "Maintenance Mode" template, for when the site has been temporarily disabled.

editor.tmpl.php
	The default template for /admin/ pages. Typically not user-modified, as it includes a fair amount of routing logic.

error401.tmpl.php
	The default "Not authorized" error page

error403.tmpl.php
	The default "Forbidden" error page

error500.tmpl.php
	The default "Internal server error" error page

exception.tmpl.php
	Manifesto's built-in exception renderer. When logged-in, this page provides a stack trace and other useful debugging information.

home.tmpl.php
	The default home page template. It contains a few event calls that are unique to the home page, but otherwise may be fully customized.

login.tmpl.php
	A bare-bones template for rendering nothing but a login form.

module.tmpl.php
	The default template for **all** module content, unless overridden by a module-specific template. The template can handle every permutation of a three-column layout, based on the toggleable setting for each module.

print.tmpl.php
	The template invoked when a page is printed. This allows for heavy customization that may be easier to accomplish by modifying a template rather than customizing a print-based stylsheet.

template_pages.tmpl.php
	By default, this template is identical to module.tmpl.php, but is included to demonstrate how a module can easily override the default templat for all of its content.

Also, the ``body`` element of each template is tagged with a class that indicates what page layout template is in use (e.g. ``l-module`` for module.tmpl.php), and the element is also tagged with a class indicating what module is currently active, e.g. ``mod-dated_posts`` for the Dated Posts module.