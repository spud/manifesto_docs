***********************
User Accounts, Roles, and Login
***********************
Manifesto has user accounts and roles fully integrated in its core, ready to use. Manifesto employs user accounts to manage access to resources and permissions for editing, viewing, and deleting content, as well as traditional user accounts for ecommerce or community-building. Manifesto uses roles to classify users into groups of permissions and privileges. There are four built-in **Roles** into which user accounts are classified.

Roles
=====

By default, any visitors to the website are considered unprivileged, **Anonymous** users. They are typically granted read-only access to public content.

A regular **User** account allows your website to manage logins for individual users. These too, have no particular privileges, but having a User-level account allows Manifesto to associate content with an individual (for example, to know that Shopping Cart #151 belongs to User “Jon Smith,” or that a comment on a blog post belongs to User “Alisha Salendar.”)

An **Editor** account is granted access to the Editor Console, and generally has full access to add, edit, and delete any content on the site.

An **Admin** account grants access to the Admin Console, where lower-level site configuration options are set. Admin users carry all of the privileges of Editors as well, and are the most powerful user accounts. There should *always* be at least one Admin user in your organization, and the Manifesto developer will generally have Admin privileges.

Any number of additional Roles may be defined, and you may offer restricted privileges to specialized Roles. For example, you may create a “Calendar Editor” role which *only* has add/edit/delete access to the Event Calendar module, and no permission to edit other content.

Permissions
===========

Privileges can be granted to user roles only on a module-by-module basis. You cannot restrict permission at the level of categories or individual content types within a module (e.g. for *Calendar Events* but not *Event Locations*). The available permissions are:

* None (this role may not access this module at all)
* Read (this role has permission to **view** content in this module)
* Add (this role can **add** *new* content in this module, but not edit existing content)
* Own (this role can **edit** content in this module, but only if it was added by the same user)
* Edit (this role can **add** and **edit** any content within this module)
* Delete (this role can **delete** and **purge** any content within this module)

.. figure:: images/role_permissions.*
   :alt: Role permissions grid

   Example permissions for the Editor role

Editors can access the Editor Console at `http://www.example.org/editor`

Admins can access the Admin Console at `http://www.example.org/admin`

If your site supports User-level accounts, there is a login screen at `http://www.example.org/usr`.

Creating new user accounts
==========================

.. todo::

   Add section for creating new accounts (at least for Editors)

To add a new User Account is easy, but there are a few caveats related to the roles to which a new user can be assigned.

A user with the Admin role can create any type of User Account : regular users, editors, and even other admins. In fact, the only way to create a new Admin or Editor is to have someone with Admin privileges do it.

An user with only an "Editor" level role can only create less-powerful users (e.g. "User" or "Member" or some other unprivileged role). These options are enforced programmatically, so that editors are not even given the opportunity to assign a role above the level of User.

* Click "New User" and you will be presented with a form to complete.
* The **Username** field is required, and is expected to be a single string with no unusual punctuation. Currently, the characters ``/%~ ,$&#{}'"=`` are considered invalid, and cannot be used in a username.
* The **Password** and **Confirm Password** need to have the same password entered into each one, to ensure that you have entered it correctly. If they do not match, you will be alerted immediately.
* **First Name** and **Last Name** should be self-explanatory.
* **Display Name** is the name used for bylines on the website. It could be a full name, nickname, or other pseudonym.
* **Email** is a required field, and the address entered is normally used to send a confirmation email in order the verify the account.
* **Email Verification**: As was just stated, Manifesto uses a confirmation email to verify that the email address associated with your account is valid. This provides a bare minimum guarantee of accountability, since we can at least confirm that we have a means for contacting the user associated with the account.
  This field is set to "Unverified" for all new users. When set to "unverified," a random key is stored in the database, and an email is automatically sent to the email address entered. The email body contains a link that corresponds to the random key, and when the user clicks on the email link, the key is erased and the user is marked as "Verified."
  An editor or administrator can automatically set the status to "Verified," if they are sure the email address is valid.
  Setting the status of this field to "Not requested" lies directly in-between — the user is not considered "unverified," but it cannot be assumed that the user has a confirmed email address either.
  User normal circumstances, a periodic script (cron job) runs to de-activate any user account that remains unverified for more than 2 days, and then will purge the account if it is not rectified within a month.
* The **Level** field will only display options that are within your authority to grant to other users. For example, an Admin is permitted to create *any* level user (including editors and other admins), but an Editor is only permitted to create user-level account (not even other editors). Levels of user accounts may be combined, but there is an implicit hierarchy: Admins need no lower permissions, because they inherit the abilities of the lower levels. Editors do not need to be lower-level Users, because an Editor-level account already includes all those permissions. The only time you really need to combine levels is to offer a combination of editor-level (but not Editor) or user-level accounts (like "Business Office" + "Events Coordinator" or "Member" + "Donor") which may selectively grant the user access to various features on the site.
* **Status** is only occasionally used, for when user accounts require approval before becoming active ("Pending" would be appropriate here), or perhaps your site offers memberships, and you want to "Disable" a user when their subscription lapses, rather than deleting it. Websites need to be specifically coded to use these status levels, as Manifesto does not utilize this field in the core.
* The **Set a cookie...** field indicates that Manifesto should set a cookie to avoid requiring a login upon every return to the site. This is equivalent to the "Remember Me" checkbox sometimes seen on other sites.
* The **Email password to user** is only available wh \\mxzmx.,men setting a new password, and will email a **plain text** copy of the password to the user. They are encouraged to change it again upon loggging in, for security.

The section entitled "Detailed Information" contains additional fields containing more information, such as phone number, alternate email, biography, etc. There is a checkbox labeled **Allow additional personal data to be displayed** — if this checkbox is *not* checked, this additional information will *not* be displayed on the website when using Manifesto's default templates. This rule, however, is only enforced by policy, so when constructing a custom template for displaying users, take care to respect this setting when determining how much user information to display.

Manifesto will automatically generate a page at ``http://www.example.org/usr/[id]/index.php``
that displays the default user profile for that user, regardless of whether or not the site navigation includes any links to such pages.

Forgotten Password
==================

Whenever there is a login form, there should be a corresponding link to a page that allows you to reset your password. The *only* way you can login if you forget your password is to have a new, temporary password sent to the email address associated with your user account.

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
