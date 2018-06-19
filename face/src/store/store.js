import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state:{
      // admininfo : {
      //   avatar: ''
      // }
      user:{},
      token:null,
      title:''
  },
  getters:{

  },
  mutations:{
    // saveAdminInfo(state, adminInfo){
  	// 	state.adminInfo = adminInfo;
  	// },
    setLogin: (state,data) => {
       localStorage.token = data;
       state.token = data
    },
    LoginOut: (state) => {
      localStorage.removeItem('token');
      state.token = null
    }
  },
  actions:{

  }

})
