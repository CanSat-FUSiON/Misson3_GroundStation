<template>
  <div class="home container">
    <div class="row">
      <div class="col-6">
        <img
          class="monitor-image"
          id="major-photo"
          alt="Connection Failed"
          src="../assets/main_camera.png"
        />
        <img
          class="monitor-image"
          alt="Vue logo"
          src="../assets/position.png"
        />
        <img
          class="monitor-image"
          alt="Vue logo"
          src="../assets/gps_display.png"
        />
      </div>
      <div class="col-6">
        <img class="monitor-image" alt="Vue logo" src="../assets/temp.png" />
        <img class="monitor-image" alt="Vue logo" src="../assets/logs.png" />
        <p>log data from esp-wroom-32</p>
        <div class="remocon">
          <h1>remote controller</h1>
          <button>forward</button>
          <div class="row">
            <div class="col-6">
              <button>left</button>
            </div>
            <div class="col-6">
              <button>right</button>
            </div>
          </div>
          <button @click="back">back</button>
        </div>
        <div>
          <button @click="photo" class="btn btn-primary">
            take-photo
          </button>
        </div>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import axios from "axios"

@Options({
  components: {
    HelloWorld,
  },
})
export default class Home extends Vue {
  photo(){
    axios.get("http://2.tcp.ngrok.io:11240/capture", {responseType: "blob"})
    .then(resp =>{
      document.getElementById("major-photo")?.setAttribute("src",window.URL.createObjectURL(resp.data));
    })
  }
}
</script>

<style >
.monitor-image {
  width: 100%;
  padding-bottom: 15px;
}
.remocon {
  padding-top: 70px;
  padding-left: 30px;
}
</style>