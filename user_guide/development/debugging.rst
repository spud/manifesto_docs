*********
Debugging
*********

Manifesto has robust debugging tools that make it easy to diagnose errors and examine preferences, request parameters, and variable values for any page request.

For an overview of the script flow that a web request takes through Manifesto, see the :doc:`flow` page.

The debugging module
--------------------

By default, you can simply enable debugging in the Site Preferences screen of the administrative interface, by clicking the "On" radio button under "Debugging Output."

Once enabled, debugging information will appear after the footer of your page request. Only logged-in editors and admin will see this content, so it will not disrupt normal operations of your site.

Specific aspects of debugging can be managed in the Debugging module configuration, but the standard configuration will display most of the information you are concerned with:

-- Current request parameters
-- Current routing information
-- Error logging at various levels
-- Available modules and their preferences
-- Every database query executed to render the output
-- Every file included during page execution

and much more. It's an invaluable tool for figuring out what's going on under the hood.

Exception handling
------------------

Recent versions of Manifesto have replaced the old generation of ErrorObjects with modern Exception throwing. In the event of an exception, Manifesto will display to authenticated editors and admins a page outlining the stack trace and other useful information related to the Exception thrown.

In the case of an uncaught exception, regular users will be redirected to a predefined error page, usually with a status code of 500 ("Internal server error").

Logging
-------

The log directory ([root]/logs by default) contains a number of log files that can be instrumental in troubleshooting:

-- php-error.log contains some generic logging
-- manifesto.log contains Manifesto-specific logging, details based on the "Log Errors" setting in the Site Prefs
-- posts.log is a log of every value submitted via POST to the site. Extremely useful for debugging form submission issues, this log can be enabled by uncommenting the line at the end of prep.inc. Because this log also captures content update submissions, it can grow very large quite quickly, so should be disabled when not actively in use.
-- sql_deletions.log contains a record of every SQL query that begins with "DELETE" to help log content that has been purged from the database
-- tidy-errors.log is only available if using the Tidy PHP extension for validating HTML submissions

Additionally, some modules like the ShoppingCart module will provide their own log files for tracking interactions with payment gateways, etc. 