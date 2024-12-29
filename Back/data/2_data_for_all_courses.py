import json
from course.models import AllCourses

data = {
    "course1":{ 
        "courseName": "زبان خارجی",
        "unit": "3",
        "type": "public_course"
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
        "courseName": "مدارهای الکتریکی و الکترونیکی",
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
        "courseName": "ریاضیات گسسته",
        "unit": "3",
        "type": "theory_course"
    },
    "course13":{ 
        "courseName": "مدارهای منطقی",
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
        "courseName": "مدارهای مجتمع دیجیتال",
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
        "courseName": "آزمایشگاه مدارهای منطقی و معماری کامپیوتر",
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
        "courseName": "طراحی الگوریتم ها",
        "unit": "3",
        "type": "theory_course"
    },
    "course25":{ 
        "courseName": "تحلیل و طراحی سیستم ها",
        "unit": "3",
        "type": "theory_course"
    },
    "course26":{ 
        "courseName": "هوش مصنوعی و سیستم های خبره",
        "unit": "3",
        "type": "theory_course"
    },
    "course27":{ 
        "courseName": "اصول طراحی کامپایلر",
        "unit": "3",
        "type": "theory_course"
    },
    "course28":{ 
        "courseName": "روش پژوهش و ارائه",
        "unit": "2",
        "type": "theory_course"
    },
    "course29":{ 
        "courseName": "پایگاه داده ها",
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
        "courseName": "آزمایشگاه سیستم های عامل",
        "unit": "1",
        "type": "practical_course"
    },
    "course33":{ 
        "courseName": "آزمایشگاه ریزپردازنده",
        "unit": "1",
        "type": "practical_course"
    },
    "course34":{ 
        "courseName": "ریزپردازنده و مدارهای واسط",
        "unit": "3",
        "type": "theory_course"
    },
    "course35":{ 
        "courseName": "کارآموزی",
        "unit": "1",
        "type": "practical_course"
    },
    "course36":{ 
        "courseName": "آزمایشگاه شبکه های کامپیوتری",
        "unit": "1",
        "type": "practical_course"
    },
    "course37":{ 
        "courseName": "مبانی امنیت سایبری",
        "unit": "3",
        "type": "theory_course"
    },
    "course38":{ 
        "courseName": "مبانی سیستم های نهفته و بیدرنگ",
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
        "courseName": "طراحی کامپیوتری سیستم های دیجیتال",
        "unit": "3",
        "type": "theory_course"
    },
    "course42":{ 
        "courseName": "سیستم های عامل",
        "unit": "3",
        "type": "theory_course"
    },
    "course43":{ 
        "courseName": "تربیت بدنی 1",
        "unit": "1",
        "type": "public_course"
    },
    "course44":{ 
        "courseName": "تربیت بدنی 2",
        "unit": "1",
        "type": "public_course"
    },
    "course45":{ 
        "courseName": "گروه معارف",
        "unit": "2",
        "type": "public_course"
    },
    "course46":{ 
        "courseName": "دانش خانواده",
        "unit": "2",
        "type": "public_course"
    },
    "course47":{ 
        "courseName": "فارسی",
        "unit": "3",
        "type": "public_course"
    },
    "course48":{ 
        "courseName": "اختیاری",
        "unit": "3",
        "type": "elective_course"
    },
    "course49":{
        "courseName": "اصول مدیریت و برنامه ریزی راهبردی فناوری اطلاعات",
        "unit": "3",
        "type": "elective_course"
    },
    "course50":{ 
        "courseName": "سیستم های اطلاعات مدیریت",
        "unit": "3",
        "type": "elective_course"
    },
    "course51":{ 
        "courseName": "کارگاه برنامه نویسی مت لب",
        "unit": "1",
        "type": "elective_course"
    },
    "course52":{ 
        "courseName": "مهندسی اینترنت",
        "unit": "3",
        "type": "elective_course"
    },
    "course53":{ 
        "courseName": "هم طراحی سخت افزار- نرم افزار",
        "unit": "3",
        "type": "elective_course"
    },
    "course54":{ 
        "courseName": "طراحی بازی های رایانه ای",
        "unit": "3",
        "type": "elective_course"
    },
    "course55":{ 
        "courseName": "مبانی رمزنگاری",
        "unit": "3",
        "type": "elective_course"
    },
    "course56":{ 
        "courseName": "مبانی بینائی کامپیوتر",
        "unit": "3",
        "type": "elective_course"
    },
    "course57":{ 
        "courseName": "آزمایشگاه پایگاه داده",
        "unit": "1",
        "type": "elective_course"
    },
    "course58":{ 
        "courseName": "مبانی اینترنت اشیا",
        "unit": "3",
        "type": "elective_course"
    },
    "course59":{ 
        "courseName": "مبانی داده کاوی",
        "unit": "3",
        "type": "elective_course"
    },
    "course60":{ 
        "courseName": "تظریه و الگوریتم های گراف",
        "unit": "3",
        "type": "elective_course"
    },
}


for key, value in data.items():
    AllCourses.objects.get_or_create(courseName=value['courseName'], unit=value['unit'], type=value['type'])