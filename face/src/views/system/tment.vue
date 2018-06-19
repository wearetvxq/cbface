<template>
    <div class="tment">
        <Row>
            <Col span="7" class="tment-left">
                <Form :label-width="80">
                  <FormItem label="部门名称:" :style="{width:'300px'}">
                      <Input placeholder="请输入新增部门名称" v-model="dptname"></Input>
                  </FormItem>
                    <FormItem label="部门状态" :style="{width:'300px'}">
                      <Col span="12">
                         <Select v-model="stat3" style="width:80px">
                             <Option v-for="item in typelist2" :value="item.value" :key="item.value">{{ item.label }}</Option>
                         </Select>
                       </Col>
                    </FormItem>
                    <FormItem label="部门描述:" :style="{width:'300px'}">
                        <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入部门描述" v-model="desc"></Input>
                    </FormItem>
                    <FormItem :style="{width:'300px'}">
                        <Button type="primary" :style="{float:'right'}" @click="refering">提交</Button>
                        <Button type="ghost" :style="{marginRight: '10px',float:'right'}" @click="reset">重置</Button>
                    </FormItem>
                </Form>
            </Col>
            <Col span="17" :style="{padding:'15px'}">
                <Form ref="formCustom">
                    <FormItem>
                        <Row>
                            <Col span="6">
                                <FormItem label="部门状态">
                                  <Col span="14">
                                    <Select v-model="state" style="width:100px">
                                        <Option v-for="item in states" :value="item.value" :key="item.value">{{ item.label }}</Option>
                                    </Select>
                                  </Col>
                                </FormItem>
                            </Col>
                            <Col span="6">
                                <FormItem label="部门名称">
                                  <Col span="14">
                                    <Select v-model="dptname1" style="width:100px">
                                      <Option v-for="i in teams" :value="i.id" :key="i.id"></Option>
                                    </Select>
                                  </Col>
                                </FormItem>
                            </Col>

                            <Col span="6">
                                <Button type="ghost" icon="ios-search-strong" @click="Search">搜索</Button>
                                <Button type="ghost" icon="ios-cloud-upload-outline" @click="expor">导出</Button>
                            </Col>
                        </Row>
                    </FormItem>
                </Form>
                <Row>
                    <Table :columns="columns1" :data="data1" ref="table" v-show="this.data1.length>0"></Table>
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
                  <FormItem label="部门名称:" :style="{width:'250px'}">
                    <Col span="15">
                        <Select v-model="dptname2">
                            <Option v-for="i in teams" :value="i.id" :key="i.id">
                                {{ i.name }}
                            </Option>
                        </Select>
                     </Col>
                  </FormItem>
                  <FormItem label="部门状态:" :style="{width:'250px'}">
                            <Col span="12">
                               <Select v-model="stat2" style="width:80px">
                                   <Option v-for="item in typelist2" :value="item.value" :key="item.value">{{ item.label }}</Option>
                               </Select>
                             </Col>
                  </FormItem>
                  <FormItem label="部门描述" :style="{width:'300px'}">
                      <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入部门描述" v-model="desc2"></Input>
                  </FormItem>
              </Form>
            </Modal>
            <Modal class="userinfo" v-model="showInfo" title="部门信息" @on-ok="confirm" @on-cancel="cancel" :closable="false">
                <Table :columns="tmentColumns" :data="tmentData"></Table>
            </Modal>
    </div>
