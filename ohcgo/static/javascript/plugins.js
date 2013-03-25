/*
 * jQuery throttle / debounce - v1.1 - 3/7/2010
 * http://benalman.com/projects/jquery-throttle-debounce-plugin/
 *
 * Copyright (c) 2010 "Cowboy" Ben Alman
 * Dual licensed under the MIT and GPL licenses.
 * http://benalman.com/about/license/
 */
(function(b,c){var $=b.jQuery||b.Cowboy||(b.Cowboy={}),a;$.throttle=a=function(e,f,j,i){var h,d=0;if(typeof f!=="boolean"){i=j;j=f;f=c}function g(){var o=this,m=+new Date()-d,n=arguments;function l(){d=+new Date();j.apply(o,n)}function k(){h=c}if(i&&!h){l()}h&&clearTimeout(h);if(i===c&&m>e){l()}else{if(f!==true){h=setTimeout(i?k:l,i===c?e-m:e)}}}if($.guid){g.guid=j.guid=j.guid||$.guid++}return g};$.debounce=function(d,e,f){return f===c?a(d,e,false):a(d,f,e!==false)}})(this);

/*
Copyright 2013 Mike Dunn
http://upshots.org/
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
(function(f){f.fn.getStyles=function(e,g){var d={},b,a;if(e&&e instanceof Array)for(var c=0,h=e.length;c<h;c++)a=e[c],d[a]=this.css(a);else if(c=this.get(0),window.getComputedStyle){var f=/\-([a-z])/g,l=function(a,b){return b.toUpperCase()};if(b=window.getComputedStyle(c,null)){var j,k;if(b.length){c=0;for(h=b.length;c<h;c++)a=b[c],j=a.replace(f,l),k=b.getPropertyValue(a),d[j]=k}else for(a in b)j=a.replace(f,l),k=b.getPropertyValue(a)||b[a],d[j]=k}}else if(b=c.currentStyle)for(a in b)d[a]=b[a];else if(b=
c.style)for(a in b)"function"!=typeof b[a]&&(d[a]=b[a]);if(g&&g instanceof Array){c=0;for(h=g.length;c<h;c++)a=g[c],delete d[a]}return d};f.fn.copyCSS=function(e,g,d){e=f(e).getStyles(g,d);this.css(e)}})(jQuery);
