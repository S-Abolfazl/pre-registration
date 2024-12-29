const error_message = 'پاسخی از سمت سرور دریافت نشد'

export default async ({ $axios, $toast, store }, inject) => {
  $axios.defaults.baseURL = store.state.server_url
  $axios.onRequest((config) => {
    if (Boolean(localStorage.getItem('token'))) {
        config.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
    }
  })

  inject(
    'reqApi',
    (url, data = {}, config = {}, getOnlyData = true, type = 'post') => {
      return new Promise((resolve, reject) => {
        switch (type) {
          case 'post':
            $axios.$post(url, data, config)
              .then((response) => {
                let check = checkResponse(response, getOnlyData, config)
                if (check.status) {
                    resolve(response.data)
                } else {
                    reject()
                }
              })
              .catch((error) => {
                checkErrorResponse(error)
                reject(error)
              })
            break
          case 'delete':
            $axios.$delete(url, { data, config })
              .then((response) => {
                let check = checkResponse(response, getOnlyData, config)
                if (check.status) {
                    resolve(check.data)
                } else {
                    reject()
                }
              })
              .catch((error) => {
                checkErrorResponse(error)
                reject()
              })
            break
          case 'put':
            $axios.$put(url, data, config)
              .then((response) => {
                let check = checkResponse(response, getOnlyData, config)
                if (check.status) {
                  resolve(check.data)
                } else {
                  reject()
                }
              })
              .catch((error) => {
                checkErrorResponse(error)
                reject()
              })
            break
          case 'patch':
            $axios.$patch(url, data)
              .then((response) => {
                let check = checkResponse(response, getOnlyData, config)
                if (check.status) {
                  resolve(check.data)
                } else {
                  reject()
                }
              })
              .catch((error) => {
                checkErrorResponse(error)
                reject()
              })
            break
          case 'get':
            let i = 0
            if (data != null) {
              for (const key in data) {
                if (i == 0) {
                  url += '?'
                }
                else {
                  url += '&'
                }
                url += `${key}=${data[key]}`
                i++
              }
            }
            $axios.$get(url)
              .then((response) => {
                let check = checkResponse(response, getOnlyData, config)
                if (check.status) {
                  resolve(check.data)
                } else {
                  reject()
                }
              })
              .catch((error) => {
                checkErrorResponse(error)
                reject()
              })
            break
        }
      })
    }
  )

  function checkResponse(response) {
    // TODO : check response.statusCode
    if (response) {
      if (response.msg == 'ok' || response.status == 200) {
        return {
          status: true,
          data: response.data,
        }
      }

      if (response.message) {
          $toast.error(response.message)
      } else {
          $toast.error(error_message)
      }

      if (response.status == 401) {
        store.dispatch('auth/error401');
      }
      return {
          status: false,
          data: [],
      }
    }
    else {
      $toast.error(error_message)
      return {
        status: false,
        data: [],
      }
    }
  }

  function checkErrorResponse(error) {
    try {
      if (error.response.data.code == "token_not_valid"){
        $axios.$post("user/refresh-token/", {
          "refresh_token" : localStorage.getItem("refresh_token")
        }).then((response) => {
          console.log("res : ", response);
          localStorage.setItem("token", response);
        })
        .catch((_) => {
          store.dispatch('auth/error401');
        });
      }
      else if (
        error &&
        error.response &&
        error.response.data &&
        error.response.data.data
      ) {
        if (typeof error.response.data.data === "object") {
          const response = error.response.data.data;
          for (const field in response) {
            if (response.hasOwnProperty(field)) {
              $toast.error(`${response[field].join(', ')}`);
            }
          }
        }
        else {
          $toast.error(error.response.data.data);
        }
      } else {
        $toast.error(error_message)
      }
    } catch (error) {}
  }
}
