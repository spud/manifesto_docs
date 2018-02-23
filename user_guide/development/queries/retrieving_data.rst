*****************************
Retrieving Data: get_record()
*****************************

The get_record() method of the Oracle class has three possible response values:

* **false, with error_flag=1** means an error was returned and is stored in the "error" property of the Oracle
* **false, with error_flag=0** means the query was executed successfully, but returned no results
* **true** which means that the Oracle's "response_array" and/or "object_array" properties will contain the results

The format of the result array is dependent upon the get_record() call. Manifesto always takes the results from the query, and stores each row as an associative array in the ``response_array`` property. Using this method, you can loop through the ``response_array`` an output the data, e.g. ::

	foreach($oracle->response_array as $i=>$row) {
		echo 'Row '.$i.' is a user with the lastname '.$row['lastname'];
	}

The advantage to object-oriented programming in this context is that you are able to work with actual objects, not just associative arrays. For this reason, the parent Oracle class in Manifesto defines a method called make_objects() that loops through the standard database results ($response_array) and builds content objects for each row. It uses the "ref_class" property of the Oracle to determine what sort of objects to instantiate. The resulting objects are stored in the object_array property of the Oracle. So, to revisit our example, you could also do ::

	foreach($oracle->object_array as $i=>$obj) {
		echo 'Row '.$i.' is a user with the lastname '.$obj->lastname;
	}

Since you have full objects at your disposal, you can leverage the full power of the object, such as echoing ``$obj->get_fullname()`` or ``$obj->display_addresses()``.

Populating the object_array property is standard procedure for Oracle clases, so if you want to avoid creating the object_array, you must call get_record(false). This optional parameter indicates that Manifesto should not attempt to call the make_objects() method for the results. This can be useful for landing pages, where your intention is to display a list of only one or two properties (like title and author), and you don't need to query the database for every field in the table when you will only be displaying a handful of fields.

Shortcuts
=========

There are few handy shortcuts in the Oracle class for frequently-used queries. Since every object in Manifesto has a unique ID (called "objectid") within its own database table, there is a shortcut for accessing a single, unique object from the database, by calling the "get_unique()" method of the appropriate Oracle class and passing the objectid of the object you are requesting. This method either returns boolean FALSE, or the object you requested, e.g. ::

	$oracle = new MediaOracle();
	$object = $oracle->get_unique(14);

If you need to perform a similar query, but on a field other than the objectid field, you can use an additional parameter to specify the field to search on, e.g. ::

	$oracle = new MediaOracle();
	$object = $oracle->get_unique('My First Picture','title');

While Manifesto is largely designed to identify unique records based on ID numbers, this extended functionality accomodates the uses of longer, text-based identifiers frequently seen in blog entries and other search-engine-optimized URLS like::

   http://www.example.com/blog/my-long-blog-title-about-whatever

Manifesto throws an exception if a get_unique query fails (since a request for an explicit piece of content is expected to succeed), so a failed query will usually redirect the user to a 404 page. If you wish to catch the exception and handle it differently, simply wrap your query in a try...catch statement::

try {
	$oracle = new MediaOracle();
	$object = $oracle->get_unique($some_id);
} catch(ResourceNotFoundException $e) {
	error_log('I tried to find Media '.$some_id.' but it was not there');
	// Continue without the media, or maybe replace it with some fallback image?
}
