******************************
Date formats and manipulations
******************************

The Manifesto Date class has a number of useful methods for displaying dates in a variety of formats and for performing date calculations. This is a quick reference to some of the more common operations.

Output Formats
**************

**Current Date/Time**
``Date::now()``
This static function will create a Manifesto Date object set to the current date and time

**MySQL date format**
*ex. 2018-01-02*
``$d = Date::now()``
``$mysql_date = $d->get_mysql_date()``

**MySQL datetime format**
*ex. 2018-01-02*
``$d = Date::now()``
``$mysql_date = $d->get_mysql_datetime()``

**MySQL time format**
*ex. 2018-01-02*
``$d = Date::now()``
``$mysql_date = $d->get_mysql_time()``

**Short format**
*ex. 01/30/12 or 30/01/12 depending on Date locale settings*
``$d = Date::now()``
``$mysql_date = $d->get_date('date_short')``

**Long format**
*ex. January 30, 2012 or 30 January 2012 depending on Date locale settings*
``$d = Date::now()``
``$mysql_date = $d->get_date('date_long')``

**Extended format**
*ex. Sunday, January 30, 2012 or Sunday, 30 January 2012 depending on Date locale settings*
``$d = Date::now()``
``$mysql_date = $d->get_date('date_extended')``

**Datetime format**
*ex. Jan 30, 2012 2:45:13 PM or 30 Jan 2012 2:45:13 PM*
``$d = Date::now()``
``$mysql_date = $d->get_date('datetime')``

**Arbitrary formats**
Any format that can be expressed to the PHP date() function may be used for Manifesto dates as well
``$d = Date::now()``
``$mysql_date = $d->get_date('l jS \of F Y h:i:s A')``
This would provide a date string like **Monday 8th of August 2005 03:12:46 PM**
