from django.contrib import admin

from .models import User , Bar , Menu, Review , Event

class UserAdmin(admin.ModelAdmin):
	list_display = [f.name for f in User._meta.fields]
	
	
admin.site.register(User,UserAdmin)

class BarAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Bar._meta.fields]


admin.site.register(Bar,BarAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Menu._meta.fields]

	
	
admin.site.register(Menu,MenuAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Review._meta.fields]


admin.site.register(Review,ReviewAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Event._meta.fields]


admin.site.register(Event,EventAdmin)
