<template>
  <q-page class="row items-center justify-evenly main-bg">
    <div class="col-7 column items-start justify-center">
      <q-card class="view-content">
        <q-card-section>
          <h3 class="text-h6 view-container-header">Stream</h3>

          <q-separator style="margin: 10px -16px 32px -16px" />

          <img id="stream" class="image-stream" />
        </q-card-section>
      </q-card>
    </div>

    <div class="col-5 column items-start view-container">
      <q-card class="view-content">
        <q-card-section>
          <h3 class="text-h6 view-container-header">Controller</h3>

          <q-separator style="margin: 10px -16px 32px -16px" />
          <p>
            Please enter URLs here : {{ message }}
          </p>

          <div class="row q-gutter-md btn-actions">
            <div class="input-container input-comURL">
              <input ref = "URL" type="string" name="ESP-WROOM-32" id="input-URL" class="input-normal" placeholder="ComputerのURL" />
            </div>
            <div class="input-container input-camURL">
              <input ref = "URL" type="string" name="ESP32CAM" id="input-URL" class="input-normal" placeholder="CaptureのURL" />
            </div>
            <div class="input-container input-streamURL">
              <input ref = "URL" type="string" name="CAM-stream" id="input-URL" class="input-normal" placeholder="StreamのURL" />
            </div>
          </div>
          <p>
            Please control CanSat with this control panel : {{ message }}
          </p>
          <div class="row q-gutter-md btn-actions">
            <q-btn
              class="control-button"
              rounded
              label="FORWARD"
              @click="control('forward')"
            />
            <q-btn
              class="control-button"
              rounded
              label="BACK"
              @click="control('back')"
            />
            <q-btn
              class="control-button"
              rounded
              label="RIGHT"
              @click="control('right')"
            />
            <q-btn
              class="control-button"
              rounded
              label="LEFT"
              @click="control('left')"
            />
            <q-btn
              class="control-button"
              rounded
              label="IMAGE PROCESS"
              @click="imageprocess_s()"
            />
            <q-btn
              class="control-button"
              rounded
              label="IMAGE PROCESS STOP"
              @click="imageprocess_e()"
            />
          </div>
          <p>
            If you want to set the running time, please enter it here : {{ message }}
          </p>
          <div class="row q-gutter-md btn-actions">
            <div class="input-container input-distance">
              <input ref = "time" type="number" required step="1" name="time" id="input-time" class="input-normal" placeholder="time" />
            </div>
            <label for="time">
              <span class="text-caption"> 
              （ms） 
              </span>
            </label>
          </div>
          <p>
            If you want to watch the stream, please click here : {{ message }}
          </p>
          <button id="toggle-stream" @click="toggle_stream">Start Stream</button>
          <div class="text-caption">
            {{ control_status_message }}
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script lang="ts">
import axios from 'axios';
import internal from 'stream';
import { defineComponent, ref } from 'vue';

const BACKEND_URL = 'http://127.0.0.1:8000';  //localhost:8000のngrokURL
var streamUrl = 'http://192.168.3.13:81';


const stopStream = () => {
  const streamButton = document.getElementById('toggle-stream')
  window.stop();
  streamButton!.innerHTML = 'Start Stream'
}

const startStream = () => {
  const streamButton = document.getElementById('toggle-stream')
  const view = document.getElementById('stream') as HTMLImageElement
  view.src = `${streamUrl}/stream`
  streamButton!.innerHTML = 'Stop Stream'
}


const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

export default defineComponent({
  name: 'Control Room',

  setup() {
    const control_status_message = ref('');
    const time = ref<HTMLInputElement| null>(null)

    return {
      time,
      control_status_message,
      async control(direction: string) {
        console.log(`Sending ${direction} message...`);

        const res = await axios
          .get(`${BACKEND_URL}/fusion/control/${direction}/${time.value?.value as string}/`)
          .catch(async (err) => {
            control_status_message.value =
              'Something went wrong. Please see console for details.';
            console.log(err);
            await sleep(3000);
            control_status_message.value = '';
          });

        if (res != null) {
          if (res.status == 200) {
            control_status_message.value = `${direction} message was successfully sent.`;
            await sleep(3000);
            control_status_message.value = '';
          } else {
            control_status_message.value = `${direction} message failed.`;
            console.log(res);
            await sleep(3000);
            control_status_message.value = '';
          }
        }
      },
      toggle_stream(){
        const streamButton = document.getElementById('toggle-stream')
        const streamEnabled = streamButton!.innerHTML === 'Stop Stream'
        if (streamEnabled) {
          stopStream()
        } else {
          startStream()
        }
      },
      imageprocess_s(){
        const res = axios
          .get(`${BACKEND_URL}/fusion/api/v1/start/`)
      },
      imageprocess_e(){
        const res = axios
          .get(`${BACKEND_URL}/fusion/api/v1/end/`)
      }
    };
  },
});
</script>

<style lang="scss">
.main-bg {
  background-color: #f3f9ff;
}

.view-container {
  padding: 16px;
}
.view-content {
  background-color: white;
  border-radius: 16px;

  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.view-container-header {
  padding: 0;
  margin: 8px;
}

.btn-actions {
  padding-bottom: 24px;
}

.image-stream {
  height: auto;
  max-width: 50vw;
  width: auto;
}


</style>
