<template>
    <div class="visitors">
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
            <Page :style="{float:'right'}" :total="totalCount" :page-size="pageSize" @on-change="changepage" size="small" show-total show-elevator></Page>
        </Row>
        <Modal v-model="showInfo"  :title='title' @on-ok="confirm" @on-cancel="cancel" :closable="false">
          <Form :label-width="80">
                <Row>
                   <Col span="18">
                     <FormItem>
                          <p class="tit">识别照片</p>
                          <div class="photo" v-for="(item,index) in pictures">
                              <img :src="item.url" class="pic"/>
                          </div>
                     </FormItem>
                   </Col>
                </Row>
                <Row>
                  <Col span="10">
                      <FormItem label="来访时间：" :style="{width:'250px'}">
                          <Input v-model="visitedTime"></Input>
                      </FormItem>
                  </Col>
                  <Col span="10">
                    <FormItem label="离开时间：" :style="{width:'250px'}">
                        <Input v-model="leaveTime"></Input>
                    </FormItem>
                  </Col>
                </Row>
                <Row>
                  <Col span="10">
                      <FormItem label="来访目的：" :style="{width:'250px'}">
                          <Input v-model="purpose"></Input>
                      </FormItem>
                  </Col>
                  <Col span="10">
                    <FormItem label="联系方式：" :style="{width:'250px'}">
                        <Input v-model="contact"></Input>
                    </FormItem>
                  </Col>
                </Row>
                <Row>
                  <Col span="10">
                      <FormItem label="被访人：" :style="{width:'250px'}">
                          <Input v-model="people"></Input>
                      </FormItem>
                  </Col>
                  <Col span="10">
                    <FormItem label="所属部门：" :style="{width:'250px'}">
                        <Input v-model="dpt"></Input>
                    </FormItem>
                  </Col>
                </Row>
                <Row>
                  <Col span="10">
                      <FormItem label="是否VIP：" :style="{width:'250px'}">
                          <Input v-model="vip"></Input>
                      </FormItem>
                  </Col>
                  <Col span="10">
                    <FormItem label="备注：" :style="{width:'250px'}">
                        <Input type="textarea" :autosize="{minRows: 2,maxRows: 10}" placeholder="请输入来访备注" v-model="remarks"></Input>
                    </FormItem>
                  </Col>
                </Row>
          </Form>
        </Modal>
    </div>
</template>
<script>
    import excel from '../../libs/tableToExcel.js'
    export default {
        data () {
            return {
                dptname:'',
                username:'',
                startTime:'',
                endTime:'',
                visitedTime:'',
                leaveTime:'',
                purpose:'',
                contact:'',
                people:'',
                user:'',
                dpt:'',
                vip:'否',
                title:'日志详情-',
                remarks:'',
                totalCount:0,
                showInfo:false,
                pictures:[],
                record:{},
                pageSize:8,
                ajaxHistoryData:[],
                columns: [
                    // {
                    //     type: 'selection',
                    //     width: 60,
                    //     align: 'center'
                    // },
                    {
                        title: '访客ID',
                        key: 'id'
                    },
                    {
                        title: '访客姓名',
                        key: 'name'
                    },
                    {
                        title: '被访人',
                        key: 'interviewed'
                    },
                    {
                        title: '被访人部门',
                        key: 'team'
                    },
                    {
                        title: '访客人数',
                        key: 'total'
                    },
                    {
                        title: '访客状态',
                        key: 'status'
                    },
                    {
                        title: '来访时间',
                        key: 'visiting',
                        width: 150
                    },
                    {
                        title: '离开时间',
                        key: 'leave',
                        width: 150
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
                                            setTimeout(() => {
                                              this.showInfo = true
                                            },500)
                                            this.$axios.get(`${this.URL_PREFIX}/v1/visitors/info/${params.row.id}`)
                                                       .then(res => {
                                                         if(res.data.code == '0'){
                                                            this.record = res.data.basic
                                                            this.pictures = res.data.topic
                                                            this.visitedTime = this.record.visiting
                                                            this.leaveTime = this.record.leave
                                                            this.purpose = this.record.purpose
                                                            this.dpt = this.record.team
                                                            this.people = this.record.interviewed
                                                            this.contact = this.record.phone
                                                            this.title = this.title+this.record.username

                                                         }else{

                                                         }
                                                       }).catch(error => {
                                                           console.log(error)
                                                       })
                                        }

                                    }
                                }, '详情')
                            ]);
                        }
                    }
                ],
                data1:[],
                teams: [
                     { id:'研发部',name:'研发部'},
                     { id:'运营部',name:'运营部'},
                     { id:'商务部',name:'商务部'},
                     { id:'财务部',name:'财务部'},
                     { id:'实施部',name:'实施部'}
                ],
            }
        },
        // filters: {
        //     formatDate(time) {
        //         var date = new Date(time);
        //         return formatDate(date, "yyyy-MM-dd hh:mm");
        //     }
        // },
        mounted () {
            //this.teamList();
            this.getVisitorList()
        },
        methods: {
            getVisitorList() {
                this.$axios.get(`${this.URL_PREFIX}/v1/visitors/list?size=10&page=1`)
                           .then(res => {
                             if(res.data.code == '0'){
                               this.data1 =  res.data.result
                               this.ajaxHistoryData = this.data
                               this.totalCount =res.data.result.length
                               this.handleListApproveHistory()
                             }
                           })
                           .catch(error => {
                              console.log(error)
                           })
            },
            //列表搜索
            Search() {
              this.transform()
              this.$axios.get(`${this.URL_PREFIX}/v1/visitors/list?page=1&size=10&team=${this.dptname}&keyword=${this.username}&starttime=${this.startTime}&endtime=${this.endTime}`)
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
            //导出表格功能
            Expor() {
              this.$axios.get(`${this.URL_PREFIX}/v1/visitors/export`).then(res => {
                  if(res.data.code == '0'){
                    setTimeout(() => {
                       excel(this.columns, this.$refs.table, '访客日志表.xls');
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
            handlechange(datetime){
              this.startTime = datetime
            },
            handlechange1(datetime){
              this.endTime = datetime
            },
            confirm() {
                this.title = '日志详情-'
            },
            cancel() {
                this.title = '日志详情-'
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
            // teamList () {
            //     var _this = this
            //       _this.$axios.get('http://192.168.188.201:8088/v1/label/team').then(function (response) {
            //         _this.teams = response.data.result
            //         console.log(response.data.result)
            //     }).catch(function (error) {
            //         console.log(error);
            //     });
            // },
        }
    }
</script>
<style lang="scss" scoped>
    .visitors{
        padding: 15px;
    }
    .leave{
      margin-left: -45px;
    }
    .tit{
      margin-left: -73px;
      margin-top: -18px;
      font-size: 12px;
      color: #495060;
    }
    .photo{
      height: 95px;
      position: relative;
      left: -75px;
      display: inline-block;
      .pic{
        width: 100px;
        height: 100px;
        margin-right: 15px;
        display: inline-block;
      }
    }
</style>
