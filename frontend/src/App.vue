<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="container is-max-widescreen">
    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="">
          <p class="title is-1">Roster Tuner 0.1 beta</p>
          <p class="subtitle is-4">For 40K army roster optimizers and fine tuners.</p>
          <div class="buttons">
            <a class="button is-patreon" href="https://www.patreon.com/roster_tuner/">
              Support in Patreon</a
            >
            <a class="button is-discord" href="https://discord.gg/NUFcmUVFaM"> Join Discord</a>
          </div>
        </div>
      </div>
    </section>
  </div>
  <div class="container is-max-widescreen">
    <RouterView />
  </div>
  <br />
  <br />
  <br />
  <br />
  <br />
  <br />
  <br />
  <br />
  <br />
  <br />
</template>

<style lang="scss">
@import './assets/master_style.scss';
</style>
