**************
Editor Console
**************

Views
=====
For the most part, all of the Editor Console pages follow a consistent format, and fall into one of 3 types of file:

- Listing pages, where all the existing content within that module is listed
   .. figure:: images/editor-view-listing.*
      :width: 800 px
      :height: 400 px
      :target: ./images/editor-view-listing.png

- Editing pages, where a form is presented to create or edit a new content object
   .. figure:: images/editor-view-editing.*
      :width: 800 px
      :height: 400 px
      :target: ./images/editor-view-editing.*

- Display pages, where rendered output from your content is displayed for your reference
   .. figure:: images/editor-view-display.*
      :width: 800 px
      :height: 400 px
      :target: ./images/editor-view-display.*


Media Browser
=============

The Media Browser is one of the most powerful tools in Manifesto. All image uploads, media files, PDFs and downloadable files are stored consistently, and with a full set of metadata for characterizing your uploads, from title and caption to keywords and taxonomies. This makes all of your uploaded files easy to find, and reusable across your entire website.

.. figure:: images/media-browser-gallery.*
   :width: 600 px
   :height: 486 px

The uniform handling of file uploads also allows Manifesto to ensure rigorous validation and sanitization of user-contributed files, to keep you safe from malicious hacking attempts.

Uploading files
---------------
Most of the time, when you need to upload a file to Manifesto -- whether embedding a photo in blog post, uploading a product shot, or making a PDF available for download -- you will upload through the Media Browser upload tab.

The interface is simple:

.. figure:: images/media-browser-upload.*
   :width: 600 px

Simply drag one or more images, audio files, PDFs, Word documents, or other media onto the target zone indicated by the grey area. For backwards compatibility, you may also click anywhere on the area to bring up a standard file selection box to locate and upload a file from your computer.

As the upload takes place, the inteface will change to display the upload progress of hte files, and they will take their place within the respository.

Once they are uploaded, Manifesto attempts to glean as much information about the file as possible, including the filename, *MIME type* (what kind of file it is), and in the case of digital photographs, it will attempt to read metadata from the image file itself, such as the date and time the photo was taken.

Bear in mind that Manifesto enages in a variety of checks to prevent malicious files from being uploaded. The most straightforward of these is to ensure that the file extension or suffix (e.g. ".jpg" or ".doc") matches the actual file type. This prevents malicious users from uploaded a javascript with an extension of ".jpg" for example. A by-product of this strict policy is that images with incorrect or missing suffixes will **not** be displayed on the site until the discrepancy is resolved.

There are also module preferences that allow you to restrict uploads to specific User Roles, or to require editor approval before displaying some file types (for sites that allow public uploads).

Selecting and inserting media
-----------------------------
By clicking on any file in the repository grid, details about that file will appear on the right-hand side of the Media Browser window. Here, you can edit information about the file, such as title, artist/owner, caption, etc. These values act as default attributes when using the media (for example, when embedding a photo in a blog post), but can be overridden on a case-by-case basis.

From the repository grid view, you can click on an image, and then click the "Use Selected Media" button to insert it into your content. If you click on an image while holding down the ALT key (Command on a Mac), you can select more than one file at a time to place (each selected image will appear semi-opaque). When you click "Use Selected Media" each of the media will be attached to your content in turn.

.. figure:: images/media-browser-gallery-multiple.*
   :width: 600 px

.. note::

   *Please note that, while images are obviously placed by inserting the image into your copy, other files such as PDFs or ZIP archives may appear as representative icons instead.*

Options when inserting media
----------------------------
.. figure:: images/media-instance-highlighted.*
   :width: 50%
   :align: right

After placing the media within your content, **you will notice that it only appears as a square placeholder.** This is intentional, to preserve space within the editor, but your image will ultimately be displayed on the page with the parameters you specify.

Clicking once on the placeholder image reveals an overlay with two icons: one to delete the image, and one to edit the properties of the media for this specific instance.

.. figure:: images/media-instance-options.*
   :width: 50%

   The interface for specifying details of media usage

The `Title` of the media is largely for reference, though some output templates may choose to display it. The other options are described here:

* **This is the icon for this content**

  Sometimes an image needs to be associated with a content object without being embedded in body copy anywhere -- perhaps a thumbnail is designed to be displayed alongside the title the listing page. In such a case, we need to designate one of the uploaded images as the official "icon" that should be used. This is called the `icon,` and it is selected by checking this radio button. Only one icon per content object can be selected.

