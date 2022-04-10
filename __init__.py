from mycroft import MycroftSkill, intent_file_handler


class CryptoInformer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('informer.crypto.intent')
    def handle_informer_crypto(self, message):
        adjective = message.data.get('adjective')
        cryptotoken = message.data.get('cryptotoken')
        currency = message.data.get('currency')

        self.speak_dialog('informer.crypto', data={
            'currency': currency,
            'cryptotoken': cryptotoken,
            'adjective': adjective
        })


def create_skill():
    return CryptoInformer()

