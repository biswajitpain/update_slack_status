import urllib.request
import urllib.parse
import json

class SlackStatusUpdater:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://slack.com/api/"

    def update_status(self, status_text, status_emoji):
        url = f"{self.base_url}users.profile.set"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json; charset=utf-8"
        }
        data = {
            "profile": {
                "status_text": status_text,
                "status_emoji": status_emoji
            }
        }
        
        req = urllib.request.Request(url, 
                                     data=json.dumps(data).encode('utf-8'), 
                                     headers=headers, 
                                     method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode('utf-8'))
                if response_data.get("ok"):
                    print(f"Successfully updated Slack status to: {status_text} {status_emoji}")
                else:
                    print(f"Failed to update Slack status. Error: {response_data}")
        except urllib.error.URLError as e:
            print(f"Error updating Slack status: {e}")