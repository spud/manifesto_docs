**************
View Templates
**************

Beyond the structured page layout templates, content is rendered within those template by including one more *view templates* populated by database content belonging to one or more installed modules.

One of the nice things about Manifesto is that, once you understand where to look, virtually all output can be redesigned, retemplated, and reorganized by overriding the template. This is as true for third-party modules as it is for built-in functionality, making Manifesto incredibly easy to customize from a design perspective.

Manifesto does not rely upon an external templating language, but its object-oriented content structure and clean template design makes it easy to work with, even for non-programmers.

A properly-designed Manifesto module contains a number of common view templates, which are usually invoked by the built-in CRUD methods common to all Manifesto content objects:

- a listing page for displaying all available content
- a standard display template for rendering the output
- often a "brief" display template for rendering brief teaser copy
- an editorial listing page for accessing content for editing
- an editing template for every content type

A module may also contain templates for custom blocks, like a sidebar block for the Dated Posts module that displays the 3 most recent posts, or a block belonging to the Accounts module that contains a quick login form. These widget-like templates are usually embedded on a page by attaching them to one of the location events, like ``page_leftbar`` invoked by the module.tmpl.php template to add content to the left-hand sidebar.

**Every** template can be overridden by a theme. If you don't like the way a module has organized its editing template, you can re-arrange it. If you want to add a custom photo section to the bottom of every Dated Post section, just copy the template to your theme, modify it, and it will automatically be called to replace the default template.

Many of the smaller, widget-like module templates contain both business logic as well as output markup, so each one of them is a self-contained database query + output template. This is a great way to familiarize yourself with building Manifesto queries and handling the output, and that skill will benefit you anywhere that you work in Manifesto. They often follow a pretty common format, e.g.

- Create a database query object (a descendent of the Oracle class)
- Execute the query
- Loop over the results and output some content for each iteration

Sometimes there is also code for caching the results and avoiding future database queries, but that is to be covered elsewhere, in a more detailed discussion of content blocks.

