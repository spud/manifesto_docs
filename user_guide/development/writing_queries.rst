***************
Writing Queries
***************

Manifesto currently works only with MySQL databases. There is a Connection class that handles the most rudimentary aspects of connecting to the database, and you should be able to use Manifesto for most activities without ever having to establishing a database connection manually.

The Oracle class (as in "ask the Oracle at Delphi", not the database company) is the parent of all database-querying classes. The properties of the Oracle class correspond largely to the various components of a database query. The most significant properties are:

* tablename
* selectfields
* where_clause
* orderby
* limit_count
* limit_start
* ref_class

So you can construct a query on any table as follows::

	$o = new Oracle;
	$o->set_tablename('mytable');
	$o->set_selectfields('mytable.*');
	$o->set_where_clause('objectid > 256');
	$o->set_limit_count(10);
	$o->set_orderby('lastname');
	$o->get_record(); // see below for more information on this method

And this will construct a query that looks like

``SELECT mytable.* FROM mytable WHERE objectid > 256 LIMIT 10 ORDER BY lastname;``

That would be the long way. Most classes are built with their own Oracle class that ex-tends the parent Oracle, so, for example, a "MediaOracle" might include a constructor method that sets reasonable defaults, e.g. ::

	function MediaOracle() {
		$this->set_tablename('media');
		$this->set_selectfields('media.*');
		$this->set_orderby('created_datetime DESC');
	}

So that you can use it more efficiently for your own queries, like ::

	$o = new MediaOracle();
	$o->set_where_clause("mime_type = 'image'");
	$o->get_record();


About get_record()
==================

The get_record() method of the Oracle class has three possible response values:

* **false, with error_flag=1** means an error was returned and is stored in the "error" property of the Oracle
* **false, with error_flag=0** means the query was executed successfully, but returned no results
* **true** which means that the Oracle's "response_array" and/or "object_array" properties will contain the results

The format of the result array is dependent upon the get_record() call. Manifesto always takes the results from the query, and stores each row as an associative array in the re-sponse_array property. Using this method, you can loop through the response_array an output the data, e.g. ::

	foreach($oracle->response_array as $i=>$row) {
		echo 'Row '.$i.' is a user with the lastname '.$row['lastname'];
	}

The advantage to object-oriented programming in this context is that you are able to work with actual objects, not just associative arrays. For this reason, the parent Oracle class in Manifesto defines a method called make_objects() that loops through the stan-dard database results ($response_array) and builds content objects for each row. It uses the "ref_class" property of the Oracle to determine what sort of objects to instanti-ate. The resulting objects are stored in the object_array property of the Oracle. So, to revisit our example, you could also do ::

	foreach($oracle->object_array as $i=>$obj) {
		echo 'Row '.$i.' is a user with the lastname '.$obj->lastname;
	}

Since you have full objects at your disposal, you can leverage the full power of the ob-ject, such as echoing ``$obj->get_fullname()`` or ``$obj->display_addresses()``.

Populating the object_array property is standard procedure for Oracle clases, so if you want to avoid creating the object_array, you must call get_record(false). This optional parameter indicates that Manifesto should not attempt to call the make_objects() method for the results. This can be useful for landing pages, where your intention is to display a list of only one or two properties (like title and author), and you don't need to query the database for every field in the table when you will only be displaying a handful of fields.

What about updates?
===================

Most database updates and inserts in Manifesto occur for a single row in the database at a time, and therefore usually correspond to properties of a Manifesto content object. Objects in Manifesto are capable of saving themselves to the database, so you rarely need to execute manual updates of the database. Most of the time, you simply populate the properties of an object using the standard setters, e.g. ``$object->set_title('My title')``
and then save the entire object to the database by calling $object->set_record()

All the complexity is handled internally by Manifesto, so you don't need to worry about it.

In cases where you do want control over the update process, there is a "set_clause" property of Oracle objects that acts much like the "where_clause" property, and there is an "update()" method that handles the rest of the procedure. For example::

	$oracle = new MediaOracle();
	$oracle->set_set_clause("mime_type = 'application'");
	$oracle->set_where_clause("mime_type = 'x-application'");
	$oracle->update();

This would produce a query like ::

   UPDATE media SET mime_type = 'application' WHERE mime_type = 'x-application';

**BUT I WANT TO DO ANYTHING I WANT!**

Fine. You can do that too. If you want to build your own SQL query, you can simply do so::

	$sql = "DELETE FROM any_table WHERE baz >= 23";
	$oracle = new Oracle();
	$oracle->send_raw_sql($sql);

And voilà, it is done.

Shortcuts
=========

There are few handy shortcuts in the Oracle class for frequently-used queries. Since every object in Manifesto has a unique ID (called "objectid") within its own database ta-ble, there is a shortcut for accessing a single, unique object from the database, by call-ing the "get_unique()" method of the appropriate Oracle class and passing the objectid of the object you are requesting. This method either returns boolean FALSE, or the ob-ject you requested, e.g. ::

	$oracle = new MediaOracle();
	$object = $oracle->get_unique(14);

