import sys
import json
import base64
import requests

URL = 'https://api.github.com/repos/copilot-com/Copilot.Net/contents/CopilotMac/Resources/OSXvnc-server?access_token=%s'
print(URL)


def main(filename, token):
    url = URL % token
    print('Upload', filename)
    print('')
    print('Getting file data...')
    resp = requests.get(url)
    data = resp.json()
    sha = data['sha']
    print('File sha', sha)
    
    print('Reading new file...')
    with open(filename) as fd:
        b64 = base64.b64encode(fd.read())
    data = {
        'path': 'CopilotMac/Resources/OSXvnc-server',
        'sha': sha,
        'content': b64,
        'message': 'OSXvnc Build',
    }
    print('Sending new file...')
    resp = requests.put(url, json=data)
    print('File uploaded')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
