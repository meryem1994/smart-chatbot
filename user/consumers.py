import json

from channels.generic.websocket import WebsocketConsumer

from django.contrib.auth.models import User

from gestion_admin.models import Article, Historique

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = User.objects.get(username=self.scope["user"])
        self.historique = Historique.objects.filter(user=self.user)
        self.article = Article.objects.get(id=self.scope['url_route']['kwargs']['room'])
        
        print(self.user, self.article)


        self.last_history = self.historique[self.historique.count()-1]
        self.last_article = self.last_history.article
        self.id = self.last_article.id
        self.title = self.last_article.title
        self.categorie = self.last_article.categorie
        self.text = self.last_article.file.read().decode('utf-8')
        print(self.last_history, self.last_article)

        print(self.text)
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
        reponse = None
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        if 'hello' in message:
            reponse = {
                'type' : 'text',
                'text' : "Hello I'am ChatBot!"
            }
        elif 'hi' in message:
            reponse= {
                'type' : 'link',
                'article' : 1,
                'text' : 'hello'
            }
        self.send(text_data=json.dumps(reponse))