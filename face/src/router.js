import main from './views/main.vue';
export const login = {
    path: '/login',
    name: 'login',
    meta: {
        title: '登录'
    },
    component: (resolve) => require(['./views/login.vue'], resolve)
}

export const homeRouter = {
    path: '/',
    name: 'otherRouter',
    redirect: '/home',
    component: main,
    children: [
        { path: 'home', title: {i18n: 'home'}, name: 'home_index',meta:{title:'首页',requireAuth:true},component: resolve => { require(['./views/home/home.vue'], resolve); } },
    ]
};

export const attendanceRouter = {
    path: '/attendance',
    name: 'attendanceRouter',
    component: main,
    children: [
        { path: 'index', title: {i18n: 'attendance'}, name: 'attendance_index',meta:{title:'考勤管理',requireAuth:true},component: resolve => { require(['./views/attendance/index.vue'], resolve); } },
        { path: 'info/:id', title: {i18n: 'attendance'}, name: 'attendance_info',meta:{title:'考勤管理详情',requireAuth:true}, component: resolve => { require(['./views/attendance/info.vue'], resolve); } },
    ]
};

export const monitorRouter = {
    path: '/monitor',
    name: 'monitorRouter',
    component: main,
    children: [
        { path: 'index', title: {i18n: 'monitor'}, name: 'monitor_index',meta:{title:'监控画面',requireAuth:true}, component: resolve => { require(['./views/monitor/index.vue'], resolve); } },
    ]
};

export const systemRouter = {
    path: '/system',
    name: 'systemRouter',
    meta:{requireAuth:true},
    component: main,
    children: [
        { path: 'user', title: {i18n: 'system'}, name: 'systemc_index',meta:{title:'用户管理',requireAuth:true}, component: resolve => { require(['./views/system/user.vue'], resolve); } },
        { path: 'employee', title: {i18n: 'system'}, name: 'systemc_index',meta:{title:'员工管理',requireAuth:true}, component: resolve => { require(['./views/system/employee.vue'], resolve); } },
        { path: 'tment', title: {i18n: 'system'}, name: 'systemc_index',meta:{title:'部门管理',requireAuth:true}, component: resolve => { require(['./views/system/tment.vue'], resolve); } },
        { path: 'access', title: {i18n: 'system'}, name: 'systemc_index',meta:{title:'权限管理',requireAuth:true}, component: resolve => { require(['./views/system/access.vue'], resolve); } },
        { path: 'attendance', title: {i18n: 'system'}, name: 'systemc_index',meta:{title:'考勤设置',requireAuth:true}, component: resolve => { require(['./views/system/attendance.vue'], resolve); } }
    ]
};

export const visitorsRouter = {
    path: '/visitors',
    name: 'visitorsRouter',
    component: main,
    children: [
        { path: 'index', title: {i18n: 'monitor'}, name: 'visitors_index',meta:{title:'访客日志',requireAuth:true}, component: resolve => { require(['./views/visitors/index.vue'], resolve); } },
    ]
}

export const routers = [
    login,
    homeRouter,
    attendanceRouter,
    monitorRouter,
    systemRouter,
    visitorsRouter
];