* **Positioning**

   This drop-down menu offers a selection of positioning options that allow you to specify how your media is to be placed. By default, images are wrapped in a `<figure>` tag (which allows it to be kept with a caption), and will appear on a line by themselves, with no specified alignment. The other options, e.g. "top-left" allow you to have text wrap around the image. If you need to have your image displayed in line with the text, select `inline` from the menu.

* **Clear**

  The `clear` checkbox tells Manifesto to insert the image only *after* clearing any earlier text that may have been wrapping around another image.

* **Display caption/Caption**

  If you wish your placed image to have a caption, check the checkbox and enter your caption. Any default caption from the Media file will already appear in the text area, but you may alter it on a case-by-case basis.

* **ALT Text**

  To provide an ALT text attribute for your image (a standard for acccessible content), enter it here. By default, the filename will appear here, but it is **not recommended to use filenames as ALT attributes.**

* **Display size/Custom W x H**

  Manifesto creates 3 different versions of all uploaded media:

  * The full-size imaage as it was uploaded
  * A `page-size` image suitable for body copy (usually ~600 pixels, configurable)
  * A `thumbnail` image to be used for icons and smaller placement (usually ~250 pixels)

  Some modules can specify that Manifesto create additional sizes for specific usage. If so configured, those sizes will appear in this menu as well.
  To avoid using excessive bandwidth, you should only insert the variation of image that will suit your needs.
  You may also specify a custom width or height for your image. Only one of these parameters is required; the image will always be resized to maintain the proper aspect ration.

* **Link to…**

  You may want users to be able to click on your image and be sent to another page. Your options here are

  * **None** (do not link the image to anything)
  * **Media Gallery** (view this image in the Media Gallery. NB: The Media Gallery is not guaranteed to be in use on your website, so check with an administrator before selecting this option)
  * **Fancybox** (this makes the full-size image appear in a lightbox interface)
  * **Raw file** (link directly to the full-size version in its own window)
  * **URL**
    Selecting this exposes a text input box where you may enter any URL you wish to link to

  Checking the `Open in new window` checkbox will open any URLs in a new browser window.

After making your selections, the modal window will close and your image will be updated.

Categories
==========

Manifesto has a robust, flexible taxonomy system for classifying content. Originally developed as a simple list of categories that could be associated with content produced by a particular module, it has developed into a system that allows for a variety of classification schemes, which may be used alone or in combinations.

*Category Groups* are collections of category terms. You may have a Category Group simply called "Categories," but you could also have one called "Regions" (containing geographical terms), or "Flavors," or "Media" or "Colors." Category Groups are created independently, but can then be *attached* to one or more module, allowing content across your site to share the same category terms.

Within a Category Group, individual categories are created, and can be organized into hierarchical structures, thereby permitting sub-categories within other categories. They may also be re-sorted and arranged into custom orders.

To **add a new Category Group,** from the listing page, click "New Category Group." You are prompted for only a few pieces of information

.. figure:: images/category-group-edit.*
   :alt: Interface for adding a category group

   Adding a new category group

* **Category Group** - the name of the collection
* **Shortname** - a URL-friendly version of the group name
* **Description** - optional explanation of the purpose of the group
* **Allow multiple selections** - this is a toggleable option that controls whether or not content using this category group are permitted to associate itself with more than one individual category from this group at a time. In other words, if a piece of content may tag itself as being available in more than one color, the "Colors" category group would check this checkbox to allow that.

To **add a new Category,** from the Category Groups listing page, you may click on the "Add" button within an existing category group. As an alternative, from the "List" page of a particular category group, there is always a "New Category" link at the bottom of the list of existing categories.

.. figure:: images/category-edit.*
   :alt: Interface for adding a category

    Adding a new category

Adding a category is straightforward:

* Select the **Category Group** to which your category will belong
* Assign it a **Parent** category (or make it a top-level category itself)
* Select the **Position** in which is will be located within the hierarchy
* Give it a **Category Name** and **Shortname** (used for URLs)
* Give it an optional **Description**
* Upload or assign an **Icon** image to it
* Optionally, the **Mark this category** box allows you to flag individual categories. This is only useful if you have designed your website to treat flagged categories differently, e.g. by only including marked categories in the sidebar, or using flagged categories as "recommended" categories.

