<template>
<main role="main">
  <div class="container">
    <div class="row">
      <div class="col-sm-6">
        <div class="jumbotron text-center">
          <p class="text-muted">Temperature</p>
          {{temp}}
        </div>
      </div>
      <div class="col-sm-6">
        <div class="jumbotron text-center">
          <p class="text-muted">Humidity</p>
          {{hum}}
        </div>
      </div>
    </div>
    <br>
    <div class="row">
      <div class="col-sm">
        <div class="jumbotron text-center">
          <h3>User Preferences</h3>
          <br>
          <form>
          <div class="row">
            <div class="col-md-6">
              <label for="userTemp">Preferred Temperature</label>
              <input type="text" class="form-control" id="userTemp" v-model="userTemp">
            </div>
            <div class="col-md-6">
              <label for="userHumidity">Preferred Humidity</label>
              <input type="text" class="form-control" id="userHumidity" v-model="userHumidity">
            </div>
          </div>
          <hr class="mb-4">
        </form>
          <button class="btn btn-primary btn-lg btn-block col-md-3" type="submit" @click="updateProfile()">Set Preference</button>
          <p v-if="fieldempty" class="red availability">Please fill in all data!</p>
        </div>
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
      temp: null,
      hum: null,
      userTemp: null,
      userHumidity: null,
      fieldempty: null
    }
  },
  methods: {
    async updateProfile() {
      if (this.userTemp == undefined || this.userHumidity == undefined) {
        this.fieldempty = true
        return
      } else {
        const ref = db.collection('users').doc(this.user.uid)
        await ref.update({
          userTemp: this.userTemp,
          userHumidity: this.userHumidity
        })
      }
    },
    async updateData(){
      let ref = await db.collection('users').doc(this.user.uid).get()
      this.temp = ref.data().temperature
      this.hum = ref.data().humidity
      setTimeout(() => {
            this.updateData()
      }, 5000)
    }
  },
  async mounted() {
    this.updateData()
    this.userTemp = this.user.userTemp
    this.userHumidity = this.user.userHumidity
  }
}
</script>


<style>
.availability {
  padding-top: 6px;
  padding-left: 3px;
}

.green {
  color: green;
}

.red {
  color: red;
}
</style>
