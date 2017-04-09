function okno(p,s,w) { 
  w=open('','','width='+s+',height='+w); 
  with(w.document) { 
   write('<html><head><title>'+p+'</title></head><body background="'+p+'"'); 
   write(' onMousedown="self.close()"></body></html>'); 
   close(); 
  } 
} 

function ZegarStart() { 
dzien=["SUN","MON","TUE","WED","THU","FRI","SAT"];
      miesiac=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
        K = new Date(); 
	godzina = K.getHours(); 
	minuty = K.getMinutes(); 
	sekundy = K.getSeconds(); 
        zegar.innerHTML = ("&nbsp&nbsp"+dzien[K.getDay()]+", "+ miesiac[K.getMonth()]+" "+K.getDay()+". "+K.getFullYear()+" / "+godzina + " : " + Math.floor(minuty/10) + minuty%10 +" : "+ Math.floor(sekundy/10)+sekundy%10);
	setTimeout('ZegarStart()',1000); } 

function ShowMenu(){ 
	mainmenu='<table cellspacing=0 class=tmn><tr><td><a href=index.php>Home</a></td></tr><tr><td class=mu>'; 
	for (i=0; i<main.length; i++) { 
		mainmenu = mainmenu +'<a href=javascript:; onmousedown=DisplaySubMenu("'+ main[i]+'");>'+ main[i]+'</a><br>';} 
	menu.innerHTML = mainmenu + '</td></tr></table><div id=subm></div>';}

function DisplaySubMenu(link){ 
	j = m[link]["submenu"].length; 
	wal = m[link]["submenu"][0];
       
	if (wal=!""){ 
		l = '<table cellspacing=0 class=tmn><tr><td class=mh>'+link+'</td></tr><tr><td class=mu>'; 
		for (k=0; k<j;k++) {
			l = l +'<a href='+ m[link]["adres"][k] + '>' + m[link]["submenu"][k]+'</a><br>';} 
		subm.innerHTML = l + '</td></tr></table>'; }}

main=["Dydaktyka","Publikacje"];
m = new Array();
m["Info"] = new Array(1);
m["Info"]["submenu"] = ["Poka¿"];
m["Info"]["adres"] = ["index.php"];
m["Zainteresowania"] = new Array(2);
m["Zainteresowania"]["submenu"] = ["Speedway","Beer","Travel"];
m["Zainteresowania"]["adres"] = ["gp.php","under.php","under.php"];
m["Dydaktyka"] = new Array(2);
m["Dydaktyka"]["submenu"] = ["Algorytmy i Struktury Danych","Optymalizacja Kombinatoryczna","Podstawy Programowania","Oceny"];
m["Dydaktyka"]["adres"] = ["aisd.php","optkomb.php","wdp.php","students.php"];
m["Referencje"] = new Array(2);
m["Referencje"]["submenu"] = ["Strony WWW"];
m["Referencje"]["adres"] = ["under.php"];
m["Publikacje"] = new Array(2);
m["Publikacje"]["submenu"] = ["Spis"];
m["Publikacje"]["adres"] = ["publications.php"];