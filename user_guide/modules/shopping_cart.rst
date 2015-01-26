**************
Shopping Cart
**************

Overview
========

The Shopping Cart module is the most complex and most powerful tool in Manifesto. It is actually several tools in one, and is designed to integrate seamlessly with all sorts of other content on your site.

The Shopping Cart module relies on the notion of what Manifesto calls a *Shopping Cartable* object. This is basically a consistent collection of data that describes all of the properties that are required to describe a product that can be purchased through the Shopping Cart system.

At the most basic level, this includes

* A name for the shopping cart line item
* A price
* Whether or not user can order more than 1
* Whether or not the item is taxable
* Whether or not the item requires shipping
* Any related options (color, size, etc)

These are the fundamental properties of a purchasable item, *and they can be applied to virtually any content in Manifesto.*

In other words, if you have a discography section of your band website, you can assign these *Shopping Cartable* properties to each of your albums, and they will automatically become part of your online store. You could do this with any sort of content, even a blog post -- "Purchase nicely-formatted printouts of this article for $.05/each."

If you are using the event calendar, you can create events that require tickets to be purchased. Rather than creating a whole new catalog for event tickets, we simply append a *Shopping Cartable* to the Event itself, and it suddenly becomes purchasable.

Adding to Cart
==============

Whenever there is a purchasable item on your site, the user will be presented the opportunity to add the item to a shopping cart, optionally with the ability to specify a quantity, or to select other options.

The specific details of the behavior of adding items to the cart depends on your developer's implementation. By default, items can only be added to the cart one at a time, and the user is redirected their shopping cart page each time. Other implentations might use AJAX to load the cart without refreshing the page.

The Checkout Process Workflow
=============================

#. User adds one or more item to their cart.

#. User goes to the cart display page (``/cart/`` by default) to review

#. After confirming line items in the cart (and optionally entering an additional donation amount), user clicks "Proceed to checkout"

#. At this point, if the system requires user accounts for checkout, the user will be prompted to login, or to create a new account

#. Otherwise, the user will be prompted for billing information.

#. If shipping is required, user is prompted to select a shipping method, and to provide a shipping address.

#. Once that information has been provided, the user is taken to the pre-order confirmation page, which displays the provided addresses and line items again for verification.

#. At the bottom of that page is a form (developed specifically for the credit card processor you have chosen) that prompts you for your credit card information and any other data the processor requires.

#. Once you submit that form, your transaction is sent off for processing.

#. Once a response -- success or failure -- is received from the credit card processor, the user is redirected to a receipt page, or, in case of failure, an error page that offers recommended courses of action to rectify the error.

Viewing Transactions
====================

Manifesto automatically creates a Shopping Cart object whenever a User adds something to their cart, but it doesn't create a Shopping Transaction until the user begins the checkout process.

From the Editor Console, you can quickly review all transactions, with the most recent at the top. The date, user email address, status, and amount are all displayed on the Shopping Cart module landing page.

Clicking on any of the transactions pulls up all of the details about that transaction: The processor-specific details (Transaction ID, payment time stamp, transaction fees, etc) and the common Manifesto details: buyer informatin, line items, tax, shipping, and net total.

If the transaction has any modular linked data, e.g. the Form Response for a form associated with the checkout, it will also appear on this page in its own section.

The Editor can change the Transaction status here, as well, to indicate the current state of processing. The available status codes are as follows (with an indication of intended meaning):

* In Progress: *Active shopping carts not yet checked out*
* Pending: *Transaction is current being processed*
* Authorized/Held: *Transaction successfully processed an authorization hold*
* Received: *Transaction was successful, and is ready for fulfillment*
* Being Processed: *Transaction is being fulfilled internally*
* Needs Shipping: *Transaction is ready to be shipped out*
* Delayed: *Transaction successful, but fulfillment delayed *
* Paritally Shipped: *Some items have already been shipped*
* Fulfilled: *Transaction fully complete, and shipped if needed*
* Failed: *Transaction failed. Details usually provided by processor*
* Declined: *Transaction failed. Details usually provided by processor*
* Disputed: *User has disputed transaction, i.e. through PayPal or credit card issuer*
* Returned: *Item or items from transaction were returned*
* Returned: *Refund has been issued for this transaction*

You may also leave internal notes, which are only viewable by Editors, not by the customers.

If your developer has given customers a place to view and track the progress of  their orders, there may also be a "Customer Notes" field for leaving more detailed information for the customer.

The "Communication" section gives you a shortcut for sending an email to the user about their order. For advanced users, you can create a series of templates (which can, for example, embed the user's order details dynamically) that can be pre-loaded into the editor for further tweaking.
