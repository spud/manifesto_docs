****************
Custom URLs
****************

**Quick Answer**

To create a short, custom URL for a page that you've created, use the Custom URLs screen. Simply select the module, and specific content item, and type in the URL you want to create.

For example, the page "Meet the President" might have the Manifesto default URL

``/mod/template_pages/display/138/index.php``

but you want it to be available at

``/meet-the-president/``

So you select "Template Pages" from the *Module* menu, "TemplatePage" from the *Content Type*, "Meet the President" from the *Item* menu. Then enter the URL ``meet-the-president`` and submit. Your shortcut will be available immediately.

**In Depth**

The systematic manner in which Manifesto organizes and accesses content means that all content has a *Manifesto default URL,* which is the URL that will always allow Manifesto to access and render the content.

The first segment of a Module URL path, usually "mod/" is what we call a *trigger* word. This means that it has a corresponding element in the routes array that specifies exactly how the rest of the URL should be parsed (segment 2 is the module, segment 3 is the function, etc).

Ultimately, however, the format of the Manifesto default URL is dependent upon entries in the ``routes.php`` file, but Manifesto's default handling of module content follows this format:

``/mod/[*module_shortname*]/display/[*content objectid*]``

Manifesto can automatically parse and render any such page request, as long as the module in question conforms to Manifesto module standards.

If you wish to affect a broad change over how URLs are constructed for a particular module, the first way is to update the Module's URL path (which controls the beginning of all automatic URLs within that module). See the Developer Guide for instructions on adding custom routes to the routes.php file.

.. note::
   Bear in mind that some modules may automatically create custom URLs for content. The Template Pages module, for example, attempts to mimic the page hierarchy by automatically generating custom URLs that prepend the parent page's URL path, so the resulting page URL shows the position of the page within the hierarchy, e.g. "/page/grandparent/parent/child/index.php." In such cases, where module's control their own URL construction, they still rely on the same custom URL interface that you will use manually. Consequently, you may see a fair number of entries in the Custom URL listing, although you did not create them manually.
