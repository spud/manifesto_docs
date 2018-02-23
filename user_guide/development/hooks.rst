*********************************
Integrating modules through hooks
*********************************

Manifesto's hook system is another name for what some systems call Events and Listeners.

Hooks are snippets of code that are peppered throughout Manifesto to give modules the opportunity to insinuate themselves into the processing that occurs when responding to a page request.

The main Page Layout templates, for example, are bare bones structures that define the skeleton structure of an HTML page. Beyond the simple structural elements, there are code blocks that basically say things like "I'm about to render the left-hand sidebar...are there any modules that want to insert content here?".
