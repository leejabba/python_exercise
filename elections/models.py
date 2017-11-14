from django.db import models

# Create your models here.
# 후보 정보 테이블 클래스
class Candidate(models.Model):
    name = models.CharField(max_length = 10)
    introduction = models.TextField()
    area = models.CharField(max_length = 15)
    party_number = models.IntegerField(default = 1)

    def __str__(self):
        return self.name + " / " + self.area

# 여론조사 정보 테이블 클래스
class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15)

    def __str__(self):
        return str(self.start_date) + " ~ " + str(self.end_date) + " (" + self.area + ")"

# 득표수 정보 테이블 클래스
class Pick(models.Model):
    poll = models.ForeignKey(Poll)
    candidate = models.ForeignKey(Candidate)
    votes = models.IntegerField(default = 0)
