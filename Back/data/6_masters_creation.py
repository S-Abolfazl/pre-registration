from master.models import Master

def add_masters():
    masters = [
    {
      "model": "appname.master",
      "pk": "550e8400-e29b-41d4-a716-446655440000",
      "fields": {
        "name": "رامک قوامی زاده میبدی",
        "education": "دکتری",
        "specialization": "فرانسه، مهندسی کامپیوتر نرم افزار",
        "description": "خوب کلا حضور غیاب نمیکنن و فکر نمیکنم خیلی براشون اهمیت داشته باشه ولی خیلی حساس به اینکه دانشجو وسط کلاس پاشه بره مخصوصا اگر دیر هم اومده باشه به دیر اومدن حساس خودشون",
        "department": "مهندسی و علوم کامپیوتر",
        "mobile_number": "29904183",
        "email": "r-gavami@sbu.ac.ir",
        "field": "نرم افزار و سامانه های شناختی",
        "rate": 4
      }
    },
    {
      "model": "appname.master",
      "pk": "660e7400-e21b-42d4-a756-556655440111",
      "fields": {
        "name": "صادق علی اکبری",
        "education": "دکتری",
        "specialization": "دانشگاه صنعتی شریف",
        "description": "اوایل ترم همزمان که خودشون می نوشتن، درس میدادن و بعد بهمون زمان میدادن که یادداشت کنیم. بعد از مدتی خودشون نوت هاشون رو در اختیارمون گذاشتن که به نظرم روش بهتری بود. تقریبا روند تدریسشون با کتاب گسسته بیات همخوانی داره و اکثر بچه های ما با این کتاب پیش رفتن. مشکل اساسی که با استاد دارم، زیاد از حد صحبت کردنشون وسط درسه. اینقدر این اتفاق افتاده که بعضی حرف هاشون بین بچه ها تبدیل به جوک شده!",
        "department": "مهندسی و علوم کامپیوتر",
        "mobile_number": "29904169",
        "email": "s_aliakbari@gmail.com",
        "field": "نرم افزار و سامانه های اطلاعاتی",
        "rate": 5
      }
    },
    {
      "model": "appname.master",
      "pk": "770e9400-e22b-45d5-a866-667755440222",
      "fields": {
        "name": "فرشاد صفايی سمنانی",
        "education": "دکتری",
        "specialization": "فرانسه، مهندسی کامپیوتر نرم افزار",
        "description": "خوب کلا حضور غیاب نمیکنن و فکر نمیکنم خیلی براشون اهمیت داشته باشه ولی خیلی حساس به اینکه دانشجو وسط کلاس پاشه بره مخصوصا اگر دیر هم اومده باشه به دیر اومدن حساس خودشون",
        "department": "مهندسی و علوم کامپیوتر",
        "mobile_number": "29904183",
        "email": "f_safai@gmail.com",
        "field": "معماری کامپیوتر و شبکه",
        "rate": 1
      }
    },
    {
        "model": "appname.master",
        "pk": "550e8400-e29b-41d4-a716-446655440000",
        "fields": {
          "name": "رامک قوامی زاده میبدی",
          "education": "دکتری",
          "specialization": "فرانسه، مهندسی کامپیوتر نرم افزار",
          "description": "خوب کلا حضور غیاب نمیکنن و فکر نمیکنم خیلی براشون اهمیت داشته باشه ولی خیلی حساس به اینکه دانشجو وسط کلاس پاشه بره مخصوصا اگر دیر هم اومده باشه به دیر اومدن حساس خودشون",
          "department": "مهندسی و علوم کامپیوتر",
          "mobile_number": "29904183",
          "email": "r-gavami@sbu.ac.ir",
          "field": "نرم افزار و سامانه های شناختی",
          "rate": 4
        }
      },
      {
        "model": "appname.master",
        "pk": "770e9400-e22b-45d5-a866-667755440222",
        "fields": {
          "name": "فرشاد صفايی سمنانی",
          "education": "دکتری",
          "specialization": "فرانسه، مهندسی کامپیوتر نرم افزار",
          "description": "خوب کلا حضور غیاب نمیکنن و فکر نمیکنم خیلی براشون اهمیت داشته باشه ولی خیلی حساس به اینکه دانشجو وسط کلاس پاشه بره مخصوصا اگر دیر هم اومده باشه به دیر اومدن حساس خودشون",
          "department": "مهندسی و علوم کامپیوتر",
          "mobile_number": "29904183",
          "email": "f_safai@gmail.com",
          "field": "معماری کامپیوتر و شبکه",
          "rate": 1
        }
      }
  ]
    for master_data in masters:
        master, created = Master.objects.get_or_create(**master_data['fields'])
        print(f"Master {master.name} created successfully.")
        
add_masters()
  