import requests as rq
import html

class Questions:
    def __init__(self):
        self.question_data = []
        self.parameters = {
                    "amount": 10,
                    "type": "boolean",
                    "category": 0,
                    }

        self.qna = []
        self.flag = 0

    def send_category(self, category):
        self.parameters['category'] = category

    def obtain_questions(self):
        resp = rq.get(url='https://opentdb.com/api.php', params=self.parameters)
        resp.raise_for_status()
        data = resp.json()

        for i in range(len(data['results'])):
           self.qna.append({'question': html.unescape(data['results'][i]['question']),
                            'answer': data['results'][i]['correct_answer']})

        return self.qna


