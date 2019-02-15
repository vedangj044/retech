RideShare
===================
------------

Ride Sharing App based on Django Web framework
------------

Introduction
------------
It is often observed that we travel to distant place, often by road, that took alone.
It burdens our pocket, even if we use chartered servies, like buses, trains etc.
Keep in mind the environmental affect, why not build something that could connect us with the people going our way, reducing not only pollution but also the cost per head.
Our app offers a very basic interface to connect to people searching for a ride on our way.
Just logon to our website and find a mate, the catchy line "connect, ride, save", suits our website the best.

Technical Stuff
---------------
We use the following libraries
* Selenium,
* Webdriver-manager
and
* Django
to connect evrything

Initially a user with his/her vehicle registers at our website, entering his 'source', 'destination' and 'time of trip'.
Then, when a user, who doesn't have a vehicle, login to our web-app, he enters his 'source' and 'destination'.
This fetches him the list of the available ride, that are on his way, he can then directly communicate to the driver and they are connected on chat.

The web-app use a basic algorithm to do so.
It uses Selenium to open chrome and analyses two things:
  1. Distance of 'source' and 'destination' entered by the user with <b>Vehicle</b>
  2. Distance of 'source' and 'destination' entered by the user <b>without Vehicle </b>
It then analayes the distance between the two destinations and filter the results putting the one with least difference at first and accordingly.

This can also be done using google APIs, but for now Selenium works the best.


Dependencies
------------

* Python 2.7 or Python >= 3.4


Install Testing Version
------------
1. Clone this repository
2. Install required libraries
3. Run manage.py runserver
