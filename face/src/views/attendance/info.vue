<template>
    <div class="attendance" v-show="this.attendance.length>0">
        <Row>
            <Col span="2" :style="{fontWeight:'bold', color: '#383f47'}">姓名：{{ userinfo.username }}</Col>
            <Col span="22">
                <Col span="2" :style="{color: '#383f47'}">
                    正常：{{ userinfo.normal }}天
                </Col>
                <Col span="2" :style="{color: '#383f47'}">
                    迟到：{{ userinfo.late }}天
                </Col>
                <Col span="2" :style="{color: '#383f47'}">
                    早退：{{ userinfo.retreat }}次
                </Col>
                <Col span="2" :style="{color: '#383f47'}">
                    脱岗：{{ userinfo.off }}次
                </Col>
                <Col span="2" :style="{color: '#383f47'}">
                    缺勤：{{ userinfo.absence }}次
                </Col>
            </Col>
        </Row>
        <Row :style="{paddingTop: '15px'}">
            <full-calendar :events="Events" lang="zh"></full-calendar>
        </Row>
    </div>
</template>
<script>
    import fullCalendar from 'vue-fullcalendar'
    export default {
        data () {
            return {
                Events : [

                ],
                userinfo: {},
                attendance:[],
                des:{}
            }
        },
        mounted () {
            this.lists();
        },
        methods: {
          getAttendanceSetting() {

          },
            lists() {
                this.$axios.get(`${this.URL_PREFIX}/v1/attendance/info/`+this.$route.params.id).then(res => {
                    this.userinfo = res.data.userinfo
                    this.attendance = res.data.result
                   //遍历
                    for (let item of this.attendance) {
                        let color = ''
                        let title = ''
                            if (item['status'] != 0){
                                if (item['status'] == 1){
                                    title = '迟'
                                    color = 'late richeng_radius'
                                }else if (item['status'] == 2){
                                    title = '脱'
                                    color = 'off richeng_radius'
                                }else if (item['status'] == 3){
                                    title = '退'
                                    color = 'early richeng_radius'
                                }else if (item['status'] == 4){
                                    title = '缺'
                                    color = 'absence richeng_radius'
                                }
                                this.des = {
                                    title: title,
                                    start: item['day'],
                                    cssClass: color,
                                    YOUR_DATA:{}
                                }
                                //console.log(this.des)
                                this.Events.push(this.des)
                            }
                    }

                }).catch(error => {
                    console.log(error);
                });
            }
        },
        components: {
          'full-calendar': fullCalendar
        }

    }
</script>
<style scoped>
    .ivu-col-span-4{
        width: 14.285%;
        text-align: center;
        font-weight: bold;
        color: '#383f47'
    }
    .calendar-title{
        height: 40px;
        line-height: 40px;
        border:1px solid #e5e9ee;
        overflow: hidden;
    }
    .calendar-content{
        height: auto;
        overflow: hidden;
        border-left: 1px solid #e5e9ee;
    }
    .calendar-content .cols{
        height: 70px;
        border: 1px solid #e5e9ee;
        border-top: none;
        border-left: none;
    }
    .attendance{
        padding: 15px;
    }
</style>
<style>
    .early{
        background-color: #FFD700!important;
        color: #FFF!important;
    }
    .absence{
        background-color: #E51C23!important;
        color: #FFF!important;
    }
    .late{
        background-color: #FF9800!important;
        color: #FFF!important;
    }
    .off{
        background-color: #246af6!important;
        color: #FFF!important;
    }
    .richeng_radius{
        border-radius: 50%;
        width: 20px;
        height: 20px;
    }
</style>
