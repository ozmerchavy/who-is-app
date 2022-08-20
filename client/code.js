const whoIsAppContainer = document.querySelector("#who-ip-app");
const historyConatiner = document.querySelector("#history");

document.body.addEventListener('click', (event) => {

    if (event.detail != 1) return;

    const style = document.createElement('style')
    style.innerText = `
        * {
            animation: none !important;
        }
        p { 
            color: var(--main-color) !important;
        }
    `;
    document.head.appendChild(style)
    window.scrollTo(0, document.body.scrollHeight, { behavior: 'smooth' });
})

async function main() {
  const ips_online_string = await fetch("/who-is-online").then((res) => res.json());
  const ips_lines = ips_online_string.split('\n')
  const [html, totalTime] = generateAnimHtml(ips_lines);

  if (ips_online_string) { // if not empty, override cool circles animaiton
    whoIsAppContainer.innerHTML = html;
  }

  const deltas_text = await fetch("/delta-history").then((res) => res.json());
  const [deltaHtml] = generateAnimHtml(deltas_text.split('\n'), totalTime + .3);
  
  historyConatiner.innerHTML = deltaHtml;
}

function generateAnimHtml(lines, base_delay = 0) {
  const seconds_per_letter = 0.03;
  let totalTimeSoFar = 0;

  const html = lines.map((fullString) => {
    fullString = fullString.trim();
    const duration = fullString.length * seconds_per_letter
    const delay = totalTimeSoFar + base_delay;
    totalTimeSoFar += duration;
    return `<span class ="typewriter" style="--text-len: ${fullString.length}; --delay: ${delay+"s"}; --duration:${duration+"s"}"> <p> ${fullString} </p> </span>`
  }).join("");

  return [html, totalTimeSoFar];
}

main();
