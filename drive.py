from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth("file")


# Try to load saved client credentials
gauth.LoadCredentialsFile("credentials.json")

if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("credentials.json")


drive = GoogleDrive(gauth)

with open("signal_out") as infile:
    for line in infile:
        if "Path: " in line:
            upload_path = line[line.find("Path:") + 6:]
print("path is: " + upload_path)
file1 = drive.CreateFile({'title': upload_path.split("/")[-1]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile(upload_path)
file1.Upload()
