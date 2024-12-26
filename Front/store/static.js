export const state = () => ({
  status,
  user_types,
  role_types,
  course_type,
})

let status = [
  { text: 'فعال', value: 'active' },
  { text: 'غیر فعال', value: 'hidden' },
]

let user_types = [
  { text: 'دانشجو', value: 'student' },
  { text: 'معاون آموزشی', value: 'academicassistant' },
  // { text: 'ادمین', value: 'admin' },
  // { text: 'پشتیبان', value: 'support' },
]

let role_types = {
  student: 'دانشجو',
  academicassistant: 'معاون آموزشی',
  admin: 'ادمین',
  support: 'پشتیبان',
}

let course_type = {
  theory_course: "اختصاصي",
  public_course: "عمومي",
  basic_course: "پايه",
  practical_course: "عملی",
  elective_course: "اختياري",
}
