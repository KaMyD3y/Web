console.assert( 1 === 2 , "acest mesaj va aparea deoarece conditia este falsa")
//console.clear() sterge consola 
console.count("false")
console.countReset("false")//reseteaza ceia ce avem la 0 
console.count("false")//numara de cite ori este false scris si iti da rezultatul
console.debug('Mesaj Salut')//sunt folosite pentru mai detaliat,pentru a intelege comportamentul!
console.dir()//afiseaza un obiect sub forma de tot ce are de la parinte la copiil!
let obj = {nume: 'Alice', vârstă: 25};
console.dir(obj);//dar pe classe cui si carei apartine!
console.log(obj)//pentru ca sa inteleg diferenta
console.dirxml()//afiseaza un element html sub forma de parinte,copiil
let element = document.getElementById('exemplu');
console.dirxml(element);
console.error("Acesta este un mesaj de erroare!")
console.group()//creaza un nou grup de mesaje in console
console.group('Grup de mesaje');
console.log('Mesaj 1');
console.log('Mesaj 2');
console.groupEnd();
console.groupCollapsed()//creaza un grup de mesaje in consola care este restrins implicit!
console.groupCollapsed('Grup de mesaje restrâns');
console.log('Mesaj 1');
console.log('Mesaj 2');
console.groupEnd();
console.groupEnd()//incheie grupul curent de mesaje!!
console.info("informatie!")//afiseaza un mesaj informativ
console.log("Salut")//afiseaza un mesaj general!
console.profile("Nume profil")//incepe inregistrarea unui profil de performanta
console.profileEnd("Nume profil")//incheie inregistrarea unui profil de performanta
console.table()//afiseaza datele sub forma de tabel!
let oameni = [
    {nume: 'Alice', vârstă: 25},
    {nume: 'Bob', vârstă: 30},
    {nume: 'Charlie', vârstă: 35}
  ];
  console.table(oameni);
console.time("Eticheta timpului")//incepe un cronometru
1+1
console.timeEnd("Eticheta timpului")//incheie un cronometru si afiseaza durata.
console.time('Eticheta timpului');
1+1
console.timeLog('Eticheta timpului');//inregistreaza valoarea actuala a unui cronometru
console.timeStamp("Eticheta timpului")//Adauga o marca de timp in cronologia consolei
console.trace()//afiseaza o trasare a stivei de apeluri!
function primul() {
    alDoilea();
  }
  
  function alDoilea() {
    console.trace('Trasare stivă de apeluri');
  }
  
  primul();
console.warn("Aceasta este un mesaj de avetizare.")//afiseaza un mesaj de avertizare.