target_time = new Date("2023-07-07 00:00:00").getTime();
formatted_time = '7/7/2023 0:00 AM';
// formatted_time = new Date(target_time).toLocaleString("en-US", {timeZone: "Europe/Berlin"});

releaseDt.innerText = formatted_time;

function update() {
  days.innerText = Math.floor((target_time - new Date().getTime()) / (1000 * 60 * 60 * 24));
  hours.innerText = Math.floor((target_time - new Date().getTime()) / (1000 * 60 * 60)) % 24;
  minutes.innerText = Math.floor((target_time - new Date().getTime()) / (1000 * 60)) % 60;
  seconds.innerText = Math.floor((target_time - new Date().getTime()) / (1000)) % 60;
}

// update every second
update();
setInterval(update, 1000);
