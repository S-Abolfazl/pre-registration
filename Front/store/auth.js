export const state = () => ({
  user: null,
  action: [],
  role_id: "",
  token: '',
  refresh_token: '',
  role: {
    is_admin: false,
    is_student: false,
    is_professor: false,
    is_supporter: false,

    admin_id: '',
    student_id: '',
    professor_id: '',
    supporter_id: '',

  },
})

export const mutations = {
  set_user(state, data) {
    state.user = data
  },
  set_action(state, data) {
    state.action = data
  },
  set_role_id(state, data) {
    state.role_id = data
  },
  set_token(state, data) {
    state.token = data.token
    state.refresh_token = data.refresh_token

    localStorage.setItem('token', data.token)
    localStorage.setItem('refresh_token', data.refresh_token)
  },
  set_role(state, keys) {
    let role = { ...state.role };

    Object.keys(role).forEach(key => {
      if (typeof role[key] === 'boolean') {
        role[key] = false;
      }
    });

    keys.forEach(key => {
      role[key] = true;
    });

    state.role = role;
  },
  set_role_empty(state) {
    state.role = {
      is_admin: false,
      is_student: false,
      is_professor: false,
      is_supporter: false,
      admin_id: '',
      student_id: '',
      professor_id: '',
      supporter_id: '',
    }
  },
}

export const actions = {
  async nuxtServerInit({ _, commit, dispatch }, redirect = true) {
    return new Promise(async (res, rej) => {
      try {
        let token = localStorage.getItem('token')
        let refresh_token = localStorage.getItem('refresh_token')
        if (token) {
          await commit('set_token', {
            'token': token,
            'refresh_token': refresh_token,
           })
          await this.$reqApi(`/user/login`, { get_token: true})
            .then(async (response) => {
              await dispatch('setAction', response.user)
              await commit('set_user', response.user)
              await dispatch('setRole', response.user)
              if (response.Authorization) {
                await commit('set_token', {
                  token: response.Authorization.token,
                  refresh_token: response.Authorization.refresh_token,
                })
              }
              res()
            })
            .catch(async (error) => {
              this.$toast.error(error)
              if (redirect) {
                dispatch('error401')
              } else {
                rej()
              }
            })
        }
        else {
          if (redirect) {
            dispatch('error401')
          } else {
            rej()
          }
        }
      }
      catch (error) {
        if (redirect) {
          dispatch('error401')
        } else {
          rej()
        }
      }
    })
  },
  async login({ commit, dispatch }, data) {

    commit('set_user', data.user)
    // await dispatch('setAction', data.user.type)
    await dispatch('setRole', data.user.type)
    await commit('set_token', {
      token: data.access_token,
      refresh_token: data.refresh_token,
    });
  },
  async logout({ dispatch }) {
    this.$reqApi('/auth/logout')
    .catch((_) => {
      this.$toast.error('خطا در خروج از سیستم')
    })
    dispatch('error401')
  },
  async error401({ commit }) {
    await commit('set_action', [])
    await commit('set_user', null)
    await commit('set_role_empty')
    await commit('set_token', {
      'token': null,
      'refresh_token': null,
    })

    localStorage.clear('token')
    localStorage.clear('refresh_token')
    window.location.href = '/#/auth/login'
  },

  async setAction({ commit }, user) {
    if (Boolean(user) && Boolean(user.actions)){
      await commit('set_action', user.actions);
    }
  },
  async setUser({ commit }, user) {
    if (Boolean(user)){
      await commit('set_user', user);
    }
  },
  async setToken({ commit }, user) {
    if (Boolean(user) && Boolean(user.token) && Boolean(user.refresh_token)){
      await commit('set_token', {
        'token': user.token,
        'refresh_token': user.refresh_token,
      });
    }
  },
  async setRole({ commit }, user) {
    if (Boolean(user) && Boolean(user.roles) && Array.isArray(user.roles) && user.roles.length > 0) {
      await commit('set_role', user.roles);
      await commit('set_role_id', user.role_id);
    }
  },
}
