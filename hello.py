from flask import Flask, url_for
from markupsafe import escape
import requests
# instance of the Flask class is the WSGI (Web Server Gateway Interface) application
app = Flask(__name__)

@app.route("/say_name/<name>")
def name(name):
    """
    Output must be escaped to protect from injection attacks
    """
    return f"<p>Hello, {escape(name)}</p>"

@app.route("/hello/")
def hello():
    return 'Hello, World'

@app.route("/rules/<int:problem_id>") # if enter string as param, will lead to invalid url
def get_problem_name(problem_id):
    return f'Problem {problem_id}'

@app.get('/login')
def login_get():
    return 'you have logged in fam'

@app.post('/login')
def login_post():
    return 'why you tryna post fam'

# with app.test_request_context(): # simulates application and request context for url_for to work, can use to run pytest cases
#     print(url_for('name', name='Xiangyun'))

def fetch_language_stats(username):
    GRAPHQL_URL = "https://leetcode.com/graphql/"
    query = """
        query getUserSubmissionStats($username: String!) {
        matchedUser(username: $username) {
            submitStats {
            totalSubmissionNum {
                count
            }
            }
        }
        }
    """
    variables = { "username": username }

    resp = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )
    resp.raise_for_status()
    return resp.json()["data"]["matchedUser"]["submitStats"]["totalSubmissionNum"]

# This call will block until the network round-trip and parsing finish:
stats = fetch_language_stats("jeryl01")
print(stats)
