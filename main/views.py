from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


grade_db = [
  {
    "_id": "356b4b97-18e2-4954-A832-6f77e5d04522",
    "index": "1",
    "teacher": "범민호",
    "phone": "010-8504-6712",
    "grade": "3",
    "num": "5",
    "contents": "탄핵의 트고 향상을 걱정도 아니할 활동이 20일을 자유이며. 때 구하지"
  },
  {
    "_id": "4feb3ad8-51b3-44c4-C1bd-b3413acbca85",
    "index": "2",
    "teacher": "함재율",
    "phone": "010-7286-4709",
    "grade": "2",
    "num": "12",
    "contents": "피어나는 기업의 헌법에 구할 하며 문서로 싹이 이웃. 국민 대통령후보자가"
  },
  {
    "_id": "cec55066-ebaf-4e4d-A7f6-e1513324a31f",
    "index": "3",
    "teacher": "빙소빈",
    "phone": "010-5658-6170",
    "grade": "3",
    "num": "13",
    "contents": "기타 듯합니다 청춘을 구하기 법원은 피선거권이 그 봄날의. 동산에는 법원은"
  },
  {
    "_id": "917c95fe-396e-475b-C244-d0e66d27c895",
    "index": "4",
    "teacher": "유혁진",
    "phone": "010-4146-3883",
    "grade": "2",
    "num": "9",
    "contents": "4분의 칼이다 교원의 비상계엄이 타오르고 40일전에 제출할 헌법재판소. 사회윤리를 외국에의"
  },
  {
    "_id": "aef7d530-d707-4288-B156-ccdfe8329b60",
    "index": "5",
    "teacher": "피영은",
    "phone": "010-6386-6108",
    "grade": "1",
    "num": "13",
    "contents": "살 임명하고 질병·노령 재판관의 이국 정부는 간에 필요가. 회의는 약동하다"
  }
]


def index(request):
    return render(request,'main/index.html')

def jejuohyun(request):
    return render(request,'main/jejuohyun.html')

def high_1st(request):
    return render(request,'main/high_1st.html')

def high_2nd(request):
    return render(request,'main/high_2nd.html')

def high_3rd(request):
    return render(request,'main/high_3rd.html')

def my_page(request):
    return render(request,'main/my_page.html')

def grade(request):
    return render(request,'main/grade.html')