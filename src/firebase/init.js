import firebase from 'firebase'
import firestore from 'firebase/firestore'

var config = {
  apiKey: "AIzaSyAhMm0S1R29jQMEymbJRxtE7MmZIilismw",
  authDomain: "autohome-hoe.firebaseapp.com",
  databaseURL: "https://autohome-hoe.firebaseio.com",
  projectId: "autohome-hoe",
  storageBucket: "autohome-hoe.appspot.com",
  messagingSenderId: "551212232531"
};

const auth = firebase.initializeApp(config);
auth.firestore().settings({
  timestampsInSnapshots: true
});
export default auth.firestore();
