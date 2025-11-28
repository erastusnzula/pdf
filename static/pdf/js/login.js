 // fetch config directly from Django
const firebaseConfig = await (await fetch("/accounts/firebase-config/")).json();

// import firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import {
    getAuth,
    GoogleAuthProvider,
    signInWithPopup
} from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";

// init firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

document.getElementById("googleBtn").addEventListener("click", async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        const idToken = await result.user.getIdToken();

        await fetch("/accounts/firebase-login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ idToken })
        });

        window.location.href = "/";

    } catch (err) {
        console.error(err);
        alert(err.code + " : " + err.message);
    }
});