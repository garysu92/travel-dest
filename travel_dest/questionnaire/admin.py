from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                 ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)