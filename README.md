# Artist Pledge Contact Form

Contact form processing customized for [Artist Pledge](https://github.com/acolorbright/artistpledge).


## Requirements

* A [Heroku](https://www.heroku.com/) account and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
* An active [Mailgun](https://www.mailgun.com) account, API key and domain


## Create, configure, and deploy a Heroku web app

```bash
    $ git clone https://github.com/acolorbright/artistpledge-contact-form.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku config:set MAILGUN_API_KEY=<KEY>
    $ heroku config:set MAILGUN_DOMAIN=<MAILGUN_DOMAIN>
    $ heroku config:set SITE_ADDRESS=<ARTIST PLEDGE SITE URL>
    $ heroku config:set SUCCESS_PAGE=<URL OF A SUCCESS PAGE TO REDIRECT TO AFTER THE MESSAGE IS SENT>
    $ heroku config:set TO_EMAIL=<EMAIL ADDRESS TO ADDRESS EMAILS TO>
    $ heroku config:set TO_NAME=<NAME TO ADDRESS EMAILS TO>
    $ git remote add heroku https://git.heroku.com/<YOUR_HEROKU_APP>.git
    $ git push heroku master
```

## Set up front-end code

In the HTML, specify the following.

```html
        <form class="join-form" action="https://<YOUR_HEROKU_APP>.herokuapp.com/send" method="POST">
          <label class="join-form__label" for="name">
            Name
            <input required type="text" name="name" placeholder="Name" />
          </label>
          <label class="join-form__label" for="email">
            Email
            <input required name="email" placeholder="name@gmail.com" type="email" />
          </label>
          <label class="join-form__label" for="phone">
            Phone Number (optional)
            <input name="phone" placeholder="+4412345678" type="phone" />
          </label>
          <fieldset>
            <legend class="join-form__label">Are you interested in:</legend>
            <br><label><input name="interested-in" type="radio" value="Making a pledge" /> Making a pledge</label>
            <br><label><input name="interested-in" type="radio" value="A custom philanthropic project" /> A custom philanthropic project</label>
          </fieldset>
          <fieldset>
            <legend class="join-form__label">Are you enquiring for:</legend>
            <br><label><input name="enquiring-for" type="radio" value="Themselves" /> Yourself</label>
            <br><label><input name="enquiring-for" type="radio" value="On behalf of an artist"/> On behalf of an artist</label>
          </fieldset>
          <label class="join-form__label" for="message">
            Let us know how we can help (optional)
            <textarea name="message"></textarea>
          </label>
          <label class="join-form__label" for="newsletter">
            <input name="newsletter" type="checkbox" /> Subscribe to our newsletter
          </label>
          <input type="submit" value="Send&nbsp;›" />
        </form>
```
