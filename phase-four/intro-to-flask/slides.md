---

title: '01_intro_flask'

---

# Intro to Flask

---

## What We'll Be Doing

- Reviewing how the web works
- Reviewing the request response cycle
- Setting up a simple flask instance 

<aside class="notes">
- front-end communicate with back-end <br />
- json-server was a really basic API <br />
- more complex APIs: data validation, authorization
</aside>

---

## What is The Internet

<img src='https://www.gao.gov/assets/extracts/726c56e9ccd46e3aaf3e4b7b75c60895/rId15_image3.png' width="800px" />

<aside class="notes">
- architecture, connect networks across the earth <br />
- ocean cables, computers, data centers, server, satelites, wifi towers
Fun Fact: ARPANET was the initial backbone of the internet which was created by the Department of Defense <br />
- packet switching: grouping data into packets that are transmitted over a digital network (with a header and payload) <br />
- metaphor: header = envelope, payload = contents inside envelope <br />
- response is a promise because it takes time for information to travel from wherever it originated, that's why I always say "we wait for the response to be fulfilled"
</aside>

---

## WWW: World Wide Web

- Web resources accessed via HTTP (HyperText Transfer Protocol)


---

## HTTP Protocol

- Hypertext Transfer Protocol
- Stateless: one request doesn't know about the next
- Sessions: share info b/w requests by storing user info on the server
- Cookies: saved in the user's browser and saves users identity (usually anonymously)...this also expires over a certain period of time

<img src="https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview/fetching_a_page.png" width="900px"/>

<aside class="notes">
- sessions usually expire over a certain period of time <br />
- sessions can be server side for large web apps, client side for smaller web apps 
<br />
What is a protocol? A set of rules on how something should be done.
HTTP is the protocol describing the structure between client and server communication 
</aside>

---

## Other Protocols Include...

- SSH (secure shell) which we've been using in Github
- HTTPS: hypertext transfer protocol secure
- SSL (secure sockets layer)
- IMAP (internet message access protocol)
- DNS (domain name system) 
- TLS (transport layer security)
etc ... 

<aside class="notes">
- convential internet communications (http) data is transmitted in plaintext and will be readable if intercepted
<br />
- ssl: establishes encrypted link between server and client <br />
- imap: stores emails on a mail server  <br />
<br />
- tls: the little lock next to the URL that makes the website secure
<br />
- dns: domain names database - this is why hosting a website and hosting the domain name happen in two different places, without dns you would have to memorize the IP address (bring up the localhost is just 127.0.0)
</aside>

---

## Static vs Dynamic Website

- static website (doesn't change) is HTML, CSS, JS that acts as template for dynamic data coming into these pages

<img src="https://rochester.kidsoutandabout.com/sites/default/files/html_css_javascript.jpeg" width="600px" />

- dynamic software content is supplied by server.  a user makes a request, and the server processes the information and sends back a response

<aside class="notes">
- websites (single domain pages on the web) <br />
- web apps (software accessible through the web)
</aside>

---

## Request Reponse Cycle

👀 What is the request-response cycle?

---

## Request Reponse Cycle

<img src="https://www.oreilly.com/api/v2/epubs/9780596802462/files/images/ugae_0104.png"/>

- client makes request to server which may contain additional data
- server responds with information which my contain data or an error
- client waits for response (as a promise)

<aside class="notes">
- this goes back to the transferring of data packets <br />
- response is a promise because it takes time for information to travel from wherever it originated, that's why I always say "we wait for the response"
</aside>

---

## URL Example

- https://pokeapi.co/api/v2/pokemon/ditto <br /> <br />
https - protocol <br />
pokeapi.co - domain name <br />
api/v2/pokemon/ditto - path

<aside class="notes">
- use an example from github where you change the user who owns the repo, the branch name, etc. <br />
- semantic ui github: https://github.com/Semantic-Org/Semantic-UI <br />
- use an example by having a student's fork of repo and changing URL to navigate to my repo <br />
- display wikipedia (they have search query)
</aside>

---

## Status Codes

😎 <br />
200: `OK` - yay
<br />
201: `Created` - you probably did a POST request

<aside class="notes">
100's - informational
200's - success
300's - redirect
400's - client error
500's - server error
</aside>

---

## Status Codes 
😕
<br />
400: `Bad Request` - there's probably something wrong with your fetch in the client
<br />
401: `Unauthorized` - are you logged in?
<br />
404: `Not Found` - maybe that record doesn't exist 

--- 

## Status Codes

😰 <br />
500: `Internal Server Error` - hopefully it's just a typo

---

## More Status Codes

[🐶](https://httpstatusdogs.com/) <br />
(click me ^)

---

## CRUD operations vs HTTP verbs

<img src="https://www.atatus.com/blog/content/images/2022/12/crud-operations.png" width="500px" />

<aside class="notes">
- CRUD: for backend databases, primitive
- HTTP/REST: method sent along with request, APIs
- We will be focusing on GET/POST/PATCH/DELETE
</aside>

---

## JSON

- lightweight data storage for data exchange
- works with any language
- easy to read

<aside class="notes">
- It’s a format to transfer data from client to server <br />
- sometimes have to specify you will be sending JSON or expecting JSON
- maybe show them postman at this time
</aside>

---

## Flask

---

## Why Flask

- built in debugger
- easily scalable
- secure cookies
- unit testing support
- lots of extensions
- small codebase - lots of control for developers

<aside class="notes">
- easy to extend core: flask has a lot of packages to add on, flask itself is very lightweight
</aside>

---

## Why Flask 

- WSGI (WIZ-ghee): web server gateway interface

- Werkzeug: WSGI library
    
- Flask provides a development WSGI through Werkzeug with `flask run` command

<aside class="notes">
- WSGI <br />
    - interface between web servers (Apache, Nginx, local development server) and web apps <br />
    - specifically for Python frameworks <br />
    - to make sure the coder doesn't have to design new applications around each server <br />
    
- Werkzeug:  <br />
- toolkit that implements requests, response objects and other utility functions <br />
    - debugger, classes to build requests and process responses, routing, making dev server <br />
- web apps are software accessed/ran via internet
</aside>

---

## Initializing a Flask App

```python
from flask import Flask 

app = Flask('mynameiswhat')
```

That's it!

---

## Creating a Route in Flask

Use a decorator!

```python
@app.route('/', methods=['GET', 'POST', ...])
def home():
    if request.method == 'GET':
        return {} 
```

<aside class="notes">

- we will not be using Flask views, we will be using React 
</aside>

---

## What do we send back?

### 🌈 JSON ✨
- We can add additional information to our response such as headers, status code, etc. with `make_response()` or with `return`

<aside class="notes">

 - with return you return [message], [status code], [headers] <br />
 - with make_response(response_body, status_code, headers) you return an object...cleaner, easier to replicate, and potentially automate
</aside>

---


## Request lifecycle
`@app.before_request`
`@app.after_request`
and more!...

```python
@app.before_request
def run_before():
    print('this is really useful when checking if a user is logged in')
```

---


## Context

- Application Context: Keeps track of current app's config variables, logger, database connections so that we don't have to pass the entire application instance (`app`) from function to function

```python
    with app.app_context():
        # add seeds
```

- [Request Context](https://tedboy.github.io/flask/generated/generated/flask.Request.html): Keeps track of current request data such as URL, headers, method, request data, etc.

```python

from flask import request

# request.method
# request.get_json()
# request.args
# request.cookies
# request.base_url
# etc.

```

---

## Debugging

`import ipdb; ipdb.set_trace()`

<br />

`flask run --debug`
