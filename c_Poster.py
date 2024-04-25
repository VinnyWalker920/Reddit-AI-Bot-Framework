import re


class Poster():
    def __init__(self,API,dataAnchor):
        self.API = API
        self.dataAnchor = dataAnchor

    def _sanitize_text(self, text):
        # Use regular expression to find and remove substrings enclosed in square brackets
        cleaned_text = re.sub(r'\s*\[.*?\]', '', text)

        # Ensure the first character is not a space
        if cleaned_text.startswith(' '):
            cleaned_text = cleaned_text.lstrip()

        # Remove quotation marks only if they exist at the beginning and end of the message
        if cleaned_text.startswith('"') and cleaned_text.endswith('"'):
            cleaned_text = cleaned_text[1:-1]

            # Ensure the first word is not an intro
        if cleaned_text.startswith('my response: '):
            cleaned_text = cleaned_text.replace('my response: ','')

            # Ensure the first letter is not :
        if cleaned_text.startswith(':'):
            cleaned_text = cleaned_text.replace(':','')
        
            # Ensure the first word is not an intro
        if cleaned_text.startswith('my response '):
            cleaned_text = cleaned_text.replace('my response ','')
        
        return cleaned_text
    

    def postReply(self, response, post):
        apiPost = self.API.submission(id=post["id"])
        apiPost.reply(self._sanitize_text(response))
        self.dataAnchor.addDatabase(self._sanitize_text(response), post)

    def postDatabase(self, response, post):
        self.dataAnchor.addDatabase(self._sanitize_text(response), post)
    







