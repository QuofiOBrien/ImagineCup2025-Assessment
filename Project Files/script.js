function changeMessage() {
  const messages = [
    "🖤 Quofi O'Brien 🖤",
    "Dream big",
    "Innovate today!",
    "Change the world",
    "You're awesome!",
    "Keep going!"
  ];
  const randomMsg = messages[Math.floor(Math.random() * messages.length)];
  document.getElementById("message").innerText = randomMsg;
}