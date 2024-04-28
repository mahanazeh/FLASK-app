from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get("/")

    # Add more tasks to simulate user behavior

# Additional configuration and task definitions can be added as needed
