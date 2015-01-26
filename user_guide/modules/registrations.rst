**************
Registrations
**************
The Registrations module was developed specifically in response to the complex options available on paper forms for camp and course registrations. It allows for the construction of **Registration** objects that contain one or more **Registration Units** which may be grouped together into tracks, or **Unit Groups.**

For example, you might have a "Diversity Conference" (a Registration) that is broken down into "Morning Track" (a Unit Group) and "Afternoon Track" (a Unit Group). Each of those tracks have 2 workshops, "Understanding Diversity" (a Registration Unit), and "Diversity in the Workplace" (a Registration unit).

Prices can be attached to Registration Units, allowing them to be added to a shopping cart for checkout just like any other purchaseable item.

Creating a new registration
===========================

To create a new Registration object is easy: it requires only a title and a description for the event, camp, or class being promoted.

.. figure:: images/registrations-add.*

You may notice that there is a special "Save…" link after the title. This is a shortcut that allows you to quickly save the new Registration without a page reload, so that you can immediately start adding Registration Units. Otherwise, you would have to submit the page and then re-edit before you could add Units (saving the Registration object initally will generate the ID needed by the Units to associate them with the Registration).

After quick-saving the registration, you will see a new section of the editing form, as below:

.. figure:: images/registrations-saved.*

Clicking on the "Add another registration unit" will popup a new modal window allowing you to enter details about the class, session, or workshop.

.. figure:: images/registrations-unit-add.*

* The Group/Track/Session field is optional, but allows you to group different registration units into logical groups like "Morning Session" and "Afternoon Session," or "Developer Track" and "Manager Track"

* The Title is required, and should reflect the name of the session, course, or workshop.

* The Description field is also optional, but permits a more detailed description, photo uploads, links to related information, etc.

If you intend to charge money for the registration, and have properly configured the Shoppng Cart module to interact with the Registration module, then an additional tab will appear in the "New Registration Unit" interface:

.. figure:: images/registrations-unit-sales.*

Here you specify the shopping cart item that corresponds to your Registration Unit. It can have a different title than the Registration Unit (which appears in the Shopping Cart), and has all the flexible options of any purchaseable item in Manifesto.

When you edit a Regsistration object, you will also see all the existing associated Registration Units, and can edit and delete them as needed. But because each Registration Unit is its own content type, there is a "Registration Units" tab in the module interface.

This alternate interface simply displays all defined Registration Units, regardless of the Registration to which each is attached.

.. note::
   Editing and/or deleting content in the Registration Units interface has exactly the same effect as editing the content from within the associated Registration interface.

Displaying Registrations
========================
Currently, the only means for displaying Registrations for signup is by using the combo "Form with Registration" template.

You must create a form using the Form Builder that collects the signup information you need (name, address, email, age, etc). Then you attach that form, and your registration object, to the new page you have created.

The template takes care of combining the two forms, and handles the processing and submission.

Viewing Processed Registrations
===============================
Because ultimately the registration units that a user selected correspond to shopping cart items, a Registration is basically viewed the same way a purchase or donation transaction is handled.

Successful paid registrations will appear in the Shopping Cart Transactions listing, and the details of the payment and registration units purchased appear there just as they would for normal shopping cart purchases.

The only difference is that, because the current purchase *also* had an associated **Form** with it, the Transaction detail page will also contain a special section entitled "**Associated Form Response**" and it will link to the full set of answers given in response to the associated Form object.

.. figure:: images/registrations-shopping-transaction.*

.. note::
   Since the Form portion of a Registration page is still a FormBuilder form, it maintains consistent behavior with other forms. In other words, if the form is configured to email responses to a staff member, that will happen even when the form is part of a larger Registration process.
