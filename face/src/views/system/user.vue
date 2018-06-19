<template>
    <div class="user">
        <Row>
            <Col span="7" class="user-left">
                <Form :label-width="80">
                    <FormItem label="用户名:" :style="{width:'300px'}">
                        <Input placeholder="请输入真实姓名" v-model="name"></Input>
                    </FormItem>
                    <FormItem label="所属部门" :style="{width:'300px'}">
                      <Col span="14">
                        <Select v-model="dptname">
                          <Option v-for="i in teams" :value="i.id" :key="i.id"></Option>
                        </Select>
                      </Col>
                    </FormItem>
                    <FormItem label="登录邮箱:" :style="{width:'300px'}">
                          <Input placeholder="请输入电子邮箱" v-model="Email3"></Input>
                    </FormItem>
                    <FormItem label="登录密码:" :style="{width:'300px'}">
                        <Input placeholder="请输入登录密码" v-model="pwd"></Input>
                    </FormItem>
                    <FormItem label="用户状态:" :style="{width:'250px'}">
                              <Col span="12">
                                 <Select v-model="stat3" style="width:80px">
                                     <Option v-for="item in typelist2" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                 </Select>
                               </Col>
                    </FormItem>
                    <FormItem label="描述:" :style="{width:'300px'}">
                        <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入员工描述" v-model="desc"></Input>
                    </FormItem>
                    <FormItem :style="{width:'300px'}">
                        <Button type="primary" :style="{float:'right'}" @click="Up">提交</Button>
                        <Button type="ghost" :style="{marginRight: '10px',float:'right'}" @click="reset">重置</Button>
                    </FormItem>
                </Form>
            </Col>
            <Col span="17" :style="{padding:'15px'}">
                <Form ref="formCustom">
                    <FormItem>
                        <Row>
                            <Col span="5">
                                <FormItem label="选择部门">
                                    <Col span="15">
                                          <Select v-model="dptname1" style="width:100px">
                                            <Option v-for="i in teams" :value="i.id" :key="i.id"></Option>
                                          </Select>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="5">
                                <FormItem label="账号状态">
                                    <Col span="14">
                                      <Select v-model="state" style="width:100px">
                                          <Option v-for="item in states" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                      </Select>
                                    </Col>
                                </FormItem>
                            </Col>

                            <Col span="5">
                                <FormItem label="邮箱地址">
                                    <Col span="15">
                                        <Input placeholder="请输入账号名称" v-model="accountname"></Input>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="9" class="btn">
                                <Button type="ghost" icon="ios-search-strong" @click="Search">搜索</Button>
                                <Button type="ghost" icon="ios-cloud-upload-outline" @click="expor">导出</Button>
                            </Col>
                        </Row>
                    </FormItem>
                </Form>
                <Row >
                    <Table :columns="columns" :data="data" ref="table" v-show="this.data.length>0"></Table>
                </Row>
                <Row :style="{marginTop: '15px'}">
                    <Page :style="{float:'right'}" :total="totalCount" size="small" :page-size="pageSize"
                     show-total show-elevator @on-change="changepage"></Page>
                </Row>
            </Col>
        </Row>
    <Modal
        v-model="modal6"
        title="用户编辑"
        width="370"
        @on-ok="submit1"
        >
          <Form :label-width="80">
              <FormItem label="用户名：" :style="{width:'250px'}">
                  <Input placeholder="请输入用户名" v-model="name2"></Input>
              </FormItem>
              <FormItem label="所属部门:" :style="{width:'250px'}">
                <Col span="15">
                    <Select v-model="dptname2">
                        <Option v-for="i in teams" :value="i.id" :key="i.id">
                            {{ i.name }}
                        </Option>
                    </Select>
                 </Col>
              </FormItem>
              <FormItem label="登录邮箱:" :style="{width:'250px'}">
                    <Input placeholder="请输入电子邮箱" v-model="Email2"></Input>
              </FormItem>
              <FormItem label="用户密码：" :style="{width:'250px'}">
                  <Input placeholder="请输入密码" v-model="pwd2"></Input>
              </FormItem>
              <FormItem label="用户状态:" :style="{width:'250px'}">
                        <Col span="12">
                           <Select v-model="stat2" style="width:80px">
                               <Option v-for="item in typelist2" :value="item.value" :key="item.value">{{ item.label }}</Option>
                           </Select>
                         </Col>
              </FormItem>
          </Form>
        </Modal>
        <Modal class="userinfo" v-model="showInfo" title="用户信息" @on-ok="confirm" @on-cancel="cancel" :closable="false">
            <Table :columns="orderColumns" :data="orderData"></Table>
        </Modal>
    </div>
