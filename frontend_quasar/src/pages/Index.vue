<template>
  <q-page class="row items-center justify-evenly main-bg">
    <div class="col-7 column items-start justify-start"></div>

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
              @click="control('left')"
            />
          </div>

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
import { defineComponent, ref } from 'vue';

const BACKEND_URL = 'http://8ea2-60-74-77-131.ngrok.io/fusion/control';  //localhost:8000のngrokURL

const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

export default defineComponent({
  name: 'Control Room',

  setup() {
    const control_status_message = ref('');

    return {
      control_status_message,
      async control(direction: string) {
        console.log(`Sending ${direction} message...`);

        const res = await axios
          .get(`${BACKEND_URL}/${direction}/`)
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
</style>
