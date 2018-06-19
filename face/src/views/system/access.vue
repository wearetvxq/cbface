<template>
    <div class="tment">
        <Row>
            <Col span="7" class="tment-left">
                <Form :label-width="60">
                    <FormItem label="菜单名称" :style="{width:'300px'}">
                        <Input placeholder="请输入权限名称" v-model="a_name"></Input>
                    </FormItem>
                    <FormItem label="菜单路由" :style="{width:'300px'}">
                        <Input placeholder="请输入权限路由" v-model="a_router"></Input>
                    </FormItem>
                    <FormItem label="菜单状态" :style="{width:'300px'}">
                        <Select v-model="a_stat">
                           <Option v-for="i in teams2" :value="i.id" :key="i.id">
                                {{ i.name }}
                            </Option>
                        </Select>
                    </FormItem>
                    <FormItem label="菜单类型" :style="{width:'300px'}">
                        <Select v-model="a_type">
                           <Option v-for="i in teams3" :value="i.id" :key="i.id">
                                {{ i.name }}
                            </Option>
                        </Select>
                    </FormItem>
                    <FormItem label="父菜单ID" :style="{width:'300px'}">
                        <Select v-model="a_id">
                           <Option v-for="i in teams4" :value="i.id" :key="i.id">
                                {{ i.name }}
                            </Option>
                        </Select>
                    </FormItem>
                    <FormItem label="菜单等级" :style="{width:'300px'}">
                        <Select v-model="a_level">
                           <Option v-for="i in teams1" :value="i.id" :key="i.id">
                                {{ i.name }}
                            </Option>
                        </Select>
                    </FormItem>
                    <FormItem label="菜单描述" :style="{width:'300px'}">
                        <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入权限描述" v-model="desc"></Input>
                    </FormItem>
                    <FormItem :style="{width:'300px'}">
                        <Button type="primary" :style="{float:'right'}" @click="submit">提交</Button>
                        <Button type="ghost" :style="{marginRight: '10px',float:'right'}" @click="reset">重置</Button>
                    </FormItem>
                </Form>
            </Col>
            <Col span="17" :style="{padding:'15px'}">
                <Form ref="formCustom">
                    <FormItem>
                        <Row>
                            <Col span="5">
                                <FormItem label="权限状态">
                                    <Col span="14">
                                        <Select v-model="accessState">
                                           <Option v-for="i in teams4" :value="i.id" :key="i.id">
                                                {{ i.name }}
                                            </Option>
                                        </Select>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="6">
                                <FormItem label="权限名称">
                                    <Col span="15">
                                        <Input v-model="accessName" placeholder="请输入权限名称"></Input>
                                    </Col>
                                </FormItem>
                            </Col>
                            <Col span="5">
                                <Button type="ghost" icon="ios-search-strong" @click="Search">搜索</Button>
                            </Col>
                        </Row>
                    </FormItem>
                </Form>
                <Row>
                    <Table :columns="columns1" :data="data1" v-show="this.data1.length>0"></Table>
                </Row>
                <Row :style="{marginTop: '15px'}">
                    <Page :style="{float:'right'}" :total="totalCount" size="small" :page-size="pageSize"
                     show-total show-elevator @on-change="changepage"></Page>
                </Row>
            </Col>
        </Row>
        <Modal
            v-model="modal6"
            title="编辑权限"
            width="370"
            @on-ok="submit1"
         >
         <Form :label-width="60">
             <FormItem label="菜单名称" :style="{width:'300px'}">
                 <Input placeholder="请输入权限名称" v-model="a_name1"></Input>
             </FormItem>
             <FormItem label="菜单路由" :style="{width:'300px'}">
                 <Input placeholder="请输入权限路由" v-model="a_router1"></Input>
             </FormItem>
             <FormItem label="菜单状态" :style="{width:'300px'}">
                 <Select v-model="a_stat1">
                    <Option v-for="i in teams2" :value="i.id" :key="i.id">
                         {{ i.name }}
                     </Option>
                 </Select>
             </FormItem>
             <FormItem label="菜单类型" :style="{width:'300px'}">
                 <Select v-model="a_type1">
                    <Option v-for="i in teams3" :value="i.id" :key="i.id">
                         {{ i.name }}
                     </Option>
                 </Select>
             </FormItem>
             <FormItem label="父菜单ID" :style="{width:'300px'}">
                 <Select v-model="a_id1">
                    <Option v-for="i in teams4" :value="i.id" :key="i.id">
                         {{ i.name }}
                     </Option>
                 </Select>
             </FormItem>
             <FormItem label="菜单等级" :style="{width:'300px'}">
                 <Select v-model="a_level1">
                    <Option v-for="i in teams1" :value="i.id" :key="i.id">
                         {{ i.name }}
                     </Option>
                 </Select>
             </FormItem>
             <FormItem label="菜单描述" :style="{width:'300px'}">
                 <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入权限描述" v-model="desc1"></Input>
             </FormItem>
          </Form>
       </modal>
       <Modal class="userinfo" v-model="showInfo" title="权限信息" @on-ok="confirm1" @on-cancel="cancel1" :closable="false">
           <Table :columns="accessColumns" :data="accessData"></Table>
       </Modal>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                id:'',
                a_name:'',
                a_router:'',
                a_stat:'',
                a_level:'',
                a_type:'',
                a_visible:'',
                a_id:'',
                desc:'',
                a_name1:'',
                a_router1:'',
                a_stat1:'',
                a_level1:'',
                a_type1:'',
                a_visible1:'',
                a_id1:'',
                desc1:'',
                showInfo:false,
                accessName:'',
                accessState:'',
                modal6:false,
                totalCount:0,
                pageSize:5,
                ajaxHistoryData:[],
                accessData:[],
                accessColumns: [
                    {
                        title: 'ID',
                        key:'id'
                    },
                    {
                        title: '菜单名称',
                        key: 'name'
                    },
                    {
                        title: '菜单路由',
                        key: 'router'
                    },
                    {
                      title:'菜单状态',
                      key:'status'
                    },
                    {
                      title:'菜单等级',
                      key:'level'
                    },
                    {
                      title:'菜单类型',
                      key:'type'
                    },
                    {
                      title:'菜单描述',
                      key:'desc'
                    }
                ],
                teams1: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'},
                ],
                teams2: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'},
                ],
                teams3: [
                  {id:'1',name:'1'},
                  {id:'2',name:'2'}
                ],
                teams4: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'},
                ],
                columns1: [
                    // {
                    //     type: 'selection',
                    //     width: 60,
                    //     align: 'center'
                    // },
                    {
                        title: '名称',
                        key: 'name'
                    },
                    {
                        title: '状态',
                        key: 'status'
                    },
                    {
                        title: ' 级别',
                        key: 'level'
                    },
                    {
                        title: '类型',
                        key: 'type'
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
                                        this.$axios.get(`${this.URL_PREFIX}/v1/system/access/query/${params.row.id}`)
                                                   .then(res => {
                                                     if(res.data.code == '0'){
                                                       this.showInfo = true
                                                       this.accessData.push(res.data.result)
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
                                          this.$axios.delete(`${this.URL_PREFIX}/v1/system/access`,{
                                              headers: { 'Content-Type': 'application/json' },
                                              data: {
                                                id:params.row.id
                                              }
                                          }).then(res => {
                                            if(res.data.code == '0'){
                                                      setTimeout(() => {
                                                       this.accessList()
                                                       this.$Message.success('删除成功')
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
                                            this.modal6 = true
                                            this.id = params.row.id
                                            this.$axios.get(`${this.URL_PREFIX}/v1/system/access/query/${params.row.id}`)
                                                       .then(res => {
                                                         if(res.data.code == '0'){
                                                           this.id = res.data.result.id
                                                           this.a_name1 = res.data.result.name
                                                           this.a_router1 = res.data.result.router
                                                           this.a_stat1 = res.data.result.status
                                                           this.a_type1 = res.data.result.type
                                                           this.a_level1 = res.data.result.level
                                                           this.desc1 = res.data.result.desc
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
                data1: []
            }
        },
        mounted () {
            this.accessList();
        },
        methods: {
          //获取权限列表
           accessList(){
             this.$axios.get(`${this.URL_PREFIX}/v1/system/access?page=1&size=10`)
                .then(res => {
                   if(res.data.code == '0'){
                        //将获取的数据保存到data1空数组中
                        this.data1 = res.data.result
                        this.ajaxHistoryData = this.data1
                        this.totalCount =res.data.result.length
                        this.handleListApproveHistory()
                   }
                  })
                  .catch(error => {
                    console.log(error)
                   })
             },
             /*
               搜索查询列表
             */
           Search() {
               //this.loading = true
               this.$axios.get(`${this.URL_PREFIX}/v1/system/access?page=1&size=10&status=${this.accessState}&keyword=${this.accessName}`)
                   .then( res=> {
                     if(res.status == '200'){
                       //this.loading = false
                      //console.log(res.data.result)
                       if(res.data.result.length == 0){
                         setTimeout(() => {
                           this.loading = false
                           this.$Message.warning('未搜索到匹配信息,请重试!')
                           this.data1 = []
                           this.totalCount = 0
                         },1500)
                       }else {
                          //this.loading = false
                          setTimeout(() => {
                            this.loading = false
                            this.data1 = res.data.result
                            this.totalCount = res.data.result.length
                            this.ajaxHistoryData = this.data1
                            this.handleListApproveHistory()
                          },1500)
                       }
                     }
                   }).catch( error => {
                     console.log(error)
                   })
           },
             //添加权限
             addAccess() {
                 if(this.a_name ==''||this.a_name == null){
                    setTimeout(() => {
                       this.$Message.warning('请输入权限名称!')
                    },600)
                 }else if(this.a_router ==''||this.a_router == null){
                   setTimeout(() => {
                      this.$Message.warning('请输入权限路由!')
                   },600)
                 }else if(this.a_stat ==''||this.a_stat == null){
                   setTimeout(() => {
                      this.$Message.warning('请选择权限状态!')
                   },600)
                 }else if(this.a_type ==''||this.a_type == null){
                   setTimeout(() => {
                      this.$Message.warning('请选择权限类型!')
                   },600)
                 }else if(this.a_id ==''||this.a_id == null){
                   setTimeout(() => {
                      this.$Message.warning('请选择权限ID!')
                   },600)
                 }else if(this.a_level ==''||this.a_level == null){
                   setTimeout(() => {
                      this.$Message.warning('请选择层级关系!')
                   },600)
                 }else{
                   this.$axios.post(`${this.URL_PREFIX}/v1/system/access`,{
                     name:this.a_name,
                     status:parseInt(this.a_stat),
                     level:parseInt(this.a_level),
                     type:parseInt(this.a_type),
                     pid:parseInt(this.a_id),
                     router:this.a_router,
                     desc:this.desc
                   }).then(res => {
                     if(res.data.code == '0'){
                       setTimeout(() => {
                         this.reset()
                         this.accessList()
                         this.$Message.success('添加权限成功')
                       },1500)
                     }else{
                       setTimeout(() => {
                         this.reset()
                         this.$Message.error('添加权限失败')
                       },1500)
                     }
                   }).catch(error => {
                     console.log(error)
                   })
                 }
             },
             //权限编辑
             compiles() {
               this.$axios.put(`${this.URL_PREFIX}/v1/system/access`,{
                   id:parseInt(this.id),
                   name:this.a_name1,
                   status:parseInt(this.a_stat1),
                   level:parseInt(this.a_level1),
                   type:parseInt(this.a_type1),
                   pid:parseInt(this.a_id1),
                   router:this.a_router1,
                   desc:this.desc1
               }).then(res => {
                   if(res.data.code == '0'){
                      setTimeout(() => {
                        this.$Message.success('编辑成功')
                        this.reset1()
                        this.accessList()
                      },1500)
                   }else{
                     setTimeout(() => {
                       this.$Message.error('编辑失败')
                     },1500)
                   }
               }).catch(error => {
                   console.log(error)
               })
             },
             confirm1() {
               this.accessData.length = 0
             },
             cancel1() {
               this.accessData.length = 0
             },
             submit() {
                this.addAccess()
             },
             //提交编辑操作
             submit1() {
                this.compiles()
             },
             //重置操作
             reset() {
               this.a_name = '',
               this.a_type = ''
               this.a_id = ''
               this.a_router = '',
               this.a_stat = '',
               this.a_level = '',
               this.a_visible = '',
               this.desc = ''
             },
              //重置编辑操作
             reset1() {
               this.a_name1 = '',
               this.a_type1 = ''
               this.a_id1 = ''
               this.a_router1 = '',
               this.a_stat1 = '',
               this.a_level1 = '',
               this.a_visible1 = '',
               this.desc1 = ''
             },
           handleListApproveHistory(){
                // 初始化显示，小于每页显示条数，全显，大于每页显示条数，取前每页条数显示
                if(this.data1 < this.pageSize){
                    this.data1 = this.ajaxHistoryData;
                }else{
                    this.data1 = this.ajaxHistoryData.slice(0,this.pageSize);
                }
            },
             changepage(index){
                var _start = ( index - 1 ) * this.pageSize;
                var _end = index * this.pageSize;
                this.data1 = this.ajaxHistoryData.slice(_start,_end);
            }
        }
    }
</script>
<style scoped>
    .tment,.ivu-row{
        height: 100%;
    }
    .tment .tment-left{
        height: 100%;
        padding: 15px;
        border-right: 1px solid #e5e9ee;
    }
</style>
