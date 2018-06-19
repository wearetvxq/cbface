<template>
    <div class="monitor">
        <Row :style="{height:'100%'}" :gutter="15">
            <Col span="12" class="monitor-list">
                <div class="monitor-box">
                    <div class="monitor-icon-box">
                        <Icon type="ios-videocam" class="monitor-icon"></Icon>
                        <p>等待画面接入</p>
                    </div>
                </div>
            </Col>
            <Col span="12" class="monitor-list">
                <div class="monitor-box">
                    <div class="monitor-icon-box">
                        <Icon type="ios-videocam" class="monitor-icon"></Icon>
                        <p>等待画面接入</p>
                    </div>
                </div>
            </Col>
            <Col span="12" class="monitor-list">
                <div class="monitor-box">
                    <div class="monitor-icon-box">
                        <Icon type="ios-videocam" class="monitor-icon"></Icon>
                        <p>等待画面接入</p>
                    </div>
                </div>
            </Col>
            <Col span="12" class="monitor-list">
                <div class="monitor-box">
                    <div class="monitor-icon-box">
                        <Icon type="ios-videocam" class="monitor-icon"></Icon>
                        <p>等待画面接入</p>
                    </div>
                </div>
            </Col>
        </Row>
        <Modal v-model="modal" title="来访登记" :styles="{top: '15px'}">
            <Form ref="formValidate" :label-width="80" :style="{width:'90%'}">
                <FormItem label="照片">
                    <img v-for="p in pics" :style="{width: '100px', height:'100px'}" :src="p.img" />
                </FormItem>
                <FormItem label="姓名">
                    <Input v-model="username" placeholder="请输入访客姓名"></Input>
                </FormItem>
                <FormItem label="来访时间">
                    <DatePicker type="datetime" v-model="posttime" placeholder="请选择来访时间" style="width: 200px"></DatePicker>
                </FormItem>
                <FormItem label="来访人数">
                    <Input v-model="total" placeholder="请输入来访人数"></Input>
                </FormItem>
                <FormItem label="联系电话">
                    <Input v-model="phone" placeholder="请输入来访人员联系电话"></Input>
                </FormItem>
                <FormItem label="来访目的">
                    <Select v-model="purpose" placeholder="请选择来访目的">
                        <Option v-for="i in purposes" :value="i.id">
                            {{ i.name }}
                        </Option>
                    </Select>
                </FormItem>
                <FormItem label="被访人">
                    <Input v-model="interviewed" placeholder="请输入被访人姓名"></Input>
                </FormItem>
                <FormItem label="被访人部门">
                    <Select v-model="team" placeholder="请选择被访人部门">
                        <Option v-for="i in teams" :value="i.id">
                            {{ i.name }}
                        </Option>
                    </Select>
                </FormItem>
            </Form>
            <div slot="footer">
                <input v-model="logId" type="hidden">
                <input v-model="camid" type="hidden">
                <Button type="ghost" @click="open">开门</Button>
                <Button type="primary" @click="recording">确定</Button>
            </div>
        </Modal>
    </div>
