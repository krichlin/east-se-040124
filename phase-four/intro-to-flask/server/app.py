#!/usr/bin/env python3

# 1a. Set Up Imports

# 1b. Create instance of Flask

# 2. Create a / route that returns Hello World
# 2a. Run the server with `flask run --debug` to check if its in the browser

#3. Create a path /longest-movies
# 3a. Import jsonify, make_response
# 3b. Use the `route` decorator
# 3c. Jsonify and return a response

# 4. Create a dynamic route
# 4a. Use the route decorator
# 4b. Return result as JSON

# 5. View the path and host with request context
# 5a. Import 'request'
# 5b. Create route `context` 
# 5c. use ipdb

# 6. Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)