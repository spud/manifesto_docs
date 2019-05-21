***************
Quick Reference
***************

Images
======

Media files in Manifesto are, for the most part, raw data structures that you will not usually interact with. 

In most cases, you will be using a MediaInstance object, which is an instance of using a particular Media object in a particular context. A MediaInstance object may have a different caption, or different output dimensions or alignment than the base Media object it represents.

Fully-instantiated Manifesto objects that support images all have an ``media_array`` property (each element is a full MediaInstance object, and the array is iterable). You may also retrieve the associated image marked as the "icon" of your content with the simple call::

$img = $obj->get_icon();

and then display it with one of the pre-built output methods::

	echo $img->insert_file(); // Output standard size image in an IMG element, optionally linking to URL from $img->linkto property
	echo $img->insert_thumb($url=null); // Output the thumbnail image in an IMG tag, optionally linking to $url
	echo $img->insert_with_caption($variant=null) // Full-blown FIGURE tag with any size variant and FIGCAPTION if $img->caption is not empty
	
Bear in mind that all of these media insertion methods will *also* work with PDFs, documents, video files, etc. Each of them will handle the proper output method determined by the Mimetypes array and the methods in the ``media_output_formats.inc`` file.

If you prefer to handle the HTML output yourself::

$img->get_urlpath($variant=null)

will get you the full URL to your media file.

Dates
=====

Manifesto uses its own internal Date object for convenience, and automatically converts database date and datetime formats to Manifesto ``Date`` objects when they are retrieved from the database. From that point, you simply need to figure out what format you want to be used in the output::

$d = Date::now();

echo $d->get_date($format=null);

**date_short**: 01/30/12 or 30/01/12
**date_long**: January 30, 2012 or 30 January 2012
**date_brief**: 01/30 or 30/01
**extended**: Sunday, 30 January 2012
**nicedate**: Jan 30, 2012 14:45 or 30 Jan, 2012 14:45
**datetime**: 30 Jan 2012 2:45:13 PM
**datetime_utc**: 30 Jan 2012 14:45:13 UTC
**datetime_short**: 1/30 14:45 EST or 30/1 14:45 EST
**time_short**: 2:45 PM or 14:45
**dow**: 0-6 (Sunday-Saturday)
**monthname**: January
**time**: 2:45:36 PM or 14:45:36
**timewithzone**: 14:45:36 EST
**week**: 13 (Week of year)
**day_short**: Sat
**day_long**: Saturday
**ical_date**: 20120130
**ical_datetime**: 20120130T144536
**date**: return default date format (30 Jan 2012)
