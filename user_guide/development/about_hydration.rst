***************
About Hydration
***************

*Hydration* is the term Manifesto uses to describe the process of pre-populating complex object properties (the kind that don't correspond to a simple Active Record-style database column). Here's an example:

Let's say we have a News object, and in addition to some basic properties like "Title" and "Body Copy," it can have one or more categories assigned to it, and it can have one or more associated images. These associated properties aren't stored in the basic "news" table in the database; they are stored in several other tables, and their association with the News object is the result of standard relational database associations.

At a basic level we can start with a plain News object number 34::

$oracle = new NewsOracle();
$news_object = $oracle->get_unique(34);
// SELECT news.* FROM news where objectid = 34;

That's one database query to retrieve the News data.

Then, to get the categories that it falls under, we might do something like::

$news_object->get_categories();
// SELECT hash_categories.* FROM hash_categories WHERE ref_class = "News" and ref_id = 34

And that would execute another database query to retrieve a list of categories.

Then, to find associated media, we might do something like::

$news_object->get_media_array();
// SELECT hash_media.* FROM hash_media WHERE ref_class = "News" and ref_id = 34

And that would execute another database query to retrieve a list of associated media.

We might also need to check access permissions or something too::

$new_object->get_permissions();
// SELECT workflow_access.* FROM workflow_access WHERE ref_class = "News" and ref_id = 34

You can see that, as we add more complex properties and relationships, it is easy to create the need for numerous database queries in order to fully form the content object we need.

If you are familiar with the difference between the Recursive List and a Modified Preorder Tree Traversal methods for dealing with hierarchical information, the process of *hydration* is a similar method of improving query efficiency.

Smarter queries
===============

The more efficient way to handle this situation is to execute **one** database query that gathers *all* the information you need.

If you carefully create a query with appropriate table joins, you can retrieve a whole slew of information as the result of a single request.

So, a more complex query like::

SELECT news.*,hash_categories.*,hash_media.*,workflow_access.* FROM news
   LEFT JOIN hash_categories ON (hash_categories.ref_id = news.objectid AND hash_categories.ref_class = "News")
   LEFT JOIN hash_media ON (hash_media.ref_id = news.objectid AND hash_media.ref_class = "News")
   LEFT JOIN workflow_access ON workflow_access.ref_id = news.objectid AND workflow_access.ref_class = "News")
WHERE news.objectid = 34

will return a series of records, which overall contain all the information we need to populate the News item fully (with categories, media, and approval access).

The problem, of course, is that while ::

$news_object = $oracle->get_unique(34);

returns a single database row, corresponding to a News object, our very complex query with table joins will return *multiple* rows based on how many relationships we have in our join tables.

Manifesto understands this, though, and knows how to loop through the data results and **consolidate** the multiple tables in a post-query processing routine known as *hydration.*

So when we get records back like (roughly)::

News item 34, category: Science
News item 34, category: Astronomy
New items 34, category: Europe
New items 34, media: Picture of Square Kilometre Array
New items 34, media: Picture of Steven Hawking
New items 34, access: Publisher

Manifesto understands this, and converts it to a single News object, like so::

News item 34 {
	headline: Deep Space is Neat!
	body: blah blah blah space blah quasar, blah
    categories: [Science, Astronomy, Europe]
    media_array: [Picture of Square Kilometre Array, Picture of Steven Hawking]
    access: Publisher
}


When This is Useful
===================

While executing a few extra database queries here and there for a single object might not be a huge problem, the problem becomes more obvious when retrieving a long list of objects.

Let's say you want a list of all the news items in your database, and the categories they include. The simple way looks like this::

$oracle = new NewsOracle();
$oracle->get_record();
$results = $oracle->object_array;
foreach($result as $news_object) {
	$news_object->get->categories();
	echo $news_object->title.': '.$news_object->category_list;
}

For 500 news objects, this requires 501 database queries.

Doing the same thing with table joins and Manifesto's built-in hydration functionality, you can accomplish the same result with **1** query.

Better, right?

Modular Flexibility
===================
To facilitate the ability to leverage this functionality, Manifesto includes two hooks in the database query and retrieval process.

The "query_hydrate" hook is called whenever an Oracle query is being built. Any module is permitted, at this point, to add select field, table joins, and where conditions to the query being built. This allows modules to write custom code to include their data in the query.

When retrieving data from joined tables, you must take care to **not** retrieve column names that might clash with column names already present in the query you're modifying. For example, you wouldn't want to retrieve the "objectid" from the "hash_categories" table, since it might override the "objectid" column already being retrieved from the `news` table.

The best way to avoid these conflicts is to carefully name the fields you wish to retrieve using aliases, e.g.

$oracle->add_selectfields('hash_categories.objectid as category_objectid,hash_categories.name as category_name');

That way, you ensure unique column names in the database results.

The "object_hydrate" hook is called whenever an Oracle query attempts to instantiate objects based on the query results. This gives each module an opportunity to wrangle their information into a format that corresponds with the object's properties.

When the News object reads in the database results in order to populate its properties, it will only handle those database columns that correspond to its default properties. When it encounters a database column called "category_name," and it has no corresponding object property called "category_name," it stores the value in a catch-all property called "props"

$obj->props is an array of data that doesn't have a corresponding property in the object. Any results that come back from a database query that don't correspond to a property are stored in $obj->props['dynamic'].

So after our complex join, but before object hydration, our News object would have some properties like ::

$news_object->prop['dynamic']['category_objectid'] = 12;
$news_object->prop['dynamic']['category_name'] = "Science";
$news_object->prop['dynamic']['category_shortname'] = "science";

and the object_hydrate method would loop over those results and use the data to instantiate a full Category object, which is then attached to the News post.