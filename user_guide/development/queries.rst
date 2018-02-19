*******
Queries
*******

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

	$oracle = new Oracle;
	$oracle->set_tablename('mytable');
	$oracle->set_selectfields('mytable.*');
	$oracle->set_where_clause('objectid > 256');
	$oracle->set_limit_count(10);
	$oracle->set_orderby('lastname');
	$oracle->get_record(); // see below for more information on this method

And this will construct a query that looks like

``SELECT mytable.* FROM mytable WHERE objectid > 256 LIMIT 10 ORDER BY lastname;``

That would be the long way. Most classes are built with their own Oracle class that extends the parent Oracle, so, for example, a "MediaOracle" might include a constructor method that sets reasonable defaults, e.g. ::

	function MediaOracle() {
		$this->set_tablename('media');
		$this->set_selectfields('media.*');
		$this->set_orderby('created_datetime DESC');
	}

So that you can use it more efficiently for your own queries, like ::

	$oracle = new MediaOracle();
	$oracle->set_where_clause("mime_type = 'image'");
	$oracle->get_record();

Building the query programmatically
===================================

set_module
----------
Sets the name of the module responsible for this query. Used largely for auditing and tracking purposes.

set_tablename
-------------
This method sets the primary database table to be queried. If a query will join multiple tables, this method should be used to set the first table, and ``add_tablename`` should be used for the rest. This method designates the initial table as the $master table as well, and that is used by some common join queries (e.g. ``hash_category`` joins) to know which table's ``objectid`` to join on. This method is *destructive* in that subsequent calls will overwrite the initial fields.

add_tablename
-------------
This method adds a table to the initial query. It is generally used in conjunction with a modification to the ``SELECT`` clause and/or to the ``WHERE`` clause (otherwise, why are you joining the table?). This method is *non-destructive* and *additive* in that subsequent calls will append to the existing query.

set_selectfields
----------------
This method sets the initial ``SELECT`` part of the query (minus the word ``select``), listing the fields you wish to retrieve from the query. Because Manifesto is modular, it is often possible for other modules to add tablenames and select fields to the initial query, so it is standard practice to include full ``table.fieldname`` references in the ``SELECT`` section to avoid name collisions.  This method is *destructive* in that subsequent calls will overwrite the initial fields.

add_selectfields
----------------
This method adds one or more fields to the ``SELECT`` portion of a query. It must be used in conjunction with ``add_tablename`` because you must be joining the table from which you are selecting the fields. This method is *non-destructive* and *additive* in that subsequent calls will append to the existing query.

set_where_clause
----------------
This method establishes the conditions for the query in the ``WHERE`` clause. This method is *always additive* in that calls will always append to the existing query. The most basic example is to pass in a simple comparitive statement like ``"objectid = 23"``. And while multiple calls to this method may be chained together, you may also pass in more complex statements like ``"objectid = 23 AND (post_date > '2018-01-01' OR status = 'New')"``. See more examples below.

prepend_where_clause
--------------------
This behaves almost exactly like ``set_where_clause``, but it is inserted at the beginning of the ``WHERE`` clause during execution. Normally, this shouldn't be necessary, but it can be used to help manually optimize queries by adjusting the priority of the conditions.

set_having_clause
-----------------
This sets the ``HAVING`` portion of a query. This method is *destructive* in that subsequent calls will overwrite the initial fields.

set_join
--------
This method allows you to pass in an entire straight join statement in a single call, e.g.::

$this->set_join('hash_categories ON (hash_categories.category = othertable.objectid)');

This method is *always additive* in that calls will always append to the existing query.

set_left_join
-------------
This method allows you to pass in an entire left join statement in a single call, e.g.::

$this->set_left_join('hash_categories ON (hash_categories.category = othertable.objectid)');

This method is *always additive* in that calls will always append to the existing query.

set_right_join
--------------
This method allows you to pass in an entire right join statement in a single call, e.g.::

$this->set_right_join('hash_categories ON (hash_categories.category = othertable.objectid)');

This method is *always additive* in that calls will always append to the existing query.

set_union
---------
This method allows you to pass in a whole other Oracle object to join the two combined queries with a ``UNION`` statement.


.. toctree::
   :maxdepth: 3
   :caption: More about queries
   
   queries/retrieving_data
   queries/updates
   queries/joins
   queries/ganging_results
