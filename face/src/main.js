import Vue from 'vue';
import iView from 'iview';
import VueRouter from 'vue-router';
import { routers } from './router';
import { store } from './store/store'
import Axios from 'axios'
import Vuex from 'vuex';
import Util from './libs/util';
import App from './app.vue';
import 'iview/dist/styles/iview.css';

import VueI18n from 'vue-i18n';
import Locales from './locale';
import zhLocale from 'iview/src/locale/lang/zh-CN';
import enLocale from 'iview/src/locale/lang/en-US';
import '../theme/index.less';
import echarts from 'echarts';

Vue.use(VueRouter);

//axios全局引用
Vue.prototype.$axios = Axios

//接口地址
if (process.env.NODE_ENV !== 'development') {
   Vue.prototype.URL_PREFIX = 'http://127.0.0.1:81'
 } else {
   Vue.prototype.URL_PREFIX = 'http://127.0.0.1:81'
 }


Vue.use(Vuex);
Vue.use(VueI18n);
Vue.use(iView);

//按需引入 减少文件体积
import { Button, Table, FormItem, Page, Select, Upload, CheckboxGroup, Modal} from 'iview';
Vue.component('Button', Button);
Vue.component('Table', Table);
Vue.component('FormItem', FormItem);
Vue.component('Page', Page);
Vue.component('Select', Select);
Vue.component('Upload', Upload);
Vue.component('CheckboxGroup', CheckboxGroup);
Vue.component('Modal', Modal);

// 自动设置语言
const navLang = navigator.language;
const localLang = (navLang === 'zh-CN' || navLang === 'en-US') ? navLang : false;
const lang = window.localStorage.getItem('language') || localLang || 'zh-CN';

Vue.config.lang = lang;

// 多语言配置
const locales = Locales;
const mergeZH = Object.assign(zhLocale, locales['zh-CN']);
const mergeEN = Object.assign(enLocale, locales['en-US']);
Vue.locale('zh-CN', mergeZH);
Vue.locale('en-US', mergeEN);


// 路由配置
const RouterConfig = {
    mode: 'history',
    routes: routers
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    Util.title(to.meta.title);
    next();
});

//页面刷新时store.token会被清空,需重新赋值token

if(window.localStorage.getItem('token')){
    store.commit('setLogin', window.localStorage.getItem('token'))
}

//路由拦截 实现用户登录权限控制

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    Util.title(to.meta.title);
    if (to.matched.some(res => res.meta.requireAuth)) {// 判断是否需要登录权限
      if (store.state.token) {// 判断是否登录
        next();
      }else {
        // 没登录则跳转到登录界面
          next({
          path: '/login',
          query: {redirect: to.fullPath}
        })

      }
  }else{
    next()
  }
});

router.afterEach(() => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});
new Vue({
    el: '#app',
    router: router,
    store: store,
    render: h => h(App)
});
