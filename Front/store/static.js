export const state = () => ({
  status,
  user_types,
  role_types,
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
