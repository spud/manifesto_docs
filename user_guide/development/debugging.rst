*********
Debugging
*********

Manifesto has robust debugging tools that make it easy to diagnose errors and examine preferences, request parameters, and variable values for any page request.

The debugging module
--------------------

By default, you can simply enable debugging in the Site Preferences screen of the administrative interface.

Once enabled, debugging information will appear after the footer of your page request. Only logged-in users will see this content, so it will not disrupt normal operations of your site.

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


