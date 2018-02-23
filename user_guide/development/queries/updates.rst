*******************
What about updates?
*******************

Most database updates and inserts in Manifesto occur for a single row in the database at a time, corresponding to the properties of a Manifesto content object. 

Objects in Manifesto are capable of saving themselves to the database, so you rarely need to execute manual updates of the database. Most of the time, you simply populate the properties of an object using the standard setters, e.g.::

$object->set_title('My title');
$object->set_body('<p>This is the body of my content.</p>');

and then save the entire object to the database by calling::

$object->set_record();

All the complexity is handled internally by Manifesto, so you don't need to worry about it.

In cases where you *do* want control over the update process, there is a "set_clause" property of Oracle objects that acts much like the "where_clause" property, and there is an "update()" method that handles the rest of the procedure. For example::

	$oracle = new MediaOracle();
	$oracle->set_set_clause("mime_type = 'application'");
	$oracle->set_where_clause("mime_type = 'x-application'");
	$oracle->update();

This would produce a query like ::

   UPDATE media SET mime_type = 'application' WHERE mime_type = 'x-application';

**BUT I WANT TO DO ANYTHING I WANT!**

Fine. You can do that too. If you want to build your own SQL query, you can simply do so::

	$oracle = new Oracle();
	$oracle->send_raw_sql("DELETE FROM any_table WHERE baz >= 23");

And voilà, it is done.

