This is a fork of [ousenko/simple-contact-form](ousenko/simple-contact-form), changed to use Mailgun instead of
Mandrill (which is now only available as a Mailchimp add-on).

Simple contact form processing
----------------------------------

You have a static website (e.g. Jekyll), and wanna give your visitors the ability to reach you, huh?
No problem!

All we need is [Mailgun](http://mailgun.com) and [Heroku](http://heroku.com) accounts, and a bit of Python to get it work.


0. Assumptions
--------------------

You have:

* Heroku toolbelt installed
* Active Mailgun account, API key and domain

1. Create a Heroku web app
---------------------


```bash
    $ git clone https://github.com/heldinz/simple-contact-form.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku config:set MAILGUN_API_KEY=<KEY>
    $ heroku config:set MAILGUN_DOMAIN=<MAILGUN_DOMAIN>
    $ heroku config:set SITE_ADDRESS=<YOUR SITE URL>
    $ heroku config:set USER_NAME=<YOUR NAME>
    $ heroku config:set USER_EMAIL=<YOUR EMAIL>
```

2. Front-end setup
-------------------

In your HTML form code specify the following:

```html
<form action="https://<YOUR_HEROKU_APP>.herokuapp.com/send" method="POST">
  Name: <input type="text" name="name"><br>
  Email address: <input type="text" name="email"><br>
  Message: <textarea name="message" cols="40" rows="5"></textarea>
  <input type="submit" value="Send Message">
</form>
```


3. Enjoy! 🎉
-----------
