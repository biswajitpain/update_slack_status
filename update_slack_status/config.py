class ConfigManager:
    @staticmethod
    def load_config():
        return {
            'slack_token': 'your-slack-token-here',
            'wifi_status_map': {
                'Home WiFi': ('Working from home', ':house:'),
                'Office WiFi': ('In the office', ':office:'),
                'Starbucks': ('Working from Starbucks', ':coffee:'),
                # Add more mappings as needed
            }
        }