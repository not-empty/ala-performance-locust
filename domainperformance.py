import json
import os
import requests
from dotenv import load_dotenv
from locust import between, events, HttpUser, task


class DomainPerformance(HttpUser):
    load_dotenv()

    authToken = None
    context = os.getenv('CONTEXT')
    domain = os.getenv('DOMAIN')
    filterList = os.getenv('FILTER_LIST')
    host = os.getenv('HOST')
    insertBody = json.loads(os.getenv('INSERT_DATA'))
    objectId = None
    objectIdToDelete = None
    secret = os.getenv('SECRET')
    token = os.getenv('TOKEN')
    updateData = os.getenv('UPDATE_DATA')
    wait_time = between(5, 15)

    def on_start(self):
        request = self.client.post(
            '/auth/generate',
            {
                'token': self.token,
                'secret': self.secret
            }
        )

        self.authToken = json.loads(request.content)['data']['token']

    @task
    def healthCheck(self):
        self.client.get('/health')

    @task
    def list(self):
        self.client.request(
            'GET',
            '/' + self.domain + '/list',
            headers={'Authorization': self.authToken, 'Context': self.context}
        )

    @task
    def detail(self):
        self.client.request(
            'GET',
            '/' + self.domain + '/detail/' + self.objectId,
            headers={'Authorization': self.authToken, 'Context': self.context}
        )

    @task
    def edit(self):
        self.client.request(
            'PATCH',
            '/' + self.domain + '/edit/' + self.objectId,
            headers={'Authorization': self.authToken, 'Context': self.context},
            data=self.updateData
        )

    @task
    def insert(self):
        self.client.request(
            'POST',
            '/' + self.domain + '/add/',
            headers={'Authorization': self.authToken, 'Context': self.context},
            data=self.insertBody
        )

    @task
    def listWithParam(self):
        self.client.request(
            'GET',
            '/' + self.domain + '/list' + self.filterList,
            headers={'Authorization': self.authToken, 'Context': self.context}
        )

    @task
    def bulk(self):
        self.client.request(
            'POST',
            '/' + self.domain + '/bulk/',
            headers={'Authorization': self.authToken, 'Context': self.context},
            data={'ids[]': [self.objectId]}
        )

    @task
    def listDelete(self):
        self.client.request(
            'GET',
            '/' + self.domain + '/dead_list/',
            headers={'Authorization': self.authToken, 'Context': self.context}
        )


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    request = requests.post(
        DomainPerformance.host + '/auth/generate',
        data={
            'token': DomainPerformance.token,
            'secret': DomainPerformance.secret
        }
    )

    token = json.loads(request.content)['data']['token']

    request = requests.post(
        DomainPerformance.host + '/' + DomainPerformance.domain + '/add',
        headers={'Authorization': token, 'Context': DomainPerformance.context},
        data=DomainPerformance.insertBody
    )

    DomainPerformance.objectId = json.loads(request.content)['data']['id']
