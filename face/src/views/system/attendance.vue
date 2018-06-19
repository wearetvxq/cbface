<template>
    <div class="tment">
        <Row>
            <Col span="12" class="tment-left">
               <h6>上午考勤设置</h6>
               <Form ref="formDynamic" :label-width="80">
                <FormItem label="上班时间">
                    <Row>
                        <Col span="8">
                            <TimePicker type="time" placeholder="请选择上班时间" :value="startTime" @on-change="handlechange"></TimePicker>
                        </Col>
                        <Col span="2" :style="{textAlign: 'center'}">
                            晚于
                        </Col>
                        <Col span="3">
                            <Input placeholder="请填写" v-model="late"></Input>
                        </Col>
                        <Col span="4" :style="{textAlign: 'center'}">
                            分钟为迟到
                        </Col>
                    </Row>
                </FormItem>
                <FormItem label="下班时间">
                    <Row>
                        <Col span="8">
                            <TimePicker type="time" placeholder="请选择下班时间" :value="endTime" @on-change="handlechange1"></TimePicker>
                        </Col>
                        <Col span="2" :style="{textAlign: 'center'}">
                            早于
                        </Col>
                        <Col span="3">
                            <Input placeholder="请填写" v-model="early"></Input>
                        </Col>
                        <Col span="4" :style="{textAlign: 'center'}">
                            分钟为早退
                        </Col>
                    </Row>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="submitM">提交</Button>
                </FormItem>
            </Form>
            </Col>
            <Col span="12" :style="{padding:'15px'}">
                <h6>下午考勤设置</h6>
               <Form ref="formDynamic" :label-width="80">
                <FormItem label="上班时间">
                    <Row>
                        <Col span="8">
                            <TimePicker type="time" placeholder="请选择上班时间" :value="startTime1" @on-change="handlechange2"></TimePicker>
                        </Col>
                        <Col span="2" :style="{textAlign: 'center'}">
                            晚于
                        </Col>
                        <Col span="3">
                            <Input placeholder="请填写" v-model="late1"></Input>
                        </Col>
                        <Col span="4" :style="{textAlign: 'center'}">
                            分钟为迟到
                        </Col>
                    </Row>
                </FormItem>
                <FormItem label="下班时间">
                    <Row>
                        <Col span="8">
                            <TimePicker type="time" placeholder="请选择下班时间" :value="endTime1" @on-change="handlechange3"></TimePicker>
                        </Col>
                        <Col span="2" :style="{textAlign: 'center'}">
                            早于
                        </Col>
                        <Col span="3">
                            <Input placeholder="请填写" v-model="early1"></Input>
                        </Col>
                        <Col span="4" :style="{textAlign: 'center'}">
                            分钟为早退
                        </Col>
                    </Row>
                </FormItem>
                <FormItem>
                    <Button type="primary" @click="submitA">提交</Button>
                </FormItem>
            </Form>
            </Col>
        </Row>
    </div>
</template>
<script>
    export default {
      data() {
          return {
            startTime:'',
            late:'',
            endTime:'',
            early:'',
            startTime1:'',
            late1:'',
            endTime1:'',
            early1:''
          }
        },
        created() {

        },
        mounted() {
          this.getAttendanceList()
        },
        methods: {
          getAttendanceList() {
            //时间格式"20:00:20"
            this.$axios.get(`${this.URL_PREFIX}/v1/system/attendance`)
                 .then((res) => {
                   if(res.data.code == '0'){
                     this.startTime=res.data.morning.startwork
                     this.late = res.data.morning.startwork_late
                     this.endTime = res.data.morning.endwork
                     this.early = res.data.morning.endwork_late
                     this.startTime1 = res.data.afternoon.startwork
                     this.late1 = res.data.afternoon.startwork_late
                     this.endTime1 = res.data.afternoon.endwork
                     this.early1 = res.data.afternoon.endwork_late
                   }else{
                     console.log('数据获取失败')
                   }
                 })
                 .catch(error => {
                   console.log(error)
                 })
          },
          handlechange(time) {
            this.startTime = time

          },

          handlechange1(time) {
            this.endTime = time

          },
          handlechange2(time) {
           this.startTime1 = time

          },
          handlechange3(time) {
           this.endTime1 = time

          },
          submitM() {
              this.$axios.post(`${this.URL_PREFIX}/v1/system/attendance`,{
                'morning' : [
                  {
                    startwork:this.startTime,
                    endwork:this.endTime,
                    startwork_late:this.late,
                    endwork_late:this.early
                  }
                ],
                'afternoon' : []

              }).then(res => {
                if(res.data.code == '0'){
                  setTimeout(() => {
                     this.getAttendanceList()
                     this.$Message.success('设置成功')
                  },1500)
                }else{
                  setTimeout(() => {
                     this.$Message.error('设置失败')
                  },1500)
                }
              }).catch(error => {
                 console.log(error)
              })
          },
          submitA() {
            this.$axios.post(`${this.URL_PREFIX}/v1/system/attendance`,{
              'morning' : [],
              'afternoon' : [
                 {
                  startwork:this.startTime1,
                  endwork:this.endTime1,
                  startwork_late:this.late1,
                  endwork_late:this.early1
                }
              ]
            }).then(res => {
              if(res.data.code == '0'){
                setTimeout(() => {
                   this.$Message.success('设置成功')
                },1500)
              }else{
                setTimeout(() => {
                   this.$Message.error('设置失败')
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
    .tment,.ivu-row{
        height: 100%;
    }
    .tment .tment-left{
        height: 100%;
        padding: 15px;
        border-right: 1px solid #e5e9ee;
    }
</style>
