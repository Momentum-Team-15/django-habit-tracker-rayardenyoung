from rest_framework.views import APIView
from rest_framework.response import Response
from habittracker.models import Habit
from .serializers import HabitSerializer

# Create your views here.
class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all habits.
        """
        # habits = [habit.name for habit in Habit.objects.all()]
        #query for all the habits
        habits = Habit.objects.all()
        #serialize the date so that I can return habits as json
        #serialize = translating> taking it from one format & programatically putting it into another format
        #take python data(queryset) and translate it into json > involves mapping values
        #in order to map values, we're doing something similar to forms (mapping forms to model fields)
        #create an instance of a serializer/class below > will show the fields
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
    

# def habit_list(request):
#     #get the habits
#     habits = Habit.objects.all()
#     #return the response
#     return render(request, "path-to-template", {'habits': habits})