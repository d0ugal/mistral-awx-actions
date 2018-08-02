from mistral_lib import actions
from tower_cli import get_resource
from tower_cli.conf import settings


class JobCreateAction(actions.Action):

    def __init__(self, job_template, username=None, password=None, host=None):
        self.job_template = job_template
        self.username = username
        self.password = password
        self.host = host

    def run(self, ctx):
        with settings.runtime_values(
                username=self.username, password=self.password,
                host=self.host):
            res = get_resource('job')
            job = res.launch(
                job_template=self.job_template,
            )
        return job
