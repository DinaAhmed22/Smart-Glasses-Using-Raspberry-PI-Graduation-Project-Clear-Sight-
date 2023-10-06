# Import the client library
from google.cloud import translate_v2 as translate

# Create a client object
client = translate.Client()

# Translate text to Arabic
translation = client.translate('Hello, world!', target_language='ar')

# Print the translated text
print(translation['input'], '->', translation['translatedText'])