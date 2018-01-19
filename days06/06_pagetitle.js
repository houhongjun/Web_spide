var url = "http://www.baidu.com";

var page = require('webpage').create();
page.open(url,function(status){
    var title = page.evaluate(function(){
        return document.title;
    });
    console.log('Page title is '+ title.decode('utf-8').encode('gbk'));
    phantom.exit();
});