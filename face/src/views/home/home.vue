<template>
    <div class="home">
       <Form ref="formCustom">
         <Col span="8">
             <FormItem label="全天统计" >
                 <div  :style="{height:'300px',width:'300px',display:'flex'}" ref="myEchart"></div>
             </FormItem>
         </Col>
        <Col span="8">
            <FormItem label="早上统计" >
                <div  :style="{height:'300px',width:'300px',display:'flex',marginLeft:'25px'}" ref="myEchart2"></div>
            </FormItem>
         </Col>
        <Col span="8">
            <FormItem label="下午统计">
                <div  :style="{height:'300px',width:'300px',display:'flex',marginLeft:'25px'}" ref="myEchart3"></div>
            </FormItem>
         </Col>
        </Form>
        <Form>
          <Row>
              <Col span="5" >
                <FormItem label="实时通讯记录" ></FormItem>
                 <div v-for="(item,index) in visitedInfo" class="info">
                   <div class="layout-quit">
                       <Icon type="android-radio-button-off" class="person" :style="{width:'20px',color:ActiveColor}"></Icon>
                       <span>{{item.name}}&nbsp;&nbsp;&nbsp;&nbsp;{{item.team}}&nbsp;&nbsp;&nbsp;&nbsp;{{item.posttime}}</span>
                   </div>
                   <div class="layout-quits">
                       <span>{{item.desc}}</span>
                   </div>
                 </div>
                </Col>
            <Col span="18">
               <FormItem label="通行统计">
                   <Row>
                     <Col span="4">
                     <Icon type="android-checkbox-blank" :style="{width:'20px',color:'#A4D362'}"></Icon>
                     <span>内部员工</span>
                     </Col>
                     <Col span="4">
                     <Icon type="android-checkbox-blank" :style="{width:'20px',color:'#EBBF60'}"></Icon>
                     <span>陌生人</span>
                     </Col>
                     <Col span="4">
                     <Icon type="android-checkbox-blank" :style="{width:'20px',color:'#C5DD52'}"></Icon>
                     <span>VIP用户</span>
                     </Col>
                      <div :style="{height:'400px',width:'1200px'}" ref="myEchart1"></div>
                   </Row>
                </FormItem>
            </Col>
          </Row>
        </Form>
    </div>
</template>
<script>
import echarts from 'echarts';
//配置项
let option = {
    tooltip: {
      trigger: 'item',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'line' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top:'5%',
      containLabel: true
    },
    series: [{
      name: '全天统计',
      type: 'pie',
      radius: '60%',
      data:[]
    }],
    color: [
    '#EBBF60',
    '#DEAD60',
    '#A4D362',
    '#C5DD52',
  ],
}
let option1 = {
    tooltip: {
      trigger: 'item',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top:'5%',
      containLabel: true
    },
    series: [{
      name: '早上统计',
      type: 'pie',
      radius: '60%',
      data: []
    }],
    color: [
    '#EBBF60',
    '#DEAD60',
    '#A4D362',
    '#C5DD52',
  ],
}
let option2 = {
    tooltip: {
      trigger: 'item',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top:'5%',
      containLabel: true
    },
    series: [{
      name: '下午统计',
      type: 'pie',
      radius: '60%',
      hoverAnimation:true,
      data: [],
    }],
    color: [
    '#EBBF60',
    '#DEAD60',
    '#A4D362',
    '#C5DD52',
  ],
}
let option3 = {
    tooltip: {
      trigger: 'axis',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top:'5%',
      containLabel: true
    },
      xAxis : [
    {
        type : 'category',
        data : ['0','01','02','03','04','05','06','07','08','09','10'],
    }
  ],
  yAxis : [
    {
        type : 'value'
    }
  ],
  series: [
        {
        name: '内部员工',
        type:'line',
          barWidth: '60%',
          data:[50, 80, 70,74, 65,86, 37,58,69,52,42],
          color:["#A4D362"]
       },
       {
        name: '陌生人',
        type:'line',
          barWidth: '60%',
          data:[34, 28, 26,55, 46, 48, 32,64,35,38,64],
          color:["#DEAD60"]
      },
      {
        name: 'VIP用户',
        type:'line',
          barWidth: '60%',
          data:[18, 32, 35, 14, 42, 31, 22,25,42,37,75],
          color:["#C5DD52"]
      }
  ],
}

export default {

  data() {
    return {
      ActiveColor:'',
      visitedInfo:[],
      chart: null,
      chart1:null,
      chart2:null,
      chart3:null,
      starttime: null,
      endtime: null
    }
  },
  mounted() {
    this.getPie()
    this.getData()
    this.getLine()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose();
    this.chart = null;
  },
    methods: {
    //获取实时通讯录接口数据
    getData(){
       this.$axios.get(`${this.URL_PREFIX}/v1/index/by`)
                  .then(res => {
                    if(res.data.code == '0'){
                      this.visitedInfo = res.data.result
                      for(let item of this.visitedInfo){
                        if(item.team=="陌生人"){
                           this.ActiveColor='#aaf'
                        }else if(item.team=='vip用户'){
                           this.ActiveColor = '#7cd39e'
                        }else{
                          this.ActiveColor='#74b1f5'
                        }
                      }
                    }
                  }).catch(error => {
                    console.log(error)
                  })
    },
    //获取饼图数据
      getPie(){
        this.$axios.get(`${this.URL_PREFIX}/v1/index/pie`)
                   .then(res => {
                     if(res.data.code == '0'){
                        this.chart = echarts.init(this.$refs.myEchart);   //day
                        this.chart2 = echarts.init(this.$refs.myEchart2); //morning
                        this.chart3 = echarts.init(this.$refs.myEchart3); //afternoon
                        option.series[0].data = res.data.day
                        option1.series[0].data = res.data.morning
                        option2.series[0].data = res.data.afternoon
                        this.chart.setOption(option,true);
                        this.chart2.setOption(option1,true);
                        this.chart3.setOption(option2,true);
                     }
                   }).catch(error => {
                     console.log(error)
                   })
      },
    //获取通行折线图数据
     getLine(){
       this.$axios.get(`${this.URL_PREFIX}/v1/index/log`)
                  .then(res => {
                  //  if(res.data.code == '0'){
                      this.chart1 = echarts.init(this.$refs.myEchart1); //line
                      this.chart1.setOption(option3,true);
                  //  }
                  }).catch(error => {
                    console.log(error)
                  })
     }
  }
    }
</script>
<style scoped>
.home{
     padding: 15px;
}
.layout-quit .person{
  font-size: 18px;
}
.layout-quit{
  margin-left: 30px;
  line-height: 25px;
}
.layout-quits{
  margin-left: 53px;
  line-height: 35px;
}
.quit{
  margin-left: 30px;
}
.info{
  margin-left: -30px;
}
</style>
