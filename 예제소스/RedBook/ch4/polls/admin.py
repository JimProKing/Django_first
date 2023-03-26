from django.contrib import admin
from polls.models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):    # 테이블 형식으로 보여주기.
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']    # 이렇게 코딩하면, 하나에 다 들어감.
    fieldsets = [                               # 각 필드를 분리해서 보여줄 수 있음.
        ('Question Statement', {'fields': ['question_text']}),
        # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),    # 이렇게 하면 필드 접기 기능 사용가능.
    ]
    inlines = [ChoiceInline]    # choice 모델 클래스 같이보기
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']  # 우측 필터 사이드 바.(오늘, 7일, 1달, 1년 등)
    search_fields = ['question_text']   # 검색 박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
