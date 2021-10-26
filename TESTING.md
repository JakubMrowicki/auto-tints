[Back to README.md](https://github.com/JakubMrowicki/auto-tints/tree/main/README.md)

This testing file demonstrates testing performed for each app. Browse by clicking on the table of contents below.
# Table of Contents
1. [auto_tints](#auto_tints)
2. [cart](#cart)
3. [checkout](#checkout)
4. [home](#home)
5. [pages](#pages)
6. [products](#products)
7. [admin](#admin)

# auto_tints
## What is auto_tints?
auto_tints is the django main app which stores ```settings.py``` etc.

## Tests

# cart
## What is cart?
cart is a custom django app which handles the shopping cart on the store.

## Tests

# checkout
## What is checkout?
checkout is a custom django app which handles checkout procedures for the store.

## Tests

# home
## What is home?
home is a custom django app which handles the home page content. In this case it's a category view.

## / Tests
Test Description | Result | Comment
--- | --- | ---
Does visiting this page show all categories? | Yes | -
Is the page responsive on mobile? | Yes | -
Does clicking on a category show all products from said category? | Yes | -
Does the page have a navigation bar and footer? | Yes | Responsive
Does the page have an about section? | Yes | -

# pages
## What is pages?
pages is a custom django app which handles misc pages on the website such as the FAQ and user profiles.

## /pages/faq(#collapse-id) Tests
Test Description | Result | Comment
--- | --- | ---
Does visiting /pages/faq show relevant content? | Yes | FAQ are displayed as a collapse element
Does visiting /pages/faq#returns open and scroll to the relevant section? | Yes | JavaScript enabled.

## /profile/ Tests
Test Description | Result | Comment
--- | --- | ---
Can you visit this page without logging in? | No | Redirect to login
Does the page show a form for updating delivery info? | Yes | Form works as intended
Does the page show an order history? | Yes | -
Can you click on any order to show the order confirmation? | Yes | -

## /order_history/<order_number> Tests
Test Description | Result | Comment
--- | --- | ---
Does visiting this page show an order? | Yes | Provided that the order number is valid
What if it's not? | No | page not found error
Can non-owners of the order see this page? | Yes | So non-registered order owners can be linked their order confirmation.

# products
## What is products?
products is a custom django app which handles products, categories and product reviews.

## /products/ Tests
Test Description | Result | Comment
--- | --- | ---
Does this page display a list of products? | Yes | Products are shown in a responsive manner.
Does using a URL parameter for categories result in only products from that category? | Yes | -
Does using a false category result in an error response? | Yes | "No products found"
Does searching for a particular keyword show relevant items? | Yes | -
Does searching for a blank keyword show an error message? | Yes | "You didn't enter any search criteria"
Does each product have an edit button when logged in as superuser? | Yes | It takes me to the correct edit product view.

## /edit_product/<int:product_id>/ Tests
Test Description | Result | Comment
--- | --- | ---
Does navigating to this page populate the form using the product_id? | Yes | All form fields work as intended.
Does navigating to this page using a bogus product_id result in an error? | Yes | 404 Page not found.
Does navigating to this page while not logged in as superuser result in an error? | Yes | Will redirect to log in
Does the form validation work? | Yes | -

## /delete_product/<int:product_id>/ Tests
Test Description | Result | Comment
--- | --- | ---
Is the product removed from the database? | Yes | -
Can non-superusers or non-logged-in users remove products? | No | Redirect to login

## /products/add_product/ Tests
Test Description | Result | Comment
--- | --- | ---
Does the category field show all categories? | Yes | -
Can you view this page as a non superuser? | No | Will redirect to log in
Does the form validation work? | Yes | -

## /products/<int:product_id>/ Tests
Test Description | Result | Comment
--- | --- | ---
Does navigating to this page show a responsive view of the product and it's details? | Yes | -
Does navigating to this page using a bogus product_id throw an error? | Yes | "Product Not Found"
Does adding to cart work? | Yes | Product is added to cart and toast notification to confirm is shown
Does the page show a link to edit the product as superuser? | Yes | Not visible unless superuser
Does the page show reviews correctly? | Yes | Shows latest 5 reviews
Does the page require you to log in to post a review? | Yes | -
Does the page allow you to remove a review? | Yes | Only if you are the review creator or if superuser
Does the add_review form allow you to post a review if not logged in? | No | Redirect to log in
Does the add_review view allow you to post multiple reviews for the same product? | No | Only one review, per product, per user.

# admin
## What is admin?
admin is a native django app which is the admin panel for django driven applications.

## Tests
Test Description | Result | Comment
--- | --- | ---
Do all models have informative columns? | Yes | All models in the admin are easy to sort through