</template>
<script>
import excel from '../../libs/tableToExcel.js'
import axios from 'axios';
    export default {
        data () {
            return {
                modal6:false,
                id:'',
                dpt2:'',
                state:'',
                departmentname:null,
                stat2:'',
                stat3:'',
                teams2:'',
                dptname:'',
                dptname1:'',
                dptname2:'',
                desc:'',
                desc2:'',
                ajaxHistoryData:[],
                pageSize:10,
                totalCount:0,
                showInfo:false,
                teams: [
                     { id:'研发部',name:'研发部'},
                     { id:'运营部',name:'运营部'},
                     { id:'商务部',name:'商务部'},
                     { id:'财务部',name:'财务部'},
                     { id:'实施部',name:'实施部'}
                ],
                tmentColumns: [
                    {
                        title: 'ID',
                        key:'id'
                    },
                    {
                        title: '部门名称',
                        key: 'name'
                    },
                    {
                        title: '部门描述',
                        key: 'remarks'
                    },
                    {
                      title:'部门状态',
                      key:'status'
                    }
                ],
                tmentData:[],
                states:[
                  {value:'启用',label:'启用'},
                  {value:'禁用',label:'禁用'}
                ],
                typelist2:[
                  { value:'1',label:'1'},
                  { value:'2',label:'2'},
                  { value:'3',label:'3'}
                ],
                teams2: [
                     { id:'1',name:'1'},
                     { id:'2',name:'2'},
                     { id:'3',name:'3'}

                ],
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
                        title: '人数',
                        key: 'total'
                    },
                    {
                        title:'状态',
                        key:'status'
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
                                          this.$axios.get(`${this.URL_PREFIX}/v1/system/tment/query/${params.row.id}`)
                                                     .then(res => {
                                                       if(res.data.code == '0'){
                                                         this.showInfo = true
                                                         this.tmentData.push(res.data.result)
                                                       }else{

                                                       }
                                                     }).catch(error => {
                                                         console.log(error)
                                                     })
                                            //this.$router.push({path: '/attendance/info'});
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
                                                this.$axios.delete(`${this.URL_PREFIX}/v1/system/tment`,{
                                                    headers: { 'Content-Type': 'application/json' },
                                                    data: {
                                                      id:params.row.id
                                                    }
                                                }).then(res => {
                                                  if(res.data.code == '0'){
                                                            setTimeout(() => {
                                                             this.getDpt()
                                                             this.$Message.success('删除成功')
                                                            },1500)
                                                        }else if(res.data.code == '10003'){
                                                          setTimeout(() => {
                                                            this.$Message.warning('删除的部门不存在')
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
                                            //this.id = params.row.id
                                            this.$axios.get(`${this.URL_PREFIX}/v1/system/tment/query/${params.row.id}`)
                                                       .then(res => {
                                                         if(res.data.code == '0'){
                                                            this.id = res.data.result.id
                                                            this.dptname2 = res.data.result.name
                                                            this.stat2 = res.data.result.status
                                                            this.desc2 =  res.data.result.remarks
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
         mounted (){
            this.getDpt()
        },
        methods: {
          /*
            获取部门列表数据
          */
          getDpt(){
           this.$axios.get(`${this.URL_PREFIX}/v1/system/tment/list?page=1&size=10`).then(res => {
                    if(res.data.code == '0'){
                      //将获取的数据保存到data1空数组中
                      this.data1 = res.data.result
                      this.totalCount =res.data.result.length
                      this.ajaxHistoryData = this.data1
                      this.handleListApproveHistory()
                    }
                  })
                  .catch(error => {
                    console.log(error)
                  })
          },
          //新增部门
          addDpt(){
             if(this.dptname ==''||this.dptname == null) {
               setTimeout(()=> {
                   this.$Message.warning('请输入新增部门名称!')
               },600)
             }else if(this.stat3 ==''||this.stat3 == null){
               setTimeout(()=> {
                   this.$Message.warning('请选择部门状态!')
               },600)
             }else{
               this.$axios.post(`${this.URL_PREFIX}/v1/system/tment`,{
                   name:this.dptname,
                   status:parseInt(this.stat3),
                   remarks:this.desc
               }).then(res => {
                   if(res.data.code == '0'){
                       setTimeout(() => {
                         this.reset()
                         this.getDpt()
                         this.$Message.success('新增部门成功')
                       },1500)
                   }else{
                     setTimeout(() => {
                       this.reset()
                       this.$Message.error('新增部门失败')
                     },1500)
                   }
               }).catch(error => {
                   console.log(error)
               })
             }
          },
          /*
            部门搜索查询列表
          */
        Search() {
            //this.loading = true

            this.$axios.get(`${this.URL_PREFIX}/system/tment/list?page=1&size=10&status=${this.state}&keyword=${this.dptname1}`)
                .then( res=> {
                  if(res.data.code == '0'){
                    //this.loading = false
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
                         this.ajaxHistoryData = this.data
                         this.handleListApproveHistory()
                       },1500)
                    }
                  }else{
                    setTimeout(() => {
                          this.$Message.warning('未搜索到匹配信息,请重试!')
                            this.data1 = []
                            this.totalCount = 0
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
                 this.$axios.get(`${this.URL_PREFIX}/v1/system/tment/export?page=1&size=10`)
                 .then(res => {
                     if(res.data.code == '0'){
                        setTimeout(() => {
                          excel(this.columns1,this.$refs.table, '部门信息.xls');
                          this.$Message.success('导出成功')
                        },1500)
                     }else{
                       setTimeout(() => {
                         this.$Message.error('导出失败')
                       },1500)
                     }
                 }).catch(error => {
                     console.log(error)
                 })
             },
             //部门编辑
             compiles() {
               //this.transform()
               this.$axios.put(`${this.URL_PREFIX}/v1/system/tment`,{
                   id:parseInt(this.id),
                   name:this.dptname2,
                   status:parseInt(this.stat2),
                   remarks:this.desc2
               }).then(res => {
                   if(res.data.code == '0'){
                     setTimeout(() => {
                        this.getDpt()
                        this.$Message.success('编辑成功!')
                     },1500)
                   }else{
                     setTimeout(() => {
                       this.$Message.error('编辑失败!')
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
             //提交部门编辑操作
             submit1() {
                  this.compiles()
             },
             //提交新增部门操作
             refering() {
                this.addDpt()
             },
             reset() {
                 this.dptname = ''
                 this.stat3 = ''
                 this.desc = ''
             },
             confirm() {
                 this.tmentData.length = 0
             },
             cancel() {
                 this.tmentData.length = 0
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
<style>
    .ivu-modal-content {
       width: 700px;
     }
</style>

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
