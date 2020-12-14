# from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from polls.serializers import QuestionSerializer
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic
# from django.utils import timezone
from .models import Choice, Question
from rest_framework import viewsets
from .serializers import QuestionSerializer



class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class= QuestionSerializer










# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions.(not including those set to be published in the future)"""
#         return Question.objects.filter(
#                 pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#     """
#     Excludes any questions that aren't published yet.
#     """
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):

#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', 
#     args=(question.id,)))


# @csrf_exempt

# def question_list(request):
#     if request.method == 'GET':
#         questions=Question.objects.all()
#         serializer=QuestionSerializer(questions,many=True)
#         return JsonResponse(serializer.data,safe=False)

#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=QuestionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def question_detail(request,pk):
#     try:
#         question=Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return HttpResponse(status=404)
        
#     if request.method== 'GET':
#         serializer=QuestionSerializer(question)
#         return JsonResponse(serializer.data)
        
#     elif request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=QuestionSerializer(question,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         question.delete()
#         return HttpResponse(status=204)
