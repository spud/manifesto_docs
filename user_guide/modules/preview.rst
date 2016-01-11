**************
Preview
**************
The Preview module is designed to allow draft content to be reviewed, saved, and edited before being published. The module itself does not define a new type of content, but it injects itself into select content types, replacing the normal "Submit" buttons with new functionality that saves a temporary copy of the content, allowing you to preview the content, and permitting rudimentary publishing moderation.

Certain user roles can be defined as "Publishers," allowing them to fully submit and publish content, and others as "Drafters," who may add and edit content, but are not permitted to publish it.

The act of previewing your content is simple: edit or create a new piece of content which has been attached to the Preview module (for example, a Blog Post, or a Template Page), and you'll notice that the "Submit" button at the bottom of the form has been replaced by a "Save Draft & Preview" button. If you are authorized as a Publisher, you will also still see the traditional "Submit" button which may be used to submit and publish the content in the usual manner.

If you attempt to edit a content object that already has a draft revisions, you will be notified at the top of the editing interface, and you are given the opportunity to switch over to editing the draft instead.

The Preview listing page displays all current draft revisions, grouped by content type (e.g. all Blog Post previews, all Template Page previews, all Staff previews, etc).

.. figure:: images/preview-listing.*
   :align: center
   :width: 75%
   :alt: Listing of preview objects

* Click on the title to preview that content on the front end
* **Edit** the draft to continuing updating and modifying the content
* **Approve** the draft to insert it, or to have it replace the old content
* **Delete** the draft altogether

Limitations
===========
The Preview module currently allows only one draft revision per piece of content, so you may not create and save multiple preview versions.