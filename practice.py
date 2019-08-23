class Jobs:

    jobseeker = "Daniel"

    def __init__(self, company, url, title):
        self.company = company
        self.url = url
        self.title = title
    
    def print_func(self):
        print("Company name: " + self.company + "\t\t Title: " + self.title + "\t\t URL: " + self.url)
    
    @classmethod
    def get_job_seeker(cls):
        print(cls.jobseeker)
    
    @staticmethod
    def get_info():
        print("This static method will not have instance nor class variables")


job1 = Jobs("Kaiser", "Intern", "kp.org")
job1.print_func()
job1.get_job_seeker()

Jobs.get_info()