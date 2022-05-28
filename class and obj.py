class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name,age,tracks,score):
    self.name = str(name)
    self.age = int(age)
    self.tracks = list(tracks)
    self.score + float(score)


def change_name(self, change_name):
    self.change_name = change_name
    print("name was changed from", self .name, "to", change_name )

def change_age(self, change_age):
    self.change_age = change_age
    print("his age was changed from", self.age, "to", change_age)

def change_tracks(self, change_tracks):
    self.change_tracks = change_tracks
    print("his age was changed from", self.tracks, "to", change_tracks)

def change_score(self, change_score):
    self.change_score = change_score
    print("his age was changed from", self.score, "to", change_score)




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
