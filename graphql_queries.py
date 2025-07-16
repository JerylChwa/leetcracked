import requests

class GraphQLqueries():
    GRAPHQL_URL = "https://leetcode.com/graphql/"

    def __init__(self, username: str) -> None:
        self.username = username

    def fetch_submission_nums(self):
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
        variables = { "username" : self.username }

        resp = requests.post(
            self.GRAPHQL_URL,
            json={"query": query, "variables": variables},
            headers={"Content-Type": "application/json"}
        )
        
        resp.raise_for_status()
        
        return resp.json()["data"]["matchedUser"]["submitStats"]["totalSubmissionNum"]