</template>
<script>
    // import axios from 'axios';
    import dateUtil from 'iview/src/utils/date'
    export default {
        data () {
            return {
                modal: false,
                username: null,
                posttime: null,
                total: null,
                phone: null,
                purpose: null,
                purposes: [],
                interviewed: null,
                team: null,
                logId: null,
                camid: null,
                pics: [],
                teams: []
            }
        },
        mounted () {

            this.teamList();
            this.purposeList();
            this.timing();
        },
        methods: {
            teamList () {
                var _this = this
                _this.$axios.get(`${this.URL_PREFIX}/v1/label/team`).then(function (response) {
                    _this.teams = response.data.result
                    console.log(response.data.result)
                }).catch(function (error) {
                    console.log(error);
                });
            },
            purposeList () {
                var _this = this
                _this.$axios.get(`${this.URL_PREFIX}/v1/label/purpose`).then(function (response) {
                    _this.purposes = response.data.result
                }).catch(function (error) {
                    console.log(error);
                });
            },
            timing () {
                var _this = this
                let interval = setInterval(function (){
                    _this.$axios.get('http://127.0.0.1:81/v1/monitor/polling').then(function (response) {
                        console.log(response.data)
                        let res = response.data
                        if (res.code == 0 && res.result != 0){
                            console.log(res.result.pic)
                            _this.pics = res.result.pic
                            _this.modal = true
                            _this.logId = res.result.id
                            _this.camid = res.result.camid
                            _this.posttime = res.result.posttime
                            clearInterval(interval)
                        }
                    }).catch(function (error) {
                        console.log(error);
                    });
                }, 2000);
            },
            recording () {
                if (this.username == null){
                    this.$Message.warning('请输入来访人员姓名');
                }else if (this.posttime == null){
                    this.$Message.warning('请选择来访日期');
                }else if (this.total == null){
                    this.$Message.warning('请输入来访人数');
                }else if (this.phone == null){
                    this.$Message.warning('请输入来访人员联系电话');
                }else if (this.purpose == null){
                    this.$Message.warning('请选择来访目的');
                }else if (this.interviewed == null){
                    this.$Message.warning('请输入被访人姓名');
                }else if (this.team == null){
                    this.$Message.warning('请选择被访人所在部门');
                }else{
                    var strtime = dateUtil.format(this.posttime, 'yyyy-MM-dd HH:mm:ss')
                    var date = new Date(strtime.replace(/-/g, '/'));
                    var _this = this
                    _this.$axios.post(`${this.URL_PREFIX}/v1/monitor`, {
                        visitId: this.camid,
                        username: this.username,
                        posttime: date.getTime().toString(),
                        total: this.total,
                        phone: this.phone,
                        purpose: this.purpose,
                        interviewed: this.interviewed,
                        team: this.team,
                        pic: this.pics,
                        id: this.logId

                    }).then(function (response) {
                        if (response.data.code == '0'){
                            _this.$Message.success('访客登记成功');
                            setTimeout(function (){
                                _this.modal = false
                            }, 2000);
                            _this.timing()
                        }else{
                           _this.$Message.warning('系统错误，请联系管理员或稍后再试！');
                        }
                    }).catch(function (error) {
                        _this.$Message.warning('系统错误，请联系管理员或稍后再试！');
                    });
                }
            },
            open () {
                //this.$Message.warning('功能完善中...');
                this.$axios.post(`${this.URL_PREFIX}/v1/monitor/open`,{
                    status:'5'
                }).then(res => {
                  if(res.data.code == '0'){
                    setTimeout(() => {
                        this.$Message.success('操作成功')
                    },1500)
                  }else{
                    setTimeout(() => {
                        this.$Message.error('操作失败')
                    },1500)
                  }
                }).catch(error => {
                  console.log(error)
                })
            }

        }
    }
</script>
<style scoped>
    .monitor{
        padding: 15px;
        height: 100%;
    }
    .monitor .monitor-list{
        height: 50%;
        overflow: hidden;
    }
    .monitor .monitor-list .monitor-box{
        height: 100%;
        background-color: #383f47;
        color: #b3b4b5;
    }
    .monitor .monitor-list:nth-child(1),.monitor .monitor-list:nth-child(2){
        padding-bottom: 15px;
    }
    .monitor .monitor-list .monitor-icon-box{
        width: 100%;
        height: 100%;
        position: relative;
        overflow: auto;
    }
    .monitor .monitor-icon-box .monitor-icon{
        position: absolute;
        font-size: 60px;
        color: #b3b4b5;
        left:50%;
        top:50%;
        transform:translate(-50%,-50%)
    }
    .monitor .monitor-icon-box p{
        position: absolute;
        top: 57%;
        text-align: center;
        width: 100%;
    }
</style>
<style>
    .ivu-modal-content{
        border-radius: 0px!important;
    }
    .ivu-modal-header{
        padding: 9px 15px!important;
        background-color: #3F8D76;
    }
    .ivu-modal-header .ivu-modal-header-inner{
        color: #FFF;
    }
    .ivu-modal-close{
        top: 4px!important;
    }
    .ivu-modal-close .ivu-icon-ios-close-empty{
        color: #FFF!important;
    }
    .ivu-modal{
        width: 420px!important;
    }
</style>
