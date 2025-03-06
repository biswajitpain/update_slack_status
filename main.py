from update_slack_status import get_wifi_name, SlackStatusUpdater, ConfigManager
import time

def main():
    config = ConfigManager.load_config()
    updater = SlackStatusUpdater(config['slack_token'])
    
    while True:
        wifi_name = get_wifi_name()
        if wifi_name in config['wifi_status_map']:
            status_text, status_emoji = config['wifi_status_map'][wifi_name]
            updater.update_status(status_text, status_emoji)
        else:
            print(f"No status mapping for WiFi: {wifi_name}")
        
        # Wait for 5 minutes before checking again
        time.sleep(300)

if __name__ == "__main__":
    main()