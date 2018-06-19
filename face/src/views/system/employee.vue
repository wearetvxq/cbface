<template>
    <div class="employee">
        <Row>
            <Col span="7" class="employee-left">
                <Form :label-width="60">
                    <FormItem label="员工头像" :style="{marginBottom:'14px'}" id="myform">
                        <Upload
                            ref="upload"
                            :show-upload-list="false"
                            :before-upload="handleBeforeUpload"
                            :format="['jpg','jpeg','png']"
                            :max-size="2048"
                            type="drag"
                            action="`${this.URL_PREFIX}/v1/system/userpic`"
                            style="display: inline-block;width:80px;">
                            <div style="width: 80px;height:80px;line-height: 80px;">
                                <Icon type="camera" color="#e6eaf0" size="25"></Icon>
                            </div>
                        </Upload>

                    </FormItem>
                    <FormItem label="员工姓名" :style="{width:'300px'}">
                        <Input placeholder="请输入员工姓名" v-model="uname"></Input>
                    </FormItem>
                    <FormItem label="所属部门" :style="{width:'300px'}">
                      <Col span="15">
                          <Select v-model="dptname">
                              <Option v-for="i in teams" :value="i.id" :key="i.id">
                                  {{ i.name }}
                              </Option>
                          </Select>
                       </Col>
                    </FormItem>
                    <FormItem label="员工性别" :style="{width:'300px'}">
                        <Select v-model="sex">
                          <Option v-for="i in sexs" :value="i.id" :key="i.id">
                              {{ i.name }}
                          </Option>
                        </Select>
                    </FormItem>
                    <FormItem label="员工状态" :style="{width:'300px'}">
                      <Select v-model="state">
                        <Option v-for="i in states" :value="i.id" :key="i.id">
                            {{ i.name }}
                        </Option>
                      </Select>
                    </FormItem>
                    <FormItem label="描述:" :style="{width:'300px'}">
                        <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入员工描述" v-model="desc"></Input>
                    </FormItem>
                    <FormItem :style="{width:'300px'}">
                        <Button type="primary" :style="{float:'right'}" @click="Commit" :loading="loadingStatus">提交</Button>
                        <Button type="ghost" :style="{marginRight: '10px',float:'right'}" @click="reset">重置</Button>
                    </FormItem>
                </Form>
            </Col>
            <Col span="17" :style="{padding:'15px'}">
                <Form ref="formCustom">
                    <FormItem>
                        <Row>
                            <Col span="5">
                              <FormItem label="所在部门">
                                  <Select v-model="dptname1" style="width:80px">
                                    <Option v-for="i in teams" :value="i.id" :key="i.id">
                                        {{ i.name }}
                                    </Option>
                                  </Select>
                              </FormItem>
                            </Col>
                            <Col span="5">
                                <FormItem label="账号状态">
                                    <Col span="14">
                                        <Select v-model="state1" style="width:100px">
                                            <Option v-for="item in states1" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                        </Select>
                                    </Col>
                                </FormItem>
                            </Col>

                            <Col span="5">
                                <FormItem label="员工姓名">
                                    <Col span="15">
                                        <Input placeholder="请输入员工姓名" v-model="employeeName"></Input>
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
                <Row>
                    <Table :columns="columns1" :data="data" ref="table" v-show="this.data.length>0"></Table>
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
            @0n-cancel="cancel"
         >
         <Form :label-width="80">
             <FormItem label="员工头像:" :style="{marginBottom:'14px'}">
                 <Upload
                     ref="upload"
                     :show-upload-list="false"
                     :format="['jpg','jpeg','png']"
                     :max-size="2048"
                     type="drag"
                     :before-upload="handleBeforeUpload"
                     action="`${this.URL_PREFIX}/v1/system/userpic`"
                     style="display: inline-block;width:80px;">
                     <div style="width: 80px;height:80px;line-height: 80px;">
                         <Icon type="camera" color="#e6eaf0" size="25"></Icon>
                     </div>
                 </Upload>
             </FormItem>
             <FormItem label="员工姓名:" :style="{width:'300px'}">
                 <Input placeholder="请输入员工姓名" v-model="uname2"></Input>
             </FormItem>
             <FormItem label="所属部门:" :style="{width:'300px'}">
               <Col span="15">
                   <Select v-model="dptname2">
                       <Option v-for="i in teams" :value="i.id" :key="i.id">
                           {{ i.name }}
                       </Option>
                   </Select>
                </Col>
             </FormItem>
             <FormItem label="员工性别:" :style="{width:'300px'}">
                 <Select v-model="sex1">
                   <Option v-for="i in sexs" :value="i.id" :key="i.id">
                       {{ i.name }}
                   </Option>
                 </Select>
             </FormItem>
             <FormItem label="员工状态:" :style="{width:'300px'}">
                 <Select v-model="state2">
                   <Option v-for="i in states" :value="i.id" :key="i.id">
                       {{ i.name }}
                   </Option>
                 </Select>
             </FormItem>
             <FormItem label="描述:" :style="{width:'300px'}">
                 <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入员工描述" v-model="desc2"></Input>
             </FormItem>
         </Form>
       </Modal>
       <Modal class="emploeeinfo" v-model="showInfo" title="员工信息" @on-ok="confirm1" @on-cancel="cancel1" :closable="false">
           <Table :columns="orderColumns" :data="employeeData"></Table>
       </Modal>
       <Modal v-model="modal2" width="360">
        <p slot="header" style="color:#f60;text-align:center">
            <Icon type="information-circled"></Icon>
            <span>提示</span>
        </p>
        <div style="text-align:center">
            <p>头像上传中,请勿进行其它操作</p>
            <p>该窗口会在上传完成后自动关闭,请等待</p>
        </div>
        <div slot="footer">
            <Button type="error" size="large">提示</Button>
        </div>
    </Modal>
    </div>
