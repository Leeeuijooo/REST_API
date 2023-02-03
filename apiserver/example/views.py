from rest_framework.response import Response
from rest_framework.decorators import api_view


# @으로 시작하는 것은 decorator 라고 하는데
# 자주 사용하거나 만들기가 복잡한 코드가 있을 때
# 이 코드를 직접 작성하는 대신에 decorator 가 그 코드를 대신 작성

@api_view(['GET'])

def helloAPI(request):
    return Response('전송될 데이터')

# Create your views here.
