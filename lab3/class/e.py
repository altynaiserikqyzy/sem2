class student:
    def __init__(self , name , age , faculty , score):
        self.name = name 
        self.age=age
        self.faculty=faculty
        self.score=score

    def passes(self):
        if self.score>50:
            print(f"Yes, {self.name} passes")
        else:
            print(f"No , {self.name} fails")
a = student("Altynai" , 18 , "FIT" , 70)
