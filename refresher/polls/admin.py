from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Area"
admin.site.index_title = "Welcome to the Polls Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

    inlines = [ChoiceInline]


# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
