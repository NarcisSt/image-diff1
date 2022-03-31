Scrieți o aplicație Python care să primească ca argumente la linia de comandă numele unei imagini de Docker (public accesibilă pe hub.docker.com) și două tag-uri ale acesteia. 


Pe baza informațiilor primite aplicația va oferi utilizatorului un jurnal care să conțină modificări notabile referitoare la pachetele disponibile în cele două versiuni ale imaginii primite. 

 


Un exemplu de apel al aplicației: 


diff.py --image alpine --first-tag 3.12 --second-tag 3.15.1 

 


Sugestii: 


- pentru procesarea argumentelor primite la linia de comandă (sys.argv) se poate folosi argparse sau orice altă bibliotecă (sau implementare) 


- formatul în care informația este oferită utilizatorului este la latidinea dumneavoastră (de exemplu: JSON, YAML, XML, text, tabel, etc.) 


- pentru procesarea imaginilor de Docker se poate folosi Syft (https://github.com/anchore/syft/) 


 

Cerințe: 


- se va folosi git ca și VCS (Version Control System); 


- repository-ul poate fi pe oricare dintre platformele (GitHub, Gitlab, Bitbucket); 


- repository-ul poate fi privat atât timp cât unul dintre colegii noștrii va avea acces la el; 


- timpul investit pentru implementarea soluției trebuie să fie de maxim 2 ore. 