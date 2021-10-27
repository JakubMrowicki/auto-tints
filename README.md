# Auto Tints - Automotive Window Tinting Supplies

![AmIResponsive](https://i.imgur.com/AbbDmYY.png)

[View Project on Heroku](https://auto-tints.herokuapp.com/)


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
key | type | required?
--- | --- | ---
user | OneToOneField | Yes
default_phone_number | CharField | No
default_street_address1 | CharField | No
default_street_address2 | CharField | No
default_town_or_city | CharField | No
default_county | CharField | No
default_postcode | CharField | No
default_country | CountryField | No

__'Category' Model__
key | type | required?
--- | --- | ---
name | CharField | No
description | CharField | No
friendly_name | CharField | No
image | ImageField | No

__'Product' Model__
key | type | required?
--- | --- | ---
category | ForeignKey | No
sku | CharField | No
name | CharField | No
description | TextField | No
price | DecimalField | Yes
image | ImageField | No

__'Order' Model__
key | type | required?
--- | --- | ---
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

__'OrderLineItem' Model__
key | type | required?
--- | --- | ---
order | ForeignKey | Yes
product | ForeignKey | Yes
quantity | IntegerField | Yes
lineitem_total | DecimalField | Yes

__'Faq' Model__
key | type | required?
--- | --- | ---
collapse_id | CharField | Yes
title | CharField | Yes
body | TextField | Yes

__'Review' Model__
key | type | required?
--- | --- | ---
product | ForeignKey | Yes
user | ForeignKey | Yes
body | TextField | Yes
date | DateTimeField | Yes(auto)
recommend | BooleanField | Yes

### Interaction Design
* Check out with or without an account.
* Search & sort functionality
* View categories, products, faq, about and contact details.

---
## Skeleton Plane
Wireframes can be found [here](https://github.com/JakubMrowicki/auto-tints/tree/main/wireframes)

The footer will contain copyright information.
---
## Surface Plane
### Colours
__Primary Colours:__
Colour | Colour Code | Preview
--- | --- | :---:
Black | #000000 | ![#000000](https://via.placeholder.com/15/000000/000000?text=+)
Grey | #212529 | ![!212529](https://via.placeholder.com/15/212529/000000?text=+)
White | #FFFFFF | ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+)


__Text Body Colours:__
Colour | Colour Code | Preview
--- | --- | :---:
White | #ffffff | ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)
Black | #212529 | ![#212529](https://via.placeholder.com/15/212529/000000?text=+)


### Typography

"[Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue)" will be used for any headings.

"[Open Sans](https://fonts.google.com/specimen/Open+Sans)" will be used for the body.
# 4: Features
* Products
    * Product Detail page
        * Admin: Edit/Delete Product
        * Reviews
            * Add or remove you own reviews
            * Admin: Remove any review
* Categories
    * View Categories on homepage/navbar
* Cart
    * View cart
    * Edit and update cart items
    * Calculate total cost
* Checkout
    * Complete an order using Stripe payments
    * Email order to user
* FAQ
    * Admin: Manage FAQ sections
* Profile
    * Update saved delivery info
    * View order history
    * View previous orders

## Future Features/Changes
I learned so much about Django thoughout this project but I really didn't give myself enough time to create something I was really proud of. I definitely want to create more with Django now that I'm more familiar with e-commerce websites and how their procedures work.

Some features I would add are listed below:
* Forum feature
* Override the Django user model instead of creating a UserProfile model
* Complete redesign

# 5: Technologies Used
This project uses the following technologies:
* HTML5
* CSS3
* JavaScript
* jQuery
* Python
* Django
* Postgres
* AWS
* Stripe
* Bootstrap 5
* FontAwesome Icons
* Google Fonts
* Github & Git
* GitPod
* Heroku

# 6: Trials & Testing
* Website was run through the Mobile-Friendly Test by Google and was deemed Mobile Friendly. To further test this, I opened the website on my phone as well as friends and co-workers phones.
    * [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly/result?id=kQDvopK48p9ZjX_PgRgvqQ)
* Validated HTML, CSS and JS using validators.
* Checked that all links are working using [w3 Link Checker](https://validator.w3.org/checklink).
* Ran style.css through [Autoprefixer](https://autoprefixer.github.io/) to add vendor prefixes.
* [TESTING.md](https://github.com/JakubMrowicki/auto-tints/tree/main/TESTING.md) for more app specific testing.

# 7: Problem Areas & Solutions
* I wanted to link to specific items in the FAQ page but I couldn't find a clear way to do so.
    * __Solution:__ I added some javascript to handle the URL hash, if a hash is present it will open and scroll to the relevant collapse item.
* Django doesn't have a form field with the ```type="tel"``` attribute and wouldn't let me change the attribute in the forms.py file.
    * __Solution:__ I added some javascript to update the type from ```text``` to ```tel```.

# 8: Code Validation
HTML was Validated using the [W3 Validator](https://validator.w3.org/).

CSS was Validated using [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.

JavaScript was Validated using [JSHint](https://jshint.com/) with no major errors.

bash command ```flake8 --exclude=*/migrations/*``` was used to tidy up Python code.

# 9: Website Deployment
This project is deployed to the public by using Heroku. This is how I did it.

To deploy this app you will need an [AWS account](https://aws.amazon.com/), a [Heroku account](https://signup.heroku.com/login) and a [Stripe account](https://dashboard.stripe.com/register). You can follow the links to register with those service providers.

Also, make sure you install all the app dependencies from ```requirements.txt``` and that no files such as the ```Procfile``` are missing before you begin.

AWS Setup:
1. Log in to your AWS account and search for S3.
2. Create an S3 Bucket for your files and unblock public access to it, take note of your ARN here.
3. In the permissions tab use the following configuration.
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
4. In the policy tab, use the policy generator and generate an ```S3 Bucket Policy``` and allow all pricipals by typing a star. Take your ARN from before and paste it into the ARN box. Click add statement then generate your policy.
5. Copy your policy into your bucket and add a ```/*``` to the end of the resource key and save.
6. In the access control list tab, under public access click on everyone, select List Objects and save.
7. Next search for IAM and create a new group with a name of your choosing.
8. On the left handside, under "Access Management" click on Policies and create a policy. Go to the JSON tab and import a managed policy named ```AmazonS3FullAccess```. Get your S3 bucket ARN again and paste that in after "Resource", as a list (first the ARN, then also the ARN with a slash and star). Click "next tags" and then "next review". Give it any name and description. Click "create policy".
9. Back in your Groups, click on the group you created, go to permissions and attach the policy you just created.(add permisions, attach policy).
10. Under "Access Management" again, this time click on "Users" and add a user, give it programmatic access and click next. Add this user to your previously created group and download the CSV file at the end.
11. You will need to update ```settings.py``` at the bottom of the file. Variables like ```AWS_STORAGE_BUCKET_NAME``` and ```AWS_S3_REGION_NAME``` need to match your bucket.


Heroku Setup
1. Create a new app using the dashboard on Heroku and select a region closest to you.
2. In the Resources tab of your App, add Heroku Postgres to store your database tables.
3. Add your Heroku app url to ```ALLOWED_HOSTS``` in ```settings.py```.
4. Add the following veriables to your ```settings tab```
```
DATABASE_URL = This is prefilled for you.
SECRET_KEY = Generate your own key at https://djecrety.ir/
USE_AWS = True
AWS_ACCESS_KEY_ID = From CSV downloaded earlier
AWS_SECRET_ACCESS_KEY = From CSV downloaded earlier
STRIPE_PUBLIC_KEY = We will fill this at the end
STRIPE_SECRET_KEY = We will fill this at the end
STRIPE_WH_SECRET = We will fill this at the end
```
5. In the ```Deploy``` tab, connect your GitHub and select the repo for this project.
6. At the bottom you can enable automatic deploys or manually click ```Deploy Branch```.
4. Once that's running. Using dj_database_url in ```settings.py``` use your Heroku Postgres URL from your Config Variables to connect to your new database.
5. From your dev environment, use ```python3 manage.py migrate``` to create the necessary tables to run the app.
6. Use ```python3 manage.py loaddata``` to load any fixtures.
7. Create a superuser using ```python3 manage.py createsuperuser``` so you can log in to the admin panel.
8. You can now go back to ```settings.py``` and switch your ```DATABASE``` settings back so it searches env variables for the Heroku Postgres URL again.

Stripe Setup:
1. Log in to your Stripe account and click "Developers" top right of the page.
2. In the API Keys section on the left. Take note of your Publishable Key and Secret Key, use these to fill your Heroku config variables.
3. Next click on Webhooks on the left and add an endpoint.
4. Your URL should look like this "```your_heroku_app_url```/checkout/wh/"
5. Add all events to your endpoint.
6. Reveal your Signing Secret and add it to your Heroku config variable ```STRIPE_WH_SECRET```

[View On Heroku](https://auto-tints.herokuapp.com/)

# 10: Credits & Acknowledgments
* First and foremost, the creator of Boutique Ado's walkthrough project could not have been any more useful as a resource to get this project to where it is today. Biggest credit of all to the creator at Code Institute.
* [Django Documentation](https://docs.djangoproject.com/)
* [Python Documentation](https://docs.python.org/)
* [AllAuth Documentation](https://django-allauth.readthedocs.io/)
# 11: Repository Support
For support please email at [xdshiftblue@gmail.com](mailto:xdshiftblue@gmail.com)