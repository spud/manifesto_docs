***********************
User accounts and Login
***********************
Manifesto employs user accounts to manage access to resources and permissions for editing, viewing, and deleting content. There are four built-in **Roles** into which User accounts are classified.

Roles
=====

By default, any visitors to the website are considered unprivileged, **Anonymous** users.

A regular **User** account allows your website to manage logins for individual users. These too, have no particular privileges, but having a User-level account allows Manifesto to associate content with an individual (for example, to know that Shopping Cart #151 belongs to User “Jon Smith,” or that a comment on a blog post belongs to User “Alisha Somebody.”)

An **Editor** account is granted access to the Editor Console, and generally has full access to add, edit, and delete any content on the site.

An **Admin** account grants access to the Admin Console, where lower-level site configuration options are set. Admin users carry all of the privileges of Editors as well, and are the most powerful user accounts. There should *always* be at least one Admin user in your organization, and the Manifesto developer will generally have Admin privileges.

Any number of additional Roles may be defined, and you may offer restricted privileges to specialized Roles. For example, you may create a “Calendar Editor” role which *only* has add/edit/delete access to the Event Calendar module, and no permission to edit other content.

Permissions
===========

Privileges can be granted to user roles only on a module-by-module basis. You cannot restrict permission at the level of categories or individual content types within a module (e.g. for Calendar Events but not Event Locations). The available permissions are:

* None (this role may not access this module at all)
* Read (this role has permission to **view** content in this module)
* Add (this role can **add** *new* content in this module, but not edit existing content)
* Own (this role can **edit** content in this module, but only if it was added by the same user)
* Edit (this role can **add** and **edit** any content within this module)
* Delete (this role can **delete** and **purge** any content within this module)

.. figure:: images/role_permissions.*

   Example permissions for the Editor role

If your site supports User-level accounts, there is a login screen at `http://|yoursite.example.com|/usr`.

Editors can access the Editor Console at `http://|yoursite.example.com|/editor`

Admins can access the Admin Console at `http://|yoursite.example.com|/admin`

Creating new user accounts
==========================

.. todo::

   Add section for creating new accounts (at least for Editors)

Forgotten Password
==================

Whenever there is a login form, there shoudl be a corresponding link to a page that allows you to reset your password. The *only* way you can login if you forget your password is to have a new, temporary password sent to the email address associated with your user account.

It is imposslble to "retrieve" an existing password. They are encrypted with a one-way hash, and can only be set to a new value, not revealed.

After entering your username into the "Forgot Password" form, hit submit, and an email will be generated and sent to your email address. When you receive that email, it will contain a link to the Manifesto website. When you click that link, the user account will have a new, random password set. You may use that password to login and create a new password for yourself.

If you receive such an email, and did not request a new password, simply ignore the email and your password will remain unchanged.

Account page
============

Once logged in, you may edit the details of your user account. Regular users may use the /usr/ page to edit and modify their personal information, but websites that make use of user accounts may also have custom navigation elements designed to facilitate access to your account information.

Editors and Admins will find their account details under the **My Account** link on the left-hand side.

By default, only your name and email address are ever publicly revealed. There are additional details (addresses, chat IDs, phone) that may or may not be displayed to the public based on design customization and the setting of the "Allow this information to be publicly displayed" checkbox.

Changing your Password
======================
To change your password, simply edit your account and provide a new password (and confirm it in the second box) and submit. Your new password will be set, and will be required the *next* time you login.
