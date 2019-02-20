import datetime

from django.db import models
from django.utils import timezone

# Model の情報を使って、データベースのスキーマなどを自動で作ってくれる


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # ForeignKey を利用してクラス間の関係を定義する
    # この場合、それぞれの Choice に対して一つの Question が対応する（一対一）関係を定義している
    #
    # on_delete は、参照するオブジェクトが削除された時の動作を指定する引数
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text