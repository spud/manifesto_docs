***************
Ganging Results
***************

The multiple-rows-per-person format can be somewhat inconvenient to work with when you are iterating over the results and hope to have each iteration correspond to a single person.

To handle situations like this, the generic Oracle class includes a "gangby" property. If you set ::

   $oracle->set_gangby('objectid');

Then the results are returned to you as an array of arrays -- the outermost array corresponds to a single ID number (and therefore to a single person), and its contents are an array, each element of which is one of the rows corresponding to that user.

So to iterate through your results, you could do this::

	foreach($results as $id=>$array) {
		$firstname = $array[0]['first'];
		$lastname = $array[0]['last'];

		echo $id.': '.$firstname.' '.$lastname.'<br />';

		foreach($array as $pref_array) {
			echo '&nbsp;'.$pref_aray['pref'].' = '.$pref_array['value'].'<br />';
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