If you need to perform a similar query, but on a field other than the objectid field, you can use an additional parameter to specify the field to search on, e.g. ::

	$oracle = new MediaOracle();
	$object = $oracle->get_unique('My First Picture','title');

While Manifesto is largely designed to identify unique records based on ID numbers, this extended functionality accomodates the uses of longer, text-based identifiers fre-quently seen in blog entries and other search-engine-optimized URLS like::

   http://www.example.com/blog/my-long-blog-title-about-whatever

To cover the possibility of errors, the complete code sequence would look something like this::

	$oracle = new MediaOracle();
	if ($object = $oracle->get_unique(14)) {
		// do stuff with the object, e.g.
		$object->display();
	} else {
		if ($oracle->error_flag) {
			// an error occurred in the query! Tell the Oracle to dis-play it!
			$oracle->display_error();
		} else {
			// no error, but no result either! Inform the user!
			echo ('There was no object with that ID');
		}
	}

Complex Conditions, Joins and Such
==================================

All this simple stuff is nice, but sometimes you need to perform substantially more com-plex queries, with table joins. The procedure is much the same as in the basic queries. Whenever you are dealing with queries that involve more than one table, it is a good idea to get in the habit of using full table notation for field names, e.g. "users.firstname" instead of "firstname". This can avoid substantial confusion when joined tables contain identically-named fields.

The set_tablename() method defines the primary table for the query (the significance of being "primary" comes into play when generating objects from the result array).

If you want to perform simple cross-joins, the add_tablename() method will append one or more databases to the query. Any time you employ additional tables you will also want to include a "where" clause that restricts the results to the appropriate matching rows in the secondary table. So, for example, you could get a list of users AND their preferences with something like this::

	$oracle = new UserOracle(); // sets the tablename to "users" in the constructor
	$oracle->add_tablename('user_prefs');
	$oracle->set_selectfields('users.*,user_prefs.preference,user_prefs.value');
	$oracle->set_where_clause('users_prefs.user_id = users.objectid');
	$oracle->get_record(false);
	$results = $oracle->response_array;

The raw SQL query generated by the code above would be::

	SELECT users.*, user_prefs.preference, user_prefs.value
	FROM users JOIN user_prefs
	WHERE user_prefs.user_id = users.objectid

and you would receive an array of results. However, the number of results would NOT correspond to the number of users. It would equal

``number of users * number of preferences for each user``

So you would have, for example,

==  =====   ====    ==========  ========
ID	First	Last	Pref		Value
==  =====   ====    ==========  ========
12  John    Doe	    last_login	01/01/09
12  John    Doe	    user_type	Editor
12  John    Doe	    eyes		Blue
15  Susan   Smith   last_login	12/31/08
15  Susan   Smith   user_type	User
==  =====   ====    ==========  ========

Ganging Results
===============
This multiple-rows-per-person format can be somewhat inconvenient to work with when you are looping through the results and hope to have each iteration correspond to a single person.

To handle situations like this, the generic Oracle class includes a "gangby" property. If you set ::

   $oracle->set_gangby('id');

Then the results are returned to you as an array of arrays -- the outermost array corre-sponds to a single ID number (and therefore to a single person), and its contents are an array, each element of which is one of the rows corresponding to that user.

So to iterate through your results, you could do this::

	foreach($results as $id=>$array) {
		$firstname = $array[0]['first'];
		$lastname = $array[0]['last'];
		echo $id.': '.$firstname.' '.$lastname.'<br />';
		foreach($array as $pref_array) {
			echo $pref_aray['pref'].' = '.$pref_array['value'].'<br />';
		}
		echo '<br />';
	}

And you would print::

	12: John Doe
	last_login = 01/01/09
	user_type = Editor
	eyes = Blue

	15: Susan Smith
	last_login = 12/31/08
	user_type = User

Left Joins
==========
If you're very familiar with SQL, you would realize that the query above would return no results for a user if the user had NO preferences set. You would not even see their ID, first, or last name. To get results back from a JOIN that includes records with no rows in the joined table, you need to use a LEFT JOIN. A left join basically says "give me results for ALL users no matter what, and if they have no preferences, return NULL in the cor-responding fields."

The query above, re-written as a left join, would look like this::

	$oracle = new UserOracle();
	$oracle->set_selectfields('users.*,user_prefs.preference,user_prefs.value');
	$oracle->set_left_join('user_prefs ON users_prefs.user_id = us-ers.objectid');
	$oracle->get_record(false);
	$results = $oracle->response_array;

and the results might look like this:

==  =====   ======  ==========  ========
ID	First	Last	Pref		Value
==  =====   ======  ==========  ========
12  John    Doe	    last_login	01/01/09
12  John    Doe	    user_type	Editor
12  John    Doe	    eyes		Blue
15  Susan   Smith   last_login	12/31/08
15  Susan   Smith   user_type	User
16	Bob	    Barker  NULL        NULL
==  =====   ======  ==========  ========

because the user whose ID is 16 has no preferences set in the user_prefs table.
