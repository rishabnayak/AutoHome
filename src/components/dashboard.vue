<template>
<main role="main">
  <div class="container">
    <div class="row">
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Wd1</p>
          {{wd1}}
        </div>
      </div>
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Wd2</p>
          {{wd2}}
        </div>
      </div>
      <div class="col-sm">
        <div class="jumbotron text-center">
          <p class="text-muted">Wd3</p>
          {{wd3}}
        </div>
      </div>
    </div>
    <br>
    <div v-if="fall">
      <div class="jumbotron text-center">
        <h3>Fall Detected!</h3>
      </div>
    </div>
    <br>
    <div v-if="collide">
      <div class="jumbotron text-center">
        <h3>Collision Imminent!</h3>
      </div>
    </div>
  </div>

  <hr class="featurette-divider">

    <footer class="container">
        <p class="float-right"><a href="#">Back to top</a></p>
        <p>© 2018 AutoHome · <a>
                <router-link :to="{ name: 'privacy'}">Privacy</router-link>
              </a></p>
      </footer>
</main>
</template>

<script>
import firebase from 'firebase'
import firebaseui from 'firebaseui'
import db from '@/firebase/init.js'
import axios from 'axios'
export default {
  name: 'dashboard',
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  data() {
    return {
      feedin: null,
      collide: null,
      wd1: null,
      wd2: null,
      wd3: null,
      split: null,
      fall: null,
      econtact: null
    }
  },
  methods: {
    getFeedin() {
      axios.get(
          'https://io.adafruit.com/api/v2/Stepify/feeds/out/data/last', {
            headers: {
              'X-AIO-Key': '3a5f9b06eb9047d1a7007d45367a887d',
              'Content-Type': 'application/json'
            }
          }
        )
        .then((response) => {
          this.feedin = response.data.value;
          this.split = this.feedin.split("'");
          this.collide = this.split[0]
          this.wd1 = this.split[1]
          this.wd2 = this.split[2]
          this.wd3 = this.split[3]
          this.fall = this.split[4]
          if (this.collide == 'Ok') {
            this.collide = false
          } else {
            this.collide = true
          }
          if (this.fall == 'falling') {
            this.fall = true
          } else {
            this.fall = false
          }
          setTimeout(() => {
            this.getFeedin()
          }, 2000)
        });
    }
  },
  mounted() {
    this.getFeedin()
    this.econtact = this.user.econtact
    axios.post('https://io.adafruit.com/api/v2/Stepify/feeds/econtact/data', {
      "value": this.user.econtact
    }, {
      headers: {
        'X-AIO-Key': '3a5f9b06eb9047d1a7007d45367a887d',
        'Content-Type': 'application/json'
      }
    })
  }
}
</script>
