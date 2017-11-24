
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload

import mimetypes

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'drive_client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('.')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)

    return credentials


def upload_file(drive_service, filepath):
  """Insert new file.

  Args:
    service: Drive API service instance.
    title: Title of the file to insert, including the extension.
    description: Description of the file to insert.
    parent_id: Parent folder's ID.
    mime_type: MIME type of the file to insert.
    filename: Filename of the file to insert.
  Returns:
    Inserted file metadata if successful, None otherwise.
  """

  file_metadata = {'name': filepath.split("/")[-1]}
  mime_type = mimetypes.guess_type(filepath)[0]
  media = MediaFileUpload(filepath,
                        mimetype=mime_type)

  file = drive_service.files().create(body = file_metadata, media_body=media, fields = "id").execute()

  # .create(body=file_metadata,
  #                                   media_body=media,
                                    # fields='id').execute()


  # Uncomment the following line to print the File ID
  # print 'File ID: %s' % file['id']

  return file
  # except Exception as e:
  #   print('An error occurred: ' + str(e))
  #   return None

# def upload_file(drive_service, filepath):

#     mime_type = mimetypes.guess_type(filepath)

#     file_metadata = {'title': filepath.split("/")[-1]}
#     media = MediaFileUpload(filepath,
#                             mimetype=mime_type)
#     file = drive_service.files().insert(body=file_metadata,
#                                         media_body=media,
#                                         fields='id').execute()
#     print('File ID: %s' % file.get('id'))


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    with open("signal_out") as infile:
        for line in infile:
            if "Path: " in line:
                filepath = line[line.find("Path:") + 6:]
    
    if not filepath:
        print("file_path_error")
        exit()

    upload_file(service, filepath)

if __name__ == '__main__':
    main()