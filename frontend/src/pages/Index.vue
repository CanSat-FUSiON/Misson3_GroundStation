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
              @click="control('left', time)"
            />
            <q-btn
              class="control-button"
              rounded
              label="FIRE"
              @click="control('fire', time)"
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
            <label for="time">
              時間
              <span class="text-caption">
              （単位: ms）
              </span>
            </label>
            <div class="input-container input-distance">
              <input ref = "time" type="number" required step="1" name="time" id="input-time" class="input-normal" placeholder="time" />
            </div>
          </div>
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
var streamUrl = 'https://098e-2409-13-7040-9a00-ed2b-63db-6739-bcdf.jp.ngrok.io'; //ローカル環境を立ち上げる，ngrokでトンネリングする，ストリーム用のURLを踏んでVisit Siteをクリック，ストリーム用のURLをコードに書き込む，ローカル環境で動作するか確認する，ngrokでトンネリングしたフロントエンドのURLを踏む


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
