# 복습
1. Admin 사이트 역할
- 데이터 베이스 데이터 관리
    - 데이터 생성, 조회, 변경, 삭제 등의 기능 제공.
    - look and feel UI 제공.
      - 직접 코딩하려면 빡셈.
    - 장고에서는 테이블을 하나의 클래스로 정의
      - 컬럼은 변수(attribute)로 매핑함.
- PK default
  - Not Null
  - Autoincrement

>     pub_date = models.DateTimeField('date published')
pub_date 컬럼에 대한 레이블 문구.
- admin 사이트에서 이거 보게될거임.

FK(Forigen Key)
- 항상 다른 테이블의 PK에 연결됨
  - Question 클래스의 id변수까지 지정할 필요 없음.
    - Question 클래스만 지정하면 됨.
- FK로 지정된 컬럼은 _id 접미사 붙음.

> __str__() 메소드
- 객체를 문자열로 표현할 때 사용하는 함수.
  - 이거 정의 안하면, 테이블명이 제대로 표시되지 않음.
    - python2에서는 __unicode__() 사용.


# 4.1 Admin 사이트 꾸미기.

1. polls/models.py
여기서, 사용할 필드들 형식 등 지정해야함.
```
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

# 4.1.2 필드 순서 변경하기
데이터가 아닌, 양식을 변경하려면(ex 순서)
polls/admin.py
이거 수정하면 됨.

# 4.2.1 Create
```
>>> from polls.models import Question,Choice
>>> from django.utils import timezone
>>> q = Question(question_text = "What's new?", pub_date=timezone.now())
>>> q.save()
```

# 4.2.2 Read
```
Question.objects.filter(
    question_text_startswith = 'what
).exclude(
    pub_date_gte = timezone.now()
).filter(
    question_text__contains = 'hob'
)
```

# note
1. admin사이트 더 많은 기능 찾아보기
<a href = "">https://docs.djangoproject.com/en/4.0/ref/contrib/admin/