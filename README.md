Here's a comprehensive README.md for your Slack WiFi Status Updater package:

```markdown
# Slack WiFi Status Updater

Automatically update your Slack status based on your WiFi connection. This tool helps maintain your work status by detecting your current WiFi network and updating your Slack status accordingly.

## Features

- Automatically detects current WiFi network
- Updates Slack status based on predefined WiFi-to-status mappings
- Supports multiple operating systems (macOS, Windows, Linux)
- Runs on schedule during working hours
- No external dependencies (uses only Python standard library)
- Easy to configure and customize

## Prerequisites

- Python 3.6 or higher
- Slack workspace access
- Slack API token with appropriate permissions

## Installation

1. Clone the repository or download the zip file:
```bash
git clone https://github.com/yourusername/slack-wifi-status.git
cd slack-wifi-status
```

2. Create the bundle:
```bash
python create_bundle.py
```

3. Extract the bundle:
```bash
python -m zipfile -e slack_wifi_status_bundle.zip slack_wifi_status_extracted
```

## Configuration

1. Create a Slack App:
   - Go to [Slack API](https://api.slack.com/apps)
   - Click "Create New App"
   - Select "From scratch"
   - Choose your workspace
   - Under "OAuth & Permissions", add the following scopes:
     - `users.profile:write`
   - Install the app to your workspace
   - Copy the "User OAuth Token" (starts with `xoxp-`)

2. Update the configuration:
   - Open `slack_wifi_status/config.py`
   - Add your Slack token
   - Configure your WiFi-to-status mappings:
```python
{
    'slack_token': 'xoxp-your-token-here',
    'wifi_status_map': {
        'Home WiFi': ('Working from home', ':house:'),
        'Office WiFi': ('In the office', ':office:'),
        'Starbucks': ('Working from Starbucks', ':coffee:'),
    }
}
```

## Setting Up Automated Runs (macOS)

### Using Cron

1. Create a shell script (`run_slack_wifi_status.sh`):
```bash
#!/bin/bash
cd /path/to/slack_wifi_status_extracted
/usr/bin/python3 main.py
```

2. Make it executable:
```bash
chmod +x /path/to/run_slack_wifi_status.sh
```

3. Add to crontab:
```bash
crontab -e
```

4. Add the following line to run every hour during working hours (9 AM to 5 PM, Monday to Friday):
```
0 9-17 * * 1-5 /path/to/run_slack_wifi_status.sh >> /tmp/slack_wifi_status.log 2>&1
```

### Troubleshooting Cron

If the cron job isn't working:

1. Grant Full Disk Access to cron:
   - System Preferences > Security & Privacy > Privacy
   - Click on "Full Disk Access"
   - Click "+" and add `/usr/sbin/cron`

2. Check the logs:
```bash
tail -f /tmp/slack_wifi_status.log
```

## Manual Usage

You can also run the script manually:

```bash
cd slack_wifi_status_extracted
python main.py
```

## Customization

### Adding New WiFi Networks

Update the `wifi_status_map` in `config.py`:

```python
'wifi_status_map': {
    'New WiFi Name': ('Custom Status', ':emoji:'),
    # Add more mappings as needed
}
```

### Modifying Working Hours

Edit the cron schedule in your crontab:

```bash
# Format: minute hour day month weekday command
# Example: Run from 8 AM to 6 PM
0 8-18 * * 1-5 /path/to/run_slack_wifi_status.sh
```

## Project Structure

```
slack_wifi_status/
├── slack_wifi_status/
│   ├── __init__.py
│   ├── wifi_checker.py
│   ├── slack_updater.py
│   └── config.py
├── main.py
└── create_bundle.py
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Security Notes

- Keep your Slack token secure
- Don't commit the token to version control
- Consider using environment variables for sensitive data

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Slack API Documentation
- Python Standard Library
- Contributors and maintainers

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com].
```

This README provides:
- Clear installation instructions
- Detailed configuration steps
- Setup instructions for automated runs
- Troubleshooting guidance
- Customization options
- Project structure overview
- Security considerations
- License and support information

You may want to customize this README further based on:
- Your specific implementation details
- Additional features you've added
- Specific requirements for your environment
- Contact information and support channels
- Any specific licensing requirements

Remember to update the placeholder values (like email addresses and URLs) with your actual information before publishing.