</template>
<script>
    import excel from '../../libs/tableToExcel.js'
    export default {
        data() {
            return {
                modal6:false,
                showInfo: false,
                dptname:'',
                dptname1:'',
                dptname2:'',
                model7:'',
                name:'',
                name1:'',
                name2:'',
                stat:'',
                team:'',
                state:'',
                accountname:'',
                stat2:'',
                stat3:'',
                id:'',
                id2:null,
                teams: [
                     { id:'研发部',name:'研发部'},
                     { id:'运营部',name:'运营部'},
                     { id:'商务部',name:'商务部'},
                     { id:'财务部',name:'财务部'},
                     { id:'实施部',name:'实施部'}
                ],
                states:[
                  {value:'1',label:'1'},
                  {value:'2',label:'2'},
                  {value:'3',label:'3'}
                ],
                Email:'',
                Email2:'',
                Email3:'',
                dpt:'',
                dpt1:'',
                dpt2:'',
                pwd:'',
                pwd1:'',
                pwd2:'',
                desc:'',
                total: 0,
                totalCount:0,
                pageSize:8,
                ajaxHistoryData:[],
                typelist2:[
                  {value:'1',label:'1'},
                  {value:'2',label:'2'},
                  {value:'3',label:'3'}
                ],
                orderColumns: [
                    {
                        title: 'ID',
                        key:'id'
                    },
                    {
                        title: '邮箱地址',
                        key: 'mail'
                    },
                    {
                        title: '所属部门',
                        key: 'team'
                    },
                    {
                      title:'用户名',
                      key:'username'
                    }
                ],
                orderData: [],
                columns: [
                    // {
                    //     type: 'selection',
                    //     align: 'center'
                    // },
                    {
                        title: 'ID',
                        key: 'id',
                    },
                    {
                        title: '姓名',
                        key: 'username'
                    },
                    {
                        title: '账号',
                        width:160,
                        key: 'mail'
                    },
                    {
                        title: '状态',
                        key: 'status',
                        width:80
                    },
                    {
                        title: '创建时间',
                        key: 'posttime',
                        width: 150
                    },
                    {
                        title: '操作',
                        key: 'operating',
                        width: 200,
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'info',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                          let  _this = this
                                          this.$axios.get(`${this.URL_PREFIX}/v1/system/user/query/${params.row.id}`)
                                                     .then(res => {
                                                       if(res.data.code == '0'){
                                                         this.showInfo = true
                                                         //console.log(res.data.result)
                                                         this.orderData.push(res.data.result)

                                                         //动态路由跳转
                                                          // let argu = { id: params.row.id };
                                                          // this.$router.push({
                                                          //     name: 'user_info',
                                                          //     params: argu
                                                          // });
                                                       }else{

                                                       }
                                                     }).catch(error => {
                                                         console.log(error)
                                                     })
                                        }
                                    }
                                }, '详情'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                          //添加请求头
                                          // let config = {
                                          //   headers: { 'Content-Type': 'application/json' }
                                          //  };
                                           this.$axios.delete(`${this.URL_PREFIX}/v1/system/user`,{
                                               headers: { 'Content-Type': 'application/json' },
                                               data: {
                                                 id:params.row.id
                                               }
                                           }).then(res => {
                                             if(res.data.code == '0'){
                                                       setTimeout(() => {
                                                        this.getUserList()
                                                        this.$Message.success('删除成功')
                                                       },1500)
                                                   }else if(res.data.code == '10003'){
                                                     setTimeout(() => {
                                                       this.$Message.warning('删除的用户不存在')
                                                     },1500)
                                                   }else{
                                                     setTimeout(() => {
                                                      this.$Message.error('删除失败')
                                                     },1500)
                                                  }
                                           }).catch(error => {
                                             console.log(error)
                                           })
                                        }
                                    }
                                }, '删除'),
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.id = params.row.id
                                            this.modal6 = true
                                            this.$axios.get(`${this.URL_PREFIX}/v1/system/user/query/${params.row.id}`)
                                                       .then(res => {
                                                         if(res.data.code == '0'){
                                                            this.name2 = res.data.result.username
                                                            this.dptname2 = res.data.result.team
                                                            this.Email2 = res.data.result.mail
                                                         }
                                                       }).catch(error => {
                                                           console.log(error)
                                                       })

                                        }
                                    }
                                }, '编辑'),
                            ]);
                        }
                    }
                ],
                data: [],
                teams1: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'}

                ],
                teams2: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'}

                ]
            }
        },
        mounted () {
            this.getUserList();
        },
        methods: {
          /*
            获取系统用户列表
          */
           getUserList() {

             this.$axios.get(`${this.URL_PREFIX}/v1/system/user/list?page=1&size=10`).then( res => {
                   if(res.data.code == '0'){
                        //将获取的数据保存到data空数组中
                        this.data = res.data.result
                        this.ajaxHistoryData = this.data
                        this.totalCount =res.data.result.length
                        this.handleListApproveHistory()
                    }
                  }).catch(error => {
                    console.log(error)
                   })
             },
             /*
               搜索查询列表
             */
           Search() {
               //this.transform()
               //this.loading = true
               //http://39.108.165.149:7006
               this.$axios.get(`${this.URL_PREFIX}/v1/system/user/list?page=1&size=10&team=${this.dptname1}&status=${this.state}&keyword=${this.accountname}`)
                   .then( res=> {
                     if(res.data.code == '0'){
                       //this.loading = false
                      //console.log(res.data.result)
                       if(res.data.result.length == 0){
                         setTimeout(() => {
                           this.loading = false
                           this.$Message.warning('未搜索到匹配信息,请重试!')
                           this.data = []
                           this.totalCount = 0
                         },1500)
                       }else {
                          //this.loading = false
                          setTimeout(() => {
                            this.loading = false
                            this.data = res.data.result
                            this.totalCount = res.data.result.length
                            this.ajaxHistoryData = this.data
                            this.handleListApproveHistory()
                          },1500)
                       }
                     }else{
                       setTimeout(() => {
                             this.$Message.warning('未搜索到匹配信息,请重试!')
                             this.data = []
                       },1500)


                     }
                   }).catch( error => {
                     console.log(error)
                   })
           },
             /*
                导出
             */
             expor(){
                 this.$axios.get(`${this.URL_PREFIX}/v1/system/user/export?page=1&size=10`).then(res => {
                     if(res.data.code == '0'){
                       setTimeout(() => {
                          excel(this.columns, this.$refs.table, '用户信息表.xls');
                          this.$Message.success('导出成功!')
                       },1500)
                     }else{
                       setTimeout(() => {
                          this.$Message.warning('导出失败!')
                       },1500)
                     }
                 }).catch(error => {
                     console.log(error)
                 })
             },
             /*
              系统用户添加
             */
             addNewUser() {
               if(this.name ==''||this.name == null){
                 setTimeout(()=> {
                   this.$Message.warning('请输入您的用户名!')
                 },600)
               }else if(this.dptname ==''||this.dptname == null){
                 setTimeout(()=> {
                   this.$Message.warning('请选择所属部门!')
                 },600)
               }else if(this.Email3 ==''||this.Email3 == null){
                 setTimeout(()=> {
                   this.$Message.warning('请输入您的登录邮箱!')
                 },600)
               }else if(this.pwd ==''||this.Email3 == null){
                 setTimeout(()=> {
                   this.$Message.warning('请输入您的登录密码!')
                 },600)
               }else if(this.stat3 ==''||this.stat3 == null){
                 setTimeout(()=> {
                   this.$Message.warning('请选择用户状态!')
                 },600)
               }else{
                 this.transform()
                 this.$axios.post(`${this.URL_PREFIX}/v1/system/user`,{
                     team:this.dptname,
                     mail:this.Email3,
                     username:this.name,
                     status:parseInt(this.stat3),
                     passwd:this.pwd
                 }).then(res => {
                     if(res.data.code == '0'){
                         setTimeout(() => {
                           this.getUserList()
                           this.$Message.success('新增用户成功')
                           this.reset()
                         },1500)
                     }else{
                       setTimeout(() => {
                         this.$Message.error('新增用户失败')
                         this.reset()
                       },1500)
                     }
                 }).catch(error => {
                     console.log(error)
                 })
               }
             },
             //系统用户编辑
             compiles() {
               this.transform()
               this.$axios.put(`${this.URL_PREFIX}/v1/system/user`,{
                   id:parseInt(this.id),
                   team:this.dptname2,
                   mail:this.Email2,
                   username:this.name2,
                   status:parseInt(this.stat2),
                   passwd:this.pwd2
               }).then(res => {
                   if(res.data.code == '0'){
                     setTimeout(() => {
                        this.getUserList()
                        this.$Message.success('编辑成功!')
                        this.reset2()
                     },1500)
                   }else{
                     setTimeout(() => {
                       this.$Message.error('编辑失败!')
                       this.reset2()
                     },1500)
                   }
               }).catch(error => {
                   console.log(error)
               })
             },
             transform() {
               if(this.dptname =='研发部'||this.dptname1 =='研发部'||this.dptname2 =='研发部'){
                 this.dptname = 0
                 this.dptname1 = 0
                 this.dptname2 = 0
               }else if(this.dptname =='财务部'||this.dptname1 =='财务部'||this.dptname2 =='财务部'){
                 this.dptname = 1
                 this.dptname1 = 1
                 this.dptname2 = 1
               }else if(this.dptname =='运营部'||this.dptname1 =='运营部'||this.dptname2 =='运营部'){
                 this.dptname = 2
                 this.dptname1 = 2
                 this.dptname2 = 2
               }else if(this.dptname =='商务部'||this.dptname1 =='商务部'||this.dptname2 =='商务部'){
                 this.dptname = 3
                 this.dptname1 = 3
                 this.dptname2 = 3
               }else if(this.dptname =='实施部'||this.dptname1 =='实施部'||this.dptname2 =='实施部'){
                 this.dptname = 4
                 this.dptname1 = 4
                 this.dptname2 = 4
               }
             },
             //提交系统用户添加操作
             Up() {
                this.addNewUser()
             },
             confirm() {
               this.orderData.length = 0
             },
             cancel() {
               this.orderData.length = 0
             },
             /*
                分页逻辑处理
             */
           handleListApproveHistory(){
                // 初始化显示，小于每页显示条数，全显，大于每页显示条数，取前每页条数显示
                if(this.data < this.pageSize){
                    this.data = this.ajaxHistoryData;
                }else{
                    this.data = this.ajaxHistoryData.slice(0,this.pageSize);
                }
            },
            /*
              页码跳转
            */
             changepage(index){
                var _start = ( index - 1 ) * this.pageSize;
                var _end = index * this.pageSize;
                this.data = this.ajaxHistoryData.slice(_start,_end);
            },
            /*
              确认提交添加新用户
            */
            submit() {
              this.addNewUser()
            },
            /*
              提交用户编辑结果
            */
            submit1() {
                this.compiles()
            },
            /*
              重置输入记录
            */
            reset() {
                this.name=''
                this.dptname = ''
                this.pwd = ''
                this.dpt = ''
                this.desc = ''
                this.stat3=''
                this.Email3=''
            },
            //清空编辑记录
            reset2() {
              this.name2 = ''
              this.pwd2 = ''
              this.dpt2 = ''
              this.stat2=''
              this.Email2=''
            },
            /*
              提交
            */
            up() {

            }
        }
    }
</script>
<style lang="scss">
    .user,.ivu-row{
        height: 100%;
    }
    .user .user-left{
        height: 100%;
        padding: 15px;
        border-right: 1px solid #e5e9ee;
    }
    .btn{
      Button{
        margin-left: 18px;
      }
    }

    .ivu-modal-content {
       width: 700px;
     }


</style>
