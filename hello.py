from flask import Flask, url_for
from markupsafe import escape
from graphql_queries import GraphQLqueries
# instance of the Flask class is the WSGI (Web Server Gateway Interface) application
app = Flask(__name__)


@app.route("/<username>")
def fetch_language_stats(username):
    gql_query = GraphQLqueries(username)
    
    return gql_query.fetch_submission_nums()


