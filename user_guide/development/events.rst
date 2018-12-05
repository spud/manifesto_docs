**********************************
Integrating modules through events
**********************************

Events are points in the code — they can be in layout templates or in functional execution — that are peppered throughout Manifesto to give modules the opportunity to insinuate themselves into the processing that occurs when responding to a page request.

The main page layout templates, for example, are bare-bones structures that define the skeleton of an HTML page. Beyond the simple structural elements, the templates include code blocks that basically say things like "I'm about to render the left-hand sidebar...are there any modules that want to insert content here?" Similarly, there are events that occur every time content is deleted, so a module could act upon the data before the deletion occurs.

