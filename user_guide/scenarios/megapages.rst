****************
Mega-pages
****************

Mega-pages aren't a module per se, but a special set of templates that are designed to create long, scrolling pages that are actually an aggregate of parent and child pages, each of which is managed on the backend as individual content.

In the Editor Console, all of the pages are managed as a hierarchy of pages, divided up into the six main sections of the site. The idea is that each of the six top-level sections would initially be displayed as a single page, with full child pages directly embedded.

All pages have a title, summary, and body copy field, and beyond that, different templates may have additional fields.

Of course, those child pages each have their own template as well, so they in turn may also embed grandchild pages, either partially or entirely depending on their own template.

Here is a breakdown of the current Template Pages:

* **Level 1 Megapage**
  This template is designed to display a section-specific banner, with custom image and custom prayer at the top. The body copy of the current page is then displayed.

  Pages which are immediate children of these top-level pages are displayed beneath the master page, in sequential ordrer. Many of these second-level pages also have child pages, and you will often see photo/summary teasers linking to these third-level pages.

* **Child Block**
  This is the most common page template, and is designed to be embedded on a Level 1 or Level 2 megapage. It is also capable of embedded links to its own child pages in one of two formats.

  In addition to the standard fields, the Child Block also contains a *Content Info* field (allowing one or more contact to be listed in the sidebar), an *Event Category* that allows you to embed a listing of upcoming events within a particular category, a *Links* collection that permits the addition of related links in the sidebar. And you can specify whether child pages are linked using a single-column (stacked) layout, or a two-column (grid) layout.

* **Level 2 Megapage**
  This template is a cross between the first two templates described above. It is designed to have full child pages embedded on it, but it also includes the events, links, and contact fields used by the Child Block.

* **Calendar View**
  This is a good example of a module-specific template, designed to output content from another module, embedded on your template page.

  In this case, you may select a category from which to pull events, and the template takes care of querying the database for upcoming events within that category, and displays them on the page.

* **Photo Gallery**
  This template allows you to select from the available categories to build a page with photos in the Media Gallery that are assigned to that category. The template pulls the 9 most recent matching images, and displays them in a custom-designed grid.

* **Standalone Form**
  Another module-specific template, this template allows you to select an already-create form from the FormBuilder module, and to build a page to display it. The template also allows you to control what happens after a user submits the form: you can either display a custom confirmation messsage, or you can redirect the user to a URL of your choosing.

* **Form with Registration**
  This is a complex template that essential combines and performs two tasks at once: including a form to be filled out by the user, *and* allow the user to select Registration Items (e.g. a class, camp schedule, etc.) which have corresponding prices and require a checkout process.

  First, the page embeds the form you select. Then, below that appears the Registration form, including all available Registration Units. The user completes the form and the registration selections, and Manifesto cleverly does two things:

  #. It submits the FormBuilder form via AJAX, checks for errors, and returns the result.

  #. If that submission was successful, it submits the Registration portion of the page, adding items to a shopping cart, and ultimately directing the user through the Checkout processs.

* **Staff Directory** and **Staff Listing**
  These two templates are designed to output sub-sections of the entries in the Staff module. They differ only in the manner by which they group and display the resulting staff entries.

With only these 9 templates, we have been able to generate nearly 500 pages with a good balance of consistency and variation.