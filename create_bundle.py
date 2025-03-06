import os
import zipfile
import shutil

def create_bundle():
    # Create the zip file
    with zipfile.ZipFile('slack_wifi_status_bundle.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add main script
        zipf.write('main.py')

        # Add slack_wifi_status package
        for root, dirs, files in os.walk('slack_wifi_status'):
            for file in files:
                zipf.write(os.path.join(root, file))

    print("Bundle created: slack_wifi_status_bundle.zip")

if __name__ == "__main__":
    create_bundle()