const { ips } = require('./base')

let regExp = /((25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]\d)(\.)){3}(25[0-5]|2[0-4][0-9]|1\d{2}|[1-9]\d)/g;

console.log(ips.match(regExp))
