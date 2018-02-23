****************************
Modularity and Regimentation
****************************

When we say that Manifesto is a *modular* CMS, we mean something more than *"it has plugins."* Manifesto is both modular and rigidly structured, which allows its modules themselves to be modular, designed to interoperate with other modules as seamlessly as they might work with the core.

For example, while Manifesto is perfectly capable of executing a complete SQL query (simply written out as a string), it virtually always builds a complete SQL query using Oracle objects, composed of discrete units (select fields, where clause, order by, etc) concatenated together before being executed. Why does it use so much extra overhead to do things that way?

The answer is *to ensure modularity.* Building a database query in steps provides an architecture for other modules to inject their own code into the query (with permission, of course), and this opens endless possibilities for module development. We can, for example, create a "restricted access" module than allows you to set special permissions on ANY piece of content on the site -- whether it be a page, a user profile, or an MP3 download. The module wouldn't care -- it would simply inject some SQL into every (relevant) query that would simply exclude results if the permissions were not right. Similarly, we could create a module that would lookup metadata for every single row of a set of database results.

Of course, this comes at the cost of a certain simplicity for database queries; we want to avoid executing raw SQL in most circumstances, since it would bypass many of the hooks that make Manifesto modular and flexible.
