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
          <p>Please enter URLs here : {{ message }}</p>

          <div class="row q-gutter-md btn-actions">

            <div class="input-container input-comURL">
              <q-input
              outlined
              v-model="ESP32URL"
              type="text"
              name="ESP-WROOM-32"
              id="input-URL"
              class="input-normal"
              label="Computer's URL"
              />

            </div>

            <div class="input-container input-camURL">
              <q-input

              outlined
              v-model="CaptureURL"
              type="text"
              name="ESP32CAM"
              id="input-URL"
              class="input-normal"
              label="Capture's URL"

              />
            </div>

            <div class="input-container input-streamURL">
              <q-input

              outlined
              v-model="StreamURL"
              type="text"
              name="CAM-stream"
              id="input-URL"
              class="input-normal"
              placeholder="Stream's URL" />
            </div>
          </div>
          <p>
            If an emergency arises, please click here immediately : {{ message }}
          </p>
          <div class="row q-gutter-md btn-action">
            <q-btn
            class="control-button"
            rounded
            label="EMERGENCY STOP"
            @click="stopautomatic()"
            />
          </div>
          <p>Please control CanSat with control panel : {{ message }}</p>
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
              label="RIGHT-FORWARD"
              @click="control('right_forward')"
            />
            <q-btn
              class="control-button"
              rounded
              label="LEFT-FORWARD"
              @click="control('left_forward')"
            />
            <q-btn
              class="control-button"
              rounded
              label="RIGHT-BACK"
              @click="control('right_back')"
            />
            <q-btn
              class="control-button"
              rounded
              label="LEFT-BACK"
              @click="control('left_back')"
            />
            <q-btn
              class="control-button"
              rounded
              label="FIRE"
              @click="control('fire')"
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
          <div class="row q-gutter-md btn-actions">

            <div class="input-container input-distance">
              <input
              ref = "time"
              type="number"
              required
              step="1"
              name="time"
              id="input-time"
              class="input-normal"
              placeholder="time" />
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
import GpsDate from '@/components/GpsDate.vue'


//const BACKEND_URL = 'http://192.168.11.11';  //localhost:8000のngrokURL
//var streamUrl = 'http://192.168.3.13:81';


//const stopStream = () => {
  //const streamButton = document.getElementById('toggle-stream')
  //window.stop();
  //streamButton!.innerHTML = 'Start Stream'
//}

//const startStream = () => {
  //const streamButton = document.getElementById('toggle-stream')
  //const view = document.getElementById('stream') as HTMLImageElement
  //view.src = `${streamUrl}/stream`
  //streamButton!.innerHTML = 'Stop Stream'
//}



const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

export default defineComponent({
  name: 'Control Room',

  setup() {
    const control_status_message = ref('');
    const time = ref<HTMLInputElement | null>(null);
    const StreamURL = ref('');
    const ESP32URL = ref('');
    const CaptureURL = ref('');


    const startStream = () => {
      const streamButton = document.getElementById('toggle-stream');
      const view = document.getElementById('stream') as HTMLImageElement;
      view.src = `${StreamURL.value}/stream`;
      streamButton!.innerHTML = 'Stop Stream';
    };


    const stopStream = () => {
      const streamButton = document.getElementById('toggle-stream');
      window.stop();
      streamButton!.innerHTML = 'start Stream';
    }

    return {
      time,
      control_status_message,
      StreamURL,
      ESP32URL,
      CaptureURL,
      async control(direction: string) {
        console.log(`Sending ${direction} message...`);

        const res = await axios
          .get(

            `${ESP32URL.value}/api/v1/control/${direction}/${
              time.value?.value as string
            }/?esp=${ESP32URL.value}`
            )

          .catch(async (err) => {
            control_status_message.value =
              'Something went wrong. Please see console for details.';
            console.log(err);
            await sleep(10000);
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
      toggle_stream() {
        const streamButton = document.getElementById('toggle-stream');
        const streamEnabled = streamButton!.innerHTML === 'Stop Stream';
        if (streamEnabled) {

          // eslint-disable-next-line @typescript-eslint/no-unsafe-call

          stopStream();
        } else {
          startStream();
        }
      },

      imageprocess_s(){
        const res = axios
          .get(
            `${ESP32URL.value}/api/v1/image/start/?cap=${
              CaptureURL.value}&esp=${ESP32URL.value}`
              );
      },
      imageprocess_e(){
        const res = axios
          .get(
            `${ESP32URL.value}/api/v1/image/end/`);
      },
      startautomatic() {
        const res = axios.get(`${ESP32URL.value}/start`);
      },
      stopautomatic() {

        const res = axios.get(`${ESP32URL.value}/end`);
      },

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
