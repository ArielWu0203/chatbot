import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAHj9gW1h4kBAATcxZC1EWE9sI8OX9xKIZA4Auoz7qFaVUDl00eOO9Jj6NPG5mEihlFZAPhRL0ecJvY659CFta8FgFoxfAI7oo4YCQZCNRu4il0iWZCbQtTm3wFYvCTnxXZCZAI4ImkFELYGeXNTGSVjvicv1H6LmPiHJZADuYcwCKlxePzrnpVN"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_img_message(id, image_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": image_url,
                    "is_reusable": True
                },
            }
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Unable to send image")
    return response

def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send button message")
    return response

