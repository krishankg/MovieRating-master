from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import MovieRatingSerializer
from rating.models import MovieRating
from rest_framework.views import APIView


# class MovieRatingListApiView(ListAPIView):
# 	serializer_class=MovieRatingSerializer

# 	def get_queryset(self,*args,**kwargs):
# 		queryset=MovieRating.objects.all()
# 		query=self.request.GET.get('q')
# 		if query is not None:
# 			queryset=queryset.filter(year=query)

# 		return queryset


class MovieYearAPIView(APIView):
	serializer_class=MovieRatingSerializer

	def get(self,request,*args,**kargs):
		queryset=MovieRating.objects.all()
		query=self.request.GET.get('q')
		if query is not None:
			queryset1=queryset.filter(year=query).order_by('-year')
			serializer=self.serializer_class(queryset1,many=True)
			return Response(serializer.data,status=200)
		else:
			serializer=self.serializer_class(queryset.order_by('-year'),many=True)
			return Response(serializer.data,status=200)




class MovieRatingSearchAPIView(APIView):
	serializer_class=MovieRatingSerializer

	def get(self,request,*args,**kwargs):
		queryset=MovieRating.objects.all()
		q=self.request.GET.get('q')
		if q is not None:
			queryset1=queryset.filter(rating__gt=q)
			serializer=self.serializer_class(queryset1,many=True)
			return Response(serializer.data,status=200)
		else:
			serializer=self.serializer_class(queryset.order_by('-rating'),many=True)
			return Response(serializer.data,status=200)