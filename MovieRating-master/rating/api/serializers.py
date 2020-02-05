from rest_framework import serializers
from rating.models import MovieRating


class MovieRatingSerializer(serializers.ModelSerializer):

	class Meta:
		model=MovieRating
		fields='__all__'