Rearranging the order of categories can be done by dragging-and-dropping rows from the listing interface. Bear in mind that moving a category which itself has sub-catgories will result in the entire "family" being relocated.

Also, you can simply edit an existing category, and use the *Parent* and *Position* menus to alter the position on the category and its sub-tree.

WYSIWYG Editor
==============

.. figure:: images/tinymce.*

The WYSIWYG editor in Manifesto is a slightly modified version of TinyMCE, a popular editor found in many CMS applications. For the most part, the buttons in the toolbar are self-explanatory, and generally behave the way such buttons operate in word processors like Microsoft Word.

Manifesto basically allows for two forms of the WYSIWYG editor: the "full HTML" version, with the ability to upload images, create tables, etc. And the "restricted HTML" version, which allows for simple formatting like bold and italic as well as link creation. For the most part, the version used is determined by the specific needs of the module and its content, so you should *not* be re-configuring the options on a regular basis.

Pasting content from other sources
----------------------------------

While you are permitted to simply paste into the editor window, there are 3 special situations where you may want to take special care before pasting:

#. **Pasting from Microsoft Word**: Because Word document often contain hidden formatting codes, there is a special *Paste from Word* button on the toolbar. When you click it, you are given a new window into which you can paste your text. Before it is inserted into the content, it is scrubbed and sanitized to remove potentially hazardous code.

#. **Pasting plain text**: If you have formatted text that you want to insert without formatting, click the icon of a clipboard with a "T" on it. This version will strip all formatting code from your input before inserting it into the editor.

#. **Pasting HTML code**: When you are given HTML code to embed in your site, for example from a YouTube or Video video "embed code," *you cannot paste it directly into the editor window.* Because it is raw HTML code, it needs to be pasted into the "Raw HTML" window. Click the "HTML" button on the end of the toolbar to see your body copy in its raw HTML form. Locate where you want the code to appear, and paste into the popup window. When you close the window, it will render the HTML in the editor so you can see it in context.

Creating Links
--------------

Creating links in the editor is easy. Simply type the text you want to appear as a link, and use your mouse to select it. Then click on the "Create link" icon (a small chain link), and a new window will popup.

.. figure:: images/tinymce-link.*

* To create a simple link to an external website, you can simply enter the URL in the "URL Path" field and submit.

* To create a link to other content on your own website, you can either paste in the URL or use the menus as shown above to select your content based on the module and content type. The cascading menus will help build your URL based on your selections.

* In order to have your links **open in a new window,** simply check the checkbox "Open in new window" and a class will be added to your link to prompt the browser to open the link in a new window. This is a good idea for external websites, so users do not lose their place in your webiste.

* You can link directly to any of the images or documents in your Media repository by selecting the "Media Storage" tab and clicking on the media you want to link to. This is particularly useful when you want to create a text link to a PDF document for download.

Uploading photos to embed in body copy
--------------------------------------

See "Selecting and inserting media" above.

Debugging
=========

Manifesto stores a fair amount of detailed debugging information when users are viewing the site. When debugging is enabled in the site preferences (by an Admin), Editors and Admins are able to view detailed debugging information at the bottom of every page on the site.

This information is **not visible by normal users,** and is harmless, so do not worry if you see it enabled on the site. It allows developers and administrators to get detailed information on database queries, responses, and site configuration settings.

The Cache
=========

Storing website data in a database is efficient for managing the content, but the number of database queries required to build a full page for the site can quickly grow unmanageable. The more times you need to request information from the database, the slower the site becomes. Because of this, a technique known as *caching* has become common. This involves requesting information from the database, and then storing the results for a reasonable amount of time, so that you aren't recreating the same database queries over and over again, wasting valuable computing power.

Because you do not want to serve your visitors stale content, however, we must ensure that the cached information is flushed and recreated whenever the database changes.

For the most part, Manifesto manages this process automatically, and you should never have to concern yourself with flushing the cache. Under various circumstances, however, you may notice that a change you made to the database is *not* being reflected on the site.

If this ever happens, the Editor Concole has a link on the left-hand menu called **Clear cached files**. It is *always* safe to click this link, which flushes all existing caches and allows them to be rebuilt as needed. Do not hestite to use this link whenever you seem unable to view changes to the front end which you have successfully confirmed on the back end.
