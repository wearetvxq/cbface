<template>
    <div class="layout">
        <Layout :style="{height: '100%'}">
            <Header :style="{background: '#3f8d76', padding: '0 10px'}">
                <img src="../assets/images/logo.png" class="layout-logo" />
                <div class="layout-quit">
                    <Icon type="person" class="person"></Icon>
                    <span>admin</span>
                    <div @click="logout">
                      <Icon type="power" class="power"></Icon>
                    </div>
                </div>
                <Modal
                  v-model="modal6"
                  title="提示"
                  :loading="loading"
                  @on-ok="asyncOK"
                  @on-cancel="cancel">
                  <p>你确定要登出该账户吗?</p>
              </Modal>
            </Header>
            <Layout :style="{height: '100%'}">
                <Sider hide-trigger :style="{background: '#ebf0f6', height: '100%'}">
                    <Menu active-name="/home" :style="{background: '#ebf0f6'}" theme="light" width="auto" :open-names="['1']" @on-select="changeMenu">
                        <MenuItem name="/home">
                            <Icon type="home"></Icon>
                            <span>首页</span>
                        </MenuItem>
                        <MenuItem name="/attendance/index">
                            <Icon type="calendar"></Icon>
                            <span>考勤管理</span>
                        </MenuItem>
                        <MenuItem name="/visitors/index">
                            <Icon type="clipboard"></Icon>
                            <span>访客日志</span>
                        </MenuItem>
                        <MenuItem name="/monitor/index">
                            <Icon type="monitor"></Icon>
                            <span>监控画面</span>
                        </MenuItem>
                        <Submenu name="5">
                            <template slot="title">
                                <Icon type="gear-b"></Icon>
                                系统设置
                            </template>
                            <MenuItem name="/system/user">用户管理</MenuItem>
                            <MenuItem name="/system/employee">员工管理</MenuItem>
                            <MenuItem name="/system/tment">部门管理</MenuItem>
                            <MenuItem name="/system/access">权限管理</MenuItem>
                            <MenuItem name="/system/attendance">考勤设置</MenuItem>
                        </Submenu>
                    </Menu>
                </Sider>
                <Layout>
                    <Breadcrumb>
                        <BreadcrumbItem>{{$route.meta.title}}</BreadcrumbItem>
                    </Breadcrumb>
                    <Content :style="{padding: '0px', minHeight: '280px', background: '#fff'}">
                        <router-view></router-view>
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>
<script>
    export default {
        data() {
          return {
             loading:true,
             modal6: false
          }
        },
        methods: {
            changeMenu (active) {
                this.$router.push({path: active});
            },
            logout() {
               this.modal6 = true
            },
            asyncOK() {
                setTimeout(()=> {
                    this.model6=false
                    this.$store.commit('LoginOut')
                    this.$router.push('/login')
                    this.$Notice.success({
                      title: '消息提示',
                      render: h => {
                          return h('span', [
                              '用户登出 ',
                              h('a', '成功'),
                          ])
                      }
                    })
                },2000)
            },
            cancel() {
              this.modal6 = false;
            }
        }
    }
</script>
<style scoped>
.layout{
    background: #f5f7f9;
    position: relative;
    height: 100%;
}
.layout-logo{
    width: 260px;
    height: 58px;
    margin-top: 2px;
    float: left;
}
.layout .layout-quit{
    width: 140px;
    height: 35px;
    line-height: 35px;
    color: #FFF;
    float: right;
    border-radius: 100px;
    margin-top: 15px;
    border: 1px solid #58b39c;
    position: relative;
}
.layout .layout-quit .power{
    font-size: 20px;
    color: #FFF;
    position: absolute;
    right: 10px;
    top: 7px;
}
.layout .layout-quit .person{
    font-size: 20px;
    color: #FFF;
    position: absolute;
    left: 10px;
    top: 7px;
}
.layout .layout-quit span{
    padding-left: 30px;
}
.ivu-breadcrumb{
    margin: 0;
    height: 45px;
    line-height: 45px;
    padding: 0 15px;
    border-bottom: 1px solid #e5e9ee;
    background-color: #f3f6fb;
}
.ivu-breadcrumb>span:last-child{
    font-size: 12px;
    font-weight: 600;
    color: #495060;
}
.ivu-menu-vertical .ivu-menu-item{
    padding: 12px 24px;
}
.ivu-menu-light.ivu-menu-vertical .ivu-menu-item-active:not(.ivu-menu-submenu){
    background-color: #d7deea;
}
.ivu-layout,.ivu-layout-content{
        height: 100%;
}
</style>
