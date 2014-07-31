<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node text="2014-07-29-archlinux-installation.org" background_color="#00bfff">
<richcontent TYPE="NOTE"><html><head></head><body><p>--org-mode: WHOLE FILE</p></body></html></richcontent>
<node text="&#x524d;&#x8a00;" position="left">
<node style="bubble" background_color="#eeee00">
<richcontent TYPE="NODE"><html>
<head>
<style type="text/css">
<!--
p { margin-top: 3px; margin-bottom: 3px; }-->
</style>
</head>
<body>
<p>Archlinux&#x7684;&#x5b89;&#x88c5;&#x4ece;&#x4e0a;&#x5e74;7&#x6708;&#x5f00;&#x59cb;&#x5c31;&#x53d6;&#x6d88;&#x4e86;&#x56fe;&#x5f62;&#x754c;&#x9762;&#x7684;&#x5f15;&#x5bfc;&#xff0c;&#x6539;&#x4e3a;&#x7eaf;&#x7cb9;&#x7684;&#x547d;&#x4ee4;&#x884c;&#x754c;&#x9762;&#xff0c;&#x4e5f;&#x5c31;&#x662f;&#x5f00;&#x673a;&#x8bfb;&#x53d6;Arch&#x5149;&#x76d8;&#x955c;&#x50cf;&#xff0c;&#x8fdb;&#x5165;&#x955c;&#x50cf;&#x91cc;&#x7684;Arch&#x57fa;&#x672c;&#x7cfb;&#x7edf;&#xff0c;&#x5728;&#x6587;&#x5b57;&#x754c;&#x9762;&#x4e0b;&#x6309;&#x9700;&#x9009;&#x62e9;Database&#x5b89;&#x88c5;&#x5230;&#x786c;&#x76d8;&#x3002;&#x4f3c;&#x4e4e;&#x4ece;&#x4eca;&#x5e74;&#x5f00;&#x59cb;Database&#x9700;&#x8981;&#x4ece;&#x7f51;&#x7edc;&#x4e0b;&#x8f7d;&#xff0c;&#x56e0;&#x6b64;&#x7f51;&#x7edc;&#x4e0d;&#x901a;&#x7684;&#x670b;&#x53cb;&#x614e;&#x4e4b;&#xff08;&#x5f53;&#x7136;&#xff0c;&#x4e0d;&#x5acc;&#x9ebb;&#x70e6;&#x53ef;&#x4ee5;&#x5148;&#x4ece;Arch&#x5b98;&#x7f51;&#x4e0a;&#x4e0b;&#x8f7d;&#x8981;&#x7528;&#x7684;Database&#x5230;U&#x76d8;&#xff0c;&#x518d;pacman -U ...&#x4e4b;&#xff09;&#x3002; <br /></p></body>
</html>
</richcontent>
</node>
</node>
<node text="&#x786c;&#x76d8;&#x5f15;&#x5bfc;&#x955c;&#x50cf;">
<node style="bubble" background_color="#eeee00">
<richcontent TYPE="NODE"><html>
<head>
<style type="text/css">
<!--
p { margin-top: 3px; margin-bottom: 3px; }-->
</style>
</head>
<body>
<p>1. &#x4ece;Archlinux&#x5b98;&#x7f51;&#x4e0b;&#x8f7d;&#x955c;&#x50cf;&#xff0c;&#x518d;&#x4e0b;&#x8f7d;grub4dos&#xff0c;&#x63d0;&#x53d6;grldr&#x3001;grldr.mbr&#x5230;&#x7cfb;&#x7edf;&#x76d8;&#xff08;&#x6211;&#x662f;C&#x76d8;&#xff09;&#xff0c;&#x5e76;&#x5728;&#x6b64;&#x533a;&#x65b0;&#x5efa;menu.lst&#xff0c;&#x5199;&#x5165;&#xff1a;<br />#+begin_src sh -n<br />title Arch <br />find --set-root /archlinux-2013.01.04-dual.iso <br />map --mem --heads=0 --sectors-per-track=0 /archlinux-2013.01.04-dual.iso (0xff) <br />map --hook <br />chainloader (0xff) <br />rm llchain<br />boot <br />#+end_src</p><p>&#x7f16;&#x8f91;C&#xff1a;\boot.ini&#xff0c;&#x5728;&#x6700;&#x5e95;&#x8865;&#x4e0a;&#xff1a; <br />&#160;`c:\grldr.mbr=&quot;Arch&quot;`</p></body>
</html>
</richcontent>
</node>
</node>
</node>
</map>