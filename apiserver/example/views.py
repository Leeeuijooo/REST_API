from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# @으로 시작하는 것은 decorator 라고 하는데
# 자주 사용하거나 만들기가 복잡한 코드가 있을 때
# 이 코드를 직접 작성하는 대신에 decorator 가 그 코드를 대신 작성

@api_view(['GET'])

def helloAPI(request):
    return Response('전송될 데이터')

# Create your views here.

@api_view(['GET','POST'])
def booksAPI(request):
    if request.method == 'GET':

        # 전체 데이터 가져오기
        books = Book.objects.all()
        # 파이썬 데이터를 JSON 형식으로 변환
        # 데이터가 1개인 경우는 many=True 생략

        serializer = BookSerializer(books, many=True)
        # 응답 전송
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # 삽입에서 넘어온 파라미터를 모델로 변환
        # 클라이언트에서는 BookSerializer 에 설정된 속성들의 값을 모두 전달해야 함
        # 전송된 파라미터를 Model 의 데이터로 변환하는 것을 역직렬화 라고 한다

        serializer = BookSerializer(data=request.data)
        # 데이터 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 상세보기 처리를 위한 메서드
@api_view(['GET'])
def bookAPI(request, bid):
    # 데이터 찾아오기
    # bid 에 해당하는 데이터가 없으면 404에러를 발생시키고 존재하면 찾아와서
    # book에 대입
    book = get_object_or_404(Book,bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework import generics, mixins
# 전체 목록 보기 와 삽입을 처리
class BooksAPIMinxins(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    # 전체 데이터와 serializer 를 설정
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # get 요청 처리
    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    # post 요청 처리
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

# 상세보기, 수정, 삭제를 처리할 클래스 - bid 를 매개변수로 받아야 한다

class BookAPIMinxins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    # 전체 데이터와 serializer 를 설정
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # 매개변수 필드를 설정
    lookup_field = 'bid'

    # bid 를 이용해서 하나의 데이터 찾아오기
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)

    # bid 를 이용해서 데이터 수정
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    # bid 를 이용해서 데이터 삭제
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)




