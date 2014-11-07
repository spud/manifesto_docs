**************
Staff
**************
The Staff module provides a convenient means of maintaining a directory of personnel, members, staff, or employeees. Combining individual profile records with a powerful system of categorization allows for flexible uses.

Staff profiles consist of basic personal information:

* Full Name
* First Name
* Middle Name
* Last Name
* Posnomials ("Ph.D","Sr",etc)
* Department
* Position
* Phone
* Address
* Address2
* City
* State
* ZIP
* Country
* Email
* Public
* Alternate Email
* Biography

When you combine this information with one or more category groups, you can develop complex records. For example, if you add 2 category groups called

**Membership Level**
and
**Region**

you could manage a nicely comprehensive, sortable directory of members.

.. note::

   Even if the module is used for something other than "staff," we will still refer to the profile records as *Staff Member*.

.. figure:: images/staff-listing.*

Creating a new staff profile
============================

1. From the listing page shown above, click the "New Staff Member" link.

.. figure:: images/staff-edit.*

2. You are presented with the editing form. In the example above, there is a single associated Category Group called *Staff Groups* with categories like *Staff* and *Clergy*. You may select more than one category to associate with your record.

3. The rest of the information is straightforward, and some fields, like *Department* and *Position*, can be used in different ways to suit various scenarios.

4. While there is a menu for *Sort Order* on the editing page, it is usually more convenient to use the drag-n-drop interface on the listing page to sort your staff members.

   .. note::

      There is currently only *one* overarching sort order that covers all staff profiles. Therefore, complex combinations of filtering (e.g. by category or department) and custom sort orders can require very careful ordering.

5. You may upload one or more images or files to associate with the profile, as with most content. If you associate an image and check the "Use this image as the icon for this content" box, for example, your display templates could use that image as the thumbnail avatar for that member.

Creating a custom sort order
============================

Templates can obviously be developed to dynamically sort staff profiles based on last name, department, or other properties of the profile, of course. But in the real world, hierarchies and org charts are complex creatures.

When sorting staff profiles, be sure that you are not filtering the listing by any particular category. There is only one sort order for the entire listing, so the only way to ensure that you are accounting for every members sort order is to sort a complete, unfiltered listing.

Drag the profiles into the desired order. The sort order will be updated on the fly as you manually shuffle the listing, and will give feedback on the completion of the sorting, so take note to allow time for the operation to complete!

.. note::

   If you suspect that your sort order has become unmanageably corrupted, you can manually request the page ``http://|yoursite.example.com|/editor/Staff/index.php?e_section=staff&function=resort``. **This will completely resort your entire set of records,** but will ensure that each record has a unique sort order, often clearing up issues.

