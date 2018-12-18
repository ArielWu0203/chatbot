from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1234567890987654321"

machine = TocMachine(
    states=[
        'user',
        'search_state',
        'help_state',
        'name_state',
        'choose_state',
        'image_state',
        'lab_state',
        'hello_state',
        'end_state'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'help_state',
            'conditions': 'is_going_to_help'
        },
	    {
	        'trigger': 'advance',
	        'source': 'user',
	        'dest': 'name_state',
	        'conditions': 'is_going_to_name'
	    },
        {
            'trigger': 'advance',
            'source': 'name_state',
            'dest': 'choose_state',
            'conditions': 'is_going_to_choose'
        },
        {
            'trigger': 'advance',
            'source': 'choose_state',
            'dest': 'image_state',
            'conditions': 'is_going_to_image'
        },
        {
            'trigger': 'advance',
            'source': 'choose_state',
            'dest': 'lab_state',
            'conditions': 'is_going_to_lab'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'search_state',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'hello_state',
            'conditions': 'is_going_to_hello'
        },
        {
            'trigger': 'advance',
            'source': 'search_state',
            'dest': 'end_state',
            'conditions': 'is_going_to_end'
        },
        {
            'trigger': 'go_back',
            'source': [
                'help_state',
                'image_state',
                'lab_state',
                'hello_state',
                'end_state'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=8000, debug=True, reloader=True)
