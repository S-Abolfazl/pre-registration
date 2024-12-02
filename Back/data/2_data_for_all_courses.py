import json
from course.models import AllCourses

data = {
    "course1":{ 
        "courseName": "زبان خارجی",
        "unit": "3",
        "type": "basic_course"
    },
    "course2":{ 
        "courseName": "مهارت های کاربردی کامپیوتر",
        "unit": "1",
        "type": "practical_course"
    },
    "course3":{ 
        "courseName": "مبانی کامپیوتر و برنامه سازی",
        "unit": "3",
        "type": "theory_course"
    },
    "course4":{ 
        "courseName": "ریاضی 1",
        "unit": "3",
        "type": "basic_course"
    },
    "course5":{ 
        "courseName": "فیزیک 1",
        "unit": "3",
        "type": "basic_course"
    },
    "course6":{ 
        "courseName": "برنامه سازی پیشرفته",
        "unit": "3",
        "type": "theory_course"
    },
    "course7":{ 
        "courseName": "ریاضی 2",
        "unit": "3",
        "type": "basic_course"
    },
    "course8":{ 
        "courseName": "معادلات دیفرانسیل",
        "unit": "3",
        "type": "basic_course"
    },
    "course9":{ 
        "courseName": "مدار های الکتریکی و الکترونیکی",
        "unit": "3",
        "type": "theory_course"
    },
    "course10":{ 
        "courseName": "فیزیک 2",
        "unit": "3",
        "type": "basic_course"
    },
    "course11":{ 
        "courseName": "آز فیزیک 2",
        "unit": "1",
        "type": "basic_course"
    },
    "course12":{ 
        "courseName": "ریاضی گسسته",
        "unit": "3",
        "type": "theory_course"
    },
    "course13":{ 
        "courseName": "مدار منطقی",
        "unit": "3",
        "type": "theory_course"
    },
    "course14":{ 
        "courseName": "جبر خطی",
        "unit": "3",
        "type": "theory_course"
    },
    "course15":{ 
        "courseName": "سیگنالها و سیستمها",
        "unit": "3",
        "type": "theory_course"
    },
    "course16":{ 
        "courseName": "مدار مجتمع دیجیتال",
        "unit": "3",
        "type": "theory_course"
    },
    "course17":{ 
        "courseName": "زبان تخصصی",
        "unit": "2",
        "type": "theory_course"
    },
    "course18":{ 
        "courseName": "ساختمان داده ها",
        "unit": "3",
        "type": "theory_course"
    },
    "course19":{ 
        "courseName": "نظریه زبانها و ماشینها",
        "unit": "3",
        "type": "theory_course"
    },
    "course20":{ 
        "courseName": "آز منطقی معماری",
        "unit": "1",
        "type": "practical_course"
    },
    "course21":{ 
        "courseName": "معماری کامپیوتر",
        "unit": "3",
        "type": "theory_course"
    },
    "course22":{ 
        "courseName": "آمار و احتمالات مهندسی",
        "unit": "3",
        "type": "basic_course"
    },
    "course23":{ 
        "courseName": "مدرسه تکمیلی",
        "unit": "0",
        "type": "theory_course"
    },
    "course24":{ 
        "courseName": "طراحی الگوریتم",
        "unit": "3",
        "type": "theory_course"
    },
    "course25":{ 
        "courseName": "تحلیل و طراحی سیستم",
        "unit": "3",
        "type": "theory_course"
    },
    "course26":{ 
        "courseName": "هوش و سیستم خبره",
        "unit": "3",
        "type": "theory_course"
    },
    "course27":{ 
        "courseName": "کامپایلر",
        "unit": "3",
        "type": "theory_course"
    },
    "course28":{ 
        "courseName": "روش پژوهش",
        "unit": "2",
        "type": "theory_course"
    },
    "course29":{ 
        "courseName": "پایگاه داده",
        "unit": "3",
        "type": "theory_course"
    },
    "course30":{ 
        "courseName": "مهندسی نرم افزار",
        "unit": "3",
        "type": "theory_course"
    },
    "course31":{ 
        "courseName": "شبکه های کامپیوتری",
        "unit": "3",
        "type": "theory_course"
    },
    "course32":{ 
        "courseName": "آز سیستم های عامل",
        "unit": "1",
        "type": "practical_course"
    },
    "course33":{ 
        "courseName": "آز ریزپردازنده",
        "unit": "1",
        "type": "practical_course"
    },
    "course34":{ 
        "courseName": "ریزپردازنده و مدار واسط",
        "unit": "3",
        "type": "theory_course"
    },
    "course35":{ 
        "courseName": "کارآموزی",
        "unit": "1",
        "type": "practical_course"
    },
    "course36":{ 
        "courseName": "آز شبکه",
        "unit": "1",
        "type": "practical_course"
    },
    "course37":{ 
        "courseName": "مبانی امنیت سایبری",
        "unit": "3",
        "type": "theory_course"
    },
    "course38":{ 
        "courseName": "سیستم نهفته بیدرنگ",
        "unit": "3",
        "type": "theory_course"
    },
    "course39":{ 
        "courseName": "پروژه کارشناسی",
        "unit": "2",
        "type": "practical_course"
    },
    "course40":{ 
        "courseName": "مبانی یادگیری ماشین",
        "unit": "3",
        "type": "theory_course"
    },
    "course41":{ 
        "courseName": "طراحی کامپیوتری سیستمهای دیجیتال",
        "unit": "3",
        "type": "theory_course"
    },
    "course42":{ 
        "courseName": "سیستم های عامل",
        "unit": "3",
        "type": "theory_course"
    }
}


for key, value in data.items():
    AllCourses.objects.create(courseName=value['courseName'], unit=value['unit'], type=value['type'])