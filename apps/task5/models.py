from django.db.models import Model, CharField, DateField, IntegerField, ForeignKey, CASCADE, DateTimeField, DO_NOTHING, \
    TextField, ManyToManyField, TimeField

from apps.common.models import BaseModel


class Season(BaseModel):
    start_date = DateField()
    end_date = DateField()


class Legue(BaseModel):
    name = CharField(max_length=128)
    season = ForeignKey("task5.Season", CASCADE, 'legues')


class Club(BaseModel):
    name = CharField(max_length=128)
    score = IntegerField(default=0)
    goals_scored = IntegerField(default=0)
    goals_conceded = IntegerField(default=0)
    description = TextField()
    lague = ForeignKey("task5.Legue", DO_NOTHING, "legues")


class Player(BaseModel):
    fullname = CharField(max_length=128)
    birthdate = DateField()
    club = ForeignKey("task5.Club", DO_NOTHING, "players")
    number = IntegerField()
    all_goals = IntegerField(default=0)
    salary = IntegerField()
    description = TextField()


class Stadion(BaseModel):
    city = CharField(max_length=128)
    century = CharField(max_length=128)
    description = TextField()


class Referee(BaseModel):
    full_name = CharField(max_length=128)
    birthdate = DateField()
    salary = IntegerField()


class Event(BaseModel):  # bolishi mumkin bogan hodisalar:  QIZIL, SARIQ
    event_name = CharField()
    description = TextField()


class Action(BaseModel):  # qaysi futbolchiga berildi
    event = ForeignKey("task5.Event", DO_NOTHING, "actions")
    player = ForeignKey("task5.Player", DO_NOTHING, "actions")
    description = TextField()


class Match(BaseModel):  # rejalashtirilgan ucharushuv
    start_date = DateTimeField()
    stadion = ForeignKey("task5.Stadion", DO_NOTHING, 'matches')
    guest = ForeignKey("task5.Club", CASCADE, "players1")
    host = ForeignKey("task5.Club", CASCADE, "players2")
    desciption = TextField()
    referee = ForeignKey("task5.Referee", DO_NOTHING, "matches")


class Game(BaseModel):  # uchrashuv tugadi
    match = ForeignKey("task5.Match", DO_NOTHING, "game", unique=True)
    goal1 = IntegerField(default=0)
    goal2 = IntegerField(default=0)
    actions = ManyToManyField("task5.Action", "matches")
    end_date = DateTimeField()


class Goal(BaseModel):
    author = ForeignKey("task5.Player", CASCADE, "goals")
    asistent = ForeignKey("task5.Player", CASCADE, "asists")
    time = TimeField()
