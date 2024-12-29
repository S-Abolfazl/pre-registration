import json
from student.models import EducationalChart

data = {
    "chart1":{
        "year": "400",
        "type": "even",
        "units": ["16", "18", "17", "17", "18", "18", "17", "19"],
        "term1":["زبان خارجی", 
        "مهارت های کاربردی کامپیوتر",
        "مبانی کامپیوتر و برنامه سازی",
        "ریاضی 1",
        "فیزیک 1",
        "فارسی"],
        "term2":["دانش خانواده", 
        "برنامه سازی پیشرفته",
        "ریاضی 2",
        "معادلات دیفرانسیل",
        "مدارهای الکتریکی و الکترونیکی",
        "فیزیک 2",
        "آز فیزیک 2"],
        "term3":["ریاضیات گسسته", 
        "مدارهای منطقی",
        "جبر خطی",
        "سیگنالها و سیستمها",
        "مدارهای مجتمع دیجیتال",
        "گروه معارف"],
        "term4":["زبان تخصصی", 
        "ساختمان داده ها",
        "نظریه زبانها و ماشینها",
        "آزمایشگاه مدارهای منطقی و معماری کامپیوتر",
        "معماری کامپیوتر",
        "آمار و احتمالات مهندسی",
        "گروه معارف"],
        "term5":["مدرسه تکمیلی", 
        "طراحی الگوریتم ها",
        "تحلیل و طراحی سیستم ها",
        "هوش مصنوعی و سیستم های خبره",
        "اصول طراحی کامپایلر",
        "سیستم های عامل",
        "تربیت بدنی 1",
        "گروه معارف"],
        "term6":["روش پژوهش و ارائه", 
        "پایگاه داده ها",
        "مهندسی نرم افزار",
        "شبکه های کامپیوتری",
        "آزمایشگاه سیستم های عامل",
        "آزمایشگاه ریزپردازنده",
        "ریزپردازنده و مدارهای واسط",
        "گروه معارف"],
        "term7":["کارآموزی", 
        "تربیت بدنی 2",
        "اختیاری",
        "آزمایشگاه شبکه های کامپیوتری",
        "مبانی امنیت سایبری",
        "اختیاری",
        "مبانی سیستم های نهفته و بیدرنگ",
        "گروه معارف"],
        "term8":["پروژه کارشناسی",
        "اختیاری",
        "مبانی یادگیری ماشین",
        "طراحی کامپیوتری سیستم های دیجیتال",
        "اختیاری",
        "اختیاری",
        "گروه معارف"]
    },
    "chart2":{
        "year": "400",
        "type": "odd",
        "units": ["16", "18", "20", "18", "18", "16", "18", "16"],
        "term1":["زبان خارجی", 
        "مهارت های کاربردی کامپیوتر",
        "مبانی کامپیوتر و برنامه سازی",
        "ریاضی 1",
        "فیزیک 1",
        "فارسی"],
        "term2":["دانش خانواده", 
        "برنامه سازی پیشرفته",
        "ریاضیات گسسته", 
        "مدارهای منطقی",
        "معادلات دیفرانسیل",
        "فیزیک 2",
        "آز فیزیک 2"],
        "term3":["زبان تخصصی", 
        "ساختمان داده ها",
        "نظریه زبانها و ماشینها",
        "معماری کامپیوتر",
        "آزمایشگاه مدارهای منطقی و معماری کامپیوتر",
        "ریاضی 2",
        "مدارهای الکتریکی و الکترونیکی",
        "گروه معارف"],
        "term4":["تربیت بدنی 1",
        "هوش مصنوعی و سیستم های خبره", 
        "سیستم های عامل",
        "جبر خطی",
        "سیگنالها و سیستمها",
        "مدارهای مجتمع دیجیتال",
        "گروه معارف"],
        "term5":["روش پژوهش و ارائه",
        "پایگاه داده ها",
        "ریزپردازنده و مدارهای واسط",
        "آزمایشگاه ریزپردازنده",
        "آزمایشگاه سیستم های عامل", 
        "شبکه های کامپیوتری",
        "آمار و احتمالات مهندسی",
        "گروه معارف"],
        "term6":["مدرسه تکمیلی",
        "طراحی الگوریتم ها",
        "تحلیل و طراحی سیستم ها",
        "اصول طراحی کامپایلر",
        "اختیاری",
        "آزمایشگاه شبکه های کامپیوتری",
        "تربیت بدنی 2",
        "گروه معارف"],
        "term7":["کارآموزی", 
        "مهندسی نرم افزار",
        "مبانی یادگیری ماشین",
        "اختیاری",
        "طراحی کامپیوتری سیستم های دیجیتال",
        "اختیاری",
        "گروه معارف"],
        "term8":["پروژه کارشناسی",
        "اختیاری",
        "مبانی امنیت سایبری",
        "مبانی سیستم های نهفته و بیدرنگ",
        "اختیاری",
        "گروه معارف"]
    }
}

for chart_name, chart_data in data.items():
    EducationalChart.objects.get_or_create(
        year=chart_data["year"],
        type=chart_data["type"],
        units=chart_data.get("units", []),
        term1=chart_data.get("term1", []),
        term2=chart_data.get("term2", []),
        term3=chart_data.get("term3", []),
        term4=chart_data.get("term4", []),
        term5=chart_data.get("term5", []),
        term6=chart_data.get("term6", []),
        term7=chart_data.get("term7", []),
        term8=chart_data.get("term8", [])
    )