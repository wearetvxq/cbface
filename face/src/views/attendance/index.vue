<template>
    <div class="attendance">
        <Form ref="formCustom">
            <FormItem>
                <Row>
                  <Col span="4">
                      <FormItem label="所在部门">
                          <Col span="15">
                                <Select v-model="dptname" style="width:100px">
                                  <Option v-for="i in teams" :value="i.id" :key="i.id"></Option>
                                </Select>
                          </Col>
                      </FormItem>
                  </Col>
                  <Col span="5">
                      <FormItem label="姓名">
                          <Col span="15">
                              <Input placeholder="请输入被访或来访人姓名" v-model="username"></Input>
                          </Col>
                      </FormItem>
                  </Col>
                  <Col span="6">
                      <FormItem label="来访时间">
                          <Col span='13'>
                              <DatePicker type="datetime" placeholder="Select date" :value="startTime" @on-change="handlechange"></DatePicker>
                          </Col>
                      </FormItem>
                  </Col>
                  <Col span='6' class="leave">
                    <FormItem label="离开时间">
                        <Col span='13'>
                            <DatePicker type="datetime" placeholder="Select date" :value="endTime" @on-change="handlechange1"></DatePicker>
                        </Col>
                    </FormItem>
                  </Col>
                  <Col span="3">
                      <Button type="ghost" icon="ios-search-strong" @click="Search">搜索</Button>
                      <Button type="ghost" icon="ios-cloud-download-outline" @click="Expor">导出</Button>
                  </Col>
                </Row>
            </FormItem>
        </Form>
        <Row>
            <Table :columns="columns" :data="data1" ref="table" v-show="this.data1.length>0"></Table>
        </Row>
        <Row :style="{marginTop: '15px'}">
            <Page :style="{float:'right'}" :total="totalCount" size="small" show-total show-elevator></Page>
        </Row>
    </div>
</template>
<script>
    //import dateUtil from 'iview/src/utils/date'
    import excel from '../../libs/tableToExcel.js'
    export default {
        data () {
            return {
                dptname:'',
                username:'',
                startTime:'',
                endTime:'',
                visitedTime:'',
                totalCount:0,
                pageSize:8,
                ajaxHistoryData:[],
                teams: [
                     { id:'研发部',name:'研发部'},
                     { id:'运营部',name:'运营部'},
                     { id:'商务部',name:'商务部'},
                     { id:'财务部',name:'财务部'},
                     { id:'实施部',name:'实施部'}
                ],
                columns: [
                    // {
                    //     type: 'selection',
                    //     width: 60,
                    //     align: 'center',
                    // },
                    {
                        title: 'ID',
                        key: 'id'
                    },
                    {
                        title: '姓名',
                        key: 'name'
                    },
                    {
                        title: '部门',
                        key: 'tment'
                    },
                    {
                        title: '正常天数',
                        key: 'normal'
                    },
                    {
                        title: '迟到次数',
                        key: 'late'
                    },
                    {
                        title: '脱岗次数',
                        key: 'off'
                    },
                    {
                        title: '早退次数',
                        key: 'quit'
                    },
                    {
                        title: '缺勤次数',
                        key: 'absence'
                    },
                    {
                        title: '操作',
                        key: 'operating',
                        render: (h, params) => {
                            return h('div', [
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
                                                this.$router.push({path:'/attendance/info/'+params.row.id})
                                        }
                                    }
                                }, '详情')
                            ]);
                        }
                    }
                ],
                data1: [],
                starttime: '',
                endtime: ''
            }
        },
        mounted () {
          this.getAttendanceList()
        },
        methods: {
          //获取考勤列表
            getAttendanceList() {
                 this.$axios.get(`${this.URL_PREFIX}/v1/attendance/list?page=1&size=10`)
                            .then(res => {
                              if(res.data.code == '0'){
                                this.data1 = res.data.result
                                this.ajaxHistoryData = this.data
                                this.totalCount =res.data.result.length
                                this.handleListApproveHistory()
                              }
                            })
                            .catch(error => {
                               console.log(error)
                            })
            },
            //列表搜索功能
            Search() {
              this.transform()
              this.$axios.get(`${this.URL_PREFIX}/v1/attendance/list?page=1&size=10&team=${this.dptname}&keyword=${this.username}&starttime=${this.startTime}&endtime=${this.endTime}`)
                  .then( res=> {
                    if(res.data.code == '0'){
                      if(res.data.result.length == 0){
                        setTimeout(() => {
                          this.$Message.warning('未搜索到匹配信息,请重试!')
                          this.data1 = []
                          this.totalCount = 0
                        },1500)
                      }else {
                         //this.loading = false
                         setTimeout(() => {
                           this.data1 = res.data.result
                           this.totalCount = res.data.result.length
                           this.ajaxHistoryData = this.data1
                           this.handleListApproveHistory()
                         },1500)
                      }
                    }else{
                      setTimeout(() => {
                            this.$Message.warning('未搜索到匹配信息,请重试!')
                            this.data1 = []
                      },1500)

                    }
                  }).catch( error => {
                    console.log(error)
                  })
            },
            //表格导出功能
            Expor() {
              this.$axios.get(`${this.URL_PREFIX}/v1/attendance/export`).then(res => {
                  if(res.data.code == '0'){
                    setTimeout(() => {
                       excel(this.columns, this.$refs.table, '考勤信息表.xls');
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
           handlechange(datetime){
             this.startTime = datetime
           },
           handlechange1(datetime){
             this.endTime = datetime
           },
           transform() {
             if(this.dptname =='研发部'){
               this.dptname = 0

             }else if(this.dptname =='财务部'){
               this.dptname = 1

             }else if(this.dptname =='运营部'){
               this.dptname = 2

             }else if(this.dptname =='商务部'){
               this.dptname = 3

             }else if(this.dptname =='实施部'){
               this.dptname = 4

             }
           },

        }
    }
</script>
<style scoped>
    .attendance{
        padding: 15px;
    }
    .leave{
      margin-left: -45px;
    }
</style>
