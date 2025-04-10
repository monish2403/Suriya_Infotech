const statusText = document.getElementById("shop-status");
const now = new Date();
const day = now.getDay();
const hour = now.getHours();

if (hour >= 10 && hour < 21) {
  statusText.innerText = "🟢 Open Now";
} else {
  statusText.innerText = "🔴 Currently Closed";
}
