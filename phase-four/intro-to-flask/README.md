# Intro to Flask

## SWBATs

- [ ] Understand how the Internet works
- [ ] Understand how the request-response cycle works
- [ ] Understand HTTP protocols
- [ ] Intialize a Flask application
- [ ] Use Flask routing and create views

---

<br />

### 1. Set up a flask app in `app.py`
#### 1a. Set up imports
#### 1b. Create an instance of a flask app

<br />

---

<br />

### 2. Create a `/` route which will return a view with  `<h1>Hello World!</h1>`
#### 2a. Run the server with `flask run --debug` to verify the route in the browser

<br />

---

<br />

### 3. Create a `/longest-movies` route 
#### 3a. Import `jsonify` and `make_response`
#### 3b. Use the `route()` decorator
#### 3c. Jsonify and return a response

<br />

---

<br />

### 4. Create a dynamic route `/productions/<string:title>` that searches for all matching records
#### 4a. Use the `route()` decorator
#### 4b. Return a result as json

<br />

---

<br />

### 5. View the path and host with request context
#### 5a. Import 'request'
#### 5b. Create route `context` 
#### 5c. Use ipdb
<br />

---

<br />

### 6. Use the before_request request hook, what this hook does is up to you.
#### - Use the decorator: `@app.before_request`
#### - Create a function `def runs_before()` that prints `Hello World`
#### - Visit a few routes!
