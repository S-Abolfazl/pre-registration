export const state = () => ({
  page_title: 'سامانه پیش ثبت نام',
  server_url: 'http://192.168.189.26:8000/',
  // TODO
  // file_url: 'https://file.ir/',
})

export const mutations = {
  set_title(state, data) {
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
