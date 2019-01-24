from courseapp.models import QuestionModel
from django.http import JsonResponse

def get_score(answers):
    score = 0
    for answer in answers:
        try:
            question = QuestionModel.objects.get(q_id=answer['q_id'])
        except QuestionModel.DoesNotExist:
            raise JsonResponse({"response": "Question Does Not Exist"})
        if answer['answer'] == question.answer:
            score+=2
        else:
            score-=1
    return score