# Simple Contact Form Processing

Note: This is a fork of [ousenko/simple-contact-form](http://github.com/ousenko/simple-contact-form),
changed to use [Mailgun](https://www.mailgun.com) instead of Mandrill (which is now only available as a Mailchimp add-on).

You have a static website (e.g. [Jekyll](https://jekyllrb.com)), and want to give your visitors the ability to contact you? No problem!

All you need is accounts at [Mailgun](https://www.mailgun.com) and [Heroku](https://www.heroku.com/), and a bit of Python.


## Requirements

* A [Heroku](https://www.heroku.com/) account and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
* An active [Mailgun](https://www.mailgun.com) account, API key and domain


## Create, configure, and deploy a Heroku web app

```bash
    $ git clone https://github.com/heldinz/simple-contact-form.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku config:set MAILGUN_API_KEY=<KEY>
    $ heroku config:set MAILGUN_DOMAIN=<MAILGUN_DOMAIN>
    $ heroku config:set SITE_ADDRESS=<YOUR SITE URL>
    $ heroku config:set SUCCESS_PAGE=<URL OF A SUCCESS PAGE TO REDIRECT TO AFTER THE MESSAGE IS SENT>
    $ heroku config:set TO_EMAIL=<YOUR EMAIL, TO ADDRESS EMAILS TO>
    $ heroku config:set TO_NAME=<YOUR NAME, TO ADDRESS EMAILS TO>
    $ git remote add heroku https://git.heroku.com/<YOUR_HEROKU_APP>.git
    $ git push heroku master
```

## Set up front-end code

In your HTML form code, specify the following.

```html
<form action="https://<YOUR_HEROKU_APP>.herokuapp.com/send" method="POST">
  Name: <input type="text" name="name" required><br>
  Email address: <input type="text" name="email" required><br>
  Message: <textarea name="message" cols="40" rows="5" required</textarea>
  <input type="submit" value="Send Message">
</form>
```


## Enjoy! 🎉
