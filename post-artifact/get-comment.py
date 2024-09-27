import sys
import os
import json

def main(json_comments):

    # Open the JSON file and load its contents into a Python object
    with open(json_comments, 'r') as file:
        data = json.load(file)

    # Now you can work with the 'data' object
    for i in range(len(data['comments'])):
        body = data['comments'][i]['body']
        auth = data['comments'][i]['author']['login']
        id   = data['comments'][i]['id']

        # Regex match to the body of the comment looking
        # for the expression "Thank you for your contribution"
        # if found, print the author and the body of the comment
        if "Your preview" in body and auth == 'github-actions':
            os.environ['COMMENT_ID'] = str(id)
            return 0

        # Set id via environment variable
        
    
    print('null')
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get-comment.py comments.json")
    else:
        main(sys.argv[1])
        
    
    