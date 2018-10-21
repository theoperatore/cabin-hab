const dnssd = require('dnssd');

const Browser = new dnssd.Browser(dnssd.tcp('_cabinthing'));

console.log('starting dns for cabinthings discovery');
Browser.on('serviceUp', s => console.log('ServiceUp', s));
Browser.on('serviceDown', s => console.log('ServiceDown', s));
Browser.on('serviceChanged', s => console.log('ServiceChanged', s));

Browser.start();
