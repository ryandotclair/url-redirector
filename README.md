# Purpose

This simple redirect web app will take whatever URL you have in the `URL` environment variable and redirect the user to that URL.

# But Why?

The `.dev` domain requires a valid SSL. Doing a simple 301 forward using DNS forwarding (like Godaddy) will not work. Thus this was born (leveraging Let's Encrypt cert--which is out of scope here) as a man-in-the-middle forward.

# Usage

`app.py` is the main app, and only real requirement is `flask`. I went overkill and provided a gunicorn webserver, because why not?

For Azure Spring Apps:

```bash
az spring app deploy --name [name of your app] --path-to-source [path to this folder] --env URL=[the url you'd like to forward to]
```