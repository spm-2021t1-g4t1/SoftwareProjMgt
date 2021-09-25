class quiz():
    def __init__(self, quizId, quizTitle):      
        self.id = quizId
        self.title = quizTitle
        self.question = []


    def getQuizId(self):
        return self.id
    
    def getQuizTitle(self):
        return self.title
    
    def getQuizType(self):
        return self.type

    def getQuizQuestion(self):
        return self.question
    
    def addQuizQuestion(self, question):
        try:
            self.question.append(question)
            return True
        except:
            return False

class question():
    def __init__(self, title, options, type, correct):
        self.title = title
        self.options = options
        self.type = type
        self.correct = correct