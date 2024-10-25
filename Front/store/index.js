let app_name = 'سامانه پیش ثبت نام'


export const state = () => ({
  page_title: 'صفحه اصلی',
  server_url: '127.0.0.1:8000',
  // TODO
  // file_url: 'https://file.ir/',
})

export const mutations = {
  set_title(state, data) {
    if (typeof data != 'string' && data.length == 0) {
      data = app_name;
    }
    state.page_title = data;
  },
  set_logo(state, data) {
    state.logo = data;
  },
  set_app_name(state, data) {
    state.logo = data;
  },
}

export const actions = {
  setPageTitle({ commit }, title) {
    commit('set_title', title)
  },
  setLogo({ commit }, type) {
    commit('set_logo', type)
  },
  setAppName({ commit }, name) {
    commit('set_app_name', name)
  },
}
