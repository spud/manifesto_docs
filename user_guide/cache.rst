*********
The Cache
*********

Storing website data in a database is efficient for managing the content, but the number of database queries required to build a full page for the site can quickly grow unmanageable. The more times you need to request information from the database, the slower the site becomes. Because of this, a technique known as *caching* has become common. This involves requesting information from the database, and then storing the results for a reasonable amount of time, so that you aren't recreating the same database queries over and over again, wasting valuable computing power.

Because you do not want to serve your visitors stale content, however, we must ensure that the cached information is flushed and recreated whenever the database changes.

For the most part, Manifesto manages this process automatically, and you should never have to concern yourself with flushing the cache. Under various circumstances, however, you may notice that a change you made to the database is *not* being reflected on the site.

If this ever happens, the Editor Concole has a link on the left-hand menu called **Clear cached files**. It is *always* safe to click this link, which flushes all existing caches and allows them to be rebuilt as needed. Do not hestite to use this link whenever you seem unable to view changes to the front end which you have successfully confirmed on the back end.
