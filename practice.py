class Jobs:

    def __init__(self, company, url, title):
        self.company = company
        self.url = url
        self.title = title
    
    def print_func(self):
        print("Company name: " + self.company + "\t\t Title: " + self.title + "\t\t URL: " + self.url)

job1 = Jobs("Kaiser", "Intern", "kp.org")
job1.print_func()