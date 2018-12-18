from transitions.extensions import GraphMachine
from utils import send_text_message
from utils import send_img_message,send_button_message
from bug_test import search_url,search_image,search_name
from test_data import search_last_name
#global
choose_arr = ["choose image","choose lab"]
choose_buttons = ["Picture","lab website"]
NAME = ""

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_menu(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'menu'
        return False

    def is_going_to_help(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'help'
        return False

    def is_going_to_name(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'name'
        return False

    def is_going_to_image(self, event):
        if event.get("postback"):
            text = event['postback']['payload'] 
            if text == choose_arr[0]:
                return True
        return False

    def is_going_to_lab(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            if text == choose_arr[1]:
                return True
        return False


    def is_going_to_choose(self, event):
        if event.get("message"):
            text = event['message']['text']
            sender_id = event['sender']['id']
            if search_name(text):
                global NAME 
                NAME = text
                return True
        return False
    
    def is_going_to_hello(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == "hello"
        return False

    def is_going_to_search(self,event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == "search"
        return False

    def is_going_to_end(self,event):
        if event.get("message"):
            text = event['message']['text']
            sender_id = event['sender']['id']

            #search name
            list = search_last_name(text)
            if not list:
                send_text_message(sender_id, "Search nothing")
                return True
            else:
                send_text_message(sender_id, list)
                return True
        return False

    def on_enter_help_state(self, event):
        print("I'm entering help state")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "Input name or search or hello or help")
        self.go_back()

    def on_enter_name_state(self,event):

        sender_id = event['sender']['id']
        text = "Input teacher's name"
        send_text_message(sender_id,text)

    def on_enter_choose_state(self,event):
        print("I'm entering choose state")

        sender_id = event['sender']['id']
        text = "choose the button"
        buttons = []
        for index in range(len(choose_arr)):
            buttons.append({"type":"postback","title":choose_buttons[index],"payload":choose_arr[index]})
        send_button_message(sender_id, text, buttons)

    def on_enter_image_state(self,event):
        sender_id = event['sender']['id']
        image_url = search_image(NAME)
        send_img_message(sender_id, image_url)
        self.go_back()

    def on_enter_lab_state(self,event):
        sender_id = event['sender']['id']
        lab_url = search_url(NAME)
        send_text_message(sender_id, lab_url)
        self.go_back()

    def on_enter_hello_state(self,event):
        sender_id = event['sender']['id']
        text = "Hello!!!"
        send_text_message(sender_id, text)
        self.go_back()

    def on_enter_search_state(self,event):
        sender_id = event['sender']['id']
        text = "Input Last name"
        send_text_message(sender_id, text)

    def on_enter_end_state(self,event):
        self.go_back()
    
