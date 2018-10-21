const dnssd = require('dnssd');

const advert = new dnssd.Advertisement(dnssd.tcp('_cabinthing'), 1339, { name: 'Cabin Status' })
  .on('error', console.error)
  .on('stopped', () => console.log('advert stopped'));

advert.start();
