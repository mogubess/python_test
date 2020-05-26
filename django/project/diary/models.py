from django.db import models

# Create your models here.
from django.utils import timezone #djangoでは、datetime.nowのかわりに、timezone.nowで現在日付時刻を取得する



class Day(models.Model):
#   id = models.AutoField(primary_key=True)#primary_key重複不可フラグ 自動で主キー
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.title


