# Auto Tints - Automotive Window Tinting Supplies

![AmIResponsive](https://i.imgur.com/AbbDmYY.png)

[View Project on Heroku]()


The goal of this project is to create an __online store__ which offers automotive window tinting supplies and tools.

# Table of Contents
1. [Overview/Description](#1-overviewdescription)
2. [User Stories](#2-user-stories)
3. [User Experience (UX)](#3-user-experienceux)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Surface Plane](#surface-plane)
4. [Features](#4-features)
    * [Future Features](#future-features)
5. [Technologies Used](#5-technologies-used)
6. [Trials & Testing](#6-trials--testing)
7. [Problem Solving](#7-problem-areas--solutions)
8. [Code Validation](#8-code-validation)
9. [Website Deployment](#9-website-deployment)
10. [Credits & Acknowledgments](#10-credits--acknowledgments)
11. [Repository Support](#11-repository-support)

# 1: Overview/Description

This project aims to create an ecommerce store utilising django and stripe.

The website will allow the user to purchase window tinting related items from the comfort of their home.

# 2: User Stories

Below are some user stories which reveal how this website is useful for the end user.
Viewing The Store:
+ 'A shopper: I want to view a list of product categories'
+ 'A shopper: I want to view a list of products in each category'
+ 'A shopper: I want to view product details'
+ 'A shopper: I want to search & sort items'
+ 'A shopper: I want to see my cart item total at all times'
+ 'A shopper: I want to see frequently asked questions'
+ 'A shopper: I want to see contact details for the store'
+ 'A shopper: I want to see an about section'

Checking Out:
+ 'A shopper: I want to purchase items without signing up'
+ 'A shopper: I want to receive an email confirming my order'

User Profiles
+ 'A shopper: I want to sign up and keep a record of my orders'
+ 'A shopper: I want to be able to recover my password'

# 3: User Experience(UX)
## Strategy Plane
* What is the purpose of this website?
    * The purpose of this project is to create an ecommerce store and sell window tinting supplies
* Who is the user?
    * DIY type user
    * Car owner & enthusiast
    * Aged 18 and over
* Value for the user?
    * Privacy in their car
    * UV light protection.

---
## Scope Plane
### Function Requirements
* Provide products that will enable the user to tint their own car. This means providing window tint film as well as installation tools.
* Search function in the store.
* User accounts

### Content Requirements
* Home page where users can view product categories to help them navigate with ease.
* Private profile where you can see their previous orders.
* A collection of frequently asked questions.
* An about and contact section.

---
## Structure Plane
### Information Architecture
* Scroll to item in FAQ

### Data Structure
__'userProfile' Model__
key | type | purpose | required?
--- | --- | --- | ---
user | OneToOneField | Yes
default_phone_number | CharField | No
default_street_address1 | CharField | No
default_street_address2 | CharField | No
default_town_or_city | CharField | No
default_county | CharField | No
default_postcode | CharField | No
default_country | CountryField | No

__'Category' Model__
key | type | purpose | required?
--- | --- | --- | ---
name | CharField | No
description | CharField | No
friendly_name | CharField | No
image | ImageField | No

__'Product' Model__
key | type | purpose | required?
--- | --- | --- | ---
category | ForeignKey | No
sku | CharField | No
name | CharField | No
description | TextField | No
price | DecimalField | Yes
image | ImageField | No

__'Order' Model__
key | type | purpose | required?
--- | --- | --- | ---
order_number | CharField | Yes
user_profile | ForeignKey | No
full_name | CharField | Yes
email | EmailField | Yes
phone_number | CharField | Yes
country | CountryField | Yes
postcode | CharField | No
town_or_city | CharField | Yes
street_address1 | CharField | Yes
street_address2 | CharField | No
county | CharField | No
date | DateTimeField | Yes(auto)
delivery_cost | DecimalField | Yes
order_total | DecimalField | Yes
grand_total | DecimalField | Yes
original_cart | TextField | Yes
stripe_pid | CharField | Yes

__'Order' Model__
key | type | purpose | required?
--- | --- | --- | ---
order | ForeignKey | Yes
product | ForeignKey | Yes
quantity | IntegerField | Yes
lineitem_total | DecimalField | Yes

__'Faq' Model__
key | type | purpose | required?
--- | --- | --- | ---
collapse_id | CharField | Yes
title | CharField | Yes
body | TextField | Yes

### Interaction Design
* Check out with or without an account.
* Search & sort functionality
* View categories, products, faq, about and contact details.

---
## Skeleton Plane
Wireframes can be found [here](https://github.com/JakubMrowicki/auto-tints/tree/main/wireframes)

---
## Surface Plane
### Colours
__Primary Colours:__
Colour | Colour Code | Preview
--- | --- | :---:
Light-Blue | #336AFF | ![#F26432](https://via.placeholder.com/15/336AFF/000000?text=+)
Green | #2B9348 | ![!2B9348](https://via.placeholder.com/15/2B9348/000000?text=+)
Red | #D90429 | ![#D90429](https://via.placeholder.com/15/D90429/000000?text=+)


__Text Body Colours:__
Colour | Colour Code | Preview
--- | --- | :---:
Charcoal | #2c3e50 | ![#2c3e50](https://via.placeholder.com/15/2c3e50/000000?text=+)


### Typography

"[Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue)" will be used for any headings.

"[Open Sans](https://fonts.google.com/specimen/Open+Sans)" will be used for the body.
# 4: Features

# 5: Technologies Used
This project uses the following technologies:
* HTML5
* CSS3
* JavaScript
* jQuery
* Python
* Django
* Postgres
* Bootstrap 5
* FontAwesome Icons
* Google Fonts
* Github & Git
* GitPod
* Heroku

# 6: Trials & Testing
* Website was run through the Mobile-Friendly Test by Google and was deemed Mobile Friendly. To further test this, I opened the website on my phone as well as friends and co-workers phones.
    * [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?id=FR_v3_v6Gc652veMM-1JZg)
* Validated HTML, CSS and JS using validators.
* Checked that all links are working.
* Ran style.css through [Autoprefixer](https://autoprefixer.github.io/) to add vendor prefixes.

# 7: Problem Areas & Solutions
* You could pin more than 5 entries if you pinned it upon creation with 5 pins already present.
    * __Solution:__ I added a check in the backend to prevent this from happening, even if you get rid of the disabled attribute on the checkbox using inspect element.

# 8: Code Validation
HTML was Validated using the [W3 Validator](https://validator.w3.org/).

CSS was Validated using [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.

JavaScript was Validated using [JSHint](https://jshint.com/) with no major errors.

# 9: Website Deployment
This project is deployed to the public by using Heroku. This is how I did it.

1. Create a new app using the dashboard on Heroku.
2. Deployment method: GitHub for automatic deployment.
3. Go to your app settings tab and configure variables to match __env.py__ file.
4. Ensure that your repository contains the requirements.txt and Procfile files.
5. You can now enable automatic deployment on Heroku.
6. Scrolling down the page, you can click deploy branch.

[View On Heroku]()

# 10: Credits & Acknowledgments
* 
# 11: Repository Support
For support please email at [xdshiftblue@gmail.com](mailto:xdshiftblue@gmail.com)