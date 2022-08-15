***************************
Glossary of Manifesto Terms
***************************

To facilitate clarity when discussing various aspects of Manifesto, this glossary offers definitions for terms used to describe elements and concepts in Manifesto.

.. glossary::
   :sorted:

   **Admin Console**
   The administrative and site configuration in Manifesto is contained behind another password-protected portal located at http://www.example.org/admin. The term *admin console* is generically used to describe that section of the website.

   **Cache**
   The *cache* is a data storage system for quickly retrieving information that might be time-intensive to recreate. For example, building a page listing your Board of Directors requires one or more database queries to retrieve the personanel listing, corresponding photos, etc. Since the listing is unlikely to change on a daily basis, it is considered safe to simply store the fully-assembled page for 24 hours, and avoid returning to the database every time the page is requested.

   There are, of course, rather complicated rules in place to help ensure that the "freshness" of the content is appropriately gauged -- a calendar listing needs more constant freshening than a privacy policy page. Manifesto is desgined to handle these situations effectively, always returning the most up-to-date content, but the cache may always be cleared manually without repercussion.

   **Content Object**
   This term is used to describe a specific instance of a *Content Type*. While "CalendarEvent" is a *content type,* the event "Lunch with Bono on January 12" is a *content object* -- a particular instance of a generic type. You can generally think of content objects as analogs to their real world counterparts: a book, an event, a user profile, an HTML page -- these are all various *content objects* you may find in Manifesto.

   There is no direct relationship between a "web page" and a "content object" -- a web page may display several content objects at once (a listing of upcoming events), or just one (a single blog post and nothing else).

   **Content Type**
   **Class**
   A specific collection of data properties ("title", "author", "body copy", "date of publication") is generically referred to as a *Content Type*. A PHP Class file in Manifesto usually defines the structure of a content type, enumerating its properties, and methods for maniulating it (display, edit, update, etc).

   Often referred to as simply a *class,* since the PHP class file is what describes the technical implementation of a content type. WordPress' "custom post types" would be individual content types in Manifesto.

  **Controller**
   Every module has a controller file, which handles the incoming request and properly routes code execution to the proper sequence. It is a standard component of the MVC (Model-View-Controller) paradigm common to many CMSes.

   Unlike most of Manifesto, controllers are purely functional programming, with a `switch` statement for handling the request, rather than the controller being an Object with methods handling the request. In Manifesto, the snippets of code for responding to a particular request are called "handers" for the sake of convenience.

   **Editor Console**
   The editorial management of content in Manifesto is contained behind a password-protected portal located at http://www.example.org/editor. The term *editor console* is generically used to describe that section of the website.

   **Event**
   Manifesto's code is filled with specific locations where outside code is permitted to interact or insinuate itself into the program execution. Those locations are called "Events" (sometimes referred to as "hooks"). For example, there is a "page_end" event that allows modules to add output to the end of the HTML page, and there is an "object_edit" event that allows modules to modify the editing interface for some kinds of content. cf. the **Listener** entry, which describes the code that responds to events.

   **Handler**
   An informal way to describe the fork responsible for responding to a particular function within a controller. For example, most modules have some code in the controller.inc file to execute whenever a page is displayed, and that code would be referred to as "the display handler."

   **Icon**
   When more than one image is associated with a content object, we may wish to select one of these images to be the official representative photo for the content. Such a selected photo is referred to as the `icon` of the content.

   **Landing Page**
   This usually refers to the top-level page of a particular section of your website, e.g. the page you arrive at when you click on "News" might be referred to as the "News landing page."

   **Listener**
   A Listener is a bit of code designed to respond when a particular event is triggered. For example, when the "page_end" event is triggered, the jQuery module has a listener that will output the code necessary to load jQuery at the end of the page.

   **Listing Page**
   This expression is used to describe the common page which displays a simple list of all the available objects in a particular module. On the back end, it is the default format for presenting existing content for editing. On the front end, this phrase might refer to e.g. the page that displays your staff directory or list of locations. For sections of the website without much textual content, the "listing page" might also be called a "landing page."

   **ManifestoObject**
   The base class from which Manifesto content types descend. It defines the basic properties of all content types, such as ID, creation date, associated media, deleted status, etc. Roughly corresponds to the generic "node" in Drupal.
      
   **Module**
   Manifesto organizes groups of content types and functionality into collections called *modules.* For example, if you decide "I want to have a calendar on my website," you are really asking for a collection of things:

   * A CalendarEvent class
   * An EventLocation class
   * Forms that allow you to edit event and location objects
   * A set of templates that can display listings, details, and other views of the information

   This collecton of class files and acoompanying scripts is referred to as a module, and such modules form the basis of a Manifesto website.

   Modules in Manifesto are designed to be self-contained, with their own class definitons, their own scripts, images, and stylesheets. Modules can be enabled and disabled on a case-by-case basis, and a well-designed module can be turned on and off without affecting any other aspects of the site.

   **Oracle**
   The class of Manifesto objects responsible for querying the appropriate tables in the database. There is a base Oracle class that contains all of the methods needed to build and execute a SQL query, and most content types define their own class of Oracle configured to their specific needs.

   So, for example, the BlogEntryOracle inherits the functionality of the Oracle class, but is pre-configured to query the `blog_entries` table, and to return results in reverse chronological order.

   **Shortname**
   The `shortname` field is a common property of many types of content in Manifesto. Basically, the `shortname` is an abbreviated, URL-friendly version of the normal identifier for the content (like `title`). In order to allow Manifesto to build programmatic URLs for content, you may often be asked to provide a `shortname` for your content. In most cases, Manifesto will try to intelligently offer a suggested shortname for you, based on the title or other identifier in your content.

   The most important thing to remember is that it needs to be URL safe. No spaces or strange punctuation. Dashed are usually used to separate words, but most other punctuation is removed.