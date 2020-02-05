from django.contrib import admin
from rating.models import MovieRating


class MovieRatingAdmin(admin.ModelAdmin):
	class Meta:
		model=MovieRating

	list_display=['title','rating','year']



admin.site.register(MovieRating,MovieRatingAdmin)