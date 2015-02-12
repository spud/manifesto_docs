**************
Blog
**************

Blogs are a great way to keep up-to-date news prominent on your site, or to give you a dated forum for longer essays, reflections, or commentaries. Blogs can be for simple announcements, a daily journal, or a thematic collections of writing.

   .. note::

   This information discusses the *Blog* module. If your site uses the *Dated Posts* module, which provides much of the same functionality without multiple blog capability, please see that section of the manual instead.

Because Manifesto can host more than one blog (perhaps the President has one, and the head of IT has a separate one), it creates a conceptual distinction between a *Blog* (the container, or umbrella), and a *Blog Entry* (the individual posts).

The *Blog* is a simple entity, with a title, coordinator, optional description, and an owner. Unlike many other modules, a Blog can have more restrictive permissions, allowing only a single person to create and edit new blog posts, rather than permitting unfettered access to anyone with Editor permissions. These are called "owners" of the blog. And a blog entry is more likely (but not required) to indicate the author, unlike most of the other content on a website.

Creating your first blog
========================

After initially installing the module, the editorial interface will prompt you to create a Blog before you can begin adding blog entries.

.. figure:: images/blog-edit.*
   :width: 600 px
   :align: center

The *Cooridinator* is simply used to describe the person or entity under whose purview the blog runs. They may or may not be a contributor themselves, but they are considered to be responsible for the blog.

The *Blog Name* and *Short Name* are self-explanatory, and the *Description* is optional -- your layout may or may not display the description at the top of the landing page, as an introduction to the blog.

The *Owners* menu will display all of the available Editor accounts (i.e. people who already have access to login to the editorial console). You may click to select a single owner, or Shift-click (or Command/Alt-click) to select a discontiguous group of owners.

For an already-existing blog, current owners will be display beneath the selection box, and individual owners can be removed at will.

Once you've created a single blog, the editorial interface changes a bit. Rather than showing you a list of your blogs (you only have one!), it defaults to displaying only your blog entries -- under the assumption that, once you have a blog set up, you want to dive right in to the entries. (If you have *more* than one blog, it will always default to displaying a list of your exisiting blogs, so that you may choose the one to which you want to contribute).

.. figure:: images/blog-listing.*
   :width: 600 px
   :align: center

.. figure:: images/blog-toolbar.*
   :align: right

In the case of having only one blog, you still may want to edit the name or details of the blog, or to return to the list of blogs so that you can add another. In such cases, you can find the appropriate links in the upper-right corner of the page, just below the "Module Options" link.

Adding another blog
===================

.. figure:: images/blog-add.*
   :width: 600 px
   :align: center

To create a new blog, you need only to return to the Blog listing page (use the icon in the upper-right if you only have one blog currently), which looks like the image above. Click on the "New Blog" link, and the rest of the process is identical to the creation of the first blog.

   .. note::

      One important thing to note is that the default landing page for the Blog module will be affected by the introduction of an additional blog. There is a module preference for how the default landing page should be constructed, where the two choices are to display the *most recent blog entries in reverse chronological order* regardless of which blog they are from, or to *group the posts by blog,* showing the most recent blog entry from each blog.

      This option can be toggled from the **Module Options** link in the upper-right corner.

Adding blog entries
===================

From the multiple-blog listing page, you may click on the "Add" button of the appropriate blog to create a new Blog Entry. If you have only one blog, the "New Blog Entry" link will be displayed at the bottom of the listing page.

.. figure:: images/blog-entry-edit-1.*
   :width: 600 px
   :align: center

The top half of the form will display the name of the blog to which this entry belongs, and, if one or more category groups are associated with the Blog module, you will be able to select one or more categories to assign to the blog entry.

The **Author/Contributor** menu should be prepopulated with your name, but allows you to select from any one of the Owners of the blog. In the case of a "Guest Editor," for a blog post, you may manually enter any name into the secondary **Author** field, and that name will be credited in the byline for that post.

The **Heading** and related **Shortname** fields are for the main title of your entry, and the corresponding URL-friendly "shortname" string, which will be used to complete the direct link URL to this entry.

.. figure:: images/blog-entry-edit-2.*
   :width: 600 px
   :align: center

Because the format of blogs often consists of displaying a landing page with an excerpt or summary paragraph, a Blog Entry contains separate fields for **Summary** and **Body**. The Summary is not required, and if your layout template calls for a summary that isn't available, it will automatically create an excerpt of the Body field to display in its place.

The **Associated Media** section works as it does with all Manifesto content, keeping track of uploaded and selected media that is attached to the current content.