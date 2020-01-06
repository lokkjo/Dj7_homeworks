from django.contrib import admin



from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')



class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
