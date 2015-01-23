*********************
Troubleshooting
*********************

Random tips for diagnosing problems, and solutions to commonly-encountered issues.

**Updated content not displaying on the front end**
===================================================

This is ususally a caching issue, and is usually quite easy to resolve: *clear the cache.*

Some background: web pages are rarely static documents being sent to your browser. Most of the time, they are complex, dynamically-generated documents pieced together from a variety of data sources. This collection and aggregation routine is a lot of work, even for a machine. *Caching* is the act of storing  already-generated results (HTML snippets, database query results, other calculated output) so they can be used again without the expense of recalculation. The next time a request is made, the pre-generated output is served as-is, avoiding the need to perform all that work again.

Your browser does this, usually on a very short term (which is why using the "Back" button works so quickly, without needing to re-request the whole page from the server). Sometimes the browser shows you stale content because it still has a stored copy. Different browsers have ways of requesting fresh content or emptying their cache, and quitting and restarting your browser is a reliable way to clear the cache.

Similarly, the server stores copies of complex rendered files too, and sends those to avoid doing all the extra work to recreate them. Of course, all of this caching of information generates a notion of "fresh" and "stale" content -- you want your pages to be served quickly (caching good!), but you don't want to serve old content after you've updated it (caching bad!).

Manifesto is designed to cache data (whole pages and partial pages) carefully, and to *flush the cache* whenever content is updated, so as to always serve fresh content.

There are occasionally situations, however, when the cache fails to be cleared automatically. In such cases, the solution is usually to click the "Clear cached files" item from the Editor or Admin Consoles. This is always a safe operation, as Manifesto will simply rebuild the cache as it needs to.

**Blurry Images**
===================================================

This is usually because the image is being displayed at a size larger than the source image (*"upsampling"*).

For example: a 250x250 image is being displayed at 500x500 because the CSS specifies `width:100%` within a 500px-wide column. The source image isn't that large, so the browser automatically scales it to a larger size, at the expense of its clarity -- blurriness is inevitable when you upscale an image.

Fortunately, this can often be solved by selecting a larger size image to insert into your content. In the earlier example, if you had selected "Thumbnail" size and found the images blurry , you could switch the size to the larger "Page default," and that instructs the server to use the larger image file as the source.

Unlike upsampling, *downsampling* will not damage the clarity of the image, so it is almost always better to choose a larger size image. The drawback of the larger size is that it increases your page size and page load time, so be cautious when selecting the appropriate image size.

Manifesto will, by default, create 3 image file versions:

#. Full-size (as it was uploaded)
#. Page default size (admin configuraable)
#. Thumbnail size (admin configurable)

So once you settle on a page design, you should try to set the "Page Default" and "Thumbnail" configuration setting to sizes that are optimized for the display sizes in your layout.