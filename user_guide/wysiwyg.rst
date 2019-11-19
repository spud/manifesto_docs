**************
WYSIWYG Editor
**************

.. figure:: images/tinymce.*

The WYSIWYG editor in Manifesto is a slightly modified version of TinyMCE, a popular editor found in many CMS applications. For the most part, the buttons in the toolbar are self-explanatory, and generally behave the way such buttons operate in word processors like Microsoft Word.

Manifesto basically allows for two forms of the WYSIWYG editor: the "full HTML" version, with the ability to upload images, create tables, etc. And the "restricted HTML" version, which allows for simple formatting like bold and italic as well as link creation. For the most part, the version used is determined by the specific needs of the module and its content, so you should *not* be re-configuring the options on a regular basis.

Pasting content from other sources
==================================

While you are permitted to simply paste into the editor window, there are 3 special situations where you may want to take special care before pasting:

#. **Pasting from Microsoft Word**: Because Word document often contain hidden formatting codes, there is a special *Paste from Word* button on the toolbar. When you click it, you are given a new window into which you can paste your text. Before it is inserted into the content, it is scrubbed and sanitized to remove potentially hazardous code.

#. **Pasting plain text**: If you have formatted text that you want to insert without formatting, click the icon of a clipboard with a "T" on it. This version will strip all formatting code from your input before inserting it into the editor.

#. **Pasting HTML code**: When you are given HTML code to embed in your site, for example from a YouTube or Video video "embed code," *you cannot paste it directly into the editor window.* Because it is raw HTML code, it needs to be pasted into the "Raw HTML" window. Click the "HTML" button on the end of the toolbar to see your body copy in its raw HTML form. Locate where you want the code to appear, and paste into the popup window. When you close the window, it will render the HTML in the editor so you can see it in context.

Creating Links
==============

Creating links in the editor is easy. Simply type the text you want to appear as a link, and use your mouse to select it. Then click on the "Create link" icon (a small chain link), and a new window will popup.

.. figure:: images/tinymce-link.*

* To create a simple link to an external website, you can simply enter the URL in the "URL Path" field and submit.

* To create a link to other content on your own website, you can either paste in the URL or use the menus as shown above to select your content based on the module and content type. The cascading menus will help build your URL based on your selections.

* In order to have your links **open in a new window,** simply check the checkbox "Open in new window" and a class will be added to your link to prompt the browser to open the link in a new window. This is a good idea for external websites, so users do not lose their place in your webiste.

* You can link directly to any of the images or documents in your Media repository by selecting the "Media Storage" tab and clicking on the media you want to link to. This is particularly useful when you want to create a text link to a PDF document for download.

Uploading photos to embed in body copy
======================================

See "`Selecting and inserting media`_" above.

See `the Routes section`_ for more information.

.. _Selecting and inserting media: media_management_.html