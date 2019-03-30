**********************************
Integrating modules through events
**********************************

Events are points in the code — they can be in layout templates or in functional execution — that are peppered throughout Manifesto to give modules the opportunity to insinuate themselves into the processing that occurs when responding to a page request.

The main page layout templates, for example, are bare-bones structures that define the skeleton of an HTML page. Beyond the simple structural elements, the templates include code blocks that basically say things like "I'm about to render the left-hand sidebar...are there any modules that want to insert content here?" Similarly, there are events that occur every time content is deleted, so a module could act upon the data before the deletion occurs.

A few dozen events are already built into the code (and modules can define their own custom events if appropriate), so most of the developer interaction consists of assigning "listeners" to the events -- functions (or entire files) -- that execute when the event is triggered.

This can take the form of including a "Recent posts" block into the footer of the home page, where an entire template can be assigned to execute, or it could take the form a module that rewrites the word "color" as "colour" in the body text of every blog post before it is displayed. 

