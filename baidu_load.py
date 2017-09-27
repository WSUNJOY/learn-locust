from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
	    self.client.get("/")

class WebsiteUser(HttpLocust):
	"""docstring for WebsiteUser"""
	task_set = UserBehavior
	min_wait = 5000
	max_wait = 9000
		