</template>
<script>
import excel from '../../libs/tableToExcel.js'
import axios from 'axios';
    export default {
        data () {
            return {
                id:'',
                topic:'',
                uname:'',
                uname2:'',
                showInfo:false,
                loadingStatus:false,
                file:null,
                filepath:'',
                modal2:false,
                dpt:'',
                state1:'',
                employeeName:'',
                dptname:'',
                dptname1:'',
                dptname2:'',
                dpt2:'',
                dpt3:'',
                id2:'',
                sex:'',
                sex1:'',
                state:'',
                state2:'',
                desc:'',
                desc2:'',
                url:'',
                modal6:false,
                teams: [
                     { id:'研发部',name:'研发部'},
                     { id:'运营部',name:'运营部'},
                     { id:'商务部',name:'商务部'},
                     { id:'财务部',name:'财务部'},
                     { id:'实施部',name:'实施部'}
                ],
                states1:[
                  {value:'启用',label:'启用'},
                  {value:'禁用',label:'禁用'}
                ],
                states:[
                  { id:'1',name:'1'},
                  { id:'2',name:'2'},
                  { id:'3',name:'3'}
                ],
                sexs: [
                     { id:'男',name:'男'},
                     { id:'女',name:'女'}
                ],
                ajaxHistoryData:[],
                pageSize:7,
                totalCount:0,
                orderColumns: [
                    {
                        title: 'ID',
                        key:'id'
                    },
                    {
                      title:'员工描述',
                      key:'remarks'
                    },
                    {
                        title: '性别',
                        key: 'sex'
                    },
                    {
                      title:'员工状态',
                      key:'status',
                      width:60
                    },
                    {
                        title: '所属部门',
                        key: 'team'
                    },
                    {
                      title:'员工照片',
                      key:'topic'
                    },
                    {
                      title:'用户名',
                      key:'username'
                    }
                ],
                employeeData:[],
                columns1: [
                    // {
                    //     type: 'selection',
                    //     width: 60,
                    //     align: 'center'
                    // },
                    {
                        title: 'ID',
                        key: 'id'
                    },
                    {
                        title: '名称',
                        key: 'name'
                    },
                    {
                        title: '性别',
                        key: 'sex'
                    },
                    {
                        title: '部门',
                        key: 'team'
                    },
                    {
                        title:'状态',
                        key:'status'
                    },
                    {
                        title: '创建时间',
                        width: 150,
                        key: 'posttime'
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
                                          this.$axios.get(`${this.URL_PREFIX}/v1/system/userpicv1/system/employee/query/${params.row.id}`)
                                                     .then(res => {
                                                       if(res.data.code == '0'){
                                                         this.showInfo = true
                                                         this.employeeData.push(res.data.result)
                                                         //this.state2 = res.data.result.status
                                                         //动态路由跳转
                                                         // let argu = { id: params.row._index };
                                                         // this.$router.push({
                                                         //     name: 'attendance_info',
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
                                            //
                                            this.$axios.delete(`${this.URL_PREFIX}/v1/system/employee`,{
                                                headers: { 'Content-Type': 'application/json' },
                                                data: {
                                                  id:params.row.id
                                                }
                                            }).then(res => {
                                              if(res.data.code == '0'){
                                                        setTimeout(() => {
                                                         this.employeelist()
                                                         this.$Message.success('删除成功')
                                                        },1500)
                                                    }else if(res.data.code == '10003'){
                                                      setTimeout(() => {
                                                        this.$Message.warning('删除的用户不存在')
                                                      },1500)
                                                    }else{
                                                      setTimeout(() => {
                                                       this.$Message.success('删除失败')
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
                                           this.$axios.get(`${this.URL_PREFIX}/v1/system/employee/query/${params.row.id}`)
                                                      .then(res => {
                                                        if(res.data.code == '0'){
                                                          this.id = res.data.result.id
                                                          this.uname2 = res.data.result.username
                                                          this.dptname2 = res.data.result.team
                                                          this.sex1 = res.data.result.sex
                                                          this.state2 =res.data.result.status
                                                          this.desc2 = res.data.result.remarks
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
                data: [

                ]
            }
        },
        mounted (){
            this.employeelist()
        },
        methods: {
          /*
            员工列表页
          */
           employeelist() {
           this.$axios.get(`${this.URL_PREFIX}/v1/system/employee/list?page=1&size=10`).then(res => {
                    if(res.data.code == '0'){
                      //将获取的数据保存到data1空数组中
                      this.data = res.data.result
                      this.totalCount =res.data.result.length
                      this.ajaxHistoryData = this.data
                      this.handleListApproveHistory()
                    }
                  })
                  .catch(error => {
                    console.log(error)
                  })
          },
          //用户头像上传接口
          UploadAvatar() {
              var formData = new FormData(document.getElementById('#myForm'));
              formData.append("files",this.file);
              console.log(this.file)
              //添加请求头
              let config = {
                headers: { 'Content-Type': 'multipart/form-data' }
               };
              this.$axios.post(`${this.URL_PREFIX}/v1/system/userpic`,formData,config)
                         .then( res => {
                            if(res.data.code == '0'){
                              this.filepath = res.data.msg;
                              setTimeout(()=> {
                                  this.modal2 = false
                              },3000)
                              setTimeout(()=> {
                                  this.$Message.success('头像上传成功!')
                              },3500)
                            }else {
                              setTimeout(()=> {
                                  this.modal2 = false
                              },3000)
                              setTimeout(()=> {
                                  this.$Message.error('上传失败请重试!')
                              },3500)
                            }
                        }).catch(error => {
                          console.log(error)
                        })

          },
          //图片上传钩子函数
          handleBeforeUpload(file) {
                 this.file = file;
                 setTimeout(()=> {
                   this.modal2 = true
                 },1000)
                 this.UploadAvatar()
                 return false;
          },
          //添加员工
          addUser(){
              if(this.filepath ==''||this.filepath == null){
                  setTimeout(() => {
                    this.$Message.warning('请上传员工头像!')
                  },600)
              }else if(this.uname ==''||this.uname == null){
                  setTimeout(() => {
                      this.$Message.warning('请输入员工姓名!')
                  },600)
              }else if(this.dptname ==''||this.dptname == null){
                setTimeout(() => {
                    this.$Message.warning('请选择员工所属部门!')
                },600)
              }else if(this.sex ==''||this.sex == null){
                setTimeout(() => {
                    this.$Message.warning('请选择员工性别!')
                },600)
              }else if(this.state ==''||this.state == null){
                setTimeout(() => {
                    this.$Message.warning('请选择员工状态!')
                },600)
              }else{
                this.transformSex()
                axios.post(`${this.URL_PREFIX}/v1/system/employee`,{
                    topic:this.filepath,
                    username:this.uname,
                    team:this.dptname,
                    sex:this.sex,
                    status:parseInt(this.state),
                    remarks:this.desc
                }).then(res => {
                    if(res.data.code == '0'){
                       setTimeout(() => {
                          this.reset()
                          this.employeelist()
                          this.$Message.success('新增员工成功')
                          this.loadingStatus = false
                          this.reset2()
                       },1500)
                    }else{
                      setTimeout(() => {
                         this.$Message.error('新增员工失败')
                         this.loadingStatus = false
                         this.reset2()
                      },1500)
                    }
                }).catch(error => {
                    console.log(error)
                })
              }
          },
          //提交新增员工操作功能
          Commit() {
              //this.loadingStatus = true
              this.addUser()

          },
          /*
            搜索查询列表
          */
        Search() {
            //this.loading = true
            this.transform()
            this.$axios.get(`${this.URL_PREFIX}/v1/system/employee/list?page=1&size=10&team=${this.dptname1}&status=${this.state1}&keyword=${this.employeeName}`)
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
          //导出操作
          expor(){
                 this.$axios.get(`${this.URL_PREFIX}/v1/system/employee/export?page=1&size=10`).then(res => {
                   if(res.data.code == '0'){
                     setTimeout(() => {
                        excel(this.columns1, this.$refs.table, '员工信息.xls');
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
             //员工编辑操作
             compiles() {
               this.transformSex()
               this.$axios.put(`${this.URL_PREFIX}/v1/system/employee?page=1&size=10`,{
                   id:this.id,
                   topic:'mail.itlaolang',
                   username:this.uname2,
                   team:this.dptname2,
                   sex:this.sex1,
                   status:parseInt(this.state2),
                   remarks:this.desc2
               }).then(res => {
                   if(res.data.code == '0'){
                     setTimeout(() => {
                       this.employeelist()
                       this.$Message.success('编辑成功')
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
             transformSex() {
               if(this.sex =='男'||this.sex1 =='男'){
                 this.sex = 1
                 this.sex1 = 1
               }else if(this.sex =='女'||this.sex1 =='女'){
                 this.sex = 2
                 this.sex1 = 2
               }
             },
             confirm1() {

                this.employeeData.length = 0
             },
             cancel1() {
                this.employeeData.length = 0
             },
             cancel() {
                 this.reset2()
             },
             //重置
             reset() {
               this.uname = ''
               this.dptname = ''
               this.sex = ''
               this.state = ''
               this.desc = ''
             },
             reset2() {
               this.uname2 = ''
               this.dpt3 = ''
               this.sex2 = ''
               this.stat2 = ''
             },
             //提交编辑员工操作
             submit1() {
                this.compiles()
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
<style lang="scss" >
    .employee,.ivu-row{
        height: 100%;
    }
    .employee .employee-left{
        height: 100%;
        padding: 15px;
        border-right: 1px solid #e5e9ee;
    }
    .ivu-modal-content {
       width: 700px;
     }

</style>
