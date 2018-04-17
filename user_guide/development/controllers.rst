***********
Controllers
***********

Controllers in Manifesto handle second-level routing of requests. While the initial ``routes.php`` file parses the request and passes it to the proper module for handling, the module's controller handles the specifics of executing the proper actual.

Manifesto's controller is actually split between two files, the ``module_prep.inc`` file, and the controller files (which is always named after its module.

The module_prep.inc file handles a few of the preliminary functions to prepare the request:

- Check the user's permissions to view content from the current module
* Send a 401 if permission fails
- If an ID has been passed in, attempt to retrieve the unique content into ``$G->contentobj``
- If this is a standard (non-AJAX) request, load the page layout template
* The actual controller file will be called from within the layout template
- If this is an AJAX request, load the controller immediately, skipping the layout

The controller file is actually a procedural script, rather than a Controller object with multiple methods to execute. In Manifesto, a controller file simply provides a switch/case statement where each case handles the requested function.
At a minimum, the controller file should handle at least two situations:

- display: When a specific ID has been requested, and Manifesto should deliver the display output of the requested content.
- default/listing: If no specific function has been requested, the standard behavior is to query the database for all content within the current module, and generate a Listing that can be iterated over to produce a brief overview of the available content.

So::

/mod/accounts/3/display/index.php

will display the output template for the User whose ID is 3 (assuming such a user exists)

while::

/mod/accounts/index.php

will display a list of all current users (usually paginated for efficiency).