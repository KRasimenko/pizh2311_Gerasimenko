from school import *
lesson = Data('class', 'object', 'inheritance', 'polymorphism', 
'encapsulation')
pupil = Pupil()
for i in lesson:
    pupil.take(i)

pupil.knowledge
['class', 'object', 'inheritance', 'polymorphism', 'encapsulation']
pupil.lose()
pupil.knowledge
['class', 'inheritance', 'polymorphism', 'encapsulation']
pupil.lose()
pupil.knowledge
['class', 'inheritance', 'polymorphism']