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
                type="string"
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
                type="string"
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
                type="string"
                name="CAM-stream"
                id="input-URL"
                class="input-normal"
                label="Stream's URL"
              />
            </div>
          </div>
          <div class="row q-gutter-md btn-actions">
            <q-banner rounded class="bg-orange-8 text-white">
              If you want to stop automatic, please click here :
              <template v-slot:action>
                <q-btn
                  push
                  color="white"
                  text-color="red"
                  class="control-button"
                  label="START AUTOMATIC"
                  @click="startautomatic()"
                />
                <q-btn
                  push
                  color="white"
                  text-color="red"
                  class="control-button"
                  label="STOP AUTOMATIC"
                  @click="stopautomatic()"
                />
              </template>
            </q-banner>
          </div>
          <div class="row q-gutter-md btn-actions">
            <q-banner rounded class="bg-yellow-8 text-white">
              Please control CanSat with this control panel :
              <template v-slot:action>
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="FORWARD"
                  @click="control('forward')"
                />
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="BACK"
                  @click="control('back')"
                />
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="RIGHT"
                  @click="control('right')"
                />
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="LEFT"
                  @click="control('left')"
                />
              </template>
            </q-banner>
            <q-banner rounded class="bg-yellow-8 text-white">
              If you want to set the running time, please enter it here :
              <template v-slot:action>
                <div class="row q-gutter-md btn-actions">
                  <div class="input-container input-distance">
                    <input
                      ref="time"
                      type="number"
                      required
                      step="1"
                      name="time"
                      id="input-time"
                      class="input-normal"
                      placeholder="time"
                    />
                  </div>
                  <label for="time">
                    <span class="text-caption"> （ms） </span>
                  </label>
                </div>
              </template>
            </q-banner>
            <q-banner rounded class="bg-yellow-8 text-white">
              If you want to start image process, please click here :
              <template v-slot:action>
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="IMAGE PROCESS"
                  @click="imageprocess_s()"
                />
                <q-btn
                  push
                  color="white"
                  text-color="orange"
                  label="IMAGE PROCESS STOP"
                  @click="imageprocess_e()"
                />
              </template>
            </q-banner>
          </div>
          <q-banner rounded class="bg-blue-8 text-white">
            If you want to watch the stream, please click here :
            <template v-slot:action>
              <q-btn
                push
                color="white"
                text-color="primary"
                id="toggle-stream"
                @click="toggle_stream"
              >
                Start Stream
              </q-btn>
            </template>
            <div class="text-caption">
              {{ control_status_message }}
            </div>
          </q-banner>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script lang="ts">
import axios from 'axios';
import internal from 'stream';
import { defineComponent, ref } from 'vue';

// var streamUrl = '******';

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

    const stopStream = () => {
      const streamButton = document.getElementById('toggle-stream');
      window.stop();
      streamButton!.innerHTML = 'Start Stream';
    };

    const startStream = () => {
      const streamButton = document.getElementById('toggle-stream');
      const view = document.getElementById('stream') as HTMLImageElement;
      view.src = `${StreamURL.value}/stream`;
      streamButton!.innerHTML = 'Stop Stream';
    };

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
            `${process.env.BACKENDURL}/api/v1/control/${direction}/${
              time.value?.value as string
            }/?esp=${ESP32URL.value}`
          )
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
      toggle_stream() {
        const streamButton = document.getElementById('toggle-stream');
        const streamEnabled = streamButton!.innerHTML === 'Stop Stream';
        if (streamEnabled) {
          stopStream();
        } else {
          startStream();
        }
      },
      imageprocess_s() {
        const res = axios.get(
          `${process.env.BACKENDURL}/api/v1/image/start/?cap=${CaptureURL.value}&esp=${ESP32URL.value}`
        );
      },
      imageprocess_e() {
        const res = axios.get(`${process.env.BACKENDURL}/api/v1/image/end/`);
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
