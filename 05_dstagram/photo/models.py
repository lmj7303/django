from django.db import models

# Create your models here.

#1.모델: 데이터베이스 저장될 데이터가 있다면 해당 데이터를 묘사한다.
#2.뷰(기능): 계산,처리-실제기능,화면
#3.URL 맵핑: 라우팅 테이블에 기록한다. urls.py에 기록-주소를 지정
#4.화면에 보여줄 것이있다:템플릿작성(html)

#장고의 기본 유저 모델
from django.contrib.auth.models import User

class Photo(models.Model):
    author=models.ForeignKey()
    Photo
    textcreated
    updated