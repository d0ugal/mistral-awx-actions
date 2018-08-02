from mistral_lib import actions
from tower_cli import get_resource
from tower_cli.conf import settings


class AwxAction(actions.Action):

    def __init__(self, job_template, username=None, password=None, host=None):
        self.job_template = job_template
        self.username = username
        self.password = password
        self.host = host

    def run(self):
        with settings.runtime_values(username='user', password='pass'):
            res = get_resource('job')
            job = res.create(
                job_template=self.job_template,
            )
        return job
