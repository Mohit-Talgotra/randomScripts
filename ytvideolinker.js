//These codes are meant to be pasted in the console window of the playlist you're trying to get the links for

// PASTE THIS FIRST
// allow pasting

//COPY & PASTE CODE 1:
let goToBottom = setInterval(() => window.scrollBy(0, 400), 1000);

//COPY & PASTE CODE 2:
clearInterval(goToBottom);
let arrayVideos = [];
console.log('\n'.repeat(50));
const links = document.querySelectorAll('a');
for (const link of links) {
    if (link.id === "video-title") {
        link.href = link.href.split('&list=')[0];
        arrayVideos.push(link.title + ';' + link.href);
        console.log(link.title + '\t' + link.href);
    }
}

//COPY & PASTE CODE 3:
let data = arrayVideos.join('\n');
let blob = new Blob([data], {type: 'text/csv'});
let elem = window.document.createElement('a');
elem.href = window.URL.createObjectURL(blob);
elem.download = 'my_data.csv';
document.body.appendChild(elem);
elem.click();
document.body.removeChild(elem);