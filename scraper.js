const https = require('https');
const fs = require('fs');

var data;

async function getNews(input, from, to) {
  return new Promise(resolve => {
    var all_articles = [];
    const apiKey = '0lRut9I2IboC0FlDg5wVabXmfIfb2hRU'
    const url = `https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=${from}&end_date=${to}&facet=false&q=${input}&sort=relevance&api-key=${apiKey}`;
    https.get(url, res => {
      data = '';
      res.on('data', chunk => {
        data += chunk;
      });
      res.on('end', () => {
        //parse data
        data = JSON.parse(data);
        console.log(data.response.docs[0].lead_paragraph);
        data.response.docs.forEach(par => {
          if (par.lead_paragraph.includes("Ukraine")) {
            fs.appendFile('./ukrainepre.txt', par.lead_paragraph + "\n", err => {
              if (err) {
                console.error(err);
              }
            });
          }
        });
        //append to file

      })
    }).on('error', err => {
      console.log(err.message);
    })
  });
}

function results() {
  console.log("Test")

  getNews("Ukraine", 20191215, 20191230)
  /* write the file
    fs.appendFile('/ukrainepre.json', content, err => {
      if (err) {
        console.error(err);
      }
      // file written successfully
    });
  */
}

